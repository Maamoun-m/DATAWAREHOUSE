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
    def __init__(self, employee_id, name=None, address=None, phone_number=None, position=None, salary=None, authority=None):
        super().__init__(employee_id, name, address, phone_number)
        self._employee_id = employee_id
        self._position = position
        self._salary = salary
        self.phone_number = phone_number
        self.name = name
        self._authority = authority

    def get_employee_id(self):
        return self._employee_id

    def set_employee_id(self, employee_id):
        self._employee_id = employee_id
    emp_id = property(get_employee_id, set_employee_id)

    def get_position(self):
        return self._position

    def set_position(self, position):
        self._position = position
    position = property(get_position, set_position)

    def get_salary(self):
        return self._salary

    def set_salary(self, salary):
        self._salary = salary
    salary = property(get_salary, set_salary)

    def get_phone_number(self):
        return self.phone_number

    def set_phone_number(self, phone):
        self.phone_number = phone
    phone = property(get_phone_number, set_phone_number)

    def get_authority(self):
        return self._authority

    def set_authority(self, authority):
        self._authority = authority
    authority = property(get_authority, set_authority)



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
from tkinter import ttk
from tkinter import simpledialog, messagebox
import datetime

# Sample data
clients_data = [
    {"client_id": 1, "name": "John Doe", "address": "123 Main St", "date": datetime.date(2021, 1, 1)},
    {"client_id": 2, "name": "Jane Smith", "address": "456 Elm St", "date": datetime.date(2021, 1, 2)},
    {"client_id": 3, "name": "Mike Johnson", "address": "789 Oak St", "date": datetime.date(2021, 1, 3)}
]

products_data = [
    {"product_id": 1, "name": "Product A", "price": 10.0},
    {"product_id": 2, "name": "Product B", "price": 20.0},
    {"product_id": 3, "name": "Product C", "price": 30.0}
]

sales_data = [
    {"sale_id": 1, "client_id": 1, "product_id": 2, "quantity": 5, "date": datetime.date(2021, 1, 4)},
    {"sale_id": 2, "client_id": 2, "product_id": 3, "quantity": 3, "date": datetime.date(2021, 1, 5)},
    {"sale_id": 3, "client_id": 3, "product_id": 1, "quantity": 2, "date": datetime.date(2021, 1, 6)}
]

invoices_data = [
    {"invoice_id": 1, "sale_id": 1, "amount": 100.0, "date": datetime.date(2021, 1, 7)},
    {"invoice_id": 2, "sale_id": 2, "amount": 90.0, "date": datetime.date(2021, 1, 8)},
    {"invoice_id": 3, "sale_id": 3, "amount": 60.0, "date": datetime.date(2021, 1, 9)}
]

employees_data = [
    {"employee_id": 1, "name": "Alice Johnson", "position": "Manager", "authority": "admin"},
    {"employee_id": 2, "name": "Bob Smith", "position": "Salesperson", "authority": "user"},
    {"employee_id": 3, "name": "Eve Davis", "position": "Assistant", "authority": "user"}
]


window = tk.Tk()
window.title("Database Viewer")

def login():
    employee_name = username_entry.get()
    employee_id = password_entry.get()

    for employee in employees_data:
        if employee["name"] == employee_name and str(employee["employee_id"]) == employee_id:
            # Remove login window and show the main window
            login_window.destroy()
            window.deiconify()
            if employee["authority"] == "admin":
                enable_editing()
            break
    else:
        # Clear the username and password fields
        username_entry.delete(0, tk.END)
        password_entry.delete(0, tk.END)
        # Show an error message
        error_label.config(text="Invalid employee name or ID")

def enable_editing():
    clients_menu.entryconfig("Add", state="normal")
    clients_menu.entryconfig("Modify", state="normal")
    clients_menu.entryconfig("Delete", state="normal")

    products_menu.entryconfig("Add", state="normal")
    products_menu.entryconfig("Modify", state="normal")
    products_menu.entryconfig("Delete", state="normal")

    sales_menu.entryconfig("Add", state="normal")
    sales_menu.entryconfig("Modify", state="normal")
    sales_menu.entryconfig("Delete", state="normal")

    invoices_menu.entryconfig("Add", state="normal")
    invoices_menu.entryconfig("Modify", state="normal")
    invoices_menu.entryconfig("Delete", state="normal")

