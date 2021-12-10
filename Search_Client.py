import os
import json

#DEFINIENDO EL GRAFO MEDIANTE UN DICCIONARIO DE PYTHON:
#PARA MEJOR COMPRENSION EL VALOR 'a': [('p',4), ('j',15), ('b',1)],
#INDICA QUE EL VERTICE 'a' ES ADYACENTE CON 'P', CON 'J' Y CON 'b' 
#CADA UNO CON SU RESPECTIVO PESO, AUNQUE EL PESO PARA HACER RECCORRIDOS EN PROFUNDIDAD
#NO ES NECESARIO, SE LO AGREGUE PARA MOSTRAR TAMBIÉN LA IMPLEMENTACIÓN DE UN GRAFO PONDERADO

grafo = {'a': [('p',4), ('j',15), ('b',1)],
       	'b': [('a',1), ('d',2), ('e',2), ('c',3)],
	'j': [('a',15)],
	'p': [('a', 4)],
	'd': [('b',2), ('g',3)],
	'e': [('b',2), ('g',4), ('f',5), ('c',2)],
	'c': [('b',3), ('e',2), ('f',5), ('i',20)],
	'g': [('d',3), ('e',4), ('f',10), ('h',1)],
	'f': [('g',10), ('e',5), ('c',5)],
	'i': [('c',20)],
	'h': [('g',1)] 
	}

#MUESTRA EL GRAFO ANTES DEL RECORRIDO
#print("Muestra el grafo antes del recorrido: \n")
#for key, lista in grafo.items():
#	print(key)
#	print(lista)

print()
os.system("pause")

def searchTravels(visitors,data):
					
	visitados = visitors
	pila = []

	origen = input("Ingresa un nodo: ")
	print("\nLista de recorrido en profundidad\n")
	#Paso 1: SE COLOCA EL VÉRTICE ORIGEN EN UNA PILA
	pila.append(origen)
	#Paso 2: MIENTRAS LA PILA NO ESTE VACÍA
	while pila:
		#paso 3: DESAPILAR UN VÉRTICE, ESTE SERÁ AHORA EL VÉRTICE ACTUAL
		actual = pila.pop()
		#FORMA ALTERNATIVA PARA DESAPILAR:
		#actual = pila[-1]
		#pila.remove(pila[-1])

		#paso 4: SI EL VÉRTICE ACTUAL NO HA SIDO VISITADO
		if actual not in visitados:
			#paso 5: PROCESAR (IMPRIMIR) EL VÉRTICE ACTUAL
			print(" -> ", data['data'+actual])
			#paso 6: COLOCAR VÉRTICE ACTUAL EN LA LISTA DE VISITADOS
			visitados.append(actual)
		#paso 7: PARA CADA VÉRTICE QUE EL VÉRTICE ACTUAL TIENE COMO DESTINO,
		#        Y QUE NO HA SIDO VISITADO:
		#        APILAR EL VERTICE
		for key, lista in grafo[actual]:
			if key not in visitados:
				pila.append(key)


def main():
	visitados = []
	with open('data.json') as file:
		data = json.load(file)
	print(data['a'])

	while True:
		
		print('a. '+data['dataa']+'\nb. '+data['datab']+'\nj. '+data['dataj']+'\np. '+data['datap']+'\nd. '+data['datad']+'\ne. '+data['datae']+'\nc. '+data['datac']+'\ng. '+data['datag']+'\nf. '+data['dataf']+'\ni. '+data['datai']+'\nh. '+data['datah']+'\n0. presiona 0 para salir del menu.')
		nodoNo = input("Ingresa un nodo que no deseas visitar: ")
		os.system('cls')	
		if nodoNo == "0" : break
		else: visitados.append(nodoNo)		
	print(visitados)		

	searchTravels(visitados,data)

	print()


	os.system("pause")