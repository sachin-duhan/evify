# namiz/settings.py
from namiz.config import Config

MONGO_URI = Config.MONGO_URI

# Eve settings
RESOURCE_METHODS = ['GET', 'POST', 'DELETE']
ITEM_METHODS = ['GET', 'PATCH', 'PUT', 'DELETE']

# Enable pagination
PAGINATION = True

# Register the domain (schemas)
DOMAIN = Config.DOMAIN

