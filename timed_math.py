import random
import time

operators = ["+", "-", "*"]
min_operation = 3
max_operation = 10
total_problem = int(input("enter the no of problems:"))

def generate_expression():
    left = random.randint(min_operation,max_operation)
    right = random.randint(min_operation,max_operation)
    operator = random.choice(operators)

    expr = str(left) + " " + operator + " " + str(right)
    answer = eval(expr)
    return expr,answer

wrong = 0
input("enter press to start")
start_time = time.time()
for i in range(total_problem):
    expr, answer = generate_expression()
    while True:
        guess = input("Problem #" + str(i + 1) + ": " + expr + " = ")
        if guess == str(answer):
            break
        wrong += 1

end_time = time.time()
total_time = round(end_time - start_time, 2)
print("Nice work! You finished in", total_time, "seconds!")
print("You got", wrong, "problems wrong.")


