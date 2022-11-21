def create_access_tokens(Authorize, email):
    access_token = Authorize.create_access_token(subject=email)
    Authorize.set_access_cookies(access_token)

    return access_token

def create_init_refresh_tokens(Authorize, email):
    refresh_token = Authorize.create_refresh_token(subject=email)
    Authorize.set_refresh_cookies(refresh_token)

    return refresh_token

def refresh_token(Authorize, user):
    new_access_token = Authorize.create_access_token(subject=user)
    Authorize.set_refresh_cookies(new_access_token)

    return new_access_token

