from pyscript import display
# Restaurant Order System using Python Data Types

# String data type
restaurant_name = "Uno's Coffee Shop (YES!)"
owner_name = "Uno Miguel"

# Integer data type
year_since = 2010

# Float data type
tax_rate = 0.08  # 8% tax

# Boolean data type
has_delivery = True
is_dine_in = True
is_takeaway = False

# List data type
product_names = ["Truffle Chicken Pasta", "Tomahawk Steak w/ Mashed Potatoes and Caesar Salad", "Garlic Bread"]
beverages = ["Iced/Hot Latte", "Sparkling Water", "Matcha Bubble Tea", "Espresso", "Cappuccino"]
desserts = ["Cheesecake", "Chocolate Lava Cake", "Tiramisu"]
appetizers = ["Bruschetta", "Stuffed Mushrooms", "Garlic Knots"]

# Tuple data type
business_hours = ("6:00 AM", "1:00 AM")

# Dictionary data type
menu = {
    "Truffle Chicken Pasta":790.99,
    "Tomahawk Steak w/ Mashed Potatoes and Caesar Salad": 1500.00,
    "Garlic Bread": 50.00,
    "Iced/Hot Latte": 30.00,
    "Sparkling Water": 20.00,
    "Matcha Bubble Tea": 120.00,
    "Espresso": 100.00,
    "Cappuccino": 130.00,
    "Cheesecake": 250.00,
    "Chocolate Lava Cake": 300.00,
    "Tiramisu": 280.00,
    "Bruschetta": 150.00,
    "Stuffed Mushrooms": 200.00,
    "Garlic Knots": 100.00
}

# Set data type
common_allergens = {"gluten", "dairy", "nuts"}

# Displaying restaurant information
display(restaurant_name, target="name1")
display(f"Owner: {owner_name}", target="owner")
display(f"Since {year_since}", target="since")
display(f"Menu Pricelist", target="heading1")

# Display menu items
display(product_names[0], target="prod1")
display(f"₱{menu['Truffle Chicken Pasta']:.2f}", target="price1")
display(product_names[1], target="prod2")
display(f"₱{menu['Tomahawk Steak w/ Mashed Potatoes and Caesar Salad']:.2f}", target="price2")
display(product_names[2], target="prod3")
display(f"₱{menu['Garlic Bread']:.2f}", target="price3")
display(beverages[0], target="prod4")
display(f"₱{menu['Iced/Hot Latte']:.2f}", target="price4")
display(beverages[1], target="prod5")
display(f"₱{menu['Sparkling Water']:.2f}", target="price5")
display(beverages[2], target="prod6")
display(f"₱{menu['Matcha Bubble Tea']:.2f}", target="price6")
display(beverages[3], target="prod7")
display(f"₱{menu['Espresso']:.2f}", target="price7")
display(beverages[4], target="prod8")
display(f"₱{menu['Cappuccino']:.2f}", target="price8")
display(desserts[0], target="prod9")
display(f"₱{menu['Cheesecake']:.2f}", target="price9")
display(desserts[1], target="prod10")
display(f"₱{menu['Chocolate Lava Cake']:.2f}", target="price10")
display(desserts[2], target="prod11")
display(f"₱{menu['Tiramisu']:.2f}", target="price11")
display(appetizers[0], target="prod12")
display(f"₱{menu['Bruschetta']:.2f}", target="price12")
display(appetizers[1], target="prod13")
display(f"₱{menu['Stuffed Mushrooms']:.2f}", target="price13")
display(appetizers[2], target="prod14")
display(f"₱{menu['Garlic Knots']:.2f}", target="price14")
# Display additional information
display(f"Shop Business Hours: {business_hours[0]} - {business_hours[1]}", target="openingHours")


# Display order type
display(f"YES! YES!", target="orderType")