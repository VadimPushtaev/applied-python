from unittest.mock import MagicMock, patch

from notes.account import Account, InvalidPasswordError, InvalidTokenError
from notes.access import NoSuchUserError
from tests import BaseTestCase


class AccountTestCase(BaseTestCase):
    def test_create(self):
        storage = MagicMock()

        fake_set_called = False

        def fake_set(key, _):
            nonlocal fake_set_called
            fake_set_called = True
            self.assertEqual('account:katya', key)
        storage.set = fake_set

        Account.create('katya', 'abc', storage)

        self.assertTrue(fake_set_called)

    @patch('notes.access.crypt')
    def test__check_password__false(self, patched_crypt):
        storage = MagicMock()
        storage.get.return_value = 'DIGEST'

        account = Account('katya')
        self.assertFalse(account._check_password('abc', storage))

        patched_crypt.assert_called_once_with('abc', 'DIGEST')

    @patch('notes.access.crypt')
    def test__check_password__true(self, patched_crypt):
        storage = MagicMock()
        storage.get.return_value = 'DIGEST'
        patched_crypt.return_value = 'DIGEST'

        account = Account('katya')
        self.assertTrue(account._check_password('abc', storage))

        patched_crypt.assert_called_once_with('abc', 'DIGEST')

    def test__check_password__no_such_user(self):
        storage = MagicMock()
        storage.get.return_value = None

        account = Account('katya')
        with self.assertRaises(NoSuchUserError):
            account._check_password('abc', storage)

    @patch('notes.account.uuid4')
    def test_create_token(self, patched_uuid4):
        patched_uuid4.return_value = 'UUID'

        storage = MagicMock()
        account = Account('katya')
        account._check_password = lambda p, s: True

        account.create_token('abc', storage)

        storage.set.assert_called_once_with('token:UUID', 'katya')

    def test__check_token(self):
        storage = MagicMock()
        storage.get.return_value = 'vasya'

        katya_acc = Account('katya')
        self.assertFalse(katya_acc._check_token('abc', storage))

        vasya_acc = Account('vasya')
        self.assertTrue(vasya_acc._check_token('abc', storage))

    def test_create_token__wrong_password(self):
        account = Account('katya')
        account._check_password = lambda p, s: False

        with self.assertRaises(InvalidPasswordError):
            account.create_token('abc', None)

    @patch('notes.account.uuid4')
    def test_create_ro_token(self, patched_uuid4):
        patched_uuid4.return_value = 'UUID'

        storage = MagicMock()
        account = Account('katya')
        account._check_token = lambda t, s: True

        account.create_ro_token('abc', storage)

        storage.set.assert_called_once_with('ro_token:UUID', 'katya')

    def test_create_token__wrong_token(self):
        account = Account('katya')
        account._check_token = lambda p, s: False

        with self.assertRaises(InvalidTokenError):
            account.create_ro_token('abc', None)
