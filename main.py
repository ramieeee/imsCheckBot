import checkBot
import getpass

def main():
    while True:
        mod = input("""which mode?
----------------------------
> Check current IMS  :   \'c\'
> Search IMS         :   \'s\'
> Add IMS            :   \'a\'
> Delete IMS         :   \'d\'
> Exit               :   \'e\'
----------------------------
=> """)

        if mod == 'e':
            print("System: Exiting the program")
            break

        elif mod == 's':
            id = input("id: ")
            pw = getpass.getpass("pw: ")

            # execute macro
            IMSCheckBot = checkBot.IMSCheckBot(id, pw, ims_nums)
            IMSCheckBot.run_program()
    
        elif mod == 'a':
            print('a')
    
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