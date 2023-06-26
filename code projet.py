# -*- coding: utf-8 -*-
"""
Created on Thu May 21 10:20:29 2023

@author: mekki
"""

import pandas as pd
class Personne:
    def __init__(self, personne_id, name=None, address=None, phone_number=None):
        self._personne_id = personne_id
        self._name = name
        self._address = address
        self._phone_number = phone_number
    
    def get_id(self):
        return self._personne_id
    
    def set_id(self, personne_id):
        self._personne_id = personne_id
    id=property(get_id,set_id)
    
    def get_name(self):
        return self._name
    def set_name(self, name):
        self._name = name
    name=property(get_name,set_name)
    
    def get_address(self):
        return self._address
    
    def set_address(self, address):
        self._address = address
    address=property(get_address,set_address)
    
    def get_phone_number(self):
        return self._phone_number
    
    def set_phone_number(self, phone_number):
        self._phone_number = phone_number
    phone=property(get_phone_number,set_phone_number)

class Supplier(Personne):
    def __init__(self, supplier_id, name=None, address=None, phone_number=None):
        super().__init__(supplier_id, name, address, phone_number)
        self._supplier_id = supplier_id
    
    def get_supplier_id(self):
        return self._supplier_id
    
    def set_supplier_id(self, supplier_id):
        self._supplier_id = supplier_id
    id=property(get_supplier_id,set_supplier_id)

class Employee(Personne):
    def __init__(self, employee_id, name=None, address=None, phone_number=None, position=None, salary=None):
        super().__init__(employee_id, name, address, phone_number)
        self._employee_id = employee_id
        self._position = position
        self._salary = salary
        self.phone_number=phone_number
        self.name=name

    def get_employee_id(self):
        return self._employee_id
    
    def set_employee_id(self, employee_id):
        self._employee_id = employee_id
    emp_id=property(get_employee_id,set_employee_id)
    
    def get_position(self):
        return self._position
    
    def set_position(self, position):
        self._position = position
    position=property(get_position,set_position)
    
    def get_salary(self):
        return self._salary

    def set_salary(self, salary):
        self._salary = salary
    salary=property(get_salary,set_salary)

    def get_phone_number(self):
        return self.phone_number

    def set_phone_number(self,phone):
        self.phone_number=phone
    phone=property(get_phone_number,set_phone_number)


class Client(Personne):
    def __init__(self, client_id, name=None, address=None, phone_number=None):
        super().__init__(client_id, name, address, phone_number)
        self._client_id = client_id
    def get_client_id(self):
        return self._client_id
    
    def set_client_id(self, client_id):
        self._client_id = client_id
    clt_id=property(get_client_id,set_client_id)


class Database:
    def __init__(self):
        self.employees = []
        self.products = []
        self.orders = []
        self.clients = []
        self.warehouse = Warehouse(capacity=1000) #on peut changer la capacité si nécessaire 
        self.sales = []
        self.suppliers = []
        self.invoices = []
        self.reports = []

    def add_employee(self, employee):
        self.employees.append(employee)

    def add_product(self, product):
        self.products.append(product)

    def add_order(self, order):
        self.orders.append(order)

    def add_client(self, client):
        self.clients.append(client)

    def add_sale(self, sale):
        self.sales.append(sale)

    def add_supplier(self, supplier):
        self.suppliers.append(supplier)

    def add_invoice(self, invoice):
        self.invoices.append(invoice)

    def add_report(self, report):
        self.reports.append(report)

    def show_database(self):
        print("Employees:")
        for employee in self.employees:
            print(employee.get_employee_id(), employee.get_name(), employee.get_position())
        
        print("\nProducts:")
        for product in self.products:
            print(product.get_product_id(), product.get_name(), product.get_price())
        
        print("\nOrders:")
        for order in self.orders:
            print(order.get_order_id(), order.get_client_id(), order.get_products(), order.get_order_date())
        
        print("\nClients:")
        for client in self.clients:
            print(client.get_client_id(), client.get_name(), client.get_address())
        
        print("\nSales:")
        for sale in self.sales:
            print(sale.get_sale_id(), sale.get_product_id(), sale.get_quantity(), sale.get_sale_date())
        
        print("\nSuppliers:")
        for supplier in self.suppliers:
            print(supplier.get_supplier_id(), supplier.get_name(), supplier.get_address())
        
        print("\nInvoices:")
        for invoice in self.invoices:
            print(invoice.get_invoice_id(), invoice.get_client_id(), invoice.get_invoice_date(), invoice.get_total_amount())
        
        print("\nReports:")
        for report in self.reports:
            print(report.get_report_id(), report.get_title(), report.get_report_date(), report.get_data())


