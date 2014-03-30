def final_position(commands, A, B):
    position = 0
    for command in commands:
        if command == "R" and position < B:
            position += 1
        elif command == "L" and position > -A:
            position -= 1
    return position
