from crypt import crypt


def get_account_key(username):
    return f'account:{username}'


def get_token_key(token):
    return f'token:{token}'


def get_ro_token_key(token):
    return f'ro_token:{token}'


def check_password(username, password, storage):
    key = get_account_key(username)
    digest = storage.get(key)
    if digest is None:
        raise NoSuchUserError()

    return crypt(password, digest) == digest


def check_token(token, expected_username, storage):
    key = get_token_key(token)
    username = storage.get(key)
    return username == expected_username


def check_ro_token(token, expected_username, storage):
    key = get_ro_token_key(token)
    username = storage.get(key)
    return username == expected_username


class NoSuchUserError(Exception):
    pass