'''
I think I got all of these functions to work. There are a couple of them that I thought could be done differently or more simply - those are commented out if you'd like to try them. To solve some of these I tried to use techniques we practiced - especially recursion. The "pascal" function was a tricky one! I think my solution works, although I am certain there's an easier way to accomplish it.
'''


# Max Num Function
def max_num(*args):
    return max(args)

# def max_num(*args):
#     return max(args)

# def max_num(num1, num2, num3):
#     return max([num1, num2, num3])

print("Max Num: " + str(max_num(3, 18, 6)))


# multi_list Function
def multi_list(items, total=1):
    if items == []:
        return total
    else:
        return multi_list(items[1:], total * items[0])

print("Multi List: " + str(multi_list([3,6,9])))


# rev_string Function
def rev_string(string, new_string= ''):
    if string == '':
        return new_string
    else:
        return rev_string(string[:-1], new_string + string[-1])
    
# def rev_string(string):
#     return string[::-1]
    
print("Rev String: " + rev_string("Reversed this string"))


# num_within Function
def num_within(num, start, end):
    return start <= num <= end

# def num_within(num, start, end):
#     return num in range(start, end + 1)

print("Num Within: " + str(num_within(10,2,5)))


# pascal Function
def pascal(n):
    rows = [[1], [1, 1]]

    if n == 1:
        print("1")
    elif n == 2:
        print("1 1")
    else:
        for row in range(2, n):
            last_row = rows[row-1]
            new_row = [1]

            for pair in range(len(last_row)-1):
                new_row.append(last_row[0] + last_row[1])
                last_row = last_row[1:]
            
            new_row.append(1)
            rows.append(new_row)

        for row in rows:
            print(" ".join([str(i) for i in row]))

print("Pascal: ")
pascal(5)