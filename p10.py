class Inventory:
    def __init__(self):
        self.items = {}

    def add_item(self, name, qty, price):
        self.items[name] = (qty, price)

    def remove_item(self, name):
        if name not in self.items:
            raise KeyError("No item named " + name)
        del self.items[name]

    def total_value(self):
        total = 0
        for qty, price in self.items.values():
            total += qty * price
        return total

    def __len__(self):
        return len(self.items)

with open("stock.txt", "w") as file:
    file.write("pen,10,25\n")
    file.write("notebook,5,120\n")
    file.write("bag,abc,1500\n")
    file.write("marker,4,80\n")

inv = Inventory()

with open("stock.txt", "r") as file:
    for line in file:
        data = line.strip().split(",")

        if len(data) != 3:
            print("Skipping invalid line")
            continue

        name, qty, price = data

        try:
            qty = int(qty)
            price = int(price)
            inv.add_item(name, qty, price)

        except ValueError:
            print("Skipping " + name + ": bad number")

print(len(inv), "items, total value", inv.total_value())
inv.remove_item("pen")
print(len(inv), "items, total value", inv.total_value())

try:
    inv.remove_item("laptop")
except KeyError as e:
    print("Error:", e)
    