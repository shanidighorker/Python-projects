"""
student:shani dihorker
ID:209290121
Assigment no.3
program:partitions
"""
def get_partitions_helper(n, m, partitions): #section1
    """
    auxiliary function
    """
    if n == 0:
        return [partitions]
    elif n < 0 or m == 0:
        return []
    else:
        return get_partitions_helper(n, m-1, partitions) + get_partitions_helper(n-m, m, partitions + [m])

def get_partitions(n):
    """
    A function that accepts as a parameter a positive integer
     and returns a nested list of all sorted divisions
    """
    return get_partitions_helper(n, n, [])

def partitions_get(n): #section2
    def helper_partitions_get(n, m, partitions):
        if n == 0:
            return [partitions]
        elif n < 0 or m == 0:
            return []
        else:
            return helper_partitions_get(n, m-1, partitions) + helper_partitions_get(n-m, m, partitions + [m])
    return helper_partitions_get(n, n, [])

try:
    with open("numbers.txt", "r") as numbers_file, open("partitions.txt", "w") as partitions_file:
        for number in numbers_file.read().split():
            try:
                number = int(number)
                if number > 0:
                    partitions = partitions_get(number)
                    partitions_file.write("{}:{}\n".format(number, partitions))
            except ValueError:
                pass
except IOError as e:
    print("An error occurred while reading/writing the files:", e)

def main():
    print(get_partitions(4))
    print(partitions_get(4))

main()