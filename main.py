import os 
import csv


class Items:
    all = []
    def __init__(self,name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity 
        Items.all.append(self)
    def info(self):
        print(f"There is {self.name} and price per pices {self.price} stroed more than {self.quantity}")
    def total_price (self):
        total =  self.price * self.quantity
        return total
    def avrage_price (self,total_price):
        avrage = total_price / self.quantity
        return avrage 
    @classmethod
    def imoprt_from_csv (cls):
        script_path = os.path.dirname(os.path.abspath(__file__))
        csv_path = os.path.join(script_path, 'employees.csv')

        with open(csv_path, 'r') as f :

            reader = csv.DictReader(f)
            items = list(reader)

        created_items = []

        for item in items :
            print(item)
            name = item.get('name')
            price_str = item.get('price')
            quantity_str = item.get('quantity')

            if name is not None and price_str is not None and quantity_str is not None:
                try:
                    price = float(price_str)
                    quantity = int(quantity_str)

                    created_item = Items(
                        name= name,
                        price = price,
                        quantity = quantity 
                    )
                    created_items.append(created_item)
                except ValueError as e:
                        price(f"Error crating item '{name}' : {e} ")
        return created_items 
    def __repr__(self):
        return f"Items({self.name}, {self.price}, {self.quantity})"

    
 
 
# item1 = Items("Mobile", 12900, 100 )
# item2 = Items("Laptop", 13000, 150 )
# item3 = Items("Computer", 14300, 58 )

created_items = Items.imoprt_from_csv()
print(created_items)



                   
