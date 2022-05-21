# operator=input("enter what operation either +,-,*,/ " )
# operate=["+","-","/","*"]
# i=0
# answer=0

# while i<=len(operate):
#  if operator==operate[0]:
#   number=int(input([]))
#   answer=answer + number
#  elif operator==operate[1]:
#   number=int(input([]))
#   answer=answer - number
#  elif operator==operate[2]:
#   number=int(input([]))
#   answer=answer / number
#  elif operator==operate[3]:
#   number=int(input([]))
#   answer=answer * number

#  else:
#   print("invalid operator")
# i=i+1

input_number = input("enter all numbers to be operated on, seperated by a space: ")
print("\n")
operate = input("enter symbol of operation, +,-,*,/, % \only ")
user_input = input_number.split()
print("these are the numbers: " + str(user_input))
for i in range(len(user_input)):
    user_input[i] = int(user_input[i])

operator = ["+", "-", "*", "/", "%"]
sum = 0
multiply = 1
for i in range(len(user_input)):
    if operate == operator[0]:
        sum = sum + user_input[i]

    elif operate == operator[1]:
        sum = sum - user_input[i]

    elif operate == operator[2]:
        multiply = multiply * user_input[i]

    elif operate == operator[3]:
        multiply = multiply / user_input[i]

    elif operate == operator[4]:
        mod = user_input[0] % user_input[1]

    else:
        print("invalid operator")

# print anser
if operate == operator[0] or operate == operator[1]:
    print("The answer is " + str(sum))

elif operate == operator[2] or operate == operator[3]:
    print("The answer is " + str(multiply))
elif operate == operator[4]:
    print("The answer is " + str(mod))
else:
    print("invalid operator")









