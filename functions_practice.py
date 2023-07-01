# hello Function
def hello():
    print('Welcome to my Function Practice Script!')


# pack Function
def pack(item1, item2, item3):
    return [item1, item2, item3]


# eat_lunch Function
def eat_lunch(list):
    if len(list) == 0:
        print("My lunchbox is empty!")
        return
    
    for item in list:
        if item == list[0]:
            print(f"First I eat {item}.")
        else:
            print(f"Next I eat {item}.")


hello()
print(pack('t-shirts', 'swimsuit', 'sunglasses'))
eat_lunch(['Ham Sandwich', 'Fruit Cup', 'Chocolate Pudding'])