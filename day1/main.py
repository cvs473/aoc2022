def check(arr, dig):
    if min(arr) < dig:
        arr[arr.index(min(arr))] = dig 

top3_carry = [0, 0, 0]

with open("input.txt", encoding="UTF-8") as items:
    tmp = 0 
    for line in items:
        if line.rstrip("\n").isdigit() == True:
            tmp += int(line.rstrip("\n"))
        else:
            check(top3_carry, tmp)
            tmp = 0

check(top3_carry, tmp)

print(sum(top3_carry))
print(top3_carry)
        
