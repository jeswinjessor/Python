def sentance_maker(phrase):
    interrogatives = ("why", "what", "how")
    capitalized = phrase.capitalize()
    if phrase.startswith(interrogatives):
        return "{}?".format(capitalized) # this will capitalize the sentacne and add ? mark if the sentace start with why, what, how
    else:
        return "{}.".format(capitalized) # this will add full stop and capitalize the normal sentance.

print(sentance_maker("how are you"))

results = []
while True:
    user_input = input("Say something: ")
    if user_input == "\end":
        break
    else:
         results.append(sentance_maker(user_input))

# will print the results line by line
for string in results:
    print(string)

# join the results
print(" ".join(results))