# Problem 8: Pooh's To Do's
# Write a function print_todo_list() that accepts a list of strings named tasks. 
# The function should then number and print each task on a new line using the format:

#Pooh's To Dos:
#1. Task 1
#2. Task 2
#...

def print_todo_list(task):
    print("Pooh's To Dos:")
    num = 1
    for t in task:
        print(f"{num}. {t}")
        num+=1
    print("\n")


if __name__ == '__main__':
    task = ["Count all the bees in the hive", "Chase all the clouds from the sky", "Think", "Stoutness Exercises"]
    print_todo_list(task)

    task = []
    print_todo_list(task)