# Program to display a table of numbers with their squares and cubes

print("Number    Square    Cube")
for number in range(1, 6):
    square = number ** 2
    cube = number ** 3
    print(f"{number:<10}{square:<10}{cube}")
