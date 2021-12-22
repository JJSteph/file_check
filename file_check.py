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

    # print('')
    # print(f'Contents of path 1:')
    # print(path_1_contents)
    # print('')

    # print(f'Contents of path 2:')
    # print(path_2_contents)
    # print('')


    ## compare the two
    ## Just comparing names
    ## Not efficient...look into other methods

    same_name_items = []

    for i in path_1_contents:
        for j in path_2_contents:

            if i == j:
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
    print(f'Path 1: {len(same_items)} / {len(path_1_contents)} files were found in path 2.')
    print('')
    print(f'Path 2: {len(same_items)} / {len(path_2_contents)} files were found in path 1.')
    print('')

    ## return list of files in both

    if len(same_items) == 0:
        print('No similar items found.')

    else:
        print(f'There were {len(same_items)} similar items found.')
        print('')

        for i in range(len(same_items)):
            print(f'File {i + 1} / {len(same_items)}: {same_items[i]}')

    print('')


if __name__ == '__main__':
    main()