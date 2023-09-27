def word_guess(word, guessed_word, guessed_letters, attempts, guess):
    
    if guess in word: #Verificamos si la letra ingresada esta presente en la palabra a adivinar
    
        for i in range(len(word)): #Recorremos la palabra a adivinar 
    
            if word[i] == guess: #Verificamos si la letra en la posicion "i" de la palabra a adivinar conincide con la letra ingresada
                guessed_word[i] = guess #Si es asi, reemplazamos el "_" por la letra adivinada
    
        if "".join(guessed_word) == word: #Verificamos si la lista de letras ingresadas por el usuario forma la palabra a adivinar, si es asi mostramos el mensaje final.
            print("¡Adivinaste! La palabra es " + "".join(guessed_word))
            return True, attempts  #Devuelve True si el jugador adivinó la palabra
        else:
            print(f"Letra correcta: {guess}")
    
    else:
        print("Letra incorrecta")
        attempts -= 1
        print(f"Te quedan {attempts} intentos")
        guessed_letters.add(guess)
        print(f"Letras utilizadas: {guessed_letters}")
    
    return False, attempts  #Devuelve False si el jugador no adivinó la palabra