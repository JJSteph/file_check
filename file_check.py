##
## File checker program
##
## 6/19/2021
##

## I'm going to try and create a program to compare files in two directories

import sys
import os


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

    print('')
    print(f'Contents of path 1:')
    print(path_1_contents)
    print('')

    print(f'Contents of path 2:')
    print(path_2_contents)
    print('')

    ## compare the two
    ## Just comparing names
    ## Not efficient...look into other methods

    same_items = []

    for i in path_1_contents:
        for j in path_2_contents:

            if i == j:
                same_items.append(i)
                

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