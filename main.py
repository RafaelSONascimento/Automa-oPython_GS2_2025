from modelos import Perfil, OrientadorCarreira


def exibir_menu_competencias(lista_competencias):
    print("\n--- Selecione suas Competências Atuais ---")
    print("Digite o número de uma competência e pressione Enter.")
    print("Você pode adicionar várias. Digite '0' para finalizar.")

    opcoes = {}
    for indice, comp in enumerate(lista_competencias, 1):
        opcoes[str(indice)] = comp
        print(f"{indice}. {comp}")

    print("\n0. Concluir e Gerar Recomendações")
    return opcoes


def main():
    print("========================================")
    print("   Bem-vindo ao Future Skills Lab!")
    print("  Seu orientador de carreiras do futuro")
    print("========================================")

    nome_usuario = input("Digite seu nome: ")
    perfil_usuario = Perfil(nome_usuario)
    orientador = OrientadorCarreira()

    todas_competencias = [
        "logica", "python", "analise_dados", "comunicacao", "criatividade",
        "empatia", "design", "colaboracao", "etica", "pensamento_critico",
        "lideranca", "adaptabilidade"
    ]
    todas_competencias = sorted(list(set(todas_competencias)))

    mapa_opcoes = exibir_menu_competencias(todas_competencias)

    while True:
        escolha = input(f"\n{perfil_usuario.nome}, escolha uma opção (ou '0' para sair): ")

        if escolha == "0":
            if not perfil_usuario.competencias_usuario:
                print("Você não selecionou nenhuma competência. Análise cancelada.")
                break
            else:
                print(
                    f"\nÓtimo! Vamos analisar seu perfil com base em {len(perfil_usuario.competencias_usuario)} competências.")
                break

        competencia_escolhida = mapa_opcoes.get(escolha)

        if competencia_escolhida:
            perfil_usuario.adicionar_competencia(competencia_escolhida)
        else:
            print("Opção inválida. Por favor, escolha um número da lista.")

    if perfil_usuario.competencias_usuario:
        recomendacoes = orientador.analisar_perfil(perfil_usuario)
        orientador.exibir_recomendacoes(recomendacoes)

    print("\nObrigado por usar o Future Skills Lab!")


# Bloco padrão para garantir que o 'main()' só rode quando executamos este arquivo
if __name__ == "__main__":
    main()