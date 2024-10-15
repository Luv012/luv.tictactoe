import tkinter as tk
from tkinter import messagebox

# Initialize the game window
root = tk.Tk()
root.title("Tic-Tac-Toe")

# Keep track of the current player and board state
current_player = "X"
board = ["", "", "", "", "", "", "", "", ""]

# Function to handle button clicks
def button_click(index):
    global current_player
    
    if buttons[index]["text"] == "" and board[index] == "":
        buttons[index]["text"] = current_player
        board[index] = current_player
        if check_winner():
            messagebox.showinfo("Tic-Tac-Toe", f"Player {current_player} wins!")
            reset_game()
        elif "" not in board:
            messagebox.showinfo("Tic-Tac-Toe", "It's a tie!")
            reset_game()
        else:
            current_player = "O" if current_player == "X" else "X"

# Function to check if someone has won
def check_winner():
    win_conditions = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Horizontal
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Vertical
        [0, 4, 8], [2, 4, 6]              # Diagonal
    ]
    
    for condition in win_conditions:
        if board[condition[0]] == board[condition[1]] == board[condition[2]] != "":
            return True
    return False

# Function to reset the game for a new round
def reset_game():
    global current_player, board
    current_player = "X"
    board = ["", "", "", "", "", "", "", "", ""]
    for button in buttons:
        button["text"] = ""

# Create a 3x3 grid of buttons
buttons = []
for i in range(9):
    button = tk.Button(root, text="", font=("Arial", 24), width=5, height=2,
                       command=lambda i=i: button_click(i))
    button.grid(row=i // 3, column=i % 3)
    buttons.append(button)

# Start the game window
root.mainloop()
