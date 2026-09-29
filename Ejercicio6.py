def Contador_Penny(biblioteca, contador = 0):
    #CASO BASE si el contador llega al final de la biblioteca o esta esta vacia terminamos
    if contador >= len(biblioteca):
        return 0
        #CASO RECURSIVO volvemos a llamar a la funcion aumentando el contador
    return 1 + Contador_Penny(biblioteca, contador + 1)