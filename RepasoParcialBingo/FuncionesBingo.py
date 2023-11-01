import random
def create_board():
    unique_num = []
    for i in range(1,26):
        while True:
            number = int(input(f"Ingrese el {i}º numero (en el rango del 1 al 75): "))
            if number <= 75 and number >= 0:
                if number not in unique_num:
                    unique_num.append(number)
                    break
                else:
                    print("Número duplicado. Intente con otro número.")
            else:
                print("Número fuera de rango. Intente con otro número.")
    bingo_board = []
    x=0
    for i in range(5):
        row = []
        for j in range(5):
            row.append(unique_num[x])
            x += 1
        bingo_board.append(row)
    return bingo_board

def play_bingo(board):
    get_numbers = []
    while len(get_numbers) < 75:
        balls = random.randint(1, 75)
        if balls not in get_numbers:
            get_numbers.append(balls)
            print(f"Bola extraída: {balls}")
            for row in board:
                if balls in row:
                    print(f"Numero encontrado!: {balls}")
                    row[row.index(balls)] = "X"  
                    break
            if check_bingo(board):
                print("¡BINGO! Has completado una línea en tu cartón")
                for row in board:
                    for element in row:
                        print(element, end=" ")
                    print()
                break

def check_bingo(board):
    
    for row in board:
        full_row = True
        for num in row:
            if num != "X":
                full_row = False
                break
        if full_row:
            return True

    for i in range(5):
        full_column = True
        for j in range(5):
            if board[j][i] != "X":
                full_column = False
                break
        if full_column:
            return True

    full_diagonal = True
    for i in range(5):
        if board[i][i] != "X":
            full_diagonal = False
            break
    if full_diagonal:
        return True

    full_diagonal = True
    for i in range(5):
        if board[i][4 - i] != "X":
            full_diagonal = False
            break
    if full_diagonal:
        return True

    return False