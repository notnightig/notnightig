# Import tkinter module
import tkinter as tk

# Define constants for window size and cell size
WINDOW_SIZE = 600
CELL_SIZE = WINDOW_SIZE / 3

# Define colors for X and O
X_COLOR = "blue"
O_COLOR = "red"

# Define a class to represent a tic tac toe board
class Board:

    # Initialize the board with an empty grid and a turn indicator
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Tic-Tac-Toe")
        self.canvas = tk.Canvas(self.window, width=WINDOW_SIZE, height=WINDOW_SIZE)
        self.canvas.pack()
        self.board = [[None for _ in range(3)] for _ in range(3)]
        self.turn = "X"
        self.draw_grid()
        self.canvas.bind("<Button-1>", self.cell_clicked)

    # Draw the grid lines on the canvas
    def draw_grid(self):
        for i in range(1, 3):
            # Draw a horizontal line
            self.canvas.create_line(0, i * CELL_SIZE, WINDOW_SIZE, i * CELL_SIZE)
            # Draw a vertical line
            self.canvas.create_line(i * CELL_SIZE, 0, i * CELL_SIZE, WINDOW_SIZE)

    # Handle mouse clicks on the canvas
    def cell_clicked(self, event):
        # Get the row and column of the clicked cell
        row = int(event.y // CELL_SIZE)
        col = int(event.x // CELL_SIZE)

        # Check if the cell is empty and it's a valid turn
        if not self.board[row][col] and self.turn:
            # Mark the cell with X or O
            self.mark_cell(row, col)

            # Check if there is a winner or a tie
            winner = self.check_winner()
            if winner:
                # Display a message with the winner or a tie
                self.display_message(f"{winner} wins!")
                # Stop the game by setting turn to None
                self.turn = None

    # Mark a cell with X or O on the board and on the canvas
    def mark_cell(self, row, col):
        # Get the center coordinates of the cell
        x = col * CELL_SIZE + CELL_SIZE / 2
        y = row * CELL_SIZE + CELL_SIZE / 2

        # Draw an X or an O on the canvas with appropriate color and font size 
        if self.turn == "X":
            text = self.canvas.create_text(x,y,text=self.turn,
                                           fill=X_COLOR,
                                           font=("Helvetica", int(-CELL_SIZE/2)))
