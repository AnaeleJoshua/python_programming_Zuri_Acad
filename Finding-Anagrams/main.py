# Check if a word is an anagrams 
# Example:
# find_anagrams("hello") --> False
# find_anagrams("racecar") --> True


def find_anagrams(word1, word2):
    # the sorted strings are checked
    if sorted(word1) == sorted(word2):
        print("True")
    else:
        print("false")

        # [assignment] Add your code here

    return True


word1 = "oshuaj"
word2 = "joshua"

find_anagrams(word1, word2)
