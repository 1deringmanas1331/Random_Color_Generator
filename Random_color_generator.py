# Import random module
import random

def generate_random_color():
    # Generate any random color code with this logic
    red = random.randint(0, 255)
    green = random.randint(0, 255)
    blue = random.randint(0, 255)
    return (red, green, blue)

if __name__ == "__main__":
    random_color = generate_random_color()
    print(f"Random Color: RGB{random_color}")
