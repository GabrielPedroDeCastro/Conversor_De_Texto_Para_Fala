import pyttsx3 # pip install pyttsx3

print("="*30, "Seja bem vindo", "="*30)
nome = input("Escreva seu nome: ")

#iniciar
bot = pyttsx3.init() 

print("Escreva algo para ela ler!!") # Quando queremos encrever a idade, podemos colocar como numeros inteiros !!!
texto = input("Escreva: ")

# Fala 
bot.say(f"Olá {nome}, tudo bem com você ?, Eu estou viva !!")
bot.say(texto)

#Executar
bot.runAndWait()
