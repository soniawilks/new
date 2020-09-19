# POZDROWIENIA



# first line of comment
# second line of comment
 
'''
    Our comment 
    first line of comment
    second line of comment
'''
 
name = "Adrian"
lastname = "Widlak"
print(name + " " + lastname)
 
example = "test"
 
quantity = 5
price = 12
print("SUM: ", quantity*price, "PLN")
print("SUM:  " + str(quantity*price) + " PLN")
 
a = 5
b = 6
 
print(a+b)
print("a + b =", a+b)
 
# int - integer - liczby
# str - string - tekst
# int() -> formatuje string do liczby: int("5") => 5
# str() -> formatuje int do stringa: str(5) => "5"
 
 
print(type(name))
 
# input - pobranie wartosci
 
product = input("Provide product name: ")
print(product)
 
 
quantity = int(input("Provide quantity: "))
# print(quantity*2)
# print(quantity*3)
 
if quantity > 6:
    print("Don't buy so many things!")
 
'''
    >
    <
    ==
    and, or
'''
 
 
# len() - zwraca ilosc znakow w stringu
 
if len(product) == 4:
    print("Your product consist with 4 letters")
    print("test")
    print(product)
 
# LOOPS - while, for
 
choice = input("Wanna add sth to your list? Y or N: ")
while choice == "Y":
    product = input("Provide product to add ")
    print(product)
    choice = input("Wanna add sth more? Y or N")
 
print("End of while loop")
 
'''
    Adrian -> 6 znakow
    name = "Adrian"
    len(name) -> 6
    index in len(name)
    0, 1, 2, 3, 4, 5
    range(5) -> 0,1,2,3,4
    range(7) -> 0,1,2,3,4,5,6
 
'''
 
def print_letter_index():
    for index in range(len(name)):
        print(index, name[index])
 
 
 
print_letter_index()
print_letter_index()

