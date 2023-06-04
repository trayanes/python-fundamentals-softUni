class Storage:
    storage = []

    def __init__(self, capacity):
        self.capacity = capacity

    def add_product(self, product: str):
        if self.capacity > 0:
            Storage.storage.append(product)
        self.capacity -= 1

    def get_products(self):
        return Storage.storage


storage_obj = Storage(4)
storage_obj.add_product("apple")
storage_obj.add_product("banana")
storage_obj.add_product("potato")
storage_obj.add_product("tomato")
storage_obj.add_product("bread")
print(storage_obj.get_products())
