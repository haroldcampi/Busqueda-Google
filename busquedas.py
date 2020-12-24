from googlesearch import search


termino = input("Busqueda: ") 
cant_resultados = int(input("Cantidad de resultados: "))

for i in search(termino, cant_resultados, lang="es"):
    print(i)