# Problem 2: Greeting
# Write a function greeting() that accepts a single parameter, a string name, and 
# prints the string "Welcome to The Hundred Acre Wood <name>! My name is Christopher Robin."

def greetings(name):
    print(f"Welcome to The Hundred Acre Wood {name}! My name is Christopher Robin.")


if __name__ == '__main__':
    greetings("Michael")
    greetings("Winnie the Pooh")