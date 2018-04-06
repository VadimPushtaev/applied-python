from datetime import datetime

from action import Action
from repository import Repository
from tests import BaseTestCase


class RepositoryTestCase(BaseTestCase):
    def setUp(self):
        super().setUp()

        self._action1 = Action('action1', [
            (2, self._resource1),
            (3, self._resource2),
        ])
        self._action2 = Action('action2', [
            (3, self._resource3),
            (3, self._resource2),
        ])
        self._repository = Repository([self._action1, self._action2])

    def test_do_action(self):
        dt = datetime(2018, 1, 1)
        self.assertTrue(self._repository.do_action('action1', dt))
        self.assertFalse(self._repository.do_action('action1', dt))

        with self.assertRaises(ValueError):
            self._repository.do_action('UNKNOWN', datetime(2018, 1, 1))

    def test__get_action_by_name(self):
        self.assertIs(self._repository._get_action_by_name('action1'), self._action1)
        self.assertIs(self._repository._get_action_by_name('action2'), self._action2)
        self.assertIsNone(self._repository._get_action_by_name('UNKNOWN'))

    def test__get_actions_index(self):
        self.assertDictEqual(
            self._repository._get_actions_index(),
            dict(action1=self._action1, action2=self._action2)
        )
