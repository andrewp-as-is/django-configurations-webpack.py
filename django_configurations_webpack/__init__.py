from configurations import Configuration, values


class WebpackMixin:

    @classmethod
    def pre_setup(cls):
        super(WebpackMixin, cls).pre_setup()
        builtin = 'webpack_loader.templatetags.webpack_loader'
        if not hasattr(cls, 'TEMPLATES') or not cls.TEMPLATES:
            cls.TEMPLATES = [{}]
        if 'OPTIONS' not in cls.TEMPLATES[0]:
            cls.TEMPLATES[0]['OPTIONS'] = {}
        if 'builtins' not in cls.TEMPLATES[0]['OPTIONS']:
            cls.TEMPLATES[0]['OPTIONS']['builtins'] = [builtin]
        if builtin not in cls.TEMPLATES[0]['OPTIONS']['builtins']:
            cls.TEMPLATES[0]['OPTIONS']['builtins'].append(builtin)

    @classmethod
    def setup(cls):
        super(WebpackMixin, cls).setup()
        if 'webpack_loader' not in cls.INSTALLED_APPS:
            cls.INSTALLED_APPS.append('webpack_loader')
        cls.WEBPACK_LOADER = {'DEFAULT': {
            'STATS_FILE': cls.WEBPACK_STATS_FILE
        }}


class WebpackDevMixin(WebpackMixin):
    WEBPACK_STATS_FILE = values.Value('./webpack-stats.json')
    CORS_ALLOW_CREDENTIALS = True
    CORS_ORIGIN_ALLOW_ALL = True

    @classmethod
    def setup(cls):
        super(WebpackDevMixin, cls).setup()
        if 'corsheaders' not in cls.INSTALLED_APPS:
            cls.INSTALLED_APPS.append('corsheaders')
        if 'corsheaders.middleware.CorsMiddleware' not in cls.MIDDLEWARE:
            cls.MIDDLEWARE.append('corsheaders.middleware.CorsMiddleware')


class WebpackProdMixin(WebpackMixin):
    WEBPACK_STATS_FILE = values.Value('./webpack-stats-prod.json')


class WebpackDevConfiguration(WebpackDevMixin, Configuration):
    pass


class WebpackProdConfiguration(WebpackProdMixin, Configuration):
    pass
