#Lotto test
import random

#Empty list
LottoNumbers = []

for i in range(6):
    number = random.randint(1, 49)
    #Checking if the number has already been picked
    while number in LottoNumbers:
        number = random.randint(1, 49)

#append lotto numbers
    LottoNumbers.append(number)

#getting user input

userNumbers = []
for i in range(6):
    number = int(input("Please enter number between 1 and 49:"))
    while (number in userNumbers or number<1 or number>49) :
        print("invalid number, please try again. ")
        break

    userNumbers.append(number)


#creating a count
count = 0
for number in userNumbers:
    if number in LottoNumbers:
        count += 1

    def total_winnings():
        if count == 0:
            message = "Win R0"
            return message
        elif count == 1:
            message = "Win R0"
            return message
        elif count == 2:
            message = "Win R20"
            return message
        elif count == 3:
            message = "Win R100.50"
            return message
        elif count == 4:
            message = "Win 2,384.00"
            return message
        elif count == 5:
            message = "Win R8,584.00"
            return message
        elif count == 6:
            message = "Win R10, 000 000.00"
            return message


print("You guessed " + str(count) + " " + "number(s) correctly")
print("Lotto numbers are: ")
print(userNumbers)
print(LottoNumbers)
print(total_winnings())