def list_clients():
    output.delete(*output.get_children())
    for client in clients_data:
        output.insert("", tk.END, text="Client", values=(client["client_id"], client["name"], client["address"], client["date"]))

def add_client():
    name = simpledialog.askstring("Add Client", "Enter client name:")
    if name:
        address = simpledialog.askstring("Add Client", "Enter client address:")
        if address:
            date = prompt_date()
            if date:
                client_id = len(clients_data) + 1
                client = {"client_id": client_id, "name": name, "address": address, "date": date}
                clients_data.append(client)
                list_clients()

def modify_client():
    selected_item = output.focus()
    if selected_item:
        item = output.item(selected_item)
        values = item["values"]
        client_id = values[0]
        for client in clients_data:
            if client["client_id"] == client_id:
                name = simpledialog.askstring("Modify Client", "Enter client name:", initialvalue=client["name"])
                if name:
                    address = simpledialog.askstring("Modify Client", "Enter client address:", initialvalue=client["address"])
                    if address:
                        date = prompt_date()
                        if date:
                            client["name"] = name
                            client["address"] = address
                            client["date"] = date
                            list_clients()
                break

def delete_client():
    selected_item = output.focus()
    if selected_item:
        item = output.item(selected_item)
        values = item["values"]
        client_id = values[0]
        client_name = values[1]
        confirmation = messagebox.askyesno("Delete Client", f"Are you sure you want to delete the client: {client_name} ({client_id})?")
        if confirmation:
            for client in clients_data:
                if client["client_id"] == client_id:
                    clients_data.remove(client)
                    break
            list_clients()

def list_products():
    output.delete(*output.get_children())
    for product in products_data:
        output.insert("", tk.END, text="Product", values=(product["product_id"], product["name"], product["price"]))

def add_product():
    name = simpledialog.askstring("Add Product", "Enter product name:")
    if name:
        price = simpledialog.askfloat("Add Product", "Enter product price:")
        if price:
            product_id = len(products_data) + 1
            product = {"product_id": product_id, "name": name, "price": price}
            products_data.append(product)
            list_products()

def modify_product():
    selected_item = output.focus()
    if selected_item:
        item = output.item(selected_item)
        values = item["values"]
        product_id = values[0]
        for product in products_data:
            if product["product_id"] == product_id:
                name = simpledialog.askstring("Modify Product", "Enter product name:", initialvalue=product["name"])
                if name:
                    price = simpledialog.askfloat("Modify Product", "Enter product price:", initialvalue=product["price"])
                    if price:
                        product["name"] = name
                        product["price"] = price
                        list_products()
                break

def delete_product():
    selected_item = output.focus()
    if selected_item:
        item = output.item(selected_item)
        values = item["values"]
        product_id = values[0]
        product_name = values[1]
        confirmation = messagebox.askyesno("Delete Product", f"Are you sure you want to delete the product: {product_name} ({product_id})?")
        if confirmation:
            for product in products_data:
                if product["product_id"] == product_id:
                    products_data.remove(product)
                    break
            list_products()

def list_sales():
    output.delete(*output.get_children())
    for sale in sales_data:
        client_id = sale["client_id"]
        product_id = sale["product_id"]
        client_name = get_client_name(client_id)
        product_name = get_product_name(product_id)
        output.insert("", tk.END, text="Sale", values=(sale["sale_id"], client_name, product_name, sale["quantity"], sale["date"]))

def add_sale():
    client_id = prompt_client_id()
    if client_id is not None:
        product_id = prompt_product_id()
        if product_id is not None:
            quantity = prompt_quantity()
            if quantity is not None:
                date = prompt_date()
                if date:
                    sale_id = len(sales_data) + 1
                    sale = {"sale_id": sale_id, "client_id": client_id, "product_id": product_id, "quantity": quantity, "date": date}
                    sales_data.append(sale)
                    list_sales()

