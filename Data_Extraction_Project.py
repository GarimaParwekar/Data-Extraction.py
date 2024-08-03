import os  # Import the os module to interact with the operating system

# Get the current working directory
Current_Directory = os.getcwd()

# Initialize an empty list to store file information
File_info_list = []

# Iterate over each item in the current directory
for item in os.listdir(Current_Directory):
    # Get the full path of the item
    path = os.path.join(Current_Directory, item)
   
    # Check if the item is a file
    if os.path.isfile(path):
        # Get the size of the file
        Size_of_file = os.path.getsize(path)
        # Append the file path and size to the list as a dictionary
        File_info_list.append({'Path_of_the_file': path, 'Size': Size_of_file})

# Print the information of each file
for file in File_info_list:
    print(file)
