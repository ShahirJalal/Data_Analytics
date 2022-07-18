# Question 1

IC = input('Please Key in your IC number (Format: 910101-01-0101): ')

print('Birth Day:',IC[4:6])
print('Birth Month:',IC[2:4])
print('Birth Year:',IC[0:2])
print('Area Code:',IC[7:9])
print('Last 4 Digits:',IC[10:])


# ------------------------------------------------------------------------
ic_no = input("Input your ic number (format: 950101-01-1549): ")

print()

print(f"Birth Day: {ic_no[4:6]}")
print(f"Birth Month: {ic_no[2:4]}")

if int(ic_no[0:2]) > 22:
  print(f"Birth Year: 19{ic_no[0:2]}")
elif int(ic_no[0:2]) <= 22:
  print(f"Birth Year: 20{ic_no[0:2]}")

print(f"Area Code: {ic_no[7:9]}")
print(f"Last 4 digits: {ic_no[-4:]}")




# ------------------------------------------------------------------------
import re

ic_no = input("Input your ic number (format: 950101-01-1549): ")
correct_format = re.match("^\d{6}-\d{2}-\d{4}$", ic_no)

if correct_format:

  print()
  print(f"Birth Day: {ic_no[4:6]}")
  print(f"Birth Month: {ic_no[2:4]}")
  
  if int(ic_no[0:2]) > 22:
    print(f"Birth Year: 19{ic_no[0:2]}")
  elif int(ic_no[0:2]) <= 22:
    print(f"Birth Year: 20{ic_no[0:2]}")
  
  print(f"Area Code: {ic_no[7:9]}")
  print(f"Last 4 digits: {ic_no[-4:]}")

else:
  print("Please insert your ic number according to this format: 950101-01-1549")
  
  
  
  
  
  
  
  
  
  
  
  
# Question 2
  
colors = ['red','green','blue']
print(f"The first colour is {colors[0]} and the last colour is {colors[-1]}.")



colors = []
while True:
  c = input("Add a colour (type 'esc' if you don't want to add more): ")
  if c == 'esc':
    break
  else:
    colors.append(c)
print()
print(f"The first colour is {colors[0]} and the last colour is {colors[-1]}.")



#########################################################################################3

# Question 3

n = input("Input a digit (0 - 9): ")

n1 = int(n)
n2 = int(n + n)
n3 = int(n + n + n)

print(f'{n1} + {n2} + {n3} = {n1 + n2 + n3}')





###########################################################################################

# Question 4

colors =[]

while True:
    color =input("Please add a color. (Type 'esc' if you don't want to add more.): ")
    if color == 'esc':
        break
    else:    
        colors.append(color)
print(f"\n\nThe color list is {colors}.\n")

def check_color(color):
  if color in colors:
    return print(f"The color '{color}' is in the list.")
  else:
    return print(f"The color '{color}' is NOT in the list.")

check_color("brown")




########################################################################################33


# Question 5

while True:
  char = input("\nInput a character: ")

  if char == "esc":
    break
  
  else:

    if len(char) == 1:

      if char in 'aeiou':
        print(f"Yes, '{char}' is a vowel.")
      else:
        print(f"No, '{char}' is NOT a vowel.")

    else:
      print("Please insert only ONE character.")



####################################################################################

sentence = input("Write a sentence that contains 'R' or 'Python' (without punctuation marks):\n")
words = sentence.split()

for i in range(len(words)):
  if words[i] == "Python":
    words[i] = "R"
  elif words[i] == "R":
    words[i] = "Python"

print(f"\nThe new sentence:")
print(*words)



#######################################################################################

# Q7

a1 = float(input("a1: "))
a2 = float(input("a2: "))
a3 = float(input("a3: "))
b1 = float(input("b1: "))
b2 = float(input("b2: "))
b3 = float(input("b3: "))

print("")
print(f"You have keyed in:")
print(f"{a1}x + {a2}y = {a3}")
print(f"{b1}x + {b2}y = {b3}")
print("")

n = a1*b2 - a2*b1
if n == 0:
  print("There is no unique solution for x and y.")
else:
  x = (a3*b2 - a2*b3) / n
  y = (a1*b3 - a3*b1) / n
  print(f"Solution: x = {x}, y = {y}")