# -*- coding: utf-8 -*-
"""
Created on Thu May 21 10:20:29 2023

@author: mekki
"""
class Personne:
    def __init__(self, personne_id, name, address, phone_number):
        self._personne_id = personne_id
        self._name = name
        self._address = address
        self._phone_number = phone_number
    
    def get_personne_id(self):
        return self._personne_id
    
    def set_personne_id(self, personne_id):
        self._personne_id = personne_id
    
    def get_name(self):
        return self._name
    
    def set_name(self, name):
        self._name = name
    
    def get_address(self):
        return self._address
    
    def set_address(self, address):
        self._address = address
    
    def get_phone_number(self):
        return self._phone_number
    
    def set_phone_number(self, phone_number):
        self._phone_number = phone_number

class Supplier(Personne):
    def __init__(self, supplier_id, name, address, phone_number):
        super().__init__(supplier_id, name, address, phone_number)
        self._supplier_id = supplier_id
    
    def get_supplier_id(self):
        return self._supplier_id
    
    def set_supplier_id(self, supplier_id):
        self._supplier_id = supplier_id

class Employee(Personne):
    def __init__(self, employee_id, name, address, phone_number, position, salary):
        super().__init__(employee_id, name, address, phone_number)
        self._employee_id = employee_id
        self._position = position
        self._salary = salary
    
    def get_employee_id(self):
        return self._employee_id
    
    def set_employee_id(self, employee_id):
        self._employee_id = employee_id
    
    def get_position(self):
        return self._position
    
    def set_position(self, position):
        self._position = position
    
    def get_salary(self):
        return self._salary
    
    def set_salary(self, salary):
        self._salary = salary

class Client(Personne):
    def __init__(self, client_id, name, address, phone_number):
        super().__init__(client_id, name, address, phone_number)
        self._client_id = client_id
    
    def get_client_id(self):
        return self._client_id
    
    def set_client_id(self, client_id):
        self._client_id = client_id

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
    
    def get_description(self):
        return self._description
    
    def set_description(self, description):
        self._description = description
    
    def get_price(self):
        return self._price
    
    def set_price(self, price):
        self._price = price
    
    def get_quantity_in_stock(self):
        return self._quantity_in_stock
    
    def set_quantity_in_stock(self, quantity_in_stock):
        self._quantity_in_stock = quantity_in_stock

class Order:
    def __init__(self, order_id, order_date, client, products):
        self._order_id = order_id
        self._order_date = order_date
        self._client = client
        self._products = products
    
    def get_order_id(self):
        return self._order_id
    
    def set_order_id(self, order_id):
        self._order_id = order_id
    
    def get_order_date(self):
        return self._order_date
    
    def set_order_date(self, order_date):
        self._order_date = order_date
    
    def get_client(self):
        return self._client
    
    def set_client(self, client):
        self._client = client
    
    def get_products(self):
        return self._products
    
    def set_products(self, products):
        self._products = products

class Warehouse:
    def __init__(self, capacity,product):
        self._capacity = capacity
        self._products_in_stock = []

    def get_capacity(self):
        return self._capacity
    
    def set_capacity(self, capacity):
        self._capacity = capacity
    
    def get_products_in_stock(self):
        return self._products_in_stock

    
    def add_product(self, product):
        self._products_in_stock.append(product)
    
    def remove_product(self, product):
        self._products_in_stock.remove(product)


class Sales:
    def __init__(self, sale_date, product, quantity_sold, sale_price, client):
        self._sale_date = sale_date
        self._product = product
        self._quantity_sold = quantity_sold
        self._sale_price = sale_price
        self._client = client
    
    def get_sale_date(self):
        return self._sale_date
    
    def set_sale_date(self, sale_date):
        self._sale_date = sale_date
    
    def get_product(self):
        return self._product
    
    def set_product(self, product):
        self._product = product
    
    def get_quantity_sold(self):
        return self._quantity_sold
    
    def set_quantity_sold(self, quantity_sold):
        self._quantity_sold = quantity_sold
    
    def get_sale_price(self):
        return self._sale_price
    
    def set_sale_price(self, sale_price):
        self._sale_price = sale_price
    
    def get_client(self):
        return self._client
    
    def set_client(self, client):
        self._client = client


class Invoice:
    def __init__(self, invoice_id, invoice_date, total_amount, products):
        self._invoice_id = invoice_id
        self._invoice_date = invoice_date
        self._total_amount = total_amount
        self._products = products
    
    def get_invoice_id(self):
        return self._invoice_id
    
    def set_invoice_id(self, invoice_id):
        self._invoice_id = invoice_id
    
    def get_invoice_date(self):
        return self._invoice_date
    
    def set_invoice_date(self, invoice_date):
        self._invoice_date = invoice_date
    
    def get_total_amount(self):
        return self._total_amount
    
    def set_total_amount(self, total_amount):
        self._total_amount = total_amount
    
    def get_products(self):
        return self._products
    
    def set_products(self, products):
        self._products = products

class Report:
    def __init__(self, revenue):
        self._report_date = report_date
        self._revenue = revenue
    
    def get_report_date(self):
        return self._report_date
    
    def set_report_date(self, report_date):
        self._report_date = report_date

    def get_revenue(self):
        return self._revenue
    
    def set_revenue(self, revenue):
        self._revenue = revenue

def stats(self, sales, products):
    sales_per_client = {}
    for sale in sales:
        client = sale.get_client().get_client_id()
        quantity_sold = sale.get_quantity_sold()
        if client in sales_per_client:
            sales_per_client[client] += quantity_sold
        else:
            sales_per_client[client] = quantity_sold
    average_sales_per_client = {client: total_sales / len(sales) for client, total_sales in sales_per_client.items()}

    sales_per_product = {}
    for sale in sales:
        product = sale.get_product().get_product_id()
        quantity_sold = sale.get_quantity_sold()
        if product in sales_per_product:
            sales_per_product[product] += quantity_sold
        else:
            sales_per_product[product] = quantity_sold

    total_revenue = sum(sale.get_sale_price() * sale.get_quantity_sold() for sale in sales)

    delivery_times = [(sale.get_sale_date() - sale.get_client().get_registration_date()).days for sale in sales]
    average_delivery_time = sum(delivery_times) / len(delivery_times)

    most_demanded_product = max(sales_per_product, key=sales_per_product.get)

    return {
        "average_sales_per_client": average_sales_per_client,
        "total_sales_per_product": sales_per_product,
        "total_revenue": total_revenue,
        "average_delivery_time": average_delivery_time,
        "most_demanded_product": most_demanded_product
    }



