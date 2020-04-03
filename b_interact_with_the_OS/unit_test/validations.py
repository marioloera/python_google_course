

def validate_user(username, minlen):
    # assert may be removed form the execution during optimizer
    assert type(username) == str, "username must be a string"

    if minlen < 1:
        raise ValueError("minlen must be at least 1")

    if len(username) < minlen:
        return False

    if not username.isalnum():
        return False

    return True

