S = "\t"
size = int(input())

def main():
    arr = []
    for i in range(size):
        # row = []
        row = size*[0]
        for j in range(size):
            v = (i + 1) * (j + 1)
            # row.append(v)
            row[j] = v

        arr.append(row)
       # print()

    print_array(arr)


def print_array(arr):
    for row in arr:
        print(S.join([str(elem) for elem in row]))

if __name__ == "__main__":
    main()
