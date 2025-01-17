_, C = input().split()
A = input()

ans = ["W", "R", "B"][(A.count("R") - A.count("B")) % 3] == C

print(["No", "Yes"][ans])
