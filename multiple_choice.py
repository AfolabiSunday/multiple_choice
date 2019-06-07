#

guess_word = 'mars'
count = 0
guessword = 'nigeria'
guessword2 = "india"
guessword3 = "andriod"
print('welcome new user')
print()
name = input('what will you want me to call you? ')
print('sound great ' + name)
print("quiz is just for fun, if you get above 2 you passed ")
print()
question = input('which planet is the best to spend your holiday ? ')
if question == guess_word:
    print('You got it right ')
    count = count + 1
else:
    print("Sorry are wrong")

print("let move on ")
print()
question2 = input("what is the name of the authors place of birth ? ")
if question2 == guessword:
    print("That correct ")
    count = count + 1
    print("you have scored " + str(count) + " so far ")
else:
    print("Wrong, you have scored " + str(count) + "so far ")

print("That was awesome, scoring " + str(count))
print("3rd question")
print()
question3 = input("which country has the highest population un the world ")
if question3 == guessword2:
    print("correct! " + name)
    count = count + 1
else:
    print("sorry, you missed " + name)
print("Good Job! " + name + " you have score " + str(count))
question4 = input("which phone model is mostly used in africa ? ")
if question4 == guessword3:
    print("that cool ")
    count = count + 1
else:
    print("lol")

print(" we have come to the end of the quizz and you scored " + str(count) + " thanks for playing ")
print(" bye ")