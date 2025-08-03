def factorial():
    try:
        n = int(input("Enter a number:"))

        if n < 0:
            print("Negative number is not allowed")
        
        f = 1
        c = n 

        while (c > 0):
            f *= c
            c -=1

            print("The factorial number is", f)
    except ValueError:
        print("Invalid input. Please enter an integer.")
        
factorial()