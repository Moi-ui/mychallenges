palindrome = lambda s: s == s[::-1]
if __name__ == "__main__":
    test_string = input("Enter a string to check if it's a palindrome: ")
    if palindrome(test_string):
        print(f'"{test_string}" is a palindrome.')
    else:
        print(f'"{test_string}" is not a palindrome.')