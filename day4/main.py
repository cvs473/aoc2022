def part_one(input_data: list) -> int:
    completely_overlapped_pairs_num = 0
    for el in input_data:
        el = el.rstrip("\n").split(',')
        assign_1 = [int(i) for i in el[0].split('-')]
        assign_2 = [int(i) for i in el[1].split('-')]
        if ((assign_1[0] >= assign_2[0] and assign_1[1] <= assign_2[1]) or
            (assign_1[0] <= assign_2[0] and assign_1[1] >= assign_2[1])):
            completely_overlapped_pairs_num += 1
    return completely_overlapped_pairs_num


def part_two(input_data: list) -> int:
    overlapped_pairs_num = 0
    for el in input_data:
        el = el.rstrip("\n").split(',')
        assign_1 = [int(i) for i in el[0].split('-')]
        assign_2 = [int(i) for i in el[1].split('-')]
        if (assign_1[1] < assign_2[0] or assign_1[0] > assign_2[1]):
            continue 
        else: overlapped_pairs_num += 1
    return overlapped_pairs_num


with open("input.txt", encoding="UTF-8") as file_in:
    lines = file_in.readlines()

print(part_one(lines))
print("----")
print(part_two(lines))
