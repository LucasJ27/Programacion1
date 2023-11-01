from FuncionesBingo import create_board,play_bingo,check_diagonal
print("¡Bienvenido al Bingo de la UTN!")
print("Vamos a crear tu carton, tienes que elegir 25 numeros a tu gusto")   
while True:      
    bingo_board = create_board()
    print()
    print("Ya tenemos tu carton creado, ahora a jugar!")
    print()
    play_bingo(bingo_board)
    options = int(input("Desea jugar de nuevo?\n1-Si\n2-No"))
    if options == 2:
        print("Gracias por jugar con nosotros!")
        break

    
        
    
    