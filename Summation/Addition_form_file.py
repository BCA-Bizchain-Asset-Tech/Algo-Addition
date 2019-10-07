# Print numbers
# Print a message when there isn't a number
# Sum the numbers and print the sum
# Save only the numbers to a new file
f = open("/Users/vijaymastaker/Desktop/numbers algo.txt", 'r')
s = f.readlines()
p = str(s)
total = 0
for line in s:
    printnum = 0
    try:
        printnum += float(line)
        total += printnum
    except ValueError:
        print("Invalid Literal for Int() With Base 10:", ValueError)
        
print("The sum is: ", total)

for line in s:
    printnum = 0
    try:
        printnum += float(line)
        total += printnum
    except ValueError:
        print("Invalid Literal for Int() With Base 10:", ValueError)
        
print("The sum is: ", total)

total

