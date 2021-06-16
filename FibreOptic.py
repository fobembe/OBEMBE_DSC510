# Python's program to calculate total cost of installation of fibre optic
# Week 2 Assignment

# Olufemi Obembe

#Create a Welcome Message for the user
user_name = input("Please enter your name")
print("Hello "+user_name)

# Retrieve Company's Name
company = input("Please enter your company name")

# Define the constants
cost = 0.87

#Retrieve the number of cable to be installed
fibre_length = int(input("Enter the quantity of fibre in fts"))

# Calculate the Total Cost of the Installation
Total_Cost = fibre_length*cost
Total_Charged = "$"+str(Total_Cost)

#Display result

print("\n------------RECEIPT--------------")
print("Company name: ",company)
print("length of fibre installed: ",fibre_length)
print("Cost of fibre length per feet: ",cost)
print("Total cost of Installation: ",Total_Charged)
