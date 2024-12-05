#List
def process_list(j):
    my_list = []

    for i in j:
        parts = i.split()
        list_type = parts[0]

        if list_type == "insert":
            index = int(parts[1])
            element = int(parts[2])
            my_list.insert(index, element)
        elif list_type == "print":
            print(my_list)
        elif list_type == "remove":
            element = int(parts[1])
            my_list.remove(element)
        elif list_type == "append":
            element = int(parts[1])
            my_list.append(element)
        elif list_type == "sort":
            my_list.sort()
        elif list_type == "pop":
            my_list.pop()
        elif list_type == "reverse":
            my_list.reverse()


def main():
    n = int(input())
    j = []
    for _ in range(n):
        i = input()
        j.append(i)
    process_list(j)


if __name__ == "__main__":
    main()


