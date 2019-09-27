def histogram(arr):
    result = {}

    for num in arr:
        result[num] = result.get(num, 0) + 1

    return result

def reverse_words(string):
    words = list(string.split(" "))
    
    print(words[::-1])

def fib(n):
    if n <= 1: return n
    else: return(fib(n-1) + fib(n-2))

def balanced_brackets(string):
    open_list = ["[","{","("]
    close_list = ["]","}",")"]

    stack = []
    for i in string:
        if i in open_list:
            stack.append(i)
        elif i in close_list:
            pos = close_list.index(i)
            if ((len(stack) > 0) and (open_list[pos] == stack[len(stack)-1])):
                stack.pop()
            else:
                return "Unbalanced"
    if len(stack) == 0:
        return "Balanced"

def is_palindrome(string):
    return string == string[::-1]

def longest_palindrome(string):
    words = list(string.split(" "))
    longest_len = 0
    longest_len_index = 0

    for i in range(len(words)):
        if is_palindrome(words[i]) and len(words[i]) > longest_len:
            longest_len = len(words[i])
            longest_len_index = i

    return words[longest_len_index]

if __name__ == "__main__":

    # arr = list(map(int, input().split()))
    # print(histogram(arr))

    reverse_words("I am Yoda!")

    print(fib(10))

    print(balanced_brackets("(()())"))

    print(longest_palindrome("asdsa assaassaassa dfghjkasdfghjkxcvbnm,xcvbn,"))