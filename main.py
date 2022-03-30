import checkBot
import getpass

def main():
    id = input("id: ")
    pw = getpass.getpass("pw: ")
    IMSCheckBot = checkBot.IMSCheckBot(id, pw)
    IMSCheckBot.run_program()

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(e)
