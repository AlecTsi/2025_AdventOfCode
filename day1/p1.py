start = 50
path = "/workspaces/2025_AdventOfCode/day1/input1.txt"
ans = 0

with open("/workspaces/2025_AdventOfCode/day1/input1.txt","r") as file:
    lines = file.readlines()
    for line in lines:
        line = line.replace("L", "-")
        line = line.replace("R","")
        line = int(line)
        print(line)

        start += line
        if start % 100 == 0:
            ans += 1
            
print(ans)
        
        
        
        

