import tkinter as tk
import pygame
import pygame.locals

# Initialize Pygame
pygame.init()

# Create the main window
window = tk.Tk()
window.title("Chess Board")

# Define the chessboard dimensions
rows = 8
cols = 8

# Define the chessboard square size
square_size = 60

# Set up Pygame display
display = pygame.display.set_mode((cols * square_size, rows * square_size))

# Create a 2D list to represent the chessboard squares
squares = [[None for _ in range(cols)] for _ in range(rows)]

# Define the Unicode symbols for chess pieces
pieces = {
    "w_king": "\u2654",
    "w_queen": "\u2655",
    "w_rook": "\u2656",
    "w_bishop": "\u2657",
    "w_knight": "\u2658",
    "w_pawn": "\u2659",
    "b_king": "\u265A",
    "b_queen": "\u265B",
    "b_rook": "\u265C",
    "b_bishop": "\u265D",
    "b_knight": "\u265E",
    "b_pawn": "\u265F"
}

# Create the chessboard GUI
for row in range(rows):
    for col in range(cols):
        color = (255, 255, 255) if (row + col) % 2 == 0 else (0, 0, 0)
        square = tk.Frame(window, width=square_size, height=square_size, bg=color)
        square.grid(row=row, column=col)
        squares[row][col] = square

        # Add chess pieces to the squares
        piece = None
        if row == 0:
            if col == 0 or col == 7:
                piece = pieces["b_rook"]
            elif col == 1 or col == 6:
                piece = pieces["b_knight"]
            elif col == 2 or col == 5:
                piece = pieces["b_bishop"]
            elif col == 3:
                piece = pieces["b_queen"]
            elif col == 4:
                piece = pieces["b_king"]
        elif row == 1:
            piece = pieces["b_pawn"]
        elif row == 6:
            piece = pieces["w_pawn"]
        elif row == 7:
            if col == 0 or col == 7:
                piece = pieces["w_rook"]
            elif col == 1 or col == 6:
                piece = pieces["w_knight"]
            elif col == 2 or col == 5:
                piece = pieces["w_bishop"]
            elif col == 3:
                piece = pieces["w_queen"]
            elif col == 4:
                piece = pieces["w_king"]

        if piece:
            label = tk.Label(square, text=piece, font=("Arial", 36))
            label.pack()

# Pygame event loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False

     # Get the mouse click position
    if pygame.mouse.get_pressed()[0]:
        mouse_pos = pygame.mouse.get_pos()
        col = mouse_pos[0] // square_size
        row = mouse_pos[1] // square_size
        print("Clicked on square:", row, col)

    # Draw the updated Pygame display
    pygame.display.update()

# Quit Pygame
pygame.quit()

# Start the Tkinter event loop
window.mainloop()