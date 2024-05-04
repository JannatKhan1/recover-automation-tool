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

import os
import subprocess  

# Gitisha ye run jupyter wala ab kaam nhi krega i have converted it to .py
# toh iske jagah .py file execute krne ki koshish kro
# plus recovery_automation.py ko bhi change krna padega 
def run_jupyter_notebook(csv_path):
    # Run the Jupyter notebook
    notebook_file = "Recovery_Automation.ipynb"
    # Execute the notebook with papermill
    os.system(f'jupyter nbconvert --execute {notebook_file} --ExecutePreprocessor.timeout=180 --to notebook --output {notebook_file} --execute "{csv_path}"')

def main():
    print("Welcome to Recover Function")
    while True:
        print("Enter your choice : ")
        print("1. Risk Assessment Report ")
        print("2. Integrity Checker")
        
        ch = int(input())

        if ch == 1:
            print("Please enter the path to the CSV file containing vulnerabilities of system: ")
            csv_path = input().strip()
            if os.path.isfile(csv_path):
                run_jupyter_notebook(csv_path)
                print("Risk Assessment Report generated successfully!")
                print(" You can find the report in file named 'cve_report.txt' !")
            else:
                print("Invalid path or file does not exist.")
        elif ch == 2:
            # Add functionality for option 2 here
            pass
        else:
            print("Invalid choice!")

        print("Repeat? (y/n)")
        if input().lower() != 'y':
            break


if __name__ == '__main__':
    main()

    