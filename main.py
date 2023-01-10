import tkinter as tk
from tkinter import messagebox


# Create a function for the Tic Tac Toe game logic
def game_logic(button):
    global btn1, btn2, btn3, btn4, btn5, btn6, btn7, btn8, btn9
    global player
    if button["text"] == " ":
        button["text"] = player
        check_for_winner()
        switch_player()

# Create a function to switch players
def switch_player():
    global player
    if player == "X":
        player = "O"
    else:
        player = "X"

# Create a function to check for a winner
def check_for_winner():
    global btn1, btn2, btn3, btn4, btn5, btn6, btn7, btn8, btn9
    global player

    # Check rows
    if btn1["text"] == player and btn2["text"] == player and btn3["text"] == player:
        game_over()
    elif btn4["text"] == player and btn5["text"] == player and btn6["text"] == player:
        game_over()
    elif btn7["text"] == player and btn8["text"] == player and btn9["text"] == player:
        game_over()

    # Check columns
    elif btn1["text"] == player and btn4["text"] == player and btn7["text"] == player:
        game_over()
    elif btn2["text"] == player and btn5["text"] == player and btn8["text"] == player:
        game_over()
    elif btn3["text"] == player and btn6["text"] == player and btn9["text"] == player:
        game_over()

    # Check diagonals
    elif btn1["text"] == player and btn5["text"] == player and btn9["text"] == player:
        game_over()
    elif btn3["text"] == player and btn5["text"] == player and btn7["text"] == player:
        game_over()

# Create a function to end the game
def game_over():
    global btn1, btn2, btn3, btn4, btn5, btn6, btn7, btn8, btn9
    global player
    messagebox.showinfo("Game Over", f"Player {player} wins!")
    btn1["text"] = " "
    btn2["text"] = " "
    btn3["text"] = " "
    btn4["text"] = " "
    btn5["text"] = " "
    btn6["text"] = " "
    btn7["text"] = " "
    btn8["text"] = " "
    btn9["text"] = " "
    player = "X"
def check_for_tie():
    global btn1, btn2, btn3, btn4, btn5, btn6, btn7, btn8, btn9
    if " " not in [btn1["text"], btn2["text"], btn3["text"], btn4["text"], btn5["text"], btn6["text"], btn7["text"], btn8["text"], btn9["text"]]:
        messagebox.showinfo("Game Over", "Its a tie!")
        btn1["text"] = " "
        btn2["text"] = " "
        btn3["text"] = " "
        btn4["text"] = " "
        btn5["text"] = " "
        btn6["text"] = " "
        btn7["text"] = " "
        btn8["text"] = " "
        btn9["text"] = " "
        player = "X"

# Create the Tkinter window and set the title
root = tk.Tk()
root.title("Tic Tac Toe")

# Create variables for the buttons and player
player = "X"
btn1 = tk.Button(root, text=" ", width=5, height=2, font=("Helvetica", 24), command=lambda: game_logic(btn1))
btn2 = tk.Button(root, text=" ", width=5, height=2, font=("Helvetica", 24), command=lambda: game_logic(btn2))
btn3 = tk.Button(root, text=" ", width=5, height=2, font=("Helvetica", 24), command=lambda: game_logic(btn3))
btn4 = tk.Button(root, text=" ", width=5, height=2, font=("Helvetica", 24), command=lambda: game_logic(btn4))
btn5 = tk.Button(root, text=" ", width=5, height=2, font=("Helvetica", 24), command=lambda: game_logic(btn5))
btn6 = tk.Button(root, text=" ", width=5, height=2, font=("Helvetica", 24), command=lambda: game_logic(btn6))
btn7 = tk.Button(root, text=" ", width=5, height=2, font=("Helvetica", 24), command=lambda: game_logic(btn7))
btn8 = tk.Button(root, text=" ", width=5, height=2, font=("Helvetica", 24), command=lambda: game_logic(btn8))
btn9 = tk.Button(root, text=" ", width=5, height=2, font=("Helvetica", 24), command=lambda: game_logic(btn9))

# Create the grid layout
btn1.grid(row=0, column=0)
btn2.grid(row=0, column=1)
btn3.grid(row=0, column=2)
btn4.grid(row=1, column=0)
btn5.grid(row=1, column=1)
btn6.grid(row=1, column=2)
btn7.grid(row=2, column=0)
btn8.grid(row=2, column=1)
btn9.grid(row=2, column=2)

root.mainloop()