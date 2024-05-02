
# Gitisha ne bola h comment krne ko, mera man toh delete krne ka tha
# def operation():
#     print(" 1.  \n 2. Integrity Checker \n 3.  \n 4. Exit")
#     print("Enter the operation you want to perform: ")
#     user_input = int(input())
#     return user_input

# a = operation()
# while(a != 4):
#     if(type(a) != int):
#         print("Enter a number!")
#     if(a < 1 or a>4):
#         print("Enter the number between 1 to 4 !")            

def main():
    print("Welcome to Recover Function")
    while True:
        print("Enter your choice : ")
        print("1. Risk Assessment Report ")
        print("2. Backup the data with Veeam Agent and Integrity Checker")
        
        ch = int(input())

        print("Repeat? (y/n)")
        if input().lower() != 'y':
            break


if __name__ == '__main__':
    main()

    