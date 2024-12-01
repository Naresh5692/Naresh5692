def is_armstrong(number):
    # Convert the number to a string to get the number of digits 
    num_str = str(number) 
    num_digits = len(num_str) 
    # Calculate the sum of each digit raised to the power of the number of digits
    armstrong_sum = sum(int(digit) ** num_digits for digit in num_str) 
    # Check if the calculated sum is equal to the original number 
    return armstrong_sum == number 

# Example usage: 
number = int(input("Enter a number: "))        
if is_armstrong(number):                  
    print(f"{number} is an Armstrong number.")     
else:
    print(f"{number} is not an Armstrong number.")   
