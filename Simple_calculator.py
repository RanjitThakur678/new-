def calc():
    print("\nWelcome to Simple Calculator")

def add(a,b):
    return a+b
def sub(a,b):
    return a-b

def mult(a,b):
    return a*b

def div(a,b):
    return a / b

calc()

print("\nPress 1 for add")
print("Press 2 for sub")
print("Press 3 for multiply")
print("Press 4 for Division \n")

while True:
    Choice = input("Enter an operation (1/2/3/4) : ")
    if Choice in ('1','2','3','4' ):

        a = float(input("\nEnter a number: "))
        b = float(input("\nEnter 2nd number:  "))

        if Choice == '1':
            # print(a ,'+', b, '=')
            print(f"\nResult :  {add(a,b)}")

        elif Choice == '2':
            # print(a ,'-', b, '=' )
            print(f"\nResult :  {sub(a,b)}")

        elif Choice == '3':
            # print(a ,'*', b, '=' )
            print(f"\nResult :  {mult(a,b)}")


        elif Choice == '4':

            # print(a ,'/', b, '='  )
            print(f"\nResult :  {div(a,b)}")
        break
    else:
        print("Invalid Option")
