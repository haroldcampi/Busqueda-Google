from googlesearch import search


termino = input("Busqueda: ") 
cant_results = int(input("Cantidad de resultados: "))

for i in search(termino, cant_results, lang="es"):
    print(i)