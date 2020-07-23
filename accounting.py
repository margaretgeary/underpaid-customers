melon_cost = 1

def accounting(txt_doc):
# Defining a function that takes a text file as an argument.    
    customer_list = open(txt_doc)
    # Opening the customer list text file.
    for line in customer_list:
    # Iterating through each line of the customer list.
        line = line.rstrip()
        # Deleting whitespace to the right of each line.
        words = line.split('|')
        # Splitting a line into a list of words at each |.

        name = words[1]
        melons = words[2]
        paid = words[3]
        # For each line, name is at index 1, melons index 2, and paid index 3.

    if melons != paid:
    # If the price of melons does not equal the price paid.
        print(f"{name} paid ${paid},",
            f"expected ${melons}"
            )
        # Print how much the customer paid versus how much was expected.

    if melons < paid:
        print(f"{name} has overpaid for their melons.")
        # If the price of melons is less than the price paid, the customer overpaid.

    elif melons > paid:
        print(f"{name} has underpaid for their melons.")
        # If the price of the melons is greater than the price paid, the customer underpaid.

    customer_list.close()
    #  Closing the txt file.

accounting("customer-orders.txt")
# Calling the function, taking the customer list as an argument.

# Homework instructions:

# melon_cost = 1.00

# customer1_name = "Joe"
# customer1_melons = 5
# customer1_paid = 5.00

# customer2_name = "Frank"
# customer2_melons = 6
# customer2_paid = 6.00

# customer3_name = "Sally"
# customer3_melons = 3
# customer3_paid = 3.00

# customer4_name = "Sean"
# customer4_melons = 9
# customer4_paid = 9.50

# customer5_name = "David"
# customer5_melons = 4
# customer5_paid = 4.00

# customer6_name = "Ashley"
# customer6_melons = 3
# customer6_paid = 2.00

# customer1_expected = customer1_melons * melon_cost
# if customer1_expected != customer1_paid:
#     print(f"{customer1_name} paid ${customer1_paid:.2f},",
#           f"expected ${customer1_expected:.2f}"
#           )

# customer2_expected = customer2_melons * melon_cost
# if customer2_expected != customer2_paid:
#     print(f"{customer2_name} paid ${customer2_paid:.2f},",
#           f"expected ${customer2_expected:.2f}"
#           )

# customer3_expected = customer3_melons * melon_cost
# if customer3_expected != customer3_paid:
#     print(f"{customer3_name} paid ${customer3_paid:.2f},",
#           f"expected ${customer3_expected:.2f}"
#           )

# customer4_expected = customer4_melons * melon_cost
# if customer4_expected != customer4_paid:
#     print(f"{customer4_name} paid ${customer4_paid:.2f},",
#           f"expected ${customer4_expected:.2f}"
#           )

# customer5_expected = customer5_melons * melon_cost
# if customer5_expected != customer5_paid:
#     print(f"{customer5_name} paid ${customer5_paid:.2f},",
#           f"expected ${customer5_expected:.2f}"
#           )

# customer6_expected = customer6_melons * melon_cost
# if customer6_expected != customer6_paid:
#     print(f"{customer6_name} paid ${customer6_paid:.2f},",
#           f"expected ${customer6_expected:.2f}"
#           )
