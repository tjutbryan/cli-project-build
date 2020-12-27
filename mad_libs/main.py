import os, sys
dir_path = os.path.dirname(os.path.realpath(__file__))
parent_dir_path = os.path.abspath(os.path.join(dir_path, os.pardir))
sys.path.insert(0, parent_dir_path)
from mad_libs.pizza import start_pizza_mad_libs
from mad_libs.baby_advice import start_baby_advice_mad_libs

def start_program():
    run_again = 'y'
    while run_again == 'y':
        print('=====================================\n' + 
                'Welcome to mad libs generator program\n' +
                '=====================================\n'+
                'Please choose the mad libs program that you want to run: \n' +
                "Input 'a' to run baby_advice mad libs\n"+
                "Input 'b' to run pizza mad libs")
        answer_choice = input('Please enter the choice: ')
        if answer_choice == 'a':
            start_baby_advice_mad_libs()
        elif answer_choice == 'b':
            start_pizza_mad_libs()
        else:
            print('oops wrong input')
        run_again = input('Lets run again shall we (y/n): ')
    
    print('======================================\n' +
        'Thank you for trying out this mad libs\n'
        '======================================')
        
if __name__ == '__main__':
    start_program()