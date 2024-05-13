'''Week 2 Data Analytics Project'''
import pathlib
import statistics
import time
import williamson_utils

#Function 1
def create_folders_for_range(start, end):
    for i in range(start, end + 1):
        pathlib.Path(f"{i}").mkdir(exist_ok=True)

#Function 2
def create_folders_from_list(folder_names):
    for folder in folder_names:
        pathlib.Path(folder).mkdir(exist_ok=True)

#Function 3
def create_prefixed_folders(folder_names, prefix):
    for folder in folder_names:
        pathlib.Path(f"{prefix}-{folder}").mkdir(exist_ok=True)

#Function 4
def create_folders_periodically(duration):
    counter = 0
    while counter <= 3:
        counter += 1
        folder_name = f"Client_{counter}"
        pathlib.Path(folder_name).mkdir(exist_ok=True)
        time.sleep(duration)

def main():
    # Print byline from imported module
    print(f"Byline: {williamson_utils.byline}")

    # Call function 1 to create folders for a range 
    create_folders_for_range(start=2006, end=2010)

    # Call function 2 to create folders given a list
    folder_names = ['Power', 'Heart Rate', 'Training']
    create_folders_from_list(folder_names)

    # Call function 3 to create folders using comprehension
    prefix = 'Cost'
    create_prefixed_folders(folder_names, prefix)

    # Call function 4 to create folders periodically using while
    duration = 5  # duration in seconds
    create_folders_periodically(duration)

    # Add options e.g., to force lowercase and remove spaces 
    # to one or more of your functions (e.g. function 2) 
    # Call your function and test these options
    '''regions = [
      "North America", 
      "South America", 
      "Europe", 
      "Asia", 
      "Africa", 
      "Oceania", 
      "Middle East"
    ]'''
    #create_folders_from_list(regions, to_lowercase=True, remove_spaces=True)
    
if __name__ == '__main__':
    main()
