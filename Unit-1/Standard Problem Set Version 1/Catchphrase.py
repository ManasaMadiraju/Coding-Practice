# Problem 3: Catchphrase
# Write a function print_catchphrase() that accepts a string character as a parameter and
# prints the catchphrase of the given character as outlined in the table below.


def print_catchphrase(character):
    catchphrases = {'Pooh' : 'Oh bother!', 'Tigger': 'TTFN: Ta-ta for now!', 'Eeyore': 'Thanks for noticing me.', 'Christopher Robin': 'Silly old bear.'}

    if character in catchphrases:
        print(catchphrases[character]) 
    else:
        print("Sorry! I don't know <character>'s catchphrase!")
        

if __name__ == '__main__':
    character = "Pooh"
    print_catchphrase(character)

    character = "Piglet"
    print_catchphrase(character)
