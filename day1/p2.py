path = "/workspaces/2025_AdventOfCode/day1/input1.txt"
start = 50
ans = 0
a2 = 0
with open(path, "r") as file:
    for line in file:
        clean_line = line.strip()
        clean_line = clean_line.replace("L", "-").replace("R", "")
        value = int(clean_line)
        start += value
        a,b = divmod(start, 100)
        # Check condition
        if b % 100 == 0:
            ans += 1
            ans += abs(a-a2) - 1
            a2 = a
        else:
            ans += abs(a-a2)
            a2 = a
print(f"Final Answer: {ans}")
