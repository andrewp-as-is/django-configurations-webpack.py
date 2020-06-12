import os

from configurations import Configuration, values

class WebpackConfiguration(Configuration):
    @classmethod
    def pre_setup(cls):
        super(WebpackConfiguration, cls).pre_setup()
        webpack_builtin = 'webpack_loader.templatetags.webpack_loader'
        if not hasattr(cls,'TEMPLATES') or not cls.TEMPLATES:
            cls.TEMPLATES = [{}]
        if 'OPTIONS' not in cls.TEMPLATES[0]:
            cls.TEMPLATES[0]['OPTIONS'] = {}
        if 'builtins' not in cls.TEMPLATES[0]['OPTIONS']:
            cls.TEMPLATES[0]['OPTIONS']['builtins'] = [webpack_builtin]
        if webpack_builtin not in cls.TEMPLATES[0]['OPTIONS']['builtins']:
            cls.TEMPLATES[0]['OPTIONS']['builtins'].append(webpack_builtin)

    @classmethod
    def setup(cls):
        super(WebpackConfiguration, cls).setup()
        if 'webpack_loader' not in cls.INSTALLED_APPS:
            cls.INSTALLED_APPS.append('webpack_loader')
        cls.WEBPACK_LOADER = {'DEFAULT':{
            'STATS_FILE': cls.WEBPACK_STATS_FILE
        }}


class WebpackDevConfiguration(WebpackConfiguration):
    WEBPACK_STATS_FILE = values.Value('./webpack-stats.json')
    CORS_ALLOW_CREDENTIALS = True
    CORS_ORIGIN_ALLOW_ALL = True

    @classmethod
    def setup(cls):
        super(WebpackDevConfiguration, cls).setup()
        if 'corsheaders' not in cls.INSTALLED_APPS:
            cls.INSTALLED_APPS.append('corsheaders')
        if 'corsheaders.middleware.CorsMiddleware' not in cls.MIDDLEWARE:
            cls.MIDDLEWARE.append('corsheaders.middleware.CorsMiddleware')

class WebpackProdConfiguration(WebpackConfiguration):
    WEBPACK_STATS_FILE = values.Value('./webpack-stats-prod.json')
