import turtle

def koch_segment(t, order, size):
    """
    Draws a single segment of the Koch curve.
    :param t: Turtle object
    :param order: Recursion level (integer)
    :param size: Length of the current segment (float)
    """
    if order == 0:
        t.forward(size)
    else:
        for angle in [60, -120, 60, 0]: # Sequence of turns for the Koch segment
            koch_segment(t, order - 1, size / 3)
            t.left(angle)

def draw_koch_snowflake(t, order, size):
    """
    Draws the complete Koch snowflake by drawing three Koch segments.
    :param t: Turtle object
    :param order: Recursion level (integer)
    :param size: Length of one side of the initial equilateral triangle (float)
    """
    for _ in range(3):
        koch_segment(t, order, size)
        t.right(120) # Turn to draw the next side of the snowflake

def main_task2():
    """
    Main function for Task 2: Koch Snowflake.
    """
    while True:
        try:
            level = int(input("Enter the recursion level for the Koch snowflake (e.g., 0, 1, 2, 3, 4): "))
            if level < 0:
                print("Level cannot be negative. Please enter a non-negative integer.")
            else:
                break
        except ValueError:
            print("Invalid input. Please enter an integer.")

    # Screen setup
    screen = turtle.Screen()
    screen.setup(width=800, height=700)
    screen.bgcolor("white")
    screen.title(f"Koch Snowflake - Level {level}")
    
    # Turtle setup
    pen = turtle.Turtle()
    pen.speed(0)  # 0 is the fastest, "fastest" also works
    pen.hideturtle()
    pen.penup()
    
    # Position the turtle to start drawing
    # Adjust starting position so the snowflake is somewhat centered
    initial_size = 300 # Adjust as needed for screen size and level
    if level == 0:
        pen.goto(-initial_size / 2, initial_size / (2 * (3**0.5) ) ) # Centering a triangle
    elif level == 1:
         pen.goto(-initial_size / 2, initial_size / 3)
    elif level == 2:
        pen.goto(-initial_size /1.5, initial_size / 2.5)
    elif level > 2 :
        pen.goto(-initial_size* ( (4/3)**(level-2) ) / 1.5 , initial_size / (2 - level*0.1) )
   
    pen.pendown()
    pen.color("blue")
    
    # Draw the snowflake
    draw_koch_snowflake(pen, level, initial_size)
    
    print(f"Koch snowflake with level {level} drawn.")
    screen.mainloop() # Keep the window open until manually closed

if __name__ == "__main__":
     main_task2()