# Find ASCII Value of a character 'X' and 'x'

ch = input("Enter any character: ")

print("The ASCII value of char " + ch + " is: ",ord(ch))

# Write Program to Compute Quotient and Remainder

divisor = 5
dividend = 27
quotient = dividend//divisor
reminder = dividend % divisor
print("Quotient is", quotient)
print("Reminder is",reminder)


# Swap two numbers using temporary variable

x = 10
y = 50
# Creating a temp variable
temp = x
x = y
y = temp
 
print("Value of x:", x)
print("Value of y:", y)


#Write Program to Check Whether a Number is Even or Odd - 88,37,1658


x=88371658

if (x % 2) == 0 :
    print("Number is Even ",x)
else :
    print("Number is Odd ",x)



#Check whether an alphabet is vowel or consonant using if..else statement - a,b,e,o

x='a'

if x in ('a','e','i','o','u') :
    print("The given Alphabet is vowel",x)
else :
    print("The given Alphabet is consonant",x)


#Write Programm to calculate GST i.e. 18% on base price 34900/-



gst = ((18/100) * 34900)

print("gst is ",gst)



#17) Write programm to calculate monthly simple intrest and compound intrest(5%/Month) on amount - 161258/-

p=161258
r=5
t=1

si=p*r*t*0.01

print("Si : ",si)


Amount = p * (pow((1 + r / 100), t))
ci = Amount - p 
print("Compound interest is", ci)


#Write programm to calculate monthly simple intrest and compound intrest(5%/Month) on amount - 161258/-

a=161258

e3=a/36

e5=a/60

emi3=e3+(0.05*e3)

emi5=e5+(0.05*e5)

print("EMI for 3 years with intrest 5%",emi3)

print("EMI for 5 years with intrest 5%",emi5)
