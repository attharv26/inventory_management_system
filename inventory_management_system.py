# author @ Atharv Pandey
# date   : 19th June, 2024
# note   : Feel free to copy, edit and modify this code


import pandas as pd
import os
class Inventory:
    def __init__(self):
        self.products = []
        self.quantities = []
        self.id=[]
        
        
    def add_product(self, product = ' '  ,  code = 0) -> None:
        self.products.append(product)
        self.id.append(code)
        try:
            quantity = int(input('Enter the Quantity:'))
        except:
            print('Quantity entered is not valid')
            return
        self.quantities.append(quantity)
        self.save_changes()
        
        
    def update_quantity(self, identifier) -> None:
        try:
            if identifier.isdigit():
                index = self.id.index(int(identifier))
            else:
                index = self.products.index(identifier)
        except:
            print('No such product in inventory ')
            return
        self.quantities[index] = int(input('Enter the quantity:'))
        self.save_changes()
        
        
    def save_changes(self) -> None:
        data = {'Product': self.products, 'product id': self.id, 'Quantity': self.quantities}
        df = pd.DataFrame(data)
        df.to_csv('inventory_report.csv', index=False)
        print("Inventory updated\n")
        
        
    def display(self) -> None:
        try:
            df = pd.read_csv('inventory_report.csv')
            print(df)
        except:
            print("create an inventory first".upper())
            return

    def sale(self, identifier) -> None:
        try:
            if identifier.isdigit():
                index = self.id.index(int(identifier))
            else:
                index = self.products.index(identifier)
        except:
            print('No such product in inventory ')
            return
        self.quantities[index] -= int(input('Enter the quantity sold:'))
        self.save_changes()
    def read_file(self):
        df= pd.read_csv('inventory_report.csv')
        data = df.to_dict()
        for keys in data['Product'].keys():
            self.products.append(((data['Product'])[keys]))
        for keys in data['product id'].keys():
            self.id.append(((data['product id'])[keys]))
        for keys in data['Quantity'].keys():
            self.quantities.append(((data['Quantity'])[keys]))
    
    
    def delete_item(self, identifier) -> None:
        index = 0
        try:
            if identifier.isdigit():
                index = self.id.index(int(identifier))
            else:
                index = self.products.index(identifier)
        except:
            print('No such product in inventory ')
            return
        del self.products[index]
        del self.id[index]
        del self.quantities[index]
        self.save_changes()
        
        
    def clear_inventory(self):
        self.products.clear()
        self.id.clear()
        self.quantities.clear()
        try:
            os.remove('inventory_report.csv')
        except:
            print('INVENTORY DOES NOT EXIST')
            
            
inventory = Inventory()
try:
    inventory.read_file()
except:
    print('Create an inventory')
while(True):
        print(' 1:Add product \n 2:update quantity \n 3:see inventory \n 4:item sale \n 5:delete item \n 6:clear inventory \n 7:exit menu')
        match (int(input("enter your choice: "))):
            case 1:
                name = input("Enter product name: ").strip().casefold()
                try:
                    digi = int(input("Enter product id: "))
                except:
                    digi = 0
                    print('NO ID ENTERED')
                if name == '':
                    inventory.add_product(code=digi)
                else:
                    inventory.add_product(product=name, code= digi)
            case 2:
                identifier = input('Enter product name or ID:" ').strip().casefold()
                inventory.update_quantity(identifier)
            case 3:
                inventory.display()
            case 4:
                inventory.sale((input('Enter product name or code: ')).strip().casefold())
            case 5:
                inventory.delete_item((input('Enter product name or code: ')).strip().casefold())
            case 6:
                inventory.clear_inventory()
            case 7:
                break
            case _:
                print("INVALID CHOICE")