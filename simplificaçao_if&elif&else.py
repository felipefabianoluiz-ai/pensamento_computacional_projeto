# definimos o dicionario (base de dados)
preço_frutas = {
    'maça' : 2.5,
    'banana': 1.8 ,
    'laranja': 3.0
}

# definimos qual fruta queremos procurar
fruta_desejada = 'maça'  
# fazemos busca direta usando o metodo .get()
# o .get() tenta encontrar a fruta; se nao achar, mostra 'fruta nao encontrada'
resultado = preço_frutas.get(fruta_desejada, 'fruta nao encontrada')

# exibimos o resultado
print(f"O preço da {fruta_desejada} é R${resultado}")
