import checkBot
import dataProcess
import checkBot

def main():
    data_control = dataProcess.DataControl()
    ims_check_bot = checkBot.IMSCheckBot()

    while True:
        mod = input("""which mode?
----------------------------
> Check current IMS-s  :   \'c\'
> Check updated IMS-s  :   \'u\'
> Add IMS              :   \'a\'
> Delete IMS           :   \'d\'
> Exit                 :   \'e\'
----------------------------
=> """)

        if mod == 'c':
            data_control.data_disp()

        elif mod == 's':
            ims_check_bot.log_in()

        elif mod == 'e':
            print("System: Exiting the program")
            break

        elif mod == 'a':
            temp = 1
            issue_num = input('IMS number: ')
            if len(int(issue_num)) != 6 or type(temp) != type(int(issue_num)):
                print('invalid number')
                break
            else:
                issue_about = input('What is this issue about?: ')

            print('Add')
            print()
    
        elif mod == 'd':
            print('d')
        
        else:
            print('No valid input. Try again.')

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(e)
        exit(0)