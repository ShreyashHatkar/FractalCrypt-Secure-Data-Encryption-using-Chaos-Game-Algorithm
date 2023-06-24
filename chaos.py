import math
import random
from tabulate import tabulate

# Define the alphabet
alphabet = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789 .,?!'

# Define the vertices of the polygon
num_vertices = len(alphabet)
angle = 2 * math.pi / num_vertices
radius = 1 / math.sqrt(2)
vertices = [(math.cos(i * angle) * radius, math.sin(i * angle) * radius) for i in range(num_vertices)]

# Define the chaos game function
def chaos_game(seed):
    random.seed(seed)
    x, y = random.random(), random.random()
    while True:
        yield x, y
        vertex = random.choice(vertices)
        x, y = (x + vertex[0]) / 2, (y + vertex[1]) / 2

# Define the function to encrypt the text
def encrypt_text(text, seed):
    letter_coordinates = {alphabet[i]: vertices[i] for i in range(len(alphabet))}
    encrypted_coords = []
    for letter in text:
        if letter not in letter_coordinates:
            continue
        target_coord = letter_coordinates[letter]
        cg = chaos_game(seed)
        for i in range(1000):
            x, y = next(cg)
        encrypted_coords.append((target_coord[0] + x, target_coord[1] + y))
    return encrypted_coords

# Get the user input
text = input("Enter the text to encrypt: ")
seed = int(input("Enter the seed value: "))

# Encrypt the text
encrypted_coords = encrypt_text(text, seed)

# Print the encrypted coordinates in a tabular format
table = []
for i in range(len(text)):
    table.append([text[i], encrypted_coords[i][0], encrypted_coords[i][1]])
print(tabulate(table, headers=["Letter", "X Coordinate", "Y Coordinate"], tablefmt="pretty"))
