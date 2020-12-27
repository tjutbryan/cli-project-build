def start_pizza_mad_libs():
    print('=======================\n' +
        'Starting pizza mad libs\n' +
        '=======================')
    adj1 = input('Please enter an adjective: ')
    nationality = input('Please enter an nationality: ')
    name = input('Please enter a name: ')
    ingredient = input('Please enter an ingredient: ')
    adj2 = input('Please enter an adjective: ')
    ingredient2 = input('Please enter an ingredient: ')
    ingredient3 = input('Please enter an ingredient: ')
    ingredient4 = input('Please enter an ingredient: ')
    type_favorite = input('Please enter your favorite type of pizza: ')
    number = input('Please enter a number: ')

    print(f'Pizza was invented by a {adj1} {nationality} chef named {name}.\n' +
    f'To make a pizza, you need to take a lump of {ingredient}, and make a thin, round {adj2} {ingredient2}.\n' + 
    f'Then you cover it with {ingredient3} sauce and {ingredient4} cheese.\n' +
    f'My favorite type of pizza is {type_favorite}. \n' + 
    f'If I could I would eat pizza {number} times a day!')