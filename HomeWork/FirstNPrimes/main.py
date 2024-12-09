import primes

def main():
    numstr = input("Enter a number: ")
    num = int(numstr)
    print(primes.first_n_primes(num))

if __name__=="__main__":
    main()