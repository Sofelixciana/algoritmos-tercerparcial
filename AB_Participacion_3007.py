# AL735098 - VEMD - Actividad búsqueda ternaria

def btemaria(arreglo, n, llave):
	l = int()
	r = int()
	mid1 = int()
	mid2 = int()
	a = int()
	b = int()
	r = n
	l = 1
	a = 0
	b = 0
	while b!=1:
		mid1 = round(l+(r-l)/3)
		mid2 = round(r-(r-l)/3)
		if arreglo[mid1-1]==llave:
			respuesta = mid1
			a = 1
			b = 1
		else:
			if arreglo[mid2-1]==llave:
				respuesta = mid2
				a = 1
				b = 1
			else:
				if arreglo[mid1-1]>llave:
					r = mid1-1
				else:
					if arreglo[mid2-1]<llave:
						l = mid2+1
					else:
						l = mid1+1
						r = mid2-1
	if a==0:
		respuesta = -1
	return respuesta

if __name__ == '__main__':
	llave = int()
	arraglo = int()
	n = int()
	ind = int()
	llave = 6
	n = 10
	arreglo = [float() for ind0 in range(10)]
	arreglo[0] = 1
	arreglo[1] = 2
	arreglo[2] = 3
	arreglo[3] = 4
	arreglo[4] = 5
	arreglo[5] = 6
	arreglo[6] = 7
	arreglo[7] = 8
	arreglo[8] = 9
	arreglo[9] = 10
	ind = btemaria(arreglo,n,llave)
	if ind!=-1:
		print("El elemento ",llave," se encontro en el lugar: ",ind)
	else:
		print("El elemento no se encontro en el arreglo")

