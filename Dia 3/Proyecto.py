print("Este es un analizador de texto")
text = input("Digite el texto a analizar: \n")
letters = set(input("Digite las letras a buscar en el texto\nanteriormente ingresado: \n"))
letters.discard(' ')
letters = list(letters)
text_reverse = text.split()
text_reverse.reverse()
result = {
    letters[0]: f"Aparece {text.lower().count(letters[0])} veces en el texto",
    letters[1]: f"Aparece {text.lower().count(letters[1])} veces en el texto",
    letters[2]: f"Aparece {text.lower().count(letters[2])} veces en el texto",
    "total_palabras": f"El numero total de palabras ingresadas es de: {len(text.split())}",
    "first_letter": f"La primera letra del texto ingresado es: {text[0]}",
    "last_letter": f"La ultima letra del texto ingresado es: {text[-1]}",
    "iverted_text": ' '.join(text_reverse),
    "python": f"Aparece python en el texto: {'python' in text.lower()}"
}

print(result)
