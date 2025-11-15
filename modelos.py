class Carreira:
    """
    Representa uma carreira futura com suas competências necessárias.
    Atributos:
        nome (str): O nome da carreira (ex: "Engenheiro de IA Ética").
        descricao (str): Uma breve descrição da carreira.
        competencias_necessarias (tuple): Uma tupla de strings com as  competências-chave (técnicas e comportamentais).
    """

    def __init__(self, nome, descricao, competencias_necessarias):
        self.nome = nome
        self.descricao = descricao
        # Usamos uma tupla, pois as competências de uma carreira são imutáveis.
        self.competencias_necessarias = tuple(competencias_necessarias)


class Perfil:
    """
    Representa o perfil de um profissional (usuário).

    Atributos:
        nome (str): Nome do usuário.
        competencias_usuario (list): Uma lista (mutável) das competências
                                     que o usuário declara possuir.
    """

    def __init__(self, nome):
        self.nome = nome
        # Usamos uma lista, pois o usuário pode adicionar/remover competências.
        self.competencias_usuario = []

    def adicionar_competencia(self, competencia):
        """Adiciona uma competência ao perfil, evitando duplicatas."""
        competencia_lower = competencia.lower()
        if competencia_lower not in self.competencias_usuario:
            self.competencias_usuario.append(competencia_lower)
            print(f"  [+] Competência '{competencia}' adicionada ao seu perfil.")
        else:
            print(f"  [!] Você já possui a competência '{competencia}'.")


class OrientadorCarreira:
    """
    O motor do sistema, responsável por analisar perfis e dar recomendações.

    Atributos:
        banco_carreiras (dict): Um dicionário que armazena as carreiras
                                disponíveis no sistema. A chave é um ID
                                e o valor é um objeto da classe Carreira.
    """

    def __init__(self):
        # O "banco de dados" de carreiras usa um dicionário.
        self.banco_carreiras = self._inicializar_banco_carreiras()

    def _inicializar_banco_carreiras(self):
        """Metodo privado para popular nosso sistema com carreiras futuras."""
        return {
            "cientista_dados": Carreira(
                "Cientista de Dados",
                "Analisa grandes volumes de dados para extrair insights e tomar decisões.",
                ("logica", "python", "analise_dados", "comunicacao")
            ),
            "designer_ux": Carreira(
                "Designer de UX/UI Focado em Acessibilidade",
                "Projeta interfaces que sejam fáceis e acessíveis para todos os usuários.",
                ("criatividade", "empatia", "design", "colaboracao")
            ),
            "especialista_ia": Carreira(
                "Especialista em IA e Ética",
                "Desenvolve modelos de IA, garantindo que sejam justos, transparentes e éticos.",
                ("logica", "python", "etica", "pensamento_critico")
            ),
            "gestor_remoto": Carreira(
                "Gestor de Times Remotos",
                "Lidera e motiva equipes distribuídas geograficamente, focado em colaboração.",
                ("colaboracao", "comunicacao", "lideranca", "adaptabilidade")
            )
        }

    def analisar_perfil(self, perfil):
        """
        Compara as competências do perfil com o banco de carreiras e
        gera recomendações.
        """
        print("\n--- Analisando seu perfil... ---")
        recomendacoes = []

        # Convertemos a lista do usuário para um set (conjunto) para otimizar a comparação
        competencias_usuario_set = set(perfil.competencias_usuario)

        for chave, carreira in self.banco_carreiras.items():
            competencias_carreira_set = set(carreira.competencias_necessarias)

            # Usamos a interseção de conjuntos para achar o "match"
            competencias_em_comum = competencias_usuario_set.intersection(competencias_carreira_set)

            # Usamos a diferença de conjuntos para achar o que "falta"
            competencias_faltantes = competencias_carreira_set.difference(competencias_usuario_set)

            pontuacao_match = len(competencias_em_comum)

            # Só recomenda se o usuário tiver pelo menos uma competência da área
            if pontuacao_match > 0:
                recomendacoes.append({
                    "carreira": carreira,
                    "pontuacao": pontuacao_match,
                    "em_comum": list(competencias_em_comum),
                    "faltantes": list(competencias_faltantes)
                })

        # Ordena as recomendações da mais alta para a mais baixa pontuação
        recomendacoes_ordenadas = sorted(recomendacoes, key=lambda rec: rec["pontuacao"], reverse=True)
        return recomendacoes_ordenadas

    def exibir_recomendacoes(self, recomendacoes):
        """Formata e exibe as recomendações no terminal."""
        if not recomendacoes:
            print("Não encontramos recomendações ideais para seu perfil no momento.")
            print("Continue explorando novas competências!")
            return

        print("\n=== Suas Recomações de Carreira ===\n")
        for rec in recomendacoes:
            carreira = rec["carreira"]
            print(f"**{carreira.nome}**")
            print(f"  Descrição: {carreira.descricao}")
            print(f"  Match: {rec['pontuacao']} de {len(carreira.competencias_necessarias)} competências.")
            print(f"  Competências que você possui: {', '.join(rec['em_comum'])}")

            if rec["faltantes"]:
                print(f"  Trilha de Aprendizado (o que falta): {', '.join(rec['faltantes'])}")
            else:
                print("  Parabéns! Você tem todas as competências mapeadas para esta carreira!")
            print("-" * 30)