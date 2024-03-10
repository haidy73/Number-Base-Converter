#farida ahmed abd-elaziz/ 20231121
#haidy gamal ahmed mahmoud/ 20230457

def bin_validation(number):
   for digit in number:
      if digit != "0" and digit != "1":
         message = "please enter a valid binary number"
         return message
# one's complement
def one_complement(number):
   res = ""
   for digit in number:
      if digit == "0":
         res += "1"
      else:
         res += "0"
   return res

# two's complement
def twos_complement(number):
   one = one_complement(number)
   carry = "1"
   complement2 = ""
   for i in one[::-1]:
      if i == "0" and carry == "0":
         carry = "0"
         complement2 = "0" + complement2
      elif i == "0" and carry == "1":
         carry = "0"
         complement2 = "1" + complement2
      elif i == "1" and carry == "0":
         carry = "0"
         complement2 = "1" + complement2
      else:  # i==1 and carry==1
         carry = "1"
         complement2 = "0" + complement2
   return complement2

def add_zeroes(num1, num2):
   return "0" * (len(num2) - len(num1)) + num1

def max_length(num1, num2):
   if num1 >= num2:
      bigger = num1
      smaller = add_zeroes(num2, num1)
   else:
      bigger = num2
      smaller = add_zeroes(num1, num2)
   return (bigger, smaller)

def addition(bigger, smaller):
   bigger, smaller = max_length(bigger, smaller)
   result = [0] * (len(bigger))
   carry = 0
   for x in range(len(bigger)-1, -1, -1):
      result[x] = int(bigger[x]) + int(smaller[x]) + carry
      if carry > 0:
         carry -= 1
      if result[x] >= 2:
         result[x] -= 2
         carry += 1
   while carry > 0:
      result = [1] + result
      carry -= 1
   return result

def subtraction(bigger, smaller):
   bigger, smaller = max_length(bigger, smaller)
   return addition(bigger, twos_complement(smaller))

def binary_calculator():
   while True:
      print("Menu 1")
      print("**Binary Calculator**")
      print("A) Insert new numbers")
      print("B) Exit")
      answer = input()
      if answer == "A" or answer == "a":
         number1 = input("Enter the first binary number: ")
         number1_validity = bin_validation(number1)
         if number1_validity == "please enter a valid binary number":
            print(number1)
            continue
         number2 = input("Enter the second binary number: ")
         number2_validity = bin_validation(number2)
         if number2_validity == "please enter a valid binary number":
            print(number2)
            continue
         print("Menu 2")
         print("**Please select the operation**")
         print("A) Compute one's complement")
         print("B) Compute two's complement")
         print("C) Addition")
         print("D) Subtraction")
         operation = input()
         if operation == "A" or operation == "a":
            ones_complement = one_complement(number1)
            print("The one's complement of", number1, "is", ones_complement)
         elif operation == "B" or operation == "b":
            two_complement = twos_complement(number1)
            print("The two's complement of", number1, "is", two_complement)
         elif operation == "C" or operation == "c":
            number2_validity = bin_validation(number2)
            if number2_validity == "please enter a valid binary number":
               print(number2)
               continue
            result = addition(number1, number2)
            print("The result of", number1, "+", number2, "is", result)
         elif operation == "D" or operation == "d":
            number2_validity = bin_validation(number2)
            if number2_validity == "please enter a valid binary number":
               print(number2)
               continue
            result = subtraction(number1, number2)
            print("The result of", number1, "-", number2, "is", result)
         else:
            print("Please select a valid choice")
      elif answer == "B" or answer == "b":
         break
      else:
         print("Please select a valid choice")

binary_calculator()

