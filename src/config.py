class Development(object):
    DEBUG = True


class Production(object):
    DEBUG = False


app_config = {
    'development': Development,
    'production': Production,
}
