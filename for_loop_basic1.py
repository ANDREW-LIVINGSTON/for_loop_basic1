# 1.Basic
for i in range(0,151,1):
    print(i)

# 2. Multiples of five
for i in range(0,1005,5):
    print(i)

# 3. counting the Dojo Way
for i in range(0,103,1):
    if i % 10 == 0:
        print("Coding Dojo")
    elif i % 5 == 0:
        print("Coding")
    else: 
        print(i)

# 4. Woah. that sucker's huge
sum = 0
for i in range(0,500001,1):
    if i % 2 != 0:
        sum += i
        print(sum)

# 5. Countdown by fours
for i in range(2018,0,-4):
    print(i)

# 6. Flexible counter
lowNum = 2
highNum = 9
mult = 3
for i in range(lowNum - 1,highNum + 1,1):
    if i % mult == 0:
        print(i)
