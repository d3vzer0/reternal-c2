import logging
from workers.main import rediscache

rediscache.delete('cache-empiretoken')
empirelog = logging.getLogger('rtempire')
