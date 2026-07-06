def menu():
    """Run the command-line menu for decoding binary numbers."""
    while True:
        print("Decode binary number enter 1")
        print("To quit enter q")
        menu_input = input(":").lower()
        if menu_input == '1':
            print("Invalid input stops the encoder.")
            user_binary_input = input("Enter binary number (01101010)" 
                        "or number (100110 10011001).\n:").lower()

            # Convert the raw user input into lists of binary digits before decoding.
            parsed_binary_input = parse_binary_input(user_binary_input) 

            # The parser returns an error message as a string if validation fails.
            if isinstance(parsed_binary_input, str):
                print(parsed_binary_input)
            else:
                # Decode each binary number separately so multiple inputs can be handled.
                for binary_number in parsed_binary_input:
                    result = binary_decoder(binary_number)
                    print(result)
        elif menu_input == 'q':
            break
        else:
            print("Invalid input")

def parse_binary_input(parsed_binary_input):
    """Convert user input into a list of valid binary digit lists."""
    # Split input by spaces so the user can enter more than one binary number.
    nested_list = parsed_binary_input.split()

    outer_list = []

    for list_ in nested_list:
        # Store the converted digits for one binary number.
        inner_list = []
        
        for str_ in list_:
            # Validate each character before converting it to an integer.
            if str_.isdigit():
                str_ = int(str_)
                if str_ == 0 or str_ == 1:
                    inner_list.append(str_)
                else:
                    return "Invalid input, invalid binary number"
            else:
                return "Invalid input, not integer"
        outer_list.append(inner_list)
    return outer_list

def binary_decoder(binary_digits):
    """Convert one list of binary digits into its decimal value."""
     
    # Store the number of binary digits so the matching powers of two can be built.
    binary_len = len(binary_digits)

    # Holds the decimal place values for the binary digits.
    powers_of_two = [] 

    # Make sure the decoder only receives valid binary digits.
    for num in binary_digits:
        if num != 0 and num != 1:
            return "Invalid input"

    # Build the powers of two from right to left: 1, 2, 4, 8, etc.
    for num in range(0,binary_len):
        n = 2 ** num
        powers_of_two.append(n)

    # Reverse the binary digits so they line up with the powers of two.
    binary_digits_reversed = reversed(binary_digits)
    
    # Add only the place values where the matching binary digit is 1.
    result = sum(n for b,n in zip(binary_digits_reversed,powers_of_two) if b == 1)
    return result

if __name__ == "__main__":
    menu()
    
