#1

def firstNfibo(n):
    a=0
    b=1
    retlist=[]
    retlist+=[a]
    if(n==1):
        return retlist
    retlist+=[b]


    for i in range(n-2):
        c=a
        a=b
        b=c+b
        retlist+=[b]
    return retlist
#print(firstNfibo(2))
def isPrime(n):
    if(n==1):
        return False
    if(n==2):
        return True
    if(n%2==0):
        return False
    for i in range(3,n,2):
        if(i*i>n):
            break
        if(n%i==0):
            return False
    return True
#2
def primefilter(numbers):
    retlist=[]

    for i in numbers:
        if(isPrime(i)):
            retlist+=[i]
    return retlist
#print(primefilter([1,2,3,4,5,6,7,8,9]))
#3
def setops(a,b):
    intersection=[]
    union=[]
    aminusb=[]
    bminusa=[]
    for i in a:
            if(i in b):
                intersection+=[i]
    for i in a:
        union+=[i]
    for i in b:
        if (not (i in a)):
            union+=[i]
    for i in a:
        if(not (i in b)):
            aminusb+=[i]
    for i in b:
        if(not (i in a)):
            bminusa+=[i]
    return (intersection,union,aminusb,bminusa)
#print(setops([1,2,3],[2,3]))
#4
def compose(notes, moves, start_position):
    song = []
    current_position = start_position
    song.append(notes[current_position])

    for move in moves:
        current_position = (current_position + move) % len(notes)
        song.append(notes[current_position])

    return song
notes = ["do", "re", "mi", "fa", "sol"]
moves = [1, -3, 4, 2,-3]
start_position = 2

result = compose(notes, moves, start_position)
#print(result)

#5 

def zero_below_diag(M):
    for i in range(len(M)):
        for j in range(len(M[0])):
            if (i>j):
                M[i][j]=0
    return M
    #6
def find_items_with_x_occurrences(x, *lists):
    occurrences = {}
    result = []

    for lst in lists:
        for item in lst:
            if item in occurrences:
                occurrences[item] += 1
            else:
                occurrences[item] = 1

    for item, count in occurrences.items():
        if count == x:
            result.append(item)

    return result
list1 = [1, 2, 3]
list2 = [2, 3, 4]
list3 = [4, 5, 6]
list4 = [4, 1, "test"]
x = 2

result = find_items_with_x_occurrences(x, list1, list2, list3, list4)
#print(result)
#7
def count_and_find_palindromes(numbers):
    palindrome_count = 0
    greatest_palindrome = None

    for number in numbers:
        if str(number) == str(number)[::-1]:
            palindrome_count += 1
            if greatest_palindrome is None or number > greatest_palindrome:
                greatest_palindrome = number

    return palindrome_count, greatest_palindrome
numbers = [123, 121, 345, 454, 678, 898, 12321, 98789, 56765]

result = count_and_find_palindromes(numbers)
#print(result)
#8
def generate_ascii_lists(x=1, strings=[], flag=True):
    result = []

    for string in strings:
        ascii_list = []
        for char in string:
            ascii_code = ord(char)
            if (ascii_code % x == 0) == flag:
                ascii_list.append(char)
        result.append(ascii_list)

    return result

x = 2
strings = ["test", "hello", "lab002"]
flag = False

result = generate_ascii_lists(x, strings, flag)
#print(result)
#9
def find_obstructed_seats(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    obstructed_seats = []

    for i in range(rows):
        for j in range(cols):
            current_height = matrix[i][j]
            obstructed = False
            for k in range(0, i):
                if matrix[k][j] >= current_height:
                    obstructed = True
                    break

            if obstructed:
                obstructed_seats.append((i, j))

    return obstructed_seats
matrix = [
    [1, 2, 3, 2, 1, 1],
    [2, 4, 4, 3, 7, 2],
    [5, 5, 2, 5, 6, 4],
    [6, 6, 7, 6, 7, 5]
]

result = find_obstructed_seats(matrix)
#print(result)

#10
def combine_lists(*input_lists):
    max_length = max(len(lst) for lst in input_lists)
    combined_tuples = []

    for i in range(max_length):
        combined_tuple = tuple(lst[i] if i < len(lst) else None for lst in input_lists)
        combined_tuples.append(combined_tuple)

    return combined_tuples

list1 = [1, 2, 3,9]
list2 = [5, 6, 7]
list3 = ["a", "b", "c"]

result = combine_lists(list1, list2, list3)
#print(result)
#11
def order_tuples(tuples):
  return sorted(tuples, key=lambda x: x[1][2])

tuples = [('abc', 'bcd'), ('abc', 'zza')]
#print(order_tuples(tuples))
#12
def group_by_rhyme(words):
  rhyming_groups = {}
  
  for word in words:
    rhyme = word[-2:]
    if rhyme not in rhyming_groups:
      rhyming_groups[rhyme] = []
    rhyming_groups[rhyme].append(word)

  return list(rhyming_groups.values())

words = ['ana', 'banana', 'carte', 'arme', 'parte']  
#print(group_by_rhyme(words))