class NodeIdGenerator:
    def __init__(self, prefix):
        self.prefix = prefix
        self.counter = 0

    def generate_id(self):
        self.counter = self.counter + 1
        return self.prefix + "-" + str(self.counter)
