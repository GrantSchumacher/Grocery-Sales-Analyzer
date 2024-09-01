import pandas as pd

print("--Sales Data Analyzer--\n")

def load_file():
    file_path = input("Enter the path of the excel file: \n").strip()

    try:
        data = pd.read_excel(file_path, header = 1)
        print("data loaded succesfully")
        return data
    except Exception as e:
        print("Error loading file. Please try again.")
        #print(e)
        load_file()
        return None
    

def main_menu():
    print("""
    Please select an option
          1. Top Performing Store
          2. Exit
    """)
    selected_menu_option = input()
    return selected_menu_option

def run_application():
    while True:
        selected_menu_option = main_menu()
        if selected_menu_option == '1':
            print("you've selected option 1")
        elif selected_menu_option == '2':
            print("Exiting Application")
            break
        else:
            print("Invalid option. Please try again")

    
df = load_file()
run_application()







    
