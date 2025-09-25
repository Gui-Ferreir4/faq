from langchain.chat_models import ChatOpenAI
from langchain.chains import RetrievalQA
from config import OPENAI_API_KEY, MODEL_NAME

def create_chatbot(vectorstore):
    """
    Cria o chatbot baseado no banco vetorial do FAQ.
    O chatbot responde apenas com base nas informações do FAQ.
    """

    # Modelo de linguagem (usando API da OpenAI)
    llm = ChatOpenAI(
        model=MODEL_NAME,
        temperature=0,  # respostas mais objetivas
        openai_api_key=OPENAI_API_KEY
    )

    # Retriever = busca os trechos mais relevantes do banco vetorial
    retriever = vectorstore.as_retriever(search_kwargs={"k": 3})

    # RetrievalQA = combina IA + busca semântica
    qa = RetrievalQA.from_chain_type(
        llm=llm,
        retriever=retriever,
        chain_type="stuff"  # insere os trechos diretamente no prompt
    )

    return qa
