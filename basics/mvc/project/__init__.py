"""
Inventory Management System for Critical Components with a Tkinter-based User Interface

This project is designed to help manage the inventory of critical components, keeping track of stock levels,
issuing alerts when stock is low, handling orders, generating reports, and providing a graphical interface for user interactions.
The system is organized into several modules, each with its own responsibilities for modularity and maintainability.

Modules:
1. inventory.py - Handles inventory management logic (adding, removing, updating components).
2. database.py - Deals with database interactions, storing and retrieving component information.
3. alerts.py - Handles alerts when stock levels are critically low.
4. orders.py - Manages ordering of new components.
5. reports.py - Generates reports for inventory analysis.
6. ui.py - Provides a user interface for inventory management using Tkinter.
7. main.py - Entry point of the project.

Author: Your Name
Date: October 4, 2024
"""

# Module 1: inventory.py
"""
Handles inventory management logic such as adding new components, removing components, and updating stock levels.
"""


# inventory.py
class Inventory:
    def __init__(self):
        self.components = {}

    def add_component(self, component_id, name, quantity, critical_level, supplier=None, lead_time=None):
        """Add a new component to the inventory."""
        self.components[component_id] = {
            'name': name,
            'quantity': quantity,
            'critical_level': critical_level,
            'supplier': supplier,
            'lead_time': lead_time
        }

    def remove_component(self, component_id):
        """Remove a component from the inventory."""
        if component_id in self.components:
            del self.components[component_id]

    def update_stock(self, component_id, quantity):
        """Update the stock quantity of a component."""
        if component_id in self.components:
            self.components[component_id]['quantity'] = quantity

    def update_critical_level(self, component_id, critical_level):
        """Update the critical level of a component."""
        if component_id in self.components:
            self.components[component_id]['critical_level'] = critical_level

    def get_component_info(self, component_id):
        """Get information about a specific component."""
        return self.components.get(component_id, None)

    def get_all_components(self):
        """Retrieve a list of all components."""
        return self.components


# Module 2: database.py
"""
Handles database interactions. This is a mock database interaction module for simplicity.
"""
# database.py
import json


class Database:
    def __init__(self, db_file='inventory_db.json'):
        self.db_file = db_file

    def save(self, data):
        """Save data to the mock database (JSON file)."""
        with open(self.db_file, 'w') as file:
            json.dump(data, file, indent=4)

    def load(self):
        """Load data from the mock database (JSON file)."""
        try:
            with open(self.db_file, 'r') as file:
                return json.load(file)
        except FileNotFoundError:
            return {}


# Module 3: alerts.py
"""
Handles alerts for components that are critically low in stock.
"""


# alerts.py
class Alerts:
    def __init__(self, inventory):
        self.inventory = inventory

    def check_critical_levels(self):
        """Check all components and issue alerts for those that have critically low stock."""
        alerts = []
        for component_id, details in self.inventory.get_all_components().items():
            if details['quantity'] <= details['critical_level']:
                alerts.append(
                    f"ALERT: Component {details['name']} is critically low: {details['quantity']} left. Supplier: {details.get('supplier', 'Unknown')}.")
        return alerts


# Module 4: orders.py
"""
Handles ordering of new components when inventory is low.
"""


# orders.py
class Orders:
    def __init__(self, inventory):
        self.inventory = inventory

    def order_component(self, component_id, order_quantity):
        """Order more of a specific component."""
        component = self.inventory.get_component_info(component_id)
        if component:
            new_quantity = component['quantity'] + order_quantity
            self.inventory.update_stock(component_id, new_quantity)
            return f"Ordered {order_quantity} units of {component['name']}. New quantity is {new_quantity}. Estimated lead time: {component.get('lead_time', 'Not specified')} days."
        return "Component not found."


# Module 5: reports.py
"""
Generates reports for inventory analysis, including critical stock levels and overall inventory status.
"""
# reports.py
import datetime


class Reports:
    def __init__(self, inventory):
        self.inventory = inventory

    def generate_stock_report(self):
        """Generate a report showing the stock level of all components."""
        report = [
            f"Inventory Report - {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n",
            "---------------------------------------------------------------"
        ]
        for component_id, details in self.inventory.get_all_components().items():
            report.append(
                f"Component ID: {component_id}, Name: {details['name']}, Quantity: {details['quantity']}, Critical Level: {details['critical_level']}, Supplier: {details.get('supplier', 'Unknown')}, Lead Time: {details.get('lead_time', 'N/A')} days"
            )
        return "\n".join(report)


