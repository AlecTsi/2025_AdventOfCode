def main():
    """
    dial starts at 50
    dial goes from 0 - 99
    Password is the # of times it points at 0 after each rotation
    """
    
    print(get_answer())

def get_answer():
    dial = 50
    ans = 0
    path = "/workspaces/2025_AdventOfCode/day1/input1.txt"

    with open(path) as f:
        turns = [int(line.strip().replace("L", "-").replace("R","")) for line in f]

    for turn in turns:
        dial = (dial + turn) % 100
        
        if dial == 0:
            ans += 1
            
    return ans
    
if __name__ == "__main__":
    main()    
        
        

