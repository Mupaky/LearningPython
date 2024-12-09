import is_squares

def main():
    numbers = []
    while True:
        numstr = input("Enter a number: ")
        numbers.append(int(numstr))
        if input("Add another number? (y/n): ") != 'y':
            break
    print(is_squares.is_list_squares(numbers))

if __name__=="__main__":
    main()
