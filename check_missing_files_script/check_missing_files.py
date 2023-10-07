import os

while True:
    # Ask the user for the folder path
    folder_path = input("Enter the folder path where your video files are located: ")

    # Ask the user for the range of expected file numbers
    min_number = int(input("Enter the minimum file number: "))
    max_number = int(input("Enter the maximum file number: "))

    # Create a set of expected file names
    expected_files = set(f'{i}.mp4' for i in range(min_number, max_number + 1))

    # List all files in the folder
    files = os.listdir(folder_path)

    # Create a set of existing file names in the folder
    existing_files = set(files)

    # Find missing files by taking the set difference
    missing_files = expected_files - existing_files

    # Sort the missing file names numerically
    missing_files = sorted(missing_files, key=lambda x: int(x.split('.')[0]))

    # Print the missing file names
    if missing_files:
        print('Missing files:')
        for file_name in missing_files:
            print(file_name)
    else:
        print('No missing files.')

    # Ask the user if they want to check another folder
    repeat = input("Do you want to check another folder? (y/n): ")
    if repeat.lower() != 'y':
        break
