from crypt import crypt, mksalt, METHOD_SHA512
from uuid import uuid4


class Account:
    def __init__(self, username):
        self._username = username

    @classmethod
    def create(cls, username, password, storage):
        key = cls._get_account_key(username)

        salt = mksalt(METHOD_SHA512)
        digest = crypt(password, salt)
        storage.set(key, digest)

    @classmethod
    def _get_account_key(cls, username):
        return f'account:{username}'

    @classmethod
    def _get_token_key(cls, token):
        return f'token:{token}'

    @classmethod
    def _get_ro_token_key(cls, token):
        return f'ro_token:{token}'

    def _check_password(self, password, storage):
        key = self._get_account_key(self._username)
        digest = storage.get(key)
        if digest is None:
            raise NoSuchUserError()

        return crypt(password, digest) == digest

    def _check_token(self, token, storage):
        key = self._get_token_key(token)
        username = storage.get(key)
        return username == self._username

    def create_token(self, password, storage):
        if not self._check_password(password, storage):
            raise InvalidPasswordError()

        token = str(uuid4())
        key = self._get_token_key(token)
        storage.set(key, self._username)

    def create_ro_token(self, master_token, storage):
        if not self._check_token(master_token, storage):
            raise InvalidTokenError()

        token = str(uuid4())
        key = self._get_ro_token_key(token)
        storage.set(key, self._username)


class InvalidPasswordError(Exception):
    pass


class NoSuchUserError(Exception):
    pass


class InvalidTokenError(Exception):
    pass