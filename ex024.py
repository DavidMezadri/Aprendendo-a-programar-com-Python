cidade = input('Digite o nome da tua cidade: ')
cidade = cidade.lower().strip().split()
print("""O nome desta cidade começa com 'Santo'?:{}""".format('santo' in cidade[0]))