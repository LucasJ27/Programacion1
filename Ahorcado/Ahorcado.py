import random
from funcionahorcado import word_guess
list_words = ["automovil", "velocidad", "conductor", "carretera", "motor", "rueda", "gasolina", "frenos", "carroceria", "neumaticos"]

attempts = 15
word = random.choice(list_words) #Elegimos una palabra al azar de la lista de palabras creada anteriormente
guessed_word = ['_'] * len(word) #Reemplazamos las letras de la palabra a adivinar con un "_"
guessed_letters = set() #En este conjunto guardamos las letras que ya hayamos utilizado

while attempts > 0:
    print(f"Adivina la palabra, tiene {len(word)} letras...")
    
    print("".join(guessed_word))  # Muestra la palabra adivinada hasta el momento
    guess = input("Ingresa una letra: ").lower()

    result, attempts = word_guess(word, guessed_word, guessed_letters, attempts, guess) #Invocamos la funcion
    if result: #Si el resultado es "True" es decir que el jugador adivino la palabra, con esta linea salimos del bucle
        break
    

if attempts == 0: #Si el jugador se queda sin intentos, mostramos el mensaje final
    print(f"Te quedaste sin intentos! La palabra era: {word}!")