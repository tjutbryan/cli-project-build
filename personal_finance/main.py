import os, sys
dir_path = os.path.dirname(os.path.realpath(__file__))
parent_dir_path = os.path.abspath(os.path.join(dir_path, os.pardir))
sys.path.insert(0, parent_dir_path)
from personal_finance.saving import saving
from personal_finance.spending import spending

def start_program():
    run_again = 'y'
    while run_again == 'y':
        print('=====================================\n' + 
                'Welcome to personal finance program\n' +
                '=====================================\n'+
                'Please choose the program that you want to run: \n' +
                "Input 'a' to run saving plan program\n"+
                "Input 'b' to run spending plan program")
        answer_choice = input('Please enter the choice: ')
        if answer_choice == 'a':
            saving()
        elif answer_choice == 'b':
            spending()
        else:
            print('oops wrong input')
        run_again = input('Lets run again shall we (y/n): ')
    
    print('======================================\n' +
        'Thank you for trying out this personal finance program\n'
        '======================================')
        
if __name__ == '__main__':
    start_program()