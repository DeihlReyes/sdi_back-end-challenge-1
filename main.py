sizes = [
    ("S", {"size": "small", "capacity": 5, "cost": 5000}),
    ("M", {"size": "medium", "capacity": 10, "cost": 8000}),
    ("L", {"size": "large", "capacity": 15, "cost": 12000})
]

sizes.sort(key=lambda x: x[1]['cost'] / x[1]['capacity'])

def calculate_cost(seatCount):
    for _, size in sizes:
        if seatCount <= size["capacity"]:
            return size["cost"], size["size"], False
    return "", "", True

def optimize_cost(seatCount):
    total_cost = 0
    size_counts = []

    for _, size in sizes:
        count = seatCount // size['capacity']
        seatCount -= count * size['capacity']
        if count != 0:
            total_cost += count * size['cost']
            size_counts.append(f'{count} x {size["size"]}')

    if seatCount > 0:
        total_cost += sizes[0][1]["cost"]
        size_counts.append(f'1 x {sizes[0][1]["size"]}')

    finalCount = ', '.join(size_counts)

    return total_cost, finalCount

def display_input():
    seatCount = int(input("Please input number (seat): "))
    cost, size, error = calculate_cost(seatCount)
    if error:
        cost, size = optimize_cost(seatCount)
    return cost, size

def display_output(cost, size):
    print("Cost: ", cost)
    print("Size: ", size)

def change_parameter(parameter):
    print(f"Change {parameter}")
    for size in sizes:
        print(f"[{size[0]}] {size[1]['size']}")
    choice = input("Enter choice: ")

    for size in sizes:
        if choice == size[0]:
            new_value = int(input(f"Enter new {parameter} for {size[1]['size']}: "))
            size[1][parameter] = new_value
            print(f"\n{parameter} changed successfully")
            return
    print("Invalid choice")

def display_options():
    print("Size".ljust(10), "Capacity".ljust(10), "Cost".ljust(10))
    print("-" * 30)
    sizes.sort(key=lambda x: x[1]['capacity'])
    for _, size in sizes:
        print(size["size"].ljust(10), str(size["capacity"]).ljust(10), str(size["cost"]).ljust(10))

    print("\nChoose an Option: ")
    print("[A] Change Cost")
    print("[B] Change Capacity")
    print("[C] Calculate Cost")
    print("[Q] Quit")
    return input("Enter choice: ")

def main():
    actions = {"A": lambda: change_parameter("cost"),
               "B": lambda: change_parameter("capacity"),
               "C": lambda: display_output(*display_input()),
               "Q": lambda: exit()}

    while True:
        choice = display_options()
        action = actions.get(choice)
        if action:
            action()
        else:
            print("Invalid choice")

if __name__ == "__main__":
    main()