
# Haidy Gamal Ahmed Mahmoud
# Farida Ahmed Abd-elaziz

while True:
    # Ask the user to insert a new number or exit the program
    menu1_result = input("A) insert a new number\nB) Exit program\n").upper()
    if menu1_result == "B":
        break

    # Show an error message and reask the user if the user choose an in valid choice
    while menu1_result != "A" and menu1_result != "B":
        print("please select a valid choice")
        menu1_result = input("A) insert a new number\nB) Exit program\n").upper()

    # Start the program if A, ask the user to insert a number and to choose the base they want to convert from
    while menu1_result == "A":
        number = input("Please insert a number: ").upper()

        number_validity = "false"
        while number_validity == "false":
            menu2_result = input(
                "Please select the base you want to convert a number from:\nA) Decimal\nB) Binary\nC) octal\nD) hexadecimal\n").upper()
            for digit in number:
                if menu2_result == "A":
                    if digit not in "0123456789":
                        print("the number you have entered is not decimal")
                        print("please select a valid choice")
                        break
                    else:
                        number_validity = "true"

                elif menu2_result == "B":
                    if digit not in "01":
                        print("the number you have entered is not binary")
                        print("please select a valid choice")
                        break
                    else:
                        number_validity = "true"

                elif menu2_result == "C":
                    if digit not in "01234567":
                        print("the number you have entered is not octal")
                        print("please select a valid choice")
                        break
                    else:
                        number_validity = "true"

                elif menu2_result == "D":
                    if digit not in "0123456789ABCDEF":
                        print("the number you have entered is not hexadecimal")
                        print("please select a valid choice")
                        break
                    else:
                        number_validity = "true"

                else:
                    break
            if menu2_result not in ["A", "B", "C", "D"]:
                print("please select a valid choice")

        # Ask the user about the base they want to convert to
        menu3_result = input("Please select the base you want to convert a number to:\nA) Decimal\nB) Binary\nC) octal\nD) hexadecimal\n").upper()

        # Reask the user if an invalid choice
        while menu3_result not in ["A", "B", "C", "D"]:
            print("please select a valid choice")
            menu3_result = input(
                "Please select the base you want to convert a number to:\nA) Decimal\nB) Binary\nC) octal\nD) hexadecimal\n").upper()

        # Functions definitions
        def from_decimal_to_binary(decimal_num):
            bin_num = ""
            while decimal_num > 0:
                remainder = decimal_num % 2
                bin_num = str(remainder) + bin_num
                decimal_num = decimal_num // 2
            return bin_num

        def from_decimal_to_octal(decimal_num):
            octal_num = ""
            while decimal_num > 0:
                remainder = decimal_num % 8
                octal_num = str(remainder) + octal_num
                decimal_num = decimal_num // 8
            return octal_num

        def from_decimal_to_hexadecimal(decimal_num):
            hexa_digits = "0123456789ABCDEF"
            hexadecimal_num = ""
            while decimal_num > 0:
                remainder = decimal_num % 16
                remainder_str = hexa_digits[remainder]
                hexadecimal_num = remainder_str + hexadecimal_num
                decimal_num = decimal_num // 16
            return hexadecimal_num

        def from_binary_to_decimal(binary_num):
            p = 0
            decimal_num = 0
            while binary_num > 0:
                digit = binary_num % 10
                decimal_value = digit * pow(2, p)
                decimal_num = decimal_num + decimal_value
                binary_num = binary_num // 10
                p = p + 1
            return decimal_num


        def from_binary_to_octal(binary_num):
            octal_num = ""
            if binary_num == 0:
                octal_num = "000"
            while binary_num > 0:
                three_digit_binary = binary_num % 1000
                p = 0
                decimal_num = 0
                while three_digit_binary > 0:
                    digit = three_digit_binary % 10
                    decimal_value = digit * pow(2, p)
                    decimal_num = decimal_num + decimal_value
                    three_digit_binary = three_digit_binary // 10
                    p += 1
                binary_num = binary_num // 1000
                octal_num = str(decimal_num) + octal_num
            return octal_num


        def from_binary_to_hexa(binary_num):
            hexa_digits = "0123456789ABCDEF"
            hexadecimal_num = ""
            while binary_num > 0:
                four_digit_binary = binary_num % 10000
                p = 0
                decimal_num = 0
                while four_digit_binary > 0:
                    digit = four_digit_binary % 10
                    decimal_value = digit * pow(2, p)
                    decimal_num = decimal_num + decimal_value
                    four_digit_binary = four_digit_binary // 10
                    p += 1
                binary_num = binary_num // 10000
                hexa_value = hexa_digits[decimal_num]
                hexadecimal_num = str(hexa_value) + hexadecimal_num
            print(hexadecimal_num)


        def from_octal_to_decimal(octal_num):
            p = 0
            decimal_num = 0
            while octal_num > 0:
                digit = octal_num % 10
                decimal_value = digit * pow(8, p)
                decimal_num = decimal_num + decimal_value
                octal_num = octal_num // 10
                p = p + 1
            return decimal_num


        def from_octal_to_binary(octal_num):
            binary_num_final = ""
            for digit in octal_num:
                decimal_value = int(digit)
                binary_num = ""
                if decimal_value == 0:
                    binary_num = "000"
                while decimal_value > 0:
                    remainder = decimal_value % 2
                    binary_num = str(remainder) + binary_num
                    decimal_value = decimal_value // 2
                while len(binary_num) < 3:
                    binary_num = "0" + binary_num
                binary_num_final = binary_num_final + binary_num
            return binary_num_final


        def from_hexa_to_decimal(hexadecimal_num):
            p = 0
            decimal_num = 0
            hexa_digits = "0123456789ABCDEF"
            for digit in reversed(hexadecimal_num):
                digit_value = hexa_digits.index(digit)
                decimal_value = digit_value * pow(16, p)
                decimal_num = decimal_num + decimal_value
                p = p + 1
            return decimal_num


        def from_hexa_to_binary(hexadecimal_num):
            hexa_digits = "0123456789ABCDEF"
            binary_num_final = ""
            for digit in hexadecimal_num:
                decimal_value = hexa_digits.index(digit)
                if decimal_value == 0:
                    binary_num = "0000"
                binary_num = ""
                while decimal_value > 0:
                    remainder = decimal_value % 2
                    binary_num = str(remainder) + binary_num
                    decimal_value = decimal_value // 2
                while len(binary_num) < 4:
                    binary_num = "0" + binary_num
                binary_num_final = binary_num_final + binary_num
            return binary_num_final

        #start the conversion process
        if menu2_result == "A":

            #from decimal to binary
            if menu3_result == "B":
                number = int(number)
                print(from_decimal_to_binary(number))

            #from decimal to octal
            elif menu3_result == "C":
                number = int(number)
                print(from_decimal_to_octal(number))

            #from decimal to hexadecimal
            elif menu3_result == "D":
                number = int(number)
                print(from_decimal_to_hexadecimal(number))



        elif menu2_result == "B":

            #from binary to decimal
            if menu3_result == "A":
                number = int(number)
                print(from_binary_to_decimal(number))

            #from binary to octal
            elif menu3_result == "C":
                number = int(number)
                print(from_binary_to_octal(number))


            #from binary to hexadecimal
            elif menu3_result == "D":
                number = int(number)
                print(from_binary_to_hexa(number))


        elif menu2_result == "C":

            #from octal tp decimal
            if menu3_result == "A":
                number = int(number)
                print(from_octal_to_decimal(number))

            #from octal to binary
            elif menu3_result == "B":
                print(from_octal_to_binary(number))

            #from octal to hexa
            elif menu3_result == "D":
                decimal = from_octal_to_binary(number)
                print(from_binary_to_hexa(decimal))


        elif menu2_result == "D":

            #from hexadecimal to decimal
            if menu3_result == "A":
                print(from_hexa_to_decimal(number))

            #from hexadecimal to binary
            elif menu3_result == "B":
                print(from_hexa_to_binary(number))

            #from hexadecimal to octal
            elif menu3_result == "C":
                binary = from_hexa_to_binary(number)
                print(from_binary_to_octal(binary))

        break

