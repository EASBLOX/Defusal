buttontext = input("text on the button")
letters = set(c.upper() for c in buttontext if c.isalpha())
digits = set(c for c in buttontext if c.isdigit())
offset = 0
TABLE = {
    "Red":    {"Red": "A", "Orange": "F", "Yellow": "G", "Green": "A", "Blue": "B", "Purple": "C", "White": "D", "Black": "E"},
    "Orange": {"Red": "G", "Orange": "D", "Yellow": "F", "Green": "B", "Blue": "A", "Purple": "E", "White": "C", "Black": "B"},
    "Yellow": {"Red": "E", "Orange": "C", "Yellow": "G", "Green": "C", "Blue": "G", "Purple": "A", "White": "B", "Black": "D"},
    "Green":  {"Red": "B", "Orange": "C", "Yellow": "D", "Green": "D", "Blue": "B", "Purple": "F", "White": "G", "Black": "A"},
    "Blue":   {"Red": "C", "Orange": "B", "Yellow": "C", "Green": "E", "Blue": "F", "Purple": "D", "White": "A", "Black": "G"},
    "Purple": {"Red": "C", "Orange": "E", "Yellow": "B", "Green": "F", "Blue": "A", "Purple": "D", "White": "G", "Black": "D"},
    "White":  {"Red": "D", "Orange": "G", "Yellow": "A", "Green": "G", "Blue": "E", "Purple": "B", "White": "E", "Black": "C"},
    "Black":  {"Red": "F", "Orange": "A", "Yellow": "E", "Green": "A", "Blue": "C", "Purple": "G", "White": "B", "Black": "F"},
}
outercolour = input("outer colour of the button").strip().title()
innercolour = input("inner colour of the button").strip().title()
case = TABLE[outercolour][innercolour]
if "A" in letters: offset = offset + 1
if "E" in letters: offset = offset + 3 
if "I" in letters: offset = offset + 2 
if "O" in letters: offset = offset - 4 
if "3" in digits: offset = offset - 1
if "4" in digits: offset = offset + 6
if "8" in digits: offset = offset + 1
if not letters: offset = offset + 3
if not digits: offset = offset - 2
new = input("is there new(not lit)")
if new == "yes":
    v1 = True
else:
    v1 = False
old = input("is there old(not lit)")
if old == "yes":
    v2 = True
else:
    v2 = False
low = input("is there low(not lit)")
if low == "yes":
    v3 = True
else:
    v3 = False
mid = input("is there mid(not lit)")
if mid == "yes":
    v4 = True
else:
    v4 = False
newlit = input("is there new(lit)")
if newlit == "yes":
    v5 = True
else:
    v5 = False
oldlit = input("is there old(lit)")
if oldlit == "yes":
    v6 = True
else:
    v6 = False
lowlit = input("is there low(lit)")
if lowlit == "yes":
    v7 = True
else:
    v7 = False
midlit = input("is there mid(lit)")
if midlit == "yes":
    v8 = True
else:
    v8 = False
if case == "A":
    if v1 == True:
        offset = offset + 1
    if v6 == True:
        offset = offset + 2
    if v7 == True:
        offset = offset - 2
    if v4 == True:
        offset = offset - 1
    if v1 == False and v2 == False and v3 == False and v4 == False and v5 == False and v6 == False and v7 == False and v8 == False:
        offset = offset - 1
if case == "B":
    if v1 == True: 
        offset = offset + 2
    if v2 == True:
        offset = offset + 4
    if v7 == True:
        offset = offset - 1
    if v8 == True:
        offset = offset - 4
    if v1 == False and v2 == False and v3 == False and v4 == False and v5 == False and v6 == False and v7 == False and v8 == False:
        offset = offset - 2
if case == "C":
    if v1 == True:
        offset = offset - 1 
    if v6 == True:
        offset = offset + 1
    if v3 == True:
        offset = offset + 3
    if v8 == True:
        offset = offset + 2
    if v1 == False and v2 == False and v3 == False and v4 == False and v5 == False and v6 == False and v7 == False and v8 == False:
        offset = offset - 3
if case == "D":
    if v5 == True:
        offset = offset + 2
    if v2 == True:
        offset = offset - 1
    if v7 == True:
         offset = offset + 4
    if v4 == True: 
        offset = offset - 1
    if v1 == False and v2 == False and v3 == False and v4 == False and v5 == False and v6 == False and v7 == False and v8 == False:
        offset = offset + 1
if case == "E":
    if v5 == True: 
        offset = offset + 1
    if v6 == True:
        offset = offset - 2
    if v3 == True:
        offset = offset + 5
    if v8 == True:
        offset = offset - 3
    if v1 == False and v2 == False and v3 == False and v4 == False and v5 == False and v6 == False and v7 == False and v8 == False:
        offset = offset + 2
if case == "F":
    if v5 == True:
        offset = offset - 4
    if v2 == True:
        offset = offset - 2
    if v7 == True:
        offset = offset + 4
    if v4 == True:
        offset = offset + 3
    if v1 == False and v2 == False and v3 == False and v4 == False and v5 == False and v6 == False and v7 == False and v8 == False:
        offset = offset + 3
if case == "G":
    if v1 == True:
        offset = offset + 3
    if v6 == True:
        offset = offset - 1
    if v3 == True:
        offset = offset + 1
    if v8 == True:
        offset = offset + 2
if offset >= 10:
    offset = offset - 10
if offset < 0:
    offset = offset + 10

print(case)
print("Press the button", offset, "times")
