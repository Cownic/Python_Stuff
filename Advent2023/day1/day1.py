#Utility to open files
def read_file(path):
    with open(path, 'r') as  file:
        rows = [line.strip() for line in file.readlines()]
    return rows

def extractfirstlastdigit_v1(word):
    first_digit = -1
    second_digit = -1
    for c in word:
        if c.isdigit() and first_digit == -1:
            first_digit = c
        elif c.isdigit():
            second_digit = c
    if (first_digit != -1 and second_digit == -1):
        second_digit = first_digit
    if (first_digit == -1 and second_digit == -1):
        first_digit = second_digit = 0
    return first_digit, second_digit

def extractfirstlastdigit_v2(word):
    lst = ['one', 'two' , 'three' , 'four' , 'five' , 'six' , 'seven' , 'eight' , 'nine']
    

if __name__=="__main__":
    file_path = 'Advent2023/day1/input.txt'
    result = read_file(file_path)
    total = 0
    for word in result:
        first, second = extractfirstlastdigit_v2(word)
        total += (int(first) * 10 + int(second))
    print(total)

    
