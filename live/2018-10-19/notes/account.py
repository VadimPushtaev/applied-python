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

    def _check_password(self, password, storage):
        key = self._get_account_key(self._username)
        digest = storage.get(key)
        if digest is None:
            raise NoSuchUserError()

        return crypt(password, digest) == digest

    def create_token(self, password, storage):
        if not self._check_password(password, storage):
            raise InvalidPasswordError()

        token = str(uuid4())
        key = self._get_token_key(token)
        storage.set(key, self._username)


class InvalidPasswordError(Exception):
    pass


class NoSuchUserError(Exception):
    pass