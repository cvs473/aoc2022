def part_one(input_data: list) -> int:
    points = 0 
    for el in input_data:
        el = el.rstrip("\n") 
        first_compartment = el[:int(len(el)/2)]
        second_compartment = el[int(len(el)/2):]
        for c in alphabet:
            if c in first_compartment and c in second_compartment:
                points += alphabet.index(c) + 1
    return points

def part_two(input_data: list) ->int:
    points = 0
    for i in range(0, len(input_data)-2, 3):
        arr = input_data[i : i+3]
        for c in alphabet:
            if c in arr[0].rstrip("\n") and c in arr[1].rstrip("\n") and c in arr[2].rstrip("\n"):
                points += alphabet.index(c) + 1
    return points


alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

with open("input.txt", encoding="UTF-8") as file_in:
    lines = file_in.readlines()


print(part_one(lines))
print("-----")
print(part_two(lines))
