# print("Hello, Module3Project")

#Storing our ice cream shop's menu items
flavors = ["vanilla", "caramel", "mint","chocolate", "cookies and cream", "cookie dough"]
cones = ["cake cone", "sugar cone", "waffle cone"]
toppings = ["sprinkles", "nuts", "cherry"]
prices = {
    "scoop": 2.50,
    "topping": 0.50,
    "cone": 0.20
}

# Displays menu
def display_menu():
    """Shows available flavors and toppings to the customer"""
    print("\n=== Welcome to the Ice Cream Shop! ===")
    print("\nAvailable Cones:")
    for cone in cones:
        print(f"- {cone}")

    print("\nAvailable Flavors: ")
    for flavor in flavors:
        print(f"- {flavor}")
    
    print("\nAvailable Toppings:")
    for topping in toppings:
        print(f"- {topping}")
    
    print("\nPrices:")
    print(f"Cones ${prices['cone']:.2f} each")
    print(f"Scoops: ${prices['scoop']:.2f} each")
    print(f"Toppings: ${prices['topping']:.2f} each")

# Asks users what cones, flavors, and toppings options they want
def get_flavors():
    """Get ice cream flavor choices from the customer"""
    chosen_flavors = []
    while True:
        try:
            num_scoops = int(input("\nHow many scoops would you like? (1-3): "))
            if 1 <= num_scoops <= 3:
                break
            print("Please choose between 1 and 3 scoops.")
        except ValueError:
            print("Please enter a number.")

    print("\nFor each scoop, enter the flavor you'd like:")
    for i in range(num_scoops):
        while True:
            flavor = input(f"Scoop {i+1}: ").lower()
            if flavor in flavors:
                chosen_flavors.append(flavor)
                break
            print("Sorry, that flavor isn't available.")
    return num_scoops, chosen_flavors

def get_cone():
    """Get cone choice for customer"""
    while True:
        cone = input("\nEnter what kind of cone you would like: ").lower()
        if cone in cones:
            print(f"You selected a {cone}.")
        return cone
    print("Sorry, that cone isn't available.")
    
def get_toppings():
    """Gets topping choices from the customer"""
    chosen_toppings = []
    while True:
        topping = input("\nEnter a topping (or 'done' if finished): ").lower()
        if topping == 'done':
            break
        if topping in toppings:
            chosen_toppings.append(topping)
            print(f"Added {topping}!")
        else:
            print("Sorry, that topping isn't available.")
    return chosen_toppings

# 10% discount calculation
def calculate_total(num_scoops, num_toppings, has_cone):
    """Calculates total and applies discount if total is over $10"""
    total = (num_scoops * prices["scoop"]) + (num_toppings * prices["topping"])
    if has_cone:
        total += prices["cone"]
    if total > 10:
        print("You earned a discount!")
        total *= 0.90
    return round(total,2)

# Allows user to search flavors
def search_flavor():
    """Allows customers to search for a flavor"""
    search = input("\nSearch for a flavor: ").lower()
    if search in flavors:
        print(f"We do have {search} available.")
    else:
        print(f"Sorry, we dont have {search} available.")

# Updated test function
def main() :
    display_menu()
    search_flavor()
    num_scoops, chosen_flavors = get_flavors()
    chosen_cone = get_cone()
    chosen_toppings = get_toppings()

    total = calculate_total(num_scoops, len(chosen_toppings), has_cone=True)
    print("\nOrder Summary: ")
    print(f"Scoops: {chosen_flavors}")
    print(f"Cone: {chosen_cone}")
    print(f"Toppings: {chosen_toppings}")
    print(f"Total: ${total:.2f}")

if __name__ == "__main__":
    main()