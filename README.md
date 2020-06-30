<!--
https://readme42.com
-->


[![](https://img.shields.io/pypi/v/django-configurations-webpack.svg?maxAge=3600)](https://pypi.org/project/django-configurations-webpack/)
[![](https://img.shields.io/badge/License-Unlicense-blue.svg?longCache=True)](https://unlicense.org/)
[![](https://github.com/andrewp-as-is/django-configurations-webpack.py/workflows/tests42/badge.svg)](https://github.com/andrewp-as-is/django-configurations-webpack.py/actions)

### Installation
```bash
$ [sudo] pip install django-configurations-webpack
```

##### `.env`
```bash
DJANGO_WEBPACK_STATS_FILE=./webpack-stats-prod.json # optional
```

#### Examples
`settings.py`
```python
from django_configurations_webpack import WebpackDevConfiguration, WebpackProdConfiguration

class Dev(WebpackDevConfiguration,...):
    ... # WEBPACK_STATS_FILE ./webpack-stats.json by default

class Prod(WebpackProdConfiguration,...):
    ... # WEBPACK_STATS_FILE ./webpack-stats-prod.json by default
```

`webpack.config.js`
```js
var path = require('path');
var BundleTracker = require('webpack-bundle-tracker');

module.exports = {
  output: {
      path: path.resolve('./assets/webpack_bundles/')
  },

  plugins: [
    new BundleTracker({filename: './webpack-stats.json'}) // './webpack-stats-prod.json' (prod)
  ]
}
```

template
```html
{% load render_bundle from webpack_loader %}
<head>
{% render_bundle 'main' 'css' %}
</head>
<body>
...
{% render_bundle 'main' 'js' %}
</body>
```

customize
```python
class Prod(WebpackProdConfiguration,...):
    WEBPACK_STATS_FILE = './webpack-stats-custom.json'
```

#### Links
+   [django-configurations](https://github.com/jazzband/django-configurations)
+   [django-webpack-loader](https://github.com/owais/django-webpack-loader)

<p align="center">
    <a href="https://readme42.com/">readme42.com</a>
</p>