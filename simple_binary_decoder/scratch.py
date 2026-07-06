binary_input = "101b100@01 010012"

nested_list = binary_input.split()
#print(list_)
#nested_list = [n for n in list_]
#print(nested_list)
outer_list = []

for list_ in nested_list:
    inner_list = []
    
    for str_ in list_:
        if str_.isdigit():
            str_ = int(str_)
            if str_ == 0 or str_ == 1:
                inner_list.append(str_)
            else:
                print("Invalid input, invalid binary number")
        else:
            print("Invalid input, not integer")
    outer_list.append(inner_list)



print(outer_list)


 