class Product:
    def __init__(self, product_id, description=None, price=None, quantity_in_stock=None):
        self._product_id = product_id
        self._description = description
        self._price = price
        self._quantity_in_stock = quantity_in_stock
    
    def get_product_id(self):
        return self._product_id
    
    def set_product_id(self, product_id):
        self._product_id = product_id
    id=property(get_product_id,set_product_id)
    
    def get_description(self):
        return self._description
    
    def set_description(self, description):
        self._description = description
    description=property(get_description,set_description)

    def get_price(self):
        return self._price
    
    def set_price(self, price):
        self._price = price
    prix=property(get_price,set_price)
    
    def get_quantity_in_stock(self):
        return self._quantity_in_stock
    
    def set_quantity_in_stock(self, quantity_in_stock):
        self._quantity_in_stock = quantity_in_stock

    stock=property(get_quantity_in_stock,set_quantity_in_stock)
    

class Order:
    def __init__(self, order_id, order_date=None, client=None, products=None):
        self._order_id = order_id
        self._order_date = order_date
        self._client = client
        self._products = products
    
    def get_order_id(self):
        return self._order_id
    
    def set_order_id(self, order_id):
        self._order_id = order_id
    id=property(get_order_id,set_order_id)
    
    def get_order_date(self):
        return self._order_date
    
    def set_order_date(self, order_date):
        self._order_date = order_date
    date=property(get_order_date,set_order_date)
    
    def get_client(self):
        return self._client
    
    def set_client(self, client):
        self._client = client
    client=property(get_client,set_client)
    
    def get_products(self):
        return self._products
    
    def set_products(self, products):
        self._products = products
    product=property(get_products,set_products)


class Warehouse:
    def __init__(self, capacity=None,quantity_in_stock=None,products_in_stock=None):
        self._capacity = capacity
        self._products_in_stock = products_in_stock
        self._quantity_in_stock=quantity_in_stock

    def get_capacity(self):
        return self._capacity
    
    def set_capacity(self, capacity):
        self._capacity = capacity
    capacity=property(get_capacity,set_capacity)
    
    def get_products_in_stock(self):
        return self._products_in_stock
    
    def add_product(self, product):
        self._products_in_stock.append(product)
    
    def remove_product(self, product):
        self._products_in_stock.remove(product)
    products=property(get_products_in_stock,add_product,remove_product)

    def get_quantity_in_stock(self):
        return self._quantity_in_stock
    def set_quantity_in_stock(self,q):
        self._quantity_in_stock=q
    quantity=property(get_quantity_in_stock,set_quantity_in_stock)