# Module 6: ui.py
"""
Provides a user interface for inventory management using Tkinter.
"""
# ui.py
import tkinter as tk
from tkinter import messagebox, simpledialog



class InventoryUI:
    def __init__(self, root, inventory, orders, alerts, reports):
        self.root = root
        self.inventory = inventory
        self.orders = orders
        self.alerts = alerts
        self.reports = reports

        root.title("Inventory Management System")
        root.geometry("600x400")

        # Create UI components
        self.component_listbox = tk.Listbox(root, width=80, height=15)
        self.component_listbox.pack()

        self.add_button = tk.Button(root, text="Add Component", command=self.add_component)
        self.add_button.pack()

        self.update_button = tk.Button(root, text="Update Stock", command=self.update_stock)
        self.update_button.pack()

        self.alerts_button = tk.Button(root, text="Check Alerts", command=self.show_alerts)
        self.alerts_button.pack()

        self.order_button = tk.Button(root, text="Order Component", command=self.order_component)
        self.order_button.pack()

        self.report_button = tk.Button(root, text="Generate Report", command=self.generate_report)
        self.report_button.pack()

        self.refresh_component_list()

    def refresh_component_list(self):
        self.component_listbox.delete(0, tk.END)
        for component_id, details in self.inventory.get_all_components().items():
            self.component_listbox.insert(tk.END,
                                          f"ID: {component_id}, Name: {details['name']}, Quantity: {details['quantity']}, Critical Level: {details['critical_level']}, Supplier: {details.get('supplier', 'Unknown')}")

    def add_component(self):
        component_id = simpledialog.askstring("Input", "Enter Component ID:")
        name = simpledialog.askstring("Input", "Enter Component Name:")
        quantity = simpledialog.askinteger("Input", "Enter Quantity:")
        critical_level = simpledialog.askinteger("Input", "Enter Critical Level:")
        supplier = simpledialog.askstring("Input", "Enter Supplier:")
        lead_time = simpledialog.askinteger("Input", "Enter Lead Time (days):")
        self.inventory.add_component(component_id, name, quantity, critical_level, supplier, lead_time)
        self.refresh_component_list()

    def update_stock(self):
        component_id = simpledialog.askstring("Input", "Enter Component ID to Update:")
        quantity = simpledialog.askinteger("Input", "Enter New Quantity:")
        self.inventory.update_stock(component_id, quantity)
        self.refresh_component_list()

    def show_alerts(self):
        critical_alerts = self.alerts.check_critical_levels()
        if critical_alerts:
            messagebox.showwarning("Critical Alerts", "\n".join(critical_alerts))
        else:
            messagebox.showinfo("No Alerts", "All components are above critical levels.")

    def order_component(self):
        component_id = simpledialog.askstring("Input", "Enter Component ID to Order:")
        order_quantity = simpledialog.askinteger("Input", "Enter Quantity to Order:")
        order_response = self.orders.order_component(component_id, order_quantity)
        messagebox.showinfo("Order Response", order_response)
        self.refresh_component_list()

    def generate_report(self):
        report = self.reports.generate_stock_report()
        report_window = tk.Toplevel(self.root)
        report_window.title("Inventory Report")
        text_widget = tk.Text(report_window, wrap='word', width=80, height=20)
        text_widget.insert(tk.END, report)
        text_widget.pack()
        text_widget.config(state='disabled')


# Module 7: main.py
"""
Entry point of the Inventory Management System. Coordinates different modules to perform inventory tasks and initialize the UI.
"""
# main.py

import tkinter as tk


def main():
    # Initialize the inventory and database
    db = Database()
    inventory = Inventory()
    inventory_data = db.load()

    # Load saved inventory data
    for component_id, details in inventory_data.items():
        inventory.add_component(component_id, details['name'], details['quantity'], details['critical_level'],
                                details.get('supplier'), details.get('lead_time'))

    # Initialize alerts, orders, and reports modules
    alerts = Alerts(inventory)
    orders = Orders(inventory)
    reports = Reports(inventory)

    # Initialize and start the UI
    root = tk.Tk()
    ui = InventoryUI(root, inventory, orders, alerts, reports)
    root.mainloop()

    # Save final state of inventory
    db.save(inventory.get_all_components())


if __name__ == "__main__":
    main()