
print("choices: rock , scissors , paper")
p1=input("P1 Choose:")
p2=input("P2 Choose:")

if (p1 == 'rock') and (p2 == 'scissors'):
    print("p1 wins")
elif (p1 == 'rock') and (p2 == 'paper'):
    print("p2 wins")
elif (p1 == 'rock') and (p2 == 'rock'):
    print("tie")
elif (p1 == 'scissors') and (p2 == 'scissors'):
    print("tie")
elif (p1 == 'scissors') and (p2 == 'rock'):
    print("p2 wins")
elif (p1 == 'scissors') and (p2 == 'paper'):
    print("p1 wins")
elif (p1 == 'paper') and (p2 == 'paper'):
    print("tie")
elif (p1 == 'paper') and (p2 == 'scissors'):
    print("p2 wins")
elif (p1 == 'paper') and (p2 == 'rock'):
    print("p2 wins")
else:
    print("invalid!!")