class Sales:
    def __init__(self,client, sale_date=None, product=None, quantity_sold=None, sale_price=None):
        self._sale_date = sale_date
        self._product = product
        self._quantity_sold = quantity_sold
        self._sale_price = sale_price
        self._client = client
    
    def get_sale_date(self):
        return self._sale_date
    
    def set_sale_date(self, sale_date):
        self._sale_date = sale_date
    sale_date=property(get_sale_date,set_sale_date)
    
    def get_product(self):
        return self._product
    
    def set_product(self, product):
        self._product = product
    prod=property(get_product,set_product)
    
    def get_quantity_sold(self):
        return self._quantity_sold
    
    def set_quantity_sold(self, quantity_sold):
        self._quantity_sold = quantity_sold
    sold=property(get_quantity_sold,set_quantity_sold)
    
    def get_sale_price(self):
        return self._sale_price
    
    def set_sale_price(self, sale_price):
        self._sale_price = sale_price
    price=property(get_sale_price,set_sale_price)
    
    def get_client(self):
        return self._client
    
    def set_client(self, client):
        self._client = client
    client=property(get_client,set_client)

    def report(self, products):
        sales_per_client = {}
        for sale in self.sales:
            client = sale.get_client().get_client_id()
            quantity_sold = sale.get_quantity_sold()
            if client in sales_per_client:
                sales_per_client[client] += quantity_sold
            else:
                sales_per_client[client] = quantity_sold

        average_sales_per_client = {client: total_sales / len(self.sales) for client, total_sales in sales_per_client.items()}

        sales_per_product = {}
        for sale in self.sales:
            product = sale.get_product().get_product_id()
            quantity_sold = sale.get_quantity_sold()
            if product in sales_per_product:
                sales_per_product[product] += quantity_sold
            else:
                sales_per_product[product] = quantity_sold

        total_revenue = sum(sale.get_sale_price() * sale.get_quantity_sold() for sale in self.sales)

        delivery_times = [(sale.get_sale_date() - sale.get_client().get_registration_date()).days for sale in self.sales]
        average_delivery_time = sum(delivery_times) / len(delivery_times)

        most_demanded_product = max(sales_per_product, key=sales_per_product.get)

        return {
            "average_sales_per_client": average_sales_per_client,
            "total_sales_per_product": sales_per_product,
            "total_revenue": total_revenue,
            "average_delivery_time": average_delivery_time,
            "most_demanded_product": most_demanded_product }

  
    def generate_report(self):
        revenue = self._quantity_sold * self._sale_price
        report_date = self._sale_date 
        report = report(report_date, revenue)
        return report
    
class Invoice:
    def __init__(self, invoice_id, invoice_date=None, total_amount=None, products=None):
        self._invoice_id = invoice_id
        self._invoice_date = invoice_date
        self._total_amount = total_amount
        self._products = products
    
    def get_invoice_id(self):
        return self._invoice_id
    
    def set_invoice_id(self, invoice_id):
        self._invoice_id = invoice_id
    id=property(get_invoice_id,set_invoice_id)
    
    def get_invoice_date(self):
        return self._invoice_date
    
    def set_invoice_date(self, invoice_date):
        self._invoice_date = invoice_date
    date=property(get_invoice_date,set_invoice_date)
    
    def get_total_amount(self):
        return self._total_amount
    
    def set_total_amount(self, total_amount):
        self._total_amount = total_amount
    total_amount=property(get_total_amount,set_total_amount)
    
    def get_products(self):
        return self._products
    
    def set_products(self, products):
        self._products = products
    products=property(get_products,set_products)






###### TESTS 

# For Personne class
df1 = pd.read_csv("C:/Users/mekki/OneDrive/Documents/Projet Stage/test_class_personne.csv")
personne_instances = []
for index, row in df1.iterrows():
    personne_id = row['personne_id']
    name = row['name']
    address = row['address']
    phone_number = row['phone_number']
    personne = Personne(personne_id, name, address, phone_number)
    personne_instances.append(personne)
#for personne in personne_instances:
    #print(personne.id, personne.name, personne.address, personne.phone)

#For Supplier class
df2=pd.read_csv("C:/Users/mekki/OneDrive/Documents/Projet Stage/test_class_supplier.csv")
supplier_instances = []
for index, row in df2.iterrows():
    supplier_id = row['supplier_id']
    name = row['name']
    address = row['address']
    phone_number = row['phone_number']
    supplier = Supplier(supplier_id, name, address, phone_number)
    supplier_instances.append(supplier)
#for  supp in supplier_instances:
    #print(supp.id,supp.name,supp.address,supp.phone)

#For Employee class 
df3=pd.read_csv("C:/Users/mekki/OneDrive/Documents/Projet Stage/test_class_employee.csv")
employee_instances = []
for index, row in df3.iterrows():
    employee_id = row['employee_id']
    name = row['name']
    address = row['address']
    phone_number = row['phone_number']
    position=row['position']
    salary=row['salary']
    employee = Employee(employee_id, name, address, phone_number,position,salary)
    employee_instances.append(employee)
