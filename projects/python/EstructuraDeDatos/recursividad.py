def recursion(x):
    if x == 7:
        return 
    else:
        print(x)
        recursion(x + 1)

def main():
    print(recursion(1))
    print("Hello World!")

if __name__ == "__main__":
    main()