numbers = [4, 2, 7, 2, 9, 4, 5]

seen = set()

for number in numbers:
    if number in seen:
        print("First duplicate:", number)
        break
    seen.add(number)
else:
    print("No duplicates found")