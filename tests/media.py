aluno = input("Digite o nome do aluno: ")

def calcular_media(notas):
    return sum(notas) / len(notas)

def classificar_media(media):
    if media >= 7.0:
        return 'Aprovado(a) ✅'
    elif media>= 5.0:
        return "Recuperação ⚠️"
    else:
        return 'Reprovado(a) ❌'


def executar_calculo():
 # Solicitar as 4 notas
    nota1 = float(input("Digite a nota 1: "))
    nota2 = float(input("Digite a nota 2: "))
    nota3 = float(input("Digite a nota 3: "))
    nota4 = float(input("Digite a nota 4: "))

    media = calcular_media([nota1,nota2,nota3,nota4])

    print(f"Aluno: {aluno}\nMedia: {media: .2f}")

    print(classificar_media(media))

executar_calculo()

