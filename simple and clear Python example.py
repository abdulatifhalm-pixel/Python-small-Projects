# Trader class
class Trader:
    def __init__(self, name):
        self.name = name
        self.products = {}

    def add_product(self, product_name, price, quantity):
        self.products[product_name] = {
            "price": price,
            "quantity": quantity
        }

    def show_products(self):
        print(f"\nProducts available with {self.name}:")
        for product, info in self.products.items():
            print(f"{product} - Price: {info['price']} | Quantity: {info['quantity']}")

    def sell(self, product_name, quantity):
        if product_name in self.products:
            if self.products[product_name]["quantity"] >= quantity:
                total_price = self.products[product_name]["price"] * quantity
                self.products[product_name]["quantity"] -= quantity
                return total_price
            else:
                print("Not enough stock!")
        else:
            print("Product not found!")
        return None


# Customer class
class Customer:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    def buy(self, trader, product_name, quantity):
        cost = trader.sell(product_name, quantity)
        if cost is not None:
            if self.balance >= cost:
                self.balance -= cost
                print(f"{self.name} bought {quantity} {product_name}(s) for {cost}")
            else:
                print("Not enough balance!")


# Main Program
trader = Trader("Ahmad Trader")
trader.add_product("Oil", 100, 50)
trader.add_product("Petrol", 80, 100)

customer = Customer("Latif", 5000)

trader.show_products()
customer.buy(trader, "Oil", 5)

print(f"\nCustomer Balance: {customer.balance}")
trader.show_products()
