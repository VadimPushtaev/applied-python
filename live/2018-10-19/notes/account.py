from crypt import crypt, mksalt, METHOD_SHA512
from uuid import uuid4

from notes.access import check_password, check_token, get_account_key, get_token_key, get_ro_token_key


class Account:
    def __init__(self, username):
        self._username = username

    @classmethod
    def create(cls, username, password, storage):
        key = get_account_key(username)

        salt = mksalt(METHOD_SHA512)
        digest = crypt(password, salt)
        storage.set(key, digest)

    def _check_password(self, password, storage):
        return check_password(self._username, password, storage)

    def _check_token(self, token, storage):
        return check_token(token, self._username, storage)

    def create_token(self, password, storage):
        if not self._check_password(password, storage):
            raise InvalidPasswordError()

        token = str(uuid4())
        key = get_token_key(token)
        storage.set(key, self._username)

    def create_ro_token(self, master_token, storage):
        if not self._check_token(master_token, storage):
            raise InvalidTokenError()

        token = str(uuid4())
        key = get_ro_token_key(token)
        storage.set(key, self._username)


class InvalidPasswordError(Exception):
    pass


class InvalidTokenError(Exception):
    pass
