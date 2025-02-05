# print("Hello, Module3Project")

#Storing our ice cream shop's menu items
flavors = ["vanilla", "caramel", "mint"]
toppings = ["sprinkles", "nuts", "cherry"]
prices = {
    "scoop": 2.50,
    "topping": 0.50
}

def display_menu():
    """Shows available flavors and toppings to the customer"""
    print("\n=== Welcome to the Ice Cream Shop! ===")
    print("\nAvailable Flavors: ")
    for flavor in flavors:
        print(f"- {flavor}")
    
    print("\nAvailable Toppings:")
    for topping in toppings:
        print(f"- {topping}")
    print("\nPrices:")
    print(f"Scoops: ${prices['scoop']:.2f} each")
    print(f"Toppings: ${prices['topping']:.2f} each")

# Simple test function
def main():
    display_menu()

if __name__ == "__main__":
    main()

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

# Updated test function
def main() :
    num_scoops, chosen_flavors = get_flavors()
    chosen_toppings = get_toppings()
    print("\nOrder Summary: ")
    print(f"Scoops: {chosen_flavors}")
    print(f"Toppings: {chosen_toppings}")

if __name__ == "__main__":
    main()