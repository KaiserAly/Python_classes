# numerical data types
x=42 #integer
type(x)
#print the elements inside of the variable x
print(x)
x # in Jupyter/IPython we don't actually need to explicitly print for the last line of a cell
pi=3.14159 #float
print(pi)
type(pi)
#let's build a function to print only pair numbers
def print_pair(num):
    if num%2==0: #remainder
        print(f"{num} is a pair number!")

for num in range(0,11):
    print_pair(num)

print("Hello world!") #we print the typical hello world

#Let's make a function to sum x to the nums
for num in range (0,11):
    x=x+num
    print(x)


