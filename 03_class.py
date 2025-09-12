def print_table(num): 
    for i in range(1, 11):
        print(f"{num} x {i} = {num*i}")

def print_tables_in_range(a, b):
    for num in range(a, b + 1):
        print(f"Multiplication table for {num}:")
        print_table(num)
        print()  # Print a newline for better readability

def main():
    while True:
        print("\nEnter the range in between you want to print multiplication table (a to b) OR a number :")
        print("Choose r=range or n=number or q=quit")
        choice = input("Enter your choice (r/n/q): ").strip().lower()
        if choice == 'n':
            num = int(input("Enter the number: "))
            print_table(num)
        elif choice == 'r':
            a = int(input("Enter the starting number (a): "))
            b = int(input("Enter the ending number (b): "))
            print_tables_in_range(a, b)
        elif choice == 'q':
            print("Exiting the multiplication table calculator.")
            break
        else:
            print("Invalid choice. Please enter 'r', 'n', or 'q'.")

if __name__== "__main__":
    main()