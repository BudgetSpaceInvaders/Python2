# Ask the user for 2 separate texts
text1 = input("Enter the first text: ")
text2 = input("Enter the second text: ")

# Remove spaces and convert to lower case
text1 = text1.replace(" ", "").lower()
text2 = text2.replace(" ", "").lower()

# Check if the two texts are anagrams
if sorted(text1) == sorted(text2):
    print("Anagrams")
else:
    print("Not anagrams")
