"""
student:shani dihorker
ID:209290121
Assigment no.2
program:generate_primes
"""

import miller_rabin as mr
def main(): #section6

   try:
      m = int(input("please enter a number:"))
      k = int(input("please enter a number:"))
   except:
      print('This is not an integer.')
      return

   try:
      f = open("primes.txt", "w")
      try:
         for counter in range(k):
            prime = mr.make_prime(m)
            f.write(str(prime) + "\n")
      except :
         print("Something went wrong when writing to the file")
      finally:
         f.close()
   except IOError:
      print("Something went wrong when opening the file")
main()







