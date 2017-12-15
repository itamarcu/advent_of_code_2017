def day_9():
    with open('input.txt') as input_file:
        line = input_file.readline()
        
    score = 0
    garbage_score = 0
    current_depth = 0
    inside_garbage = False
    skip_char = False
    for char in line:
        if inside_garbage:
            if skip_char:
                skip_char = False
            elif char == "!":
                skip_char = True
            elif char == ">":
                inside_garbage = False
            else:
                garbage_score += 1
        else:  # when inside group, not garbage
            if char == "{":
                current_depth += 1
            elif char == "}":
                score += current_depth
                current_depth -= 1
            elif char == "<":
                inside_garbage = True
    
    print("Part 1:   ", score)
    print("Part 1:   ", garbage_score)


day_9()
