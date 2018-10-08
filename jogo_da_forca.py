import random

class jogo_da_forca:

	def inicializa_jogo(self):
	    imprime_bem_vindo()

	    palavra_secreta = leitura_do_arquivo()

	    letras_acertadas = ["_" for i in palavra_secreta] #Para a quantidade de letras acrescenta um underline
	    print(letras_acertadas)

	    loop_de_jogadas(palavra_secreta, letras_acertadas)


	def imprime_bem_vindo(self):
	    print("*=" * 11)
	    print("*=*=JOGO DA FORCA=*=*=*")
	    print("*=" * 11)


	def leitura_do_arquivo(self):
	    arquivo = open("palavras_forca.txt", "r")
	    palavras = []

	    for linha in arquivo:
	    	palavras.append(linha.strip()) #Adiciona numa lista as palavras do arquivo e tira os espaços a mais

	    arquivo.close() #fecha o arquivo
	    numero = random.randrange(0, len(palavras))  # Sorteia de 0 ao tamanho do arquivo
	    palavra_secreta = palavras[numero].upper()  # Deixa maiuscula a palavra e escolhe uma palavra sorteada do arquivo

	    return palavra_secreta


	def marca_chute_correto(self, letra, letras_acertadas,palavra_secreta):
	    posicao = 0  # Orienta em qual posição esta cada palavra
	    for chute in palavra_secreta:
	    	if chute == letra:
	    		letras_acertadas[posicao] = letra  # Aloca a letra acertada na posição em que ela se encontra
	    		posicao += 1  # Feito para se ocorrer letras repetidas


	def loop_de_jogadas(self, palavra_secreta, letras_acertadas):
	    enforcou = False
	    acertou = False
	    erros = 0
	    while not enforcou and not acertou:
	    	letra = str(input("Digite a Letra: ")).strip().upper()  # Deixa maiusculo e tira os espaços em branco no inicio eno fim

	    	if(letra in palavra_secreta):
		    	marca_chute_correto(letra, letras_acertadas, palavra_secreta)
		    else:
		    	erros += 1  # Conta os erros do usuario
		    	desenha_forca(erros)

		enforcou = erros == 7  # Usa esse por causa do valor logico de resposta, se não estiver contido satisfaz a condição, logo a resposta logica e True
		acertou = "_" not in letras_acertadas  # Usa esse por causa do valor logico de resposta, se não estiver contido satisfaz a condição, logo a resposta logica e True

		print(letras_acertadas)  # Letras que foram acertas


	    if acertou:
			ganhou()
	    else:
			perdeu(palavra_secreta)
		print("FIM DE JOGO")


	def ganhou(self):
	    print("Parabéns, você ganhou!")
	    print("       ___________      ")
	    print("      '._==_==_=_.'     ")
	    print("      .-\\:      /-.    ")
	    print("     | (|:.     |) |    ")
	    print("      '-|:.     |-'     ")
	    print("        \\::.    /      ")
	    print("         '::. .'        ")
	    print("           ) (          ")
	    print("         _.' '._        ")
	    print("        '-------'       ")


	def perdeu(self, palavra_secreta):
	    print("Puxa, você foi enforcado!")
	    print("A palavra era {}".format(palavra_secreta))
	    print("    _______________         ")
	    print("   /               \       ")
	    print("  /                 \      ")
	    print("//                   \/\  ")
	    print("\|   XXXX     XXXX   | /   ")
	    print(" |   XXXX     XXXX   |/     ")
	    print(" |   XXX       XXX   |      ")
	    print(" |                   |      ")
	    print(" \__      XXX      __/     ")
	    print("   |\     XXX     /|       ")
	    print("   | |           | |        ")
	    print("   | I I I I I I I |        ")
	    print("   |  I I I I I I  |        ")
	    print("   \_             _/       ")
	    print("     \_         _/         ")
	    print("       \_______/           ")


	def desenha_forca(self, rros):
	    print("  _______     ")
	    print(" |/      |    ")

	    if erros == 1:
		print(" |      (_)   ")
		print(" |            ")
		print(" |            ")
		print(" |            ")

	    if erros == 2:
		print(" |      (_)   ")
		print(" |      \     ")
		print(" |            ")
		print(" |            ")

	    if erros == 3:
		print(" |      (_)   ")
		print(" |      \|    ")
		print(" |            ")
		print(" |            ")

	    if erros == 4:
		print(" |      (_)   ")
		print(" |      \|/   ")
		print(" |            ")
		print(" |            ")

	    if erros == 5:
		print(" |      (_)   ")
		print(" |      \|/   ")
		print(" |       |    ")
		print(" |            ")

	    if erros == 6:
		print(" |      (_)   ")
		print(" |      \|/   ")
		print(" |       |    ")
		print(" |      /     ")

	    if erros == 7:
		print(" |      (_)   ")
		print(" |      \|/   ")
		print(" |       |    ")
		print(" |      / \   ")

	    print(" |            ")
	    print("_|___         ")
	    print()
