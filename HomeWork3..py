name = input("What is your name? ")
print("Welcome {}".format(name))
print("Good Luck ! ")
print ("Start guessing...")

word ="cloud"
turns= 0
fail = 0

while fail <= 5 and turns <=5 : 
 
  guess = str(input("Please enter your guess: "))
  if guess in word:
    print("Congrats!!")
    print(guess)
    turns = turns+1
    
  else:
    print("Please again enter your guess: ")
    fail = fail+1

if fail >= 6: 
 print("Looseer..The word was: ", word)


