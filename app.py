import streamlit as st
from modules.loader import load_faq
from modules.vectorstore import build_vectorstore
from modules.chatbot import create_chatbot
from modules.ui import render_chat, chat_input

# Configuração inicial da página
st.set_page_config(page_title="FAQ Inteligente", layout="wide")

# Inicializa histórico de mensagens
if "messages" not in st.session_state:
    st.session_state["messages"] = []

# Título do app
st.title("🤖 FAQ Inteligente da Plataforma")

# 1. Carregar os dados do FAQ
try:
    faq_data = load_faq()
except Exception as e:
    st.error(f"Erro ao carregar o FAQ: {e}")
    st.stop()

# 2. Criar banco vetorial
vectorstore = build_vectorstore(faq_data)

# 3. Criar chatbot
chatbot = create_chatbot(vectorstore)

# 4. Renderizar histórico da conversa
render_chat(st.session_state["messages"])

# 5. Entrada do usuário
query = chat_input()
if query:
    # Adicionar pergunta do usuário ao histórico
    st.session_state["messages"].append({"role": "user", "content": query})

    # Obter resposta da IA
    try:
        answer = chatbot.run(query)
    except Exception as e:
        answer = f"⚠️ Erro ao processar sua pergunta: {e}"

    # Adicionar resposta da IA ao histórico
    st.session_state["messages"].append({"role": "assistant", "content": answer})

    # Atualizar a interface
    st.experimental_rerun()
