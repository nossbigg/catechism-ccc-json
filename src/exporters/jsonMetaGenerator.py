from common.config import JSON_STORE_VERSION
from datetime import datetime
from collections import namedtuple

Meta = namedtuple('Meta', 'version created_at attribution')


def generate_store_meta():
    version = JSON_STORE_VERSION
    created_at = datetime.utcnow().isoformat()
    attribution = ['Libreria Editrice Vaticana',
                   'St. Charles Borromeo Catholic Church']

    return Meta(version, created_at, attribution)
