#Metodos Computacionais
#Metodo da posicao falsa
import math

#funcao a ser alterada
def Funcao(x):										#funcao calcula valor de f() para qualquer numero dado (a,b ou x)
	return x**3 -x -2 							# ATENCAO professor, a equacao deve ser mudada aqui


#funcao encontra valor de x pela formmula do metodo da posicao falsa
def FuncaoAchaX(a,b):								
	return (a*Funcao(b) -b*Funcao(a))/(Funcao(b)-Funcao(a)) 
		
#funcao calcula erro
def posicaoFalsa(a,b):
	#["vt[0]=k","vt[1]=x","vt[2]=a","vt[3]=b","vt[4]=f(x)","vt[5]=f(a)","vt[6]=f(b)"] apenas para auxilo visual
	vt=[0,0,0,0,0,0,0] 								#lista  para calculo de elementos
	
	# Atencao para linha de baixo
	er = 0.001		                                # erro dado para o calculo,o erro deve ser mudado aqui
	
	#primeira iteracao fora do loop
	vt[0]=1											#adiciona um na primeira iteracao
	vt[2]=float(a) 									#valor de a
	vt[3]=float(b) 									#valor de b
	vt[5]=float(Funcao(a)) 							#valor de f(a)
	vt[6]=float(Funcao(b)) 							#valor de f(b)
	vt[1]=float(FuncaoAchaX(a,b))   				#valor de x
	vt[4]=float(Funcao(vt[1]))
	
	while abs(vt[4]) > er:							#testa se f(x) e maior que o erro dado
		print(vt)									#imprime nova lista apos antes e apos cada loop
		if(vt[4]*vt[5])>0:							#testa de f(x) tem o mesmo sinal de f(a)
			vt[0]=vt[0]+1							#incrementa quantidade de iteracoes
			vt[2]=vt[1]								#valor de a recebe valor de x
			vt[5]=float(Funcao(vt[2]))				#calcula novo valor para f(a)
			vt[6]=float(Funcao(vt[3]))				#calcula novo valor para f(b)
			vt[1]=float(FuncaoAchaX(vt[2],vt[3]))	#calcula novo valor par x
			vt[4]=float(Funcao(vt[1]))				#calcula novo valor para f(x)
		elif(vt[4]*vt[6])>0:						#testa de f(x) tem o mesmo sinal de f(a)
			vt[0]=vt[0]+1							#incrementa quantidade de iteracoes	
			vt[3]=vt[1]								#valor de a recebe valor de x
			vt[5]=float(Funcao(vt[2]))				#calcula novo valor para f(a)
			vt[6]=float(Funcao(vt[3]))				#calcula novo valor para f(b)
			vt[1]=float(FuncaoAchaX(vt[2],vt[3]))	#calcula novo valor para f(x)
			vt[4]=float(Funcao(vt[1]))				#calcula novo valor para f(x)
			
	print(vt)										#imprime ultima tabela
	print("O valor procurado e:")
	print(vt[1])									#imprime valor de x
	
#chamada de funcoes
print("Digite o intervalo")
#a=input()
#b=input()
posicaoFalsa(1,2)
	
