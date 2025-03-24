import random
import order as o
import item as i

# from order import o.order_id

new_order = o.Order("", "", "", 0)
order_archive = []

print("welcome to Adam'sDonald's\n------------------------------")


def show_menu():
    user_input = input("""" What would you like to do?
    "New order" - create a new order
    "Leave" - Leave Adam'sDonald's                   
""")
    return user_input


user_choice = show_menu()

while user_choice != "Leave":
    if user_choice == "New order":

        # print("what would like to order today?\n---------\n1. Adam double ... $2.50\n2. 10 for 3 special ... $3\n3. 9 piece chicken tenders ... $2")

        for x in i.sandwich:
            print(x)

            # Total for money spent Variable

        sandwich_type = int(input("Enter a sandwich type (Pick a number): "))

        loop = False

        while loop is False:
            if sandwich_type == 1:
                new_order.set_sandwich(i.sandwich[0])
                new_order.add_to_total_cost(i.sandwich[0].get_price())
                loop = True
            elif sandwich_type == 2:
                new_order.set_sandwich(i.sandwich[1])
                new_order.add_to_total_cost(i.sandwich[1].get_price())
                loop = True
            elif sandwich_type == 3:
                new_order.set_sandwich(i.sandwich[2])
                new_order.add_to_total_cost(i.sandwich[2].get_price())
                loop = True
            else:
                print("That's not an option")
                sandwich_type = int(input("Enter a sandwich type (Pick a number): "))

        # Iteration 2

        loop = False

        while loop is False:
            drink_choice = int(input("Would you like a drink? (1 for yes, 2 for no) "))
            if drink_choice == 1:
                for x in i.drink:
                    print(x)
                user_d_choice = int(input("Which size drink would you like?"))
                if user_d_choice == 1:
                    new_order.set_drink(i.drink[0])
                    new_order.add_to_total_cost(i.drink[0].get_price())
                    loop = True
                elif user_d_choice == 2:
                    new_order.set_drink(i.drink[1])
                    new_order.add_to_total_cost(i.drink[1].get_price())
                    loop = True
                elif user_d_choice == 3:
                    new_order.set_drink(i.drink[2])
                    new_order.add_to_total_cost(i.drink[2].get_price())
                    loop = True
                else:
                    print("That's not an option")
                    user_d_choice = int(input("Which size drink would you like?"))

            elif drink_choice == 2:
                print("No beverage chosen")
            else:
                drink_choice = int(input("Would you like a drink? (1 for yes, 2 for no) "))

        # Iteration 3

        loop = False

        while loop is False:
            sides_choice = int(input("Would you like a side? (1 for yes, 2 for no) "))
            for x in i.side:
                print(x)

            if sides_choice == 1:
                # print("What size would you like your side of cheese fries?\n--------\n1. small ... $0.50\n2. medium ... $1.25\n3. large ... $1.75")
                sides_chosen = int(input("Enter your chosen side (Pick a number): "))
                if sides_chosen == 1:
                    mega_size = int(input("Would you like a mega size? (1 for yes, 2 for no)"))
                    if mega_size == 1:
                        new_order.set_side(i.side[2])
                        new_order.add_to_total_cost(i.side[2].get_price())
                        loop = True
                    else:
                        new_order.set_side(i.side[0])
                        new_order.add_to_total_cost(i.side[0].get_price())
                        loop = True
                elif sides_chosen == 2:
                    new_order.set_side(i.side[1])
                    new_order.add_to_total_cost(i.side[1].get_price())
                    loop = True
                elif sides_chosen == 3:
                    new_order.set_side(i.side[2])
                    new_order.add_to_total_cost(i.side[2].get_price())
                    loop = True
                else:
                    print("That is not an option")
            else:
                print("No side chosen")

        # Iteration 4

        loop = False

        while loop is False:
            for x in i.sauce:
                print(x)
            sauce_type = int(input("How many packets of Adam sauce would you like?"))
            sauce_packet = 0.25 * sauce_type
            if sauce_type > 0:
                new_order.set_sauce(sauce_type)
                new_order.add_to_total_cost(i.sauce[0].get_price() * sauce_type)
                loop = True
            elif sauce_type <= 0:
                print("No Adam sauce for you papa")
                loop = True

                # new_order.set_sauce(i.sauce[0])
                # new_order.add_to_total_cost(i.sauce[0].get_price())
            # new_order.add_to_total_cost += (sauce_type * 0.25)
            # order[sauce_index] = sauce_type

        # if drink_choice == 1 and sides_choice == 1:
        # new_order.add_to_total_cost(-1.00)
        # print("You saved a dollar papa!! :)")

        random_number = random.randint(1, 1000)
        print(f"Your order number is {random_number}")
        # o.order_id == random_number
        print(new_order)
        # new_order.add_to_total_cost()
        order_archive.append(new_order)
        user_choice = show_menu()

for order in order_archive:
    print(order)