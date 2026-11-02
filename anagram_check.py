# Program to check whether two words are anagrams

word1 = input("Enter the first word: ").replace(" ", "").lower()
word2 = input("Enter the second word: ").replace(" ", "").lower()

if sorted(word1) == sorted(word2):
    print("The words are anagrams.")
else:
    print("The words are not anagrams.")
