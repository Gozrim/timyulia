from modules import Customers
def add_customer(customer_list):
    new_customer = Customers(int(input("Enter Customer's ID")), str(input("Enter Customer's name: ")),
                             str(input("Enter Customer's city: ")),int(input("Enter Customer's age: ")))
    customer_list.append(new_customer.__str__())
    print("Customer has been added")
    return customer_list
def find_customer(customer_list):
    id_input = input("Enter the ID of the customer you wish to find: ")
    for i in customer_list:
        temp_list = i.split(",")
        if id_input == temp_list[0]:
            return print(i)
def remove_customer(customer_list):
    id_input = str(input("Enter ID of the customer you wish to remove: "))
    for i in customer_list:
        temp_list = i.split(",")
        print(temp_list)
        if id_input == temp_list[0]:
            index = customer_list.index(i)
            customer_list.pop(index)
            print("Customer has been removed")
            return customer_list