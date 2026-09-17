def main():
    print("===== SISTEMA DE GESTÃO DE NOTAS =====")

    notas = adicionar_notas()                     
    media = calcular_media(notas)
    situacao = verificar_situacao(media)
    exibir_relatorio(notas, media, situacao)


def adicionar_notas():      # O sistema deve permitir que o usuário insira as notas dos alunos
    notas = []              # As notas devem ser armazenadas em uma lista

    quantidade = int(input("Quantas Unidades possue o curso? "))

    for i in range(quantidade):
        while True:
            nota = float(input(f"Digite a nota da {i + 1}ª Unidade: "))

            if 0 <= nota <= 10:
                notas.append(nota)
                break
            else:
                print("Nota inválida! Digite uma nota entre 0 e 10.")

    return notas


def calcular_media(notas):      # O sistema deve calcular a média das notas inseridas
    if len(notas) == 0:
        return 0

    return sum(notas) / len(notas)


def verificar_situacao(media):
    if media >= 7:              # Se a média for maior ou igual a 7, o aluno está aprovado.
        return "Aprovado"
    else:                       # Se a média for menor que 7, o aluno está reprovado
        return "Reprovado"


def exibir_relatorio(notas, media, situacao):       #Exibir as notas inseridas, a média e a situação do aluno.
    print("\n========== RELATÓRIO FINAL ==========")
    print("Notas:", notas)
    print(f"Média: {media:.2f}")
    print(f"Situação: {situacao}")
    print("=====================================")


main()

