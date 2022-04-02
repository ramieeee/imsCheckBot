import checkBot
import dataProcess
import checkBot

def main():
    data_control = dataProcess.DataControl()
    ims_check_bot = checkBot.IMSCheckBot()
    ims_check_bot.log_in()

    while True:                ### must code input_timeout
        mod = input("""\nwhich mode?
----------------------------
> \'S\' : Show all registered IMS-s
> \'s\' : Show single registered IMS
> \'u\' : Check updated IMS-s
> \'a\' : Add IMS            
> \'r\' : Remove IMS         
> \'e\' : Exit               
----------------------------
=> """).strip()

        if mod == 'S':
            data_control.data_disp_all()

        elif mod == 's':
            num = input('IMS number: ')
            data_control.data_disp_single(num)

        elif mod == 'e':
            print("\nSystem: Exiting the program")
            break

        elif mod == 'a':
            num = input('IMS number: ')
            ims_date = ims_check_bot.get_ims_date(num)
            ims_about = input('What is it about? : ')
            
            if ims_num == 0:
                continue
            else:
                data_control.data_add(ims_num, ims_date, ims_about)
    
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