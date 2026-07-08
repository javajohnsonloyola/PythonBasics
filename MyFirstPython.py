def say_hi(name):
    if name == '':
        print("You didn't enter your name!")
    else:
        print("Hi there...")
    
    for letter in name:
        print(letter)

say_hi("erik")