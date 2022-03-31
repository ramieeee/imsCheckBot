import checkBot
import dataProcess
import checkBot

def main():
    data_control = dataProcess.DataControl()
    ims_check_bot = checkBot.IMSCheckBot()
    ims_check_bot.log_in()

    while True:                ### must code input_timeout
        mod = input("""which mode?
----------------------------
> Check current IMS-s  :   \'c\'
> Check updated IMS-s  :   \'u\'
> Add IMS              :   \'a\'
> Remove IMS           :   \'r\'
> Exit                 :   \'e\'
----------------------------
=> """)

        if mod == 'c':
            data_control.data_disp()

        elif mod == 's':
            ims_check_bot.log_in()

        elif mod == 'e':
            print("\nSystem: Exiting the program")
            break

        elif mod == 'a':
            num = input('IMS number: ')
            ims_num, ims_title, ims_date = ims_check_bot.get_ims_info(num)
            if ims_num == 0:
                continue
            else:
                data_control.data_add(ims_num, ims_title, ims_date)
    
        elif mod == 'r':
            num = input('IMS number: ')
            data_control.data_del(num)
        
        else:
            print('\nSystem: No valid input. Try again.')

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print('\nSystem: Exiting the program')
        exit(0)
    except Exception as e:
        print('\nSystem: Error occured.')
        print(e)
        exit(0)