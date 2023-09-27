def part_one(input_data: list) -> int:
    points = 0
    for s in input_data:
        arr = s.rstrip("\n").split()
        match (arr[0], arr[1]):
            case ('A', 'X'):
                points += (1 + 3)
            case ('A', 'Y'):
                points += (2 + 6)
            case ('A', 'Z'):
                points += (3 + 0)
            case ('B', 'X'):
                points += (1 + 0)
            case ('B', 'Y'):
                points += (2 + 3)
            case ('B', 'Z'):
                points += (3 + 6)
            case ('C', 'X'):
                points += (1 + 6)
            case ('C', 'Y'):
                points += (2 + 0)
            case ('C', 'Z'):
                points += (3 + 3)

    return points
   

def part_two(input_data: list) -> int:
    points = 0
    for s in input_data:
        arr = s.rstrip("\n").split()
        match (arr[0], arr[1]):
            case ('A', 'X'):
                points += (3 + 0)
            case ('A', 'Y'):
                points += (1 + 3)
            case ('A', 'Z'):
                points += (2 + 6)
            case ('B', 'X'):
                points += (1 + 0)
            case ('B', 'Y'):
                points += (2 + 3)
            case ('B', 'Z'):
                points += (3 + 6)
            case ('C', 'X'):
                points += (2 + 0)
            case ('C', 'Y'):
                points += (3 + 3)
            case ('C', 'Z'):
                points += (1 + 6)

    return points

with open("input.txt", encoding="UTF-8") as file_in:
    lines = file_in.readlines()

print(part_one(lines))
print("-----")
print(part_two(lines))
