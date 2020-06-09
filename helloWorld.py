#print("hello world")
#userInput=input()
#print("you typed in", userInput)

def doubler(x):
    doubledNumber = x * 2
    return doubledNumber

print("please type in a number to double")

ugn = int(input())

dn = doubler(ugn)

print("your number doubled is",str(dn))

ddn = doubler(dn)
print("your number doubled twice is",str(ddn))
