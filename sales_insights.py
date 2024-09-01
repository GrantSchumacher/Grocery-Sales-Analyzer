import pandas as pd

print("--Sales Data Analyzer--\n")

def load_file():
    file_path = input("Enter the path of the excel file: \n").strip()

    try:
        data = pd.read_excel(file_path)
        print("data loaded succesfully")
        return data
    except Exception as e:
        print("error loading file. Please try again.")
        print(e)
        return None
    

load_file()


    
