# Data types

# S T R I N G

print("Hell")
print("Gustavo")
# Python see text inside quotation as whole one thing
# For A specific character use '[]' sq brackets

print("Gustavo"[4])
print("123"+"456")
print("Billy"+"Butcher")


#  I N T E G E R

num1 =  12345
num2 = 678910
print(num1 + num2)

n1 = 10000000
n2 = 1_00_00_000
print(n1 == n2)

num_char = len(input("Enter Your Name:"))
print("My Name has " + str(num_char) + " characters")

#Types
print(type(num_char))
print(type(n1))

a = 7429
b = "8304"
c = "Nice"
d = 93.03723

print(type(float(a)))
print(type(int(b)))
print(type(str(a)))


# Mathematical Oparations
3 + 6      #Addition
87 - 38    #Subtraction
64 * 84    #Multiplication
64/23      #Divide -> Float Value
37**74     #Exponent
645//83     #Floor Division -> Int Value

# Special Ops
result = 8/2
result /= 2
print(result)

score =  38
score += 5
print(score)

run = 84
run -= 74
print(run)

marks = 750
marks *= 8
print(marks)

म = 7
print(म)

Name = "The Great BKL"
height =  74.84
weight = 494982
age = "two months"
print("I am " + Name + " i am " + str(height) + " tall and my weight is " + str(weight) + "Kg and i am " + str(age) + " years old")

# Or You Can use F-string For such cases
print(f"I am {Name} and i am {height} tall and my weight is {weight} Kg and I am {age} years old ")
