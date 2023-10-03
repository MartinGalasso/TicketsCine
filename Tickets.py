def print_asientos(matriz_asientos: list):
    for fila in matriz_asientos:
        print ('  '.join(map(str,fila)))
    
    
def eleccion_lugar(matriz_asientos, fila, asiento):
    if 0 <= fila < len(matriz_asientos) and 0 <= asiento < len(matriz_asientos[0]):
        if matriz_asientos[fila][asiento] == 'L':
            matriz_asientos[fila][asiento] = 'X'
    return matriz_asientos
                         
def print_lugares_actualizados():
    pass
    





def main():
    matriz_asientos = [['L','L','L','L','L','L','L','L','L','L',],
                       ['L','L','L','L','L','L','L','L','L','L',],
                       ['L','L','L','L','L','L','L','L','L','L',],
                       ['L','L','L','L','L','L','L','L','L','L',],
                       ['L','L','L','L','L','L','L','L','L','L',],
                       ['L','L','L','L','L','L','L','L','L','L',],
                       ['L','L','L','L','L','L','L','L','L','L',],
                       ['L','L','L','L','L','L','L','L','L','L',],
                       ['L','L','L','L','L','L','L','L','L','L',],
                       ['L','L','L','L','L','L','L','L','L','L',]]
    
    while True:    
        print('-'*45)
        print('-'*45)
        print('\t\tBienvenido\n')
        print('\t      /MENU PRINCIPAL\ \n')
        print('1: Mostrar disponibilidad de asientos.')
        print('2: Elegir asiento[Fila/Asiento].')
        print('3: Cerrar app.\n')      
        
        menu = input('Elija una opcion: ')        
        
        if int(menu) == 1:
            print_asientos(matriz_asientos)
                
        if int(menu) == 2:
            fila = int(input('Indique la fila: '))
            asiento = int(input('Indique asiento: '))
            matriz_asientos_nueva = eleccion_lugar(matriz_asientos,fila,asiento)
            print_asientos(matriz_asientos_nueva)
        
        elif menu == '3':
                while True:
                    cerrar = str(input("¿Está seguro de cerrar? [Si/No]: ").capitalize())
                    if cerrar == 'Si':
                        print('Adios')
                        return  # Salir del bucle y finalizar el programa
                    elif cerrar == 'No':
                        break  # Volver al menú principal
                    else:
                        print('Valor no entendible, intente de nuevo')
                                      
main()                
            

        
