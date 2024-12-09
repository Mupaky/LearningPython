from group_subsets import subsets_of_list

def main():
    numbers = []
    while True:
        numstr = input("Enter a number: ")
        numbers.append(int(numstr))
        if input("Add another number? (y/n): ") != 'y':
            break
    print(subsets_of_list(numbers))

if __name__=="__main__":
    main()