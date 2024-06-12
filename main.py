# name = input('What is your name: ')

# base_salary = float(input('What is your annual salary: '))

# year_of_service = int(input('How many years have you worked: '))

# if year_of_service > 3:
#     bonus_salary = round(base_salary * 0.07, 2)
#     print(f'Hello {name}, your bonus for {year_of_service} years of service is £{bonus_salary:.2f}.')
# else:
#     bonus_salary = 0
#     print(f'Hello {name}, your bonus for {year_of_service} years of service is £{bonus_salary:.2f}.')

# dummy = ('Tekkem', 'Kem', 'Kemmy', 'KemmyTekkem')
# number_set = {1, 2, 3, 4, 5, 6, 7, 8, 9, 8, 4, 10}

# thisset = {"apple", "banana", "cherry", True, 1, 2, 3, 4, 5, 6, 7, 8, 9, 8, 4,}

# # dummy[1] = 'Keommy'

# dummy_list = list(dummy)

# print('Tuple:', dummy)
# print('List', dummy_list)
# print('Set:', number_set)
# print('Set:', thisset)

userInput1 = input('Enter a list item, any text: ')
userInput2 = input('Enter another item, any text: ')
userInput3 = input('Enter a final list item, any text: ')

# dataOutput = list(userInput1, userInput2, userInput3)
dataOutput = [userInput1, userInput2, userInput3]
dataOutput.append('Sushi')
print(dataOutput)
print(type(dataOutput))