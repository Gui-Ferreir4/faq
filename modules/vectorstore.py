from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.vectorstores import FAISS
from langchain.embeddings import OpenAIEmbeddings

def build_vectorstore(faq_data):
    """
    Constrói um banco vetorial FAISS a partir do FAQ.
    Cada pergunta + resposta é transformada em um trecho de conhecimento.
    """

    # Junta pergunta + resposta para melhor contexto
    texts = [
        f"Pergunta: {item['pergunta']}\nResposta: {item['resposta']}"
        for item in faq_data
    ]

    # Divide em pedaços menores (chunks), para evitar excesso de tokens
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=800,    # tamanho máximo de cada trecho
        chunk_overlap=100  # sobreposição para manter contexto
    )
    chunks = splitter.split_text("\n\n".join(texts))

    # Cria embeddings com OpenAI
    embeddings = OpenAIEmbeddings()

    # Cria o banco vetorial FAISS
    vectorstore = FAISS.from_texts(chunks, embeddings)

    return vectorstore
