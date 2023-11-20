import tkinter as tk

# Function to handle user's move
def make_move(col):
    # You can add your game logic here
    # This function should update the board, then call update_board_display(board) to display the result
    pass

# Function to draw X and O marks
def draw_x(canvas, x, y, size, color='red'):
    canvas.create_line(x - size, y - size, x + size, y + size, fill=color, width=4)
    canvas.create_line(x - size, y + size, x + size, y - size, fill=color, width=4)

def draw_o(canvas, x, y, size, color='blue'):
    canvas.create_oval(x - size, y - size, x + size, y + size, outline=color, width=4)

# Function to update the game board display based on the provided matrix
def update_board_display(board):
    for row in range(6):
        for col in range(7):
            tile = labels[row][col]
            if board[row][col] == 'X':
                draw_x(canvas, tile.winfo_rootx() + 32, tile.winfo_rooty() + 32, 24)
            elif board[row][col] == 'O':
                draw_o(canvas, tile.winfo_rootx() + 32, tile.winfo_rooty() + 32, 24)

# Create the main application window
root = tk.Tk()
root.title("Connect Four")

# Create a frame to hold the game board
board_frame = tk.Frame(root)
board_frame.pack()

# Create a canvas widget for drawing the game board
canvas = tk.Canvas(board_frame, width=7 * 64, height=6 * 64, bg='white')
canvas.grid(row=0, column=0, columnspan=7, rowspan=6)

# Create labels to represent the game board
labels = []
for row in range(6):
    row_labels = []
    for col in range(7):
        label = tk.Label(board_frame, text="", width=32, height=16, relief="ridge")
        label.grid(row=row, column=col)
        row_labels.append(label)
    labels.append(row_labels)

# Create buttons for each column to allow user input
buttons = []
for col in range(7):
    button = tk.Button(board_frame, text=f"Drop {col+1}", command=lambda c=col: make_move(c))
    button.grid(row=6, column=col, padx=10, pady=10)
    buttons.append(button)

# Styling for the buttons
for button in buttons:
    button.configure(bg='yellow', fg='black', width=16, height=4)

# Calculate the window size based on the board size
window_width = 7 * 64
window_height = 6 * 64 + 100  # 100 is for the button row
root.geometry(f"{window_width}x{window_height}")

# Example board matrix (replace this with your actual game board)
example_board = [
    ['X', 'O', '', '', '', '', ''],
    ['O', 'X', '', '', '', '', ''],
    ['', '', 'X', '', '', '', ''],
    ['', '', 'O', 'X', '', '', ''],
    ['', '', '', 'O', '', '', ''],
    ['', '', '', '', '', '', '']
]

# Update the game board display with the example board
update_board_display(example_board)

# Start the Tkinter main loop
root.mainloop()
