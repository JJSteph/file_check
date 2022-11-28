##
## File checker program
##
## 6/19/2021
##

## I'm going to try and create a program to compare files in two directories

import hashlib
import sys
import os
from pathlib import Path

buffer_size = 65536 # 64kb

def main():

    ## check arguments exist

    if len(sys.argv) != 3:
        print('Please enter two paths')
        sys.exit()

    else:
        path_1 = sys.argv[1]
        path_2 = sys.argv[2]


    ## get list of files in each path

    try:
        path_1_contents = os.listdir(path_1)
    except:
        print('Path not found')
        sys.exit()

    try:
        path_2_contents = os.listdir(path_2)
    except:
        print('Path not found')
        sys.exit()

    # If both paths are the same

    if path_1 == path_2:
        print('Please provide two different paths')
        sys.exit()

    ## First I'm comparing names

    same_name_items = []

    for i in path_1_contents:
        for j in path_2_contents:

            path_1_check = Path(path_1 + '/' + i)
            path_2_check = Path(path_2 + '/' + j)

            # Don't compare folders
            if path_1_check.is_dir() or path_2_check.is_dir():
                continue

            elif i == j:
                same_name_items.append(i)
                

    ## Check hashes for files with same names

    same_items = []

    for i in same_name_items:

        file_1_hash = hashlib.sha256()
        file_2_hash = hashlib.sha256()

        with open(Path(path_1, i), 'rb') as file_1, open(Path(path_2, i), 'rb') as file_2:
            while True:
                
                data_1 = file_1.read(buffer_size)
                data_2 = file_2.read(buffer_size)

                if not data_1 or not data_2:
                    # If reaches end of file
                    same_items.append(i)
                    break
                
                file_1_hash.update(data_1)
                file_2_hash.update(data_2)

                if file_1_hash.hexdigest() != file_2_hash.hexdigest():
                    break


    ## Give report on each path
    print('')
    print('Path 1:')
    print('#' * 50)
    print(path_1)
    print(f'{len(same_items)} / {len(path_1_contents)} files in path 1 were found in path 2.')
    print('\n')

    print('Path 2:')
    print('#' * 50)
    print(path_2)
    print(f'{len(same_items)} / {len(path_2_contents)} files in path 2 were found in path 1.')
    print('\n')

    ## return list of files in both

    if len(same_items) == 0:
        print('No shared files exist between the two paths.')

    else:
        print('Shared files (files in both paths):')
        print('#' * 50)
        print(f'There were {len(same_items)} shared items found')
        print('')

        for i, filename in enumerate(same_items, 1):
            file_num = "File " + str(i) + " / " + str(len(same_items)) + ":"
            print(f'{file_num} {filename}')

    print('')


if __name__ == '__main__':
    main()