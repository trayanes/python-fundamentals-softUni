class Inventory:

    def __init__(self, __capacity: int):
        self.capacity = __capacity
        self.items = []
        self.capacity_left = self.capacity * 1

    def add_item(self, item: str):
        if self.capacity > 0:
            self.items.append(item)
            self.capacity -= 1
        else:
            return "not enough room in the inventory"

    def get_capacity(self):
        return self.capacity_left

    def __repr__(self):
        return f"Items: {self.items}.\n" \
               f"Capacity left: {self.capacity}"


inventory = Inventory(2)
inventory.add_item("potion")
inventory.add_item("sword")
print(inventory.add_item("bottle"))
print(inventory.get_capacity())
print(inventory)
