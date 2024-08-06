# treino de rotina em python variaveis

idade = 25
print(idade)

#float

altura = 1,75
print(altura)

#strings(texto)

nome = 'Ruan'
print(nome)

#listas

numeros = [0, 1, 2, 3, 4]
print(numeros)

#acessando elementos lista

numeros = [0, 1, 2, 3, 4]
print(numeros[2])

# dicionario com pares chave-valor

pessoa = {
    "nome": "Ruan",
    "idade": 25,
    "altura": 1,75
}

print(pessoa)

#acessando um valor no dicionario

print(pessoa["idade"])


#operaçoes

a = 10
b = 6 
soma = a + b
print(soma)

#concatenaçao strings

saudacao = "Ola"
nome = "Carlos"
mensagem = saudacao + ", " + nome + "!"
print(mensagem)

#adiçao de elemento a lista
frutas = ["maça", "banana", "laranja"]
frutas.append("uva")
print(frutas) 

#exemplos 

largura = 5
altura = 10
area = largura * altura
print(area)

#-------------------------------------------

endereço = "Rua Alfredo Schwartz, 70"
preço = "179.000"
tamanho = "45.0"

print(f"Endereço: {endereço}")
print(f"Preço: R$ {preço}")
print(f"Tamanho: {tamanho} m2")