def modify_sale():
    selected_item = output.focus()
    if selected_item:
        item = output.item(selected_item)
        values = item["values"]
        sale_id = values[0]
        for sale in sales_data:
            if sale["sale_id"] == sale_id:
                client_id = prompt_client_id(initialvalue=sale["client_id"])
                if client_id is not None:
                    product_id = prompt_product_id(initialvalue=sale["product_id"])
                    if product_id is not None:
                        quantity = prompt_quantity(initialvalue=sale["quantity"])
                        if quantity is not None:
                            date = prompt_date(initialvalue=sale["date"])
                            if date:
                                sale["client_id"] = client_id
                                sale["product_id"] = product_id
                                sale["quantity"] = quantity
                                sale["date"] = date
                                list_sales()
                break

def delete_sale():
    selected_item = output.focus()
    if selected_item:
        item = output.item(selected_item)
        values = item["values"]
        sale_id = values[0]
        confirmation = messagebox.askyesno("Delete Sale", f"Are you sure you want to delete the sale: {sale_id}?")
        if confirmation:
            for sale in sales_data:
                if sale["sale_id"] == sale_id:
                    sales_data.remove(sale)
                    break
            list_sales()

def list_invoices():
    output.delete(*output.get_children())
    for invoice in invoices_data:
        sale_id = invoice["sale_id"]
        sale_details = get_sale_details(sale_id)
        client_name = get_client_name(sale_details["client_id"])
        product_name = get_product_name(sale_details["product_id"])
        output.insert("", tk.END, text="Invoice", values=(invoice["invoice_id"], client_name, product_name, sale_details["quantity"], invoice["amount"], invoice["date"]))

def add_invoice():
    sale_id = prompt_sale_id()
    if sale_id is not None:
        amount = simpledialog.askfloat("Add Invoice", "Enter invoice amount:")
        if amount:
            date = prompt_date()
            if date:
                invoice_id = len(invoices_data) + 1
                invoice = {"invoice_id": invoice_id, "sale_id": sale_id, "amount": amount, "date": date}
                invoices_data.append(invoice)
                list_invoices()

def modify_invoice():
    selected_item = output.focus()
    if selected_item:
        item = output.item(selected_item)
        values = item["values"]
        invoice_id = values[0]
        for invoice in invoices_data:
            if invoice["invoice_id"] == invoice_id:
                sale_id = prompt_sale_id(initialvalue=invoice["sale_id"])
                if sale_id is not None:
                    amount = simpledialog.askfloat("Modify Invoice", "Enter invoice amount:", initialvalue=invoice["amount"])
                    if amount:
                        date = prompt_date(initialvalue=invoice["date"])
                        if date:
                            invoice["sale_id"] = sale_id
                            invoice["amount"] = amount
                            invoice["date"] = date
                            list_invoices()
                break

def delete_invoice():
    selected_item = output.focus()
    if selected_item:
        item = output.item(selected_item)
        values = item["values"]
        invoice_id = values[0]
        confirmation = messagebox.askyesno("Delete Invoice", f"Are you sure you want to delete the invoice: {invoice_id}?")
        if confirmation:
            for invoice in invoices_data:
                if invoice["invoice_id"] == invoice_id:
                    invoices_data.remove(invoice)
                    break
            list_invoices()

def prompt_date(initialvalue=datetime.date.today()):
    date_str = simpledialog.askstring("Date", "Enter date (YYYY-MM-DD):", initialvalue=initialvalue)
    try:
        date = datetime.datetime.strptime(date_str, "%Y-%m-%d").date()
        return date
    except (ValueError, TypeError):
        messagebox.showerror("Invalid Date", "Invalid date format. Please enter a date in YYYY-MM-DD format.")

def prompt_client_id(initialvalue=""):
    client_id_str = simpledialog.askstring("Client ID", "Enter client ID:", initialvalue=initialvalue)
    try:
        client_id = int(client_id_str)
        if client_id > 0:
            return client_id
        else:
            messagebox.showerror("Invalid Client ID", "Client ID must be a positive integer.")
    except (ValueError, TypeError):
        messagebox.showerror("Invalid Client ID", "Invalid client ID. Please enter a valid integer value.")

def prompt_product_id(initialvalue=""):
    product_id_str = simpledialog.askstring("Product ID", "Enter product ID:", initialvalue=initialvalue)
    try:
        product_id = int(product_id_str)
        if product_id > 0:
            return product_id
        else:
            messagebox.showerror("Invalid Product ID", "Product ID must be a positive integer.")
    except (ValueError, TypeError):
        messagebox.showerror("Invalid Product ID", "Invalid product ID. Please enter a valid integer value.")

