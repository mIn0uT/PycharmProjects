# string concatenation

youtuber = "kahlid"

print("Subscribe to " + youtuber) # most common
print("Subscribe to {}".format(youtuber)) # places value inside the curly braces
print(f"Subscribe to {youtuber}") # formatting

adj = input("Input some adjective: ")
verb1 = input("Verb: ")
verb2 = input("Verb: ")
famous_person = input("Famous Person: ")

madlib = f"Computer programming is so {adj}! It makes me so excited all the time because \n" \
         f"I love to {verb1}. Stay hidrated and {verb2} like you are {famous_person}!"

print(madlib)