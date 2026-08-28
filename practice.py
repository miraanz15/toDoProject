colours = ["red", "green", "blue", "yellow", "white"]

print(colours[2])
print(colours[4])
print(f"Total colours: {len(colours)}")

colours.append("black")
print(f'Colour removed: {colours.remove("green")}')
colours.pop(0)
colours.insert(2, "orange")
print(f"Colours = {colours}")

for colour in colours:
    print(f"\n {colour}")

print("")

for number, colour in enumerate(colours, start = 1):
    print(f"{number}. {colour}")

numbers = [10,20,30,40,50]

for number in numbers:
    print(number)

print(colours[-1])

print("\n")


def no_return():
    print("I print but return nothing")

value = no_return()
print(value)