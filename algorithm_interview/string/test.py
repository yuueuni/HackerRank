import sys
import collections
import re
import time

# Palindrome
# Return True if word(or sentence) is Palindrome

# Use String - List
def palidrome1(words: str) -> bool:
    # isalnum(): string check (Alpahbet or Number)
    origin = [ w.lower() for w in words if w.isalnum() ]
    reverse_origin = origin
    reverse_origin.reverse()

    return origin == reverse_origin

# Use Deque
def palidrome2(words: str) -> bool:
    origin : Deque = collections.deque(w.lower() for w in words if w.isalnum())
    reverse_origin = origin
    reverse_origin.reverse()
    return True

def palidrome3(words: str) -> bool:
    words = re.sub('[^a-z0-9]', '', words.lower())
    return words == words[::-1]

if __name__ == '__main__':
    words = input()
    start = time.time()
    result = palidrome3(words)
    end = time.time()
    print(result, end - start)