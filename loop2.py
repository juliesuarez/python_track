
def debugging():
    hungry = True
    while hungry:
        break   
    print(hungry)
debugging()

def even_numbers(num):
    while num  in range(100):
        num +=10
        if num%2 == 0:
            print(num)
even_numbers(0)

def odd_numbers(num):
    while num in range(100):
        num +=10
        if num%2 != 0:
            print(num)
odd_numbers(1)
