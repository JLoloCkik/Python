km = float(input())
m = float(input())
cm = float(input())

cm = km * 100000 + m * 100 + cm 

merfold = cm * 0.0000062137
yard = cm * 0.010936133  - round(merfold) * 1760 
foot = cm * 0.032808398950131 - round(yard) * 3 

print(f"Mérföld:{round(merfold)} Yard:{round(yard)} Foot{round(foot)}")