import json
import os

def load_faq(path="data/faq.json"):
    """
    Carrega o JSON de FAQ.
    Retorna uma lista de dicionários com perguntas e respostas.
    """
    if not os.path.exists(path):
        raise FileNotFoundError(f"Arquivo {path} não encontrado.")

    with open(path, "r", encoding="utf-8") as f:
        try:
            data = json.load(f)
        except json.JSONDecodeError as e:
            raise ValueError(f"Erro ao carregar JSON: {e}")

    # Validação básica do conteúdo
    if not isinstance(data, list):
        raise ValueError("O arquivo JSON deve conter uma lista de perguntas e respostas.")

    for item in data:
        if "pergunta" not in item or "resposta" not in item:
            raise ValueError("Cada item no FAQ precisa ter os campos 'pergunta' e 'resposta'.")

    return data
