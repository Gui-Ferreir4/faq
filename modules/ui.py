import streamlit as st

def render_chat(messages):
    """
    Renderiza o histórico de conversa no estilo chat.
    messages: lista de dicionários com {"role": "user"|"assistant", "content": str}
    """
    for msg in messages:
        if msg["role"] == "user":
            with st.chat_message("user"):
                st.markdown(msg["content"])
        else:
            with st.chat_message("assistant"):
                st.markdown(msg["content"])

def chat_input():
    """
    Campo de entrada fixo no rodapé.
    Retorna o texto digitado pelo usuário.
    """
    return st.chat_input("Digite sua pergunta...")
