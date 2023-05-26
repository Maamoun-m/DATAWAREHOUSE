# -*- coding: utf-8 -*-
"""
Created on Thu May 21 10:20:29 2023

@author: mekki
"""
class Employee:
    def __init__(self, employee_id, name, position, salary):
        self.employee_id = employee_id #le ID doit être unique pour chaque employé
        self.name = name
        self.position = position # le poste occupé par l'employé 
        self.salary = salary

class Product:
    def __init__(self, product_id, description, price, quantity_in_stock):
        self.product_id = product_id #le ID (produit) doit être unique pour chaque produit
        self.description = description
        self.price = price
        self.quantity_in_stock = quantity_in_stock

class Order:
    def __init__(self, order_id, order_date, client, products):
        self.order_id = order_id
        self.order_date = order_date
        self.client = client
        self.products = products

class Client:
    def __init__(self, client_id, name, address, phone_number):
        self.client_id = client_id
        self.name = name
        self.address = address
        self.phone_number = phone_number

class Warehouse:
    def __init__(self, capacity):
        self.capacity = capacity
        self.products_in_stock = []

    def add_product(self, product):
        self.products_in_stock.append(product)

    def remove_product(self, product):
        self.products_in_stock.remove(product)

class Sales:
    def __init__(self, sale_date, product, quantity_sold, sale_price):
        self.sale_date = sale_date
        self.product = product
        self.quantity_sold = quantity_sold
        self.sale_price = sale_price

class Supplier:
    def __init__(self, supplier_id, name, address, phone_number):
        self.supplier_id = supplier_id
        self.name = name
        self.address = address
        self.phone_number = phone_number

class Invoice:
    def __init__(self, invoice_id, invoice_date, total_amount, products):
        self.invoice_id = invoice_id
        self.invoice_date = invoice_date
        self.total_amount = total_amount
        self.products = products

class Report:
    def __init__(self, report_date, sales_statistics, revenue):
        self.report_date = report_date
        self.sales_statistics = sales_statistics
        self.revenue = revenue

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



