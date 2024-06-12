class Product():
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __str__(self):
        return f"Product: {self.name} | Price: £{self.price}"
    
    def discount(self, percentage):
        self.price = self.price - (self.price * percentage / 100)
        return f"Discounted price: £{self.price}"
    
    def discount_value(self, value):
        value = value / 100
        return f"Discount value is: {value} OR {value * 100}%"
        
        
item = Product("Phone", 75.50)

print(item)

print(item.discount(20))
print('---------- Discount Value ----------')
print(item.discount_value(20))