#for employee in employee_instances:
    #print(employee.id,employee.name,employee.address,employee.phone,employee.position,employee.salary)

#For Client class

df4=pd.read_csv("C:/Users/mekki/OneDrive/Documents/Projet Stage/test_class_client.csv")
client_instances = []
for index, row in df4.iterrows():
    client_id = row['client_id']
    name = row['name']
    address = row['address']
    phone_number = row['phone_number']
    client = Client(client_id, name, address, phone_number)
    client_instances.append(client)
#for client in client_instances:
    #print(client.id,client.name,client.address,client.phone)

#For product class
df5=pd.read_csv("C:/Users/mekki/OneDrive/Documents/Projet Stage/test_class_product.csv")
product_instances = []

for index, row in df5.iterrows():
    product_id = row['product_id']
    description = row['description']
    price = row['price']
    quantity_in_stock = row['quantity_in_stock']
    product = Product(product_id, description, price, quantity_in_stock)
    product_instances.append(product)

#for product in product_instances:
    #print(product.id, product.description, product.prix, product.stock)

#For Order class
df6=pd.read_csv("C:/Users/mekki/OneDrive/Documents/Projet Stage/test_class_order.csv")
order_instances = []

for index, row in df6.iterrows():
    order_id = row['order_id']
    order_date = row['order_date']
    client = row['client_id']
    products = row['product_ids']
    order = Order(order_id, order_date, client, products)
    order_instances.append(order)

#for order in order_instances:
    #print(order.id, order.date, order.client, order.product)

#For Invoice class

df7=pd.read_csv("C:/Users/mekki/OneDrive/Documents/Projet Stage/test_class_invoice.csv")
invoice_instances = []

for index, row in df7.iterrows():
    invoice_id = row['invoice_id']
    invoice_date = row['invoice_date']
    total_amount = row['total_amount']
    products = row['product_ids']
    invoice = Invoice(invoice_id, invoice_date, total_amount, products)
    invoice_instances.append(invoice)

#for invoice in invoice_instances:
    #print(invoice.id,invoice.date , invoice.total_amount, invoice.products)

#For Warehouse class

df8=pd.read_csv("C:/Users/mekki/OneDrive/Documents/Projet Stage/test_class_warehouse.csv")
warehouse=Warehouse(10000,0) #on a choisit pour le moment capacity=10000
prd=0
for index, row in df8.iterrows():
    quant = row['quantity_in_stock']
    prd+=quant



#### USER INTERFACE 
import tkinter as tk

# Sample data
clients_data = [
    {"client_id": 1, "name": "John Doe", "address": "123 Main St"},
    {"client_id": 2, "name": "Jane Smith", "address": "456 Elm St"},
    {"client_id": 3, "name": "Mike Johnson", "address": "789 Oak St"}
]

employees_data = [
    {"employee_id": 1, "name": "Alice Johnson", "position": "Manager"},
    {"employee_id": 2, "name": "Bob Smith", "position": "Salesperson"},
    {"employee_id": 3, "name": "Eve Davis", "position": "Assistant"}
]

products_data = [
    {"product_id": 1, "name": "Product A", "price": 10.99},
    {"product_id": 2, "name": "Product B", "price": 5.99},
    {"product_id": 3, "name": "Product C", "price": 7.99}
]

orders_data = [
    {"order_id": 1, "product": "Product A", "quantity": 2},
    {"order_id": 2, "product": "Product C", "quantity": 5},
    {"order_id": 3, "product": "Product B", "quantity": 3}
]

suppliers_data = [
    {"supplier_id": 1, "name": "Supplier X", "address": "123 Supplier St"},
    {"supplier_id": 2, "name": "Supplier Y", "address": "456 Supplier St"},
    {"supplier_id": 3, "name": "Supplier Z", "address": "789 Supplier St"}
]

window = tk.Tk()
window.title("Database Viewer")

