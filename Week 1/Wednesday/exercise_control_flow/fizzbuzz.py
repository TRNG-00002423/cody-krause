def fizzbuzz(n):
    for i in range(1, n + 1):
        if i % 3 == 0:
            print("Fizz", end="")
        if i % 5 == 0:
            print("Buzz", end="")
        if i % 7 == 0:
            print("Boom", end="")
        if i % 3 != 0 and i % 5 != 0 and i % 7 != 0:
            print(f"{i}", end="")
        print()  # Newline after each number
        
if __name__ == "__main__":
    fizzbuzz(105)