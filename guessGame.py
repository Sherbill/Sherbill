def guessgame():
    guess = 6
    life = 1
    num = 20
    while life <= guess:
        Enum = int(input("guess your number between 0 to 50 : "))
        if num > Enum:
            print("you guess too low ")
            print("life's =", life, "max guess = ", guess)
        elif num < Enum:
            print("your number is too high")
            print("life's =", life, "max guess = ", guess)
        if Enum == 18 or Enum == 22 or Enum == 21 or Enum == 19 or Enum == 23:
            print("you are very close")

        elif num == Enum:
            print("you won!!!")
            print("you took ", life, "attempts to finish")
            print("number of guesses you have 6. your guesses ", life)
            break

        if life == 6:
            print("out of guesses you lost try next time \n the number was 20")
            print("lifes =", life, "max guess = ", guess)
        life = life + 1


guessgame()