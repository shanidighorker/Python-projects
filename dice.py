""" student:shani dihorker
Assigment no.3
program: dice"""
import random

def dice():
    throwonedice = int(input("please enter a number 1 \n 2 \n 3\n quit:")) # שלב בחירת ההטלה ע"י הקלדה של המשתמש אחד מהמספרים ויציאה
    if throwonedice == 1: #שלב חישוב ההטלה הראשונה במידה והמשתמש הקיש 1
        throwonedicet = random.randint(1, 6) #במידה והמשתמש הקיש 1 זה מטיל את הקוביה הראשונה בין 1 ל6
        print("Result of the one dice throw:", throwonedicet)

    throwonedice = int(input("please enter a number 1 \n 2 \n 3\n quit:"))
    choice = random.randint(1,6)
    sumchoice = throwonedice + choice
    print(sumchoice)

    if sumchoice == 12 or sumchoice <= 4: #התוכנית בודקת אם התוצאה בין 4 ל-12. אם כן, היא מדפיסה "You win!"
        print("you win:")
    else:
        print("You failed, try again")

    throwtwodice = int(input("please enter a number 1: \n number2: \n number3:\n quit")) # קוביה שנייה הטלה שנייה
    if throwtwodice == 2: #שלב חישוב ההטלה השנייה(2 קוביות) במידה והמשתמש הקיש 2
        choice1 = random.randint(1, 6) #במידה והמשתמש הקיש 2 זה מטיל את הקוביה בפעם השניה כלומר הטלה נוספת
        choice2 = random.randint(1, 6) #במידה והמשתמש הקיש 2 זה מטיל את הקוביה בפעם השניה כלומר הטלה נוספת זאת ההטלה השניה כי זה 2 קוביות
        choice = choice1 + choice2 #שמירת התוצאות של הטלת שתי קוביות במשתנה כדי לקבל תוצאה סופית
        print("two dice", choice)

    quit = random.randint (1,6) + random.randint (1,6)
    sumchoice = throwonedice + quit
    print(sumchoice)

    if sumchoice == 12 or sumchoice <= 4:   # התוכנית בודקת אם התוצאה בין 4 ל-12. אם כן, היא מדפיסה "You win!".
        print("you win!")
    else:
        print("You failed, try again")


dice()
