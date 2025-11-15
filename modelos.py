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
        competencias_usuario (list): Uma lista (mutável) das competências que o usuário declara possuir.
    """

    def __init__(self, nome):
        self.nome = nome
        self.competencias_usuario = []

    def adicionar_competencia(self, competencia):
        competencia_lower = competencia.lower()
        if competencia_lower not in self.competencias_usuario:
            self.competencias_usuario.append(competencia_lower)
            print(f"  [+] Competência '{competencia}' adicionada ao seu perfil.")
        else:
            print(f"  [!] Você já possui a competência '{competencia}'.")


class OrientadorCarreira:

    def __init__(self):
        self.banco_carreiras = self._inicializar_banco_carreiras()

    def _inicializar_banco_carreiras(self):
        """Metodo para nosso sistema com carreiras futuras."""
        return {
            "cientista_dados": Carreira(
                "Cientista de Dados",
                "Analisa grandes volumes de dados para extrair insights e tomar decisoes.",
                ("logica", "python", "analise_dados", "comunicacao")
            ),
            "designer_ux": Carreira(
                "Designer de UX/UI Focado em Acessibilidade",
                "Projeta interfaces que sejam faceis e acessiveis para todos os usuarios.",
                ("criatividade", "empatia", "design", "colaboracao")
            ),
            "especialista_ia": Carreira(
                "Especialista em IA e Etica",
                "Desenvolve modelos de IA, garantindo que sejam justos, transparentes e eticos.",
                ("logica", "python", "etica", "pensamento_critico")
            ),
            "gestor_remoto": Carreira(
                "Gestor de Times Remotos",
                "Lidera e motiva equipes distribuídas geograficamente, focado em colaboração.",
                ("colaboracao", "comunicacao", "lideranca", "adaptabilidade")
            )
        }

    def analisar_perfil(self, perfil):

        print("\n--- Analisando seu perfil... ---")
        recomendacoes = []

        competencias_usuario_set = set(perfil.competencias_usuario)

        for chave, carreira in self.banco_carreiras.items():
            competencias_carreira_set = set(carreira.competencias_necessarias)

            competencias_em_comum = competencias_usuario_set.intersection(competencias_carreira_set)

            competencias_faltantes = competencias_carreira_set.difference(competencias_usuario_set)

            pontuacao_match = len(competencias_em_comum)

            if pontuacao_match > 0:
                recomendacoes.append({
                    "carreira": carreira,
                    "pontuacao": pontuacao_match,
                    "em_comum": list(competencias_em_comum),
                    "faltantes": list(competencias_faltantes)
                })

        recomendacoes_ordenadas = sorted(recomendacoes, key=lambda rec: rec["pontuacao"], reverse=True)
        return recomendacoes_ordenadas

    def exibir_recomendacoes(self, recomendacoes):
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