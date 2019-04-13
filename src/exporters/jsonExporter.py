import simplejson
from collections import namedtuple

from src.common.config import JSON_STORE_PATH

JsonStore = namedtuple('JsonStore', 'toc_link_tree toc_nodes page_nodes')


def exportStoreAsJson(toc_link_tree, toc_nodes_dict, page_nodes_dict):
    store = JsonStore(toc_link_tree, toc_nodes_dict, page_nodes_dict)

    json_store = simplejson.dumps(store)
    with open(JSON_STORE_PATH, 'w+') as f:
        f.write(json_store)
