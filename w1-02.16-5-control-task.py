numbers = input().split()

if len(numbers) == 0:
    print("Must  be entered at least one value.")
    quit()

theNumber = input()
if len(theNumber) == 0:
    print("You have not entered a value to compare.")
    quit()

switch = 0
for i in numbers:
    if theNumber == i:
        print(numbers.index(i), end=" ")
        numbers[numbers.index(i)] = ""
        switch = 1
if switch == 0:
    print("Отсутствует", end="")
print()
