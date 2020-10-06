# Calculadora em Python

print("\n **************************** Calculadora em Python **************************\n");
print("1 - Soma");
print("2 - Subtração");
print("3 - Multiplicação");
print("4 - Divisão\n\n");

op = int (input("Qual operação gostaria de realizar: "));
num1 = float (input("Digite o primeiro número: "));
num2 = float (input("Digite o segundo número: "));
print("\n\n")

def calculadora():

	if(op == 1):
		resultado = lambda num1, num2: num1+num2;
		print(num1, "  +  ", num2, " = ", resultado(num1,num2));
	elif (op == 2):
		resultado = lambda num1, num2: num1-num2;
		print(num1, "  -  ", num2, " = ", resultado(num1,num2));
	elif (op == 3):
		resultado = lambda num1, num2: num1*num2;
		print(num1, "  *  ", num2, " = ", resultado(num1,num2));
	elif(op==4):
		resultado = lambda num1,num2: num1/num2;
		print(num1, "  /  ", num2, " = ", resultado(num1,num2));
	else:
		print("O operador indicado não existe!");

calculadora();

print ("\n********** operação finalizada  ************");