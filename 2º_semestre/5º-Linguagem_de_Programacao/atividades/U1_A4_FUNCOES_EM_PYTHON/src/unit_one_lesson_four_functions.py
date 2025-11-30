# -*- coding: utf-8 -*-
# Sistema de Gestão de Notas de Alunos
# Desenvolvido para a disciplina de Linguagem de Programação

# Função para adicionar notas
def adicionar_notas():
    """
    Solicita ao usuário que insira as notas do aluno e as armazena em uma lista.
    Retorna a lista de notas.
    """
    notas = []
    print("              ===   ADICIONAR NOTAS   === \n")
    
    while True:
        try:
            nota = float(input("Digite uma nota (ou -1 para finalizar): "))
            if nota == -1:
                break
            elif nota < 0 or nota > 10:
                print("\n🚫 Por favor, digite uma nota entre 0 e 10.\n")
            else:
                notas.append(nota)
                print(f"\n📌 Nota {nota} adicionada com sucesso!\n")
        except ValueError:
            print("\n🚫 Entrada inválida. Digite um número.\n")
    
    return notas

# Função para calcular a média
def calcular_media(notas):
    """
    Calcula a média das notas fornecidas.
    Retorna a média aritmética das notas.
    """
    if len(notas) == 0:
        return 0
    return sum(notas) / len(notas)

# Função para determinar a situação
def determinar_situacao(media):
    """
    Determina a situação do aluno com base na média.
    Retorna 'Aprovado' se média >= 7, caso contrário 'Reprovado'.
    """
    if media >= 7:
        return "✅ Aprovado"
    else:
        return "❌ Reprovado"

# Função para exibir relatório
def exibir_relatorio(notas, media, situacao):
    """
    Exibe um relatório completo com todas as notas, a média e a situação do aluno.
    """
    print("\n" + "="*50)
    print("\n📋 RELATÓRIO FINAL DO ALUNO")
    print("\n" + "="*50 + "\n")
    print(f"Notas inseridas: {notas}")
    print("\n" + "-"*50)
    print(f"\nQuantidade de notas: {len(notas)}")
    print("\n" + "-"*50)
    print(f"\nMédia: {media:.2f}")
    print("\n" + "-"*50)
    print(f"\nSituação: {situacao}")
    print("\n" + "="*50 + "\n\n")

# Função principal
def main():
    """
    Função principal que orquestra todo o sistema de gestão de notas.
    """
    print("\n  🖥️  SISTEMA DE GESTÃO DE NOTAS DE ALUNOS 🖥️")
    print("="*50 + "\n")
    
    # Adicionar notas
    notas = adicionar_notas()
    
    if not notas:
        print("\n❗ Nenhuma nota foi inserida. Encerrando o sistema. ❗\n")
        return
    
    # Calcular média
    media = calcular_media(notas)
    
    # Determinar situação
    situacao = determinar_situacao(media)
    
    # Exibir relatório
    exibir_relatorio(notas, media, situacao)

# Executar o programa
if __name__ == "__main__":
    main()