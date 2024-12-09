from combinations import sums_of_n

def main():
    numbers = []
    while True:
        numstr = input("Enter a number: ")
        numbers.append(int(numstr))
        if input("Add another number? (y/n): ") != 'y':
            break
    count = int(input("Enter the number of elements to combine: "))
    print(sorted(list(sums_of_n(count, numbers))))

def sorted_list_of_sums_of_n(n, lst):
    return sorted(list(sums_of_n(n, lst)))

if __name__=="__main__":
    main()