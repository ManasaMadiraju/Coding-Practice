# Problem 6: Double Trouble
# Help Winnie the Pooh double his honey! 
# Write a function doubled() that accepts a list of integers hunny_jars as a parameter and 
# multiplies each element in the list by two. Return the doubled list.

def doubled(hunny_jars):
    result = [num * 2 for num in hunny_jars]
    print(result)


if __name__ == '__main__':
    hunny_jars = [1, 2, 3]
    doubled(hunny_jars)