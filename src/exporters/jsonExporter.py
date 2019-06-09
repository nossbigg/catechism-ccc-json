import simplejson
from collections import namedtuple

from common.config import JSON_STORE_PATH

JsonStore = namedtuple(
    'JsonStore', 'toc_link_tree toc_nodes page_nodes ccc_refs')


def exportStoreAsJson(toc_link_tree, toc_nodes_dict, page_nodes_dict, ccc_refs):
    store = JsonStore(toc_link_tree, toc_nodes_dict, page_nodes_dict, ccc_refs)

    json_store = simplejson.dumps(store)
    with open(JSON_STORE_PATH, 'w+') as f:
        f.write(json_store)
