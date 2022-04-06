import checkBot
import dataProcess
import checkBot

def main():
    version = '1.1v'
    print(f"""**Welcome to IMS Comment Check Bot {version}**
You need to login with your IMS account of TMAXSoft""")

    data_control = dataProcess.DataControl()
    ims_check_bot = checkBot.IMSCheckBot()
    while True:
        flag = ims_check_bot.log_in()

        # check empty field in id or pw
        if flag == 0:
            continue

        elif ims_check_bot.login_check() == 1:
            print('\nSystem: Login successful')
            break
        else:
            print('\nSystem: ID or PW may not be right. Try again')

    while True:                ### must code input_timeout
        mod = input("""\nSelect the mode
----------------------------
> \'S\' : Show all registered IMS-s
> \'s\' : Show single registered IMS
> \'u\' : Check updated IMS-s
> \'a\' : Add IMS            
> \'r\' : Remove IMS         
> \'v\' : Check version of IMS_check_bot
> \'e\' : Exit               
----------------------------
=> """).strip()

        if mod == 'S':
            data_control.data_disp_all()

        elif mod == 's':
            num = input('IMS number: ')
            try:
                data_control.data_disp_single(num)
            except ValueError:
                print('\nSystem: Input value invalid')

        elif mod == 'u':
            print('Please wait for a while. It may take few mins')
            data_list = data_control.data_to_list()
            cnt = 0
            for num in data_list:
                ims_date, ims_comment = ims_check_bot.get_ims_info(num)
            
                if ims_date != data_control.data_date_check(num):
                    print(f'> {num} with updated comment')
                    print(f'> About: ')
                    print(f'> Update date: {ims_date}')
                    print(f'> Comment: {ims_comment}\n')
                    data_control.data_switch(num, ims_date, ims_comment)
                    cnt += 1
            print(f'System: Total {cnt} updates')

        elif mod == 'a':
            num = input('IMS number: ')
            if num == '':
                print('\nSystem: Empty number input')
                continue

            # get current IMS date and details
            details_date, details_body = ims_check_bot.get_details(num)
            if details_date == 0:
                print(f'\nSystem: IMS num {num} may not exist. Try again')
                continue
            
            # execute addition
            data_control.data_add(num, details_date, details_body)
            print('System: new IMS added with current date & time')

        elif mod == 'r':
            num = input('IMS number: ')
            if num == '':
                print('\nSystem: Empty number input')
                continue
            try:
                data_control.data_del(num)
            except ValueError:
                print('\nSystem: Input value invalid')
        
        elif mod == 'v':
            print(f'\n IMS Check Bot with version {version}')

        elif mod == 'e':
            print("\nSystem: Exiting the program")
            break
        
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