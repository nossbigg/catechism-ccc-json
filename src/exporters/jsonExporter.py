import jsonpickle

from src.common.config import JSON_STORE_PATH


class JsonStore:
    def __init__(self):
        self.toc_link_tree = []
        self.toc_nodes = {}
        self.page_nodes = {}


def exportStoreAsJson(toc_link_tree, toc_nodes_dict, page_nodes_dict):
    store = JsonStore()
    store.toc_link_tree = toc_link_tree
    store.toc_nodes = toc_nodes_dict
    store.page_nodes = page_nodes_dict

    json_store = jsonpickle.encode(store, unpicklable=False)

    with open(JSON_STORE_PATH, 'w+') as f:
        f.write(json_store)
