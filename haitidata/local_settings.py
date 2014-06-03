import os
import geonode

PROJECT_ROOT = os.path.abspath(os.path.dirname(__file__))

DEBUG = TEMPLATE_DEBUG = True

SITENAME = 'GeoNode'
SITEURL = 'http://66.36.241.75/'

DATABASE_ENGINE = 'postgresql_psycopg2'
DATABASE_NAME = 'geonode'
DATABASE_USER = 'geonode'
DATABASE_PASSWORD = 'zXNmt14n'
DATABASE_HOST = 'localhost'
DATABASE_PORT = '5432'

# Make geonode upload vector layers directly to postgis
DB_DATASTORE_NAME = 'cnigs_spatial'
DB_DATASTORE_DATABASE = 'cnigs_spatial'
DB_DATASTORE_USER = 'cnigspg'
DB_DATASTORE_PASSWORD = 'HAITIDATAPASS'
DB_DATASTORE_HOST = DATABASE_HOST
DB_DATASTORE_PORT = DATABASE_PORT
DB_DATASTORE_TYPE='postgis'

DATABASES = {
      'default': {
            'ENGINE': 'django.db.backends.postgresql_psycopg2',
            'NAME': DATABASE_NAME,
            'USER': DATABASE_USER,
            'PASSWORD': DATABASE_PASSWORD,
            'HOST': DATABASE_HOST,
            'PORT': DATABASE_PORT,
        }
    }

DB_DATASTORE=True

LANGUAGE_CODE = 'fr'

MEDIA_ROOT = '/var/www/geonode/uploaded'
STATIC_ROOT = '/var/www/geonode/static/'

# secret key used in hashing, should be a long, unique string for each
# site.  See http://docs.djangoproject.com/en/1.2/ref/settings/#secret-key
#SECRET_KEY = 'KBJ8RrPHQ0xgjTlDO0'

SECRET_KEY = 'fasdfasd4234#@#dfasdfajasnbbbsf'

# The FULLY QUALIFIED url to the GeoServer instance for this GeoNode.
GEOSERVER_BASE_URL = SITEURL + 'geoserver/'

CATALOGUE = {
    'default': {
        # The underlying CSW backend
        # ("pycsw_http", "pycsw_local", "geonetwork", "deegree")
        'ENGINE': 'geonode.catalogue.backends.pycsw_local',
        # The FULLY QUALIFIED base url to the CSW instance for this GeoNode
        'URL': '%scatalogue/csw' % SITEURL,
    }
}

# A Google Maps API key is needed for the 3D Google Earth view of maps
# See http://code.google.com/apis/maps/signup.html
GOOGLE_API_KEY = ''

GEONODE_ROOT = os.path.dirname(geonode.__file__)

TEMPLATE_DIRS = (
    os.path.join(PROJECT_ROOT, 'templates'),
    os.path.join(GEONODE_ROOT, 'templates'),
)

# Additional directories which hold static files
STATICFILES_DIRS = [
    os.path.join(PROJECT_ROOT, 'static'),
    os.path.join(GEONODE_ROOT, 'static'),
]

MAP_BASELAYERS = [{
    "source": {
        "ptype": "gxp_wmscsource",
        "url": GEOSERVER_BASE_URL + "wms",
        "restUrl": "/gs/rest"
     }
  },{
    "source": {"ptype": "gxp_olsource"},
    "type":"OpenLayers.Layer",
    "args":["No background"],
    "visibility": False,
    "fixed": True,
    "group":"background"
  }, {
    "source": {"ptype": "gxp_olsource"},
    "type":"OpenLayers.Layer.OSM",
    "args":["OpenStreetMap"],
    "visibility": False,
    "fixed": True,
    "group":"background"
  }, {
    "source": {"ptype": "gxp_mapquestsource"},
    "name":"osm",
    "group":"background",
    "visibility": True
  }, {
    "source": {"ptype": "gxp_mapquestsource"},
    "name":"naip",
    "group":"background",
    "visibility": False
  }, {
    "source": {"ptype": "gxp_bingsource"},
    "name": "AerialWithLabels",
    "fixed": True,
    "visibility": False,
    "group":"background"
  },{
    "source": {"ptype": "gxp_mapboxsource"},
  }
]

# Uncomment the following to receive emails whenever there are errors in GeoNode
#ADMINS = (
#            ('John', 'john@example.com'), 
#         )

# Uncomment the following to use a Gmail account as the email backend
EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = 'haitidatareg@gmail.com'
EMAIL_HOST_PASSWORD = 'haitidata2013#'
EMAIL_PORT = 587

DEFAULT_FROM_EMAIL = 'noreply@haitidata.org'

# For more information on available settings please consult the Django docs at
# https://docs.djangoproject.com/en/dev/ref/settings
