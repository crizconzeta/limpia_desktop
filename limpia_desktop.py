import os
from pathlib import Path
import shutil

def get_file_ext(file_input):
    '''
    function that returns the file extention of a given string.
    '''
    check_file = Path(file_input)
    return check_file.suffix.strip('.').lower()

def list_content(path, return_type):
    '''
    function that returns a list with directories or files depending on user input.
    Options: 'directory' / 'file'
    '''
    list_content = list(os.walk(path))
    if return_type == 'directory':
        return list_content[0][1]
    elif return_type == 'file':
        # return correct index, but do not include the .DS_Store file
        return ([file for file in list_content[0][2] if file != '.DS_Store'])

def execute_folder_cleanup(check_folder):
    '''
    procedure that cleans up the folder and organizes them into
    file extention named folder.
    '''
    get_files = list_content(check_folder,'file')

    for file in get_files:
        # extract file extention to get folder to create
        get_ext = get_file_ext(file)

        # create folder if it does not exist, skip if it does
        if get_ext != '':
            if get_ext not in list_content(check_folder, 'directory'):
                os.mkdir(check_folder + get_ext)

            shutil.move((check_folder + file) , (check_folder + get_ext))


if __name__ == '__main__':
    execute_folder_cleanup('/')
