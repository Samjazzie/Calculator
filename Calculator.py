#define the variable for if the person wants to continue
cont = "y"
#if they want to continue with the programe, select the operation they want to do
while cont.lower() == "y":
  #ask the user for the operation they want to do
    print("Select operation\n1.Add\n2.Subtract\n3.Multiply\n4.Divide")

    choice = input("Enter choice(1/2/3/4):")
#ask them what numbers they want to use
    number1 = int(input("Enter first number: "))
    number2 = int(input("Enter second number: "))
#if they choose 1, add the numbers
    if choice == '1':
       print(number1,"+",number2,"=", (number1 + number2))
#if they choose 2, subtract the numbers
    elif choice == '2':
       print(number1,"-",number2,"=", (number1 - number2))
#if they choose 3, multiply the numbers
    elif choice == '3':
       print(number1,"*",number2,"=", (number1 * number2))
#if they choose 4, divide the numbers
    elif choice == '4':
       print(number1,"/",number2,"=", (number1 / number2))
    else:
       print("Invalid input")
      #ask if they want to continue
    cont = input("Continue?y/n:")
  #if they choose n, end the program
    if cont == "n":
        break
