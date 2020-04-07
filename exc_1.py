#!/usr/bin/python3

import sys
print('Number of arguments:', len(sys.argv), 'arguments.')
print('Argument List:', str(sys.argv))

S = "\t"
size = 10

def main():
    arr = []
    for i in range(size):
        # row = []
        row = size*[0]
        for j in range(size):
            # print(str(i) + " " + str(j))
            # print("%d %d" %(i, j))
            v = (i + 1) * (j + 1)
            # row.append(v)
            row[j] = v

        arr.append(row)
       # print()

    # def array
    # arr=[[i*j for j in (m)] for i in (n)]
    print_array(arr)


if  len(sys.argv) is 1:
    size = 5
    
else:
    size = int(str(sys.argv))


def print_array(arr):
    for row in arr:
        print(S.join([str(elem) for elem in row]))

if __name__ == "__main__":
    main()
