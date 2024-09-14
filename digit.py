""" student:shani dihorker
Assigment no.2
program: digit"""

"""
A program that receives a 3-digit integer checks whether the number in the input
is really 3 digits and prints them in reverse order and converts the input to an integer.
"""
def digit():
    numdigit = int(input("please enter a 3 digit number:")) #קליטה של 3 ספרות מהמשתמש
    if numdigit < 1000 or numdigit > 99: #בדיקה עבור האם הספר שנקלט מהמשתמש מכיל בדיוק 3 ספרות
        digit1 = (numdigit // 10) // 10  # עבור חישוב והבאת ספרת המאות
        digit2 = (numdigit // 10) % 10  # עבור חישוב והבאת ספרת העשרות
        digit3 = (numdigit % 10)  # עבור חישוב והבאת ספרת האחדות
        print(digit3, "\t", digit2, "\t", digit1, "\t" ) #הדפסת הספרות שנקלטו מהמשתמש בסדר הפוך והדפסת רווחים ע"י"\t"

def main():
    digit()
main()
