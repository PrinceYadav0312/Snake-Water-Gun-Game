'''Snake Water Gun Game with computer.'''
import random

user_value = input("Enter your Move: ")

moves = ["Snake", "Water", "Gun"]
num = moves.index(user_value)
player = num

computer_num = random.randint(0,2)
computer_move = moves[computer_num]

print(f"Computer Move: {computer_move}")

result_matrix = [
    [0, 1, -1],
    [-1, 0, 1],
    [1, -1, 0]
]

result = result_matrix[player] [computer_num]

if result == 0:
    print("Game Draw 😵‍💫")
elif result == -1:
    print("Oops! You Loss the Game 😵‍💫")
else:
    print("Congratulation You Win 🥳")