login_window = tk.Toplevel(window)
login_window.title("Login")

username_label = tk.Label(login_window, text="Username (Employee Name):")
username_label.pack()
username_entry = tk.Entry(login_window)
username_entry.pack()

password_label = tk.Label(login_window, text="Password (Employee ID):")
password_label.pack()
password_entry = tk.Entry(login_window, show="*")
password_entry.pack()


def login():
    employee_name = username_entry.get()
    employee_id = password_entry.get()

    for employee in employees_data:
        if employee["name"] == employee_name and str(employee["employee_id"]) == employee_id:
            # Remove login window and show the main window
            login_window.destroy()
            window.deiconify()
            break
    else:
        # Clear the username and password fields
        username_entry.delete(0, tk.END)
        password_entry.delete(0, tk.END)
        # Show an error message
        error_label.config(text="Invalid employee name or ID")

        
login_button = tk.Button(login_window, text="Login", command=login)
login_button.pack()

error_label = tk.Label(login_window, fg="red")
error_label.pack()

window.withdraw()

menubar = tk.Menu(window)

main_menu = tk.Menu(menubar, tearoff=0)
menubar.add_cascade(label="Main Menu", menu=main_menu)

def show_work_in_progress():
    output.delete(1.0, tk.END)
    output.insert(tk.END, "WORK IN PROGRESS")

main_menu.add_command(label="WORK IN PROGRESS", command=show_work_in_progress)

clients_menu = tk.Menu(menubar, tearoff=0)
menubar.add_cascade(label="Clients", menu=clients_menu)

def list_clients():
    output.delete(1.0, tk.END)
    for client in clients_data:
        output.insert(tk.END, f"Client ID: {client['client_id']}\nName: {client['name']}\nAddress: {client['address']}\n\n")

clients_menu.add_command(label="List", command=list_clients)
clients_menu.add_command(label="Return to Main Menu", command=show_work_in_progress)

employees_menu = tk.Menu(menubar, tearoff=0)
menubar.add_cascade(label="Employees", menu=employees_menu)

def list_employees():
    output.delete(1.0, tk.END)
    for employee in employees_data:
        output.insert(tk.END, f"Employee ID: {employee['employee_id']}\nName: {employee['name']}\nPosition: {employee['position']}\n\n")

employees_menu.add_command(label="List", command=list_employees)
employees_menu.add_command(label="Return to Main Menu", command=show_work_in_progress)

products_menu = tk.Menu(menubar, tearoff=0)
menubar.add_cascade(label="Products", menu=products_menu)

def list_products():
    output.delete(1.0, tk.END)
    for product in products_data:
        output.insert(tk.END, f"Product ID: {product['product_id']}\nName: {product['name']}\nPrice: {product['price']}\n\n")

products_menu.add_command(label="List", command=list_products)
products_menu.add_command(label="Return to Main Menu", command=show_work_in_progress)

orders_menu = tk.Menu(menubar, tearoff=0)
menubar.add_cascade(label="Orders", menu=orders_menu)

def list_orders():
    output.delete(1.0, tk.END)
    for order in orders_data:
        output.insert(tk.END, f"Order ID: {order['order_id']}\nProduct: {order['product']}\nQuantity: {order['quantity']}\n\n")

orders_menu.add_command(label="List", command=list_orders)
orders_menu.add_command(label="Return to Main Menu", command=show_work_in_progress)

suppliers_menu = tk.Menu(menubar, tearoff=0)
menubar.add_cascade(label="Suppliers", menu=suppliers_menu)

def list_suppliers():
    output.delete(1.0, tk.END)
    for supplier in suppliers_data:
        output.insert(tk.END, f"Supplier ID: {supplier['supplier_id']}\nName: {supplier['name']}\nAddress: {supplier['address']}\n\n")

suppliers_menu.add_command(label="List", command=list_suppliers)
suppliers_menu.add_command(label="Return to Main Menu", command=show_work_in_progress)

output = tk.Text(window)
output.pack(fill=tk.BOTH, expand=True)

window.config(menu=menubar)

window.mainloop()
