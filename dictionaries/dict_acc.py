
names_dict = {
    'pancho' : {'lisboa','Jalisco', 'monterey'},
    'luis' : {'spain', 'monterey', 'romania'},
    'mari' : {'romania', 'belgium', 'toronto'}
}

# func that checks if a and b are available
def finder (a, b):
# check the elements inside a and b and compare them
    if a and b in names_dict:
# print common elements
        print('LISTS')
        print(names_dict[a])
        print(names_dict[b])
        common = names_dict[a] & names_dict[b]
        print('AND')
        print(common)
        notcom_a = names_dict[a] - common
        notcom_b = names_dict[b] - common
        print('NOT')
        print(notcom_a)
        print(notcom_b)
        #print(notcom_a | notcom_b)
        xor = names_dict[a] ^ names_dict[b]
        print('XOR')
        print(xor)
        orr = names_dict[a] | names_dict[b]
        print('OR')
        print(orr)

# if there are not common elements or not in dict, print error message
    else:
        print('Warning: No elements in common')



# def finder(a, b):
#     if a and b in names_dict:
#         comm = names_dict[a] & names_dict[b]
#         print(comm)

# def finder(a, b):
#     if a in names_dict and b in names_dict:
#         common_elements = names_dict[a] & names_dict[b]
#         print(common_elements)
#     else:
#         print('not in the list')

# finder('monterrey', 'monterrey')
finder('luis', 'mari')