n1 = input()
n2 = input()
n3 = input()
n4 = input()

if n1 == "E" or n2 == "E" or n3 == "E" or n4 == "E":
    print("false")
    quit()

if n1 == "A":
    n1 = 4
if n1 == "B":
    n1 = 3
if n1 == "C":
    n1 = 2
if n1 == "E":
    n1 = 0

if n2 == "A":
    n2 = 4
if n2 == "B":
    n2 = 3
if n2 == "C":
    n2 = 2
if n2 == "E":
    n2 = 0

if n3 == "A":
    n3 = 4
if n3 == "B":
    n3 = 3
if n3 == "C":
    n3 = 2
if n3 == "E":
    n3 = 0

if n4 == "A":
    n4= 4
if n4 == "B":
    n4= 3
if n4 == "C":
    n4= 2
if n4 == "E":
    n4= 0

media = ((n1+n2+n3+n4) / 4)

if media >= 3:
    print("true")
else:
    print("false")

