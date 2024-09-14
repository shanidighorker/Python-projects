"""
student:shani dihorker
ID:209290121
Assigment no.1
program:addlaters
"""
def add_latters(s1,s2):
    """
    A function that accepts two strings of length 1 and returns the sum
     of the letters otherwise returns None
    """
    if not (len(s1) == 1 and len(s2) == 1) : #section1
        return None
    s1 = s1.lower()
    s2 = s2.lower()
    abc = 'abcdefghijklmnopqrstuvwxyz'
    ind1 = abc.find(s1)
    ind2 = abc.find(s2)
    add = (ind1 + ind2) % 26
    return chr(add + 97)

def add_string(s1, s2): #section2
    """
    A function that receives 2 strings consisting of Latin letters and returns
    a string in which each character is the sum of the characters that match the length
    """
    if not (s1.isalpha() and s2.isalpha()): #section3
        return None
    s1 = s1.lower()
    s2 = s2.lower()
    new_string = ''
    for i in range(min(len(s1), len(s2))):
        new_string += add_latters(s1[i], s2[i])
    return new_string

def vigenere_encrypt(s, key): #section3
    """
    A function that accepts a string and a key and returns
    the result of encrypting the string using the key
    """
    if not all(c.isalpha() and c.islower() for c in key): #Checking that the key is correct,
        # using all to check if each of the members in the list are correct
        return None
    s = ''.join(c for c in s.lower() if c.isalpha()) #Converting s to lowercase and ignoring non-letter characters
    t = (key * ((len(s) // len(key)) ))[:len(s)] #Building the string t by duplicating the keys
    return add_string(s, t)


def sub_letters(s1, s2): #auxiliary function
    """
    A function that does the opposite of the function of section A
    """
    if not (len(s1) == 1 and len(s2) == 1):
        return None
    s1 = s1.lower()
    s2 = s2.lower()
    abc = 'abcdefghijklmnopqrstuvwxyz'
    ind1 = abc.find(s1)
    ind2 = abc.find(s2)
    add = (ind1 - ind2) % 26
    return chr(add + 97)

def sub_string(s1, s2): #auxiliary function
        """
        auxiliary function
        """
        if not (s1.isalpha() and s2.isalpha()):
            return None
        s1 = s1.lower()
        s2 = s2.lower()
        new_string_lat = ''
        for i in range(min(len(s1), len(s2))):
            new_string_lat += sub_letters(s1[i], s2[i])
        return new_string_lat

def vigener_decrypt(w, key): #section4
    """
    A function that accepts a string w and a key k and returns the result
    The decryption of w using the key k.
    """
    if not key.isalpha(): #If k does not consist of only Latin letters, then "None" will be returned
        return None
    if not all(c.isalpha() and c.islower() for c in key):  # Checking that the key is correct,
        # using all to check if each of the members in the list are correct
        return None
    w = ''.join(c for c in w.lower() if c.isalpha())  # Converting s to lowercase and ignoring non-letter characters
    t = (key * ((len(w) // len(key)+1)))[:len(w)]  # Building the string t by duplicating the keys
    return sub_string(w, t)


def main():
    # print(add_latters('a', 'bcd'))
    # s1 = 'x'
    # s2 = 'f'
    # print(add_string('input', 'output'))
    s = 'attackatsixoclock'
    w = 'igiuvsnimbfbrfhkx'
    key = 'input'
    print(vigenere_encrypt(s, key))
    # print(sub_string('b', 'b'))
    print(vigener_decrypt(w, key))
main()