def prompt_quantity(initialvalue=""):
    quantity_str = simpledialog.askstring("Quantity", "Enter quantity:", initialvalue=initialvalue)
    try:
        quantity = int(quantity_str)
        if quantity > 0:
            return quantity
        else:
            messagebox.showerror("Invalid Quantity", "Quantity must be a positive integer.")
    except (ValueError, TypeError):
        messagebox.showerror("Invalid Quantity", "Invalid quantity. Please enter a valid integer value.")

def prompt_sale_id(initialvalue=""):
    sale_id_str = simpledialog.askstring("Sale ID", "Enter sale ID:", initialvalue=initialvalue)
    try:
        sale_id = int(sale_id_str)
        if sale_id > 0:
            return sale_id
        else:
            messagebox.showerror("Invalid Sale ID", "Sale ID must be a positive integer.")
    except (ValueError, TypeError):
        messagebox.showerror("Invalid Sale ID", "Invalid sale ID. Please enter a valid integer value.")

def get_client_name(client_id):
    for client in clients_data:
        if client["client_id"] == client_id:
            return client["name"]
    return ""

def get_product_name(product_id):
    for product in products_data:
        if product["product_id"] == product_id:
            return product["name"]
    return ""

def get_sale_details(sale_id):
    for sale in sales_data:
        if sale["sale_id"] == sale_id:
            return sale
    return {}

# Create the login window
login_window = tk.Toplevel(window)
login_window.title("Login")

username_label = tk.Label(login_window, text="Username:")
username_label.pack()
username_entry = tk.Entry(login_window)
username_entry.pack()

password_label = tk.Label(login_window, text="Password:")
password_label.pack()
password_entry = tk.Entry(login_window, show="*")
password_entry.pack()

error_label = tk.Label(login_window, text="", fg="red")
error_label.pack()

login_button = tk.Button(login_window, text="Login", command=login)
login_button.pack()

# Create the main window
window.withdraw()

# Create the menu bar
menu_bar = tk.Menu(window)
window.config(menu=menu_bar)

# Create the Clients menu
clients_menu = tk.Menu(menu_bar, tearoff=False)
menu_bar.add_cascade(label="Clients", menu=clients_menu)
clients_menu.add_command(label="List", command=list_clients)
clients_menu.add_command(label="Add", command=add_client, state="disabled")
clients_menu.add_command(label="Modify", command=modify_client, state="disabled")
clients_menu.add_command(label="Delete", command=delete_client, state="disabled")

# Create the Products menu
products_menu = tk.Menu(menu_bar, tearoff=False)
menu_bar.add_cascade(label="Products", menu=products_menu)
products_menu.add_command(label="List", command=list_products)
products_menu.add_command(label="Add", command=add_product, state="disabled")
products_menu.add_command(label="Modify", command=modify_product, state="disabled")
products_menu.add_command(label="Delete", command=delete_product, state="disabled")

# Create the Sales menu
sales_menu = tk.Menu(menu_bar, tearoff=False)
menu_bar.add_cascade(label="Sales", menu=sales_menu)
sales_menu.add_command(label="List", command=list_sales)
sales_menu.add_command(label="Add", command=add_sale, state="disabled")
sales_menu.add_command(label="Modify", command=modify_sale, state="disabled")
sales_menu.add_command(label="Delete", command=delete_sale, state="disabled")

# Create the Invoices menu
invoices_menu = tk.Menu(menu_bar, tearoff=False)
menu_bar.add_cascade(label="Invoices", menu=invoices_menu)
invoices_menu.add_command(label="List", command=list_invoices)
invoices_menu.add_command(label="Add", command=add_invoice, state="disabled")
invoices_menu.add_command(label="Modify", command=modify_invoice, state="disabled")
invoices_menu.add_command(label="Delete", command=delete_invoice, state="disabled")

# Create the output treeview
columns = ("#1", "#2", "#3", "#4", "#5", "#6")
output = ttk.Treeview(window, columns=columns, show="headings")
output.heading("#1", text="Type")
output.heading("#2", text="ID")
output.heading("#3", text="Name")
output.heading("#4", text="Address")
output.heading("#5", text="Quantity")
output.heading("#6", text="Date")
output.pack()

window.mainloop()

