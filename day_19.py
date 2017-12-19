from operator import __add__


def day_19():
    with open("input.txt") as file:
        lines = file.readlines()
    
    matrix = {}
    for row in range(len(lines)):
        for col in range(len(lines[row])):
            matrix[(row, col)] = lines[row][col]
    
    directions = {"U": (-1, 0),
                  "D": (+1, 0),
                  "L": (0, -1),
                  "R": (0, +1)}
    
    position = (0, lines[0].index("|"))  # row, column
    direction = "D"
    letters = []
    count = 0
    while True:
        count += 1
        position = tuple(map(__add__, position, directions[direction]))
        while matrix[position] != "+":
            if matrix[position] == " ":
                print("Part 1:", "".join(letters), "Part 2:", count)
                return
            if matrix[position] not in "|-+":
                letters.append(matrix[position])
            count += 1
            position = tuple(map(__add__, position, directions[direction]))
        
        for next_dir in directions.keys():
            if directions[next_dir][0] != directions[direction][0] and \
                    directions[next_dir][1] != directions[direction][
                1]:  # shortcut hack to check only 90 deg angles
                if matrix[tuple(map(__add__, position,
                                    directions[next_dir]))] != " ":
                    direction = next_dir
                    break


day_19()
