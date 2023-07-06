# arb_args Function
def arb_args(*args):
    for arg in args:
        print(arg)


# inner_func Function
def inner_func(x, y):
    def multiply():
        return x * y
    def add():
        return x + y
    print(multiply() + add())


# lunch_lady Function
def lunch_lady(name, preference='Mystery Meat'):
    print(name)
    print(preference)


# sum_n_product Function
def sum_n_product(x, y):
    sum = x+y
    product = x*y
    return sum, product


# alias_arb_args Alias
alias_arb_args = arb_args


# arb_mean Function
def arb_mean(*args):
    print(sum(args)/len(args))


# arb_longest_string Function
def arb_longest_string(*args):
    longest = ''
    for arg in args:
        if len(arg) > len(longest):
            longest = arg
    
    return longest

# Run Functions
arb_args(1, 4, 7,3,7,42,26,74)
print('-----------------------------')
inner_func(3, 5)
print('-----------------------------')
lunch_lady('Albert')
print('-----------------------------')
print(sum_n_product(2,3))
print('-----------------------------')
alias_arb_args(1, 4, 7,3,7,42,26,74)
print('-----------------------------')
arb_mean(4,4,5,6,6)
print('-----------------------------')
print(arb_longest_string('Hi', 'Hello', 'Welcome', 'Happy to see you.', 'Just kidding.'))