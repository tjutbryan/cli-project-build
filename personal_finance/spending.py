def spending():
    print('==============================\n' +
        'Starting spending plan program\n' +
        '==============================')
    spending_dict = {}
    total_spending = 0
    spending_iteration = input('Please enter the number of spending items: ')
    for i in range(int(spending_iteration)):
        i_string = i + 1
        print(f'===================Item {i_string}===================')
        spending_name = input('Please enter the spending name (e.g housing): ')
        spending_amount = input(f'Please enter the spending amount for {spending_name}: ')
        spending_amount = get_amount_parsed(spending_amount)
        spending_dict[spending_name] = spending_amount
        total_spending += int(spending_amount)
    
    for key, value in spending_dict.items():
        percentage = round(int(value) / total_spending * 100)
        print(f'Spending for item {key} is {percentage}%')

def get_amount_parsed(amount):
    amount_parsed = ''
    for char in amount:
        if char.isdigit():
            amount_parsed += char
    return amount_parsed

