# Enter the number of rows for the pyramid 
rows = int(input("Enter the number of rows for the pyramid:"))
for i in range(1, rows + 1):
    #print spaces
    print(" " *(rows - i), end= " ")
    #print stars
    print("*" * (2*i-1)) 