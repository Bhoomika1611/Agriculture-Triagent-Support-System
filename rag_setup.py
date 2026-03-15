from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import Chroma
from langchain_huggingface import HuggingFaceEmbeddings

# FIX: specify encoding
loader = TextLoader("data/agriculture_docs.txt", encoding="utf-8")

documents = loader.load()

text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=800,
    chunk_overlap=150
)

splits = text_splitter.split_documents(documents)

embedding_model = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

vector_db = Chroma.from_documents(
    documents=splits,
    embedding=embedding_model,
    persist_directory="vector_db"
)

retriever = vector_db.as_retriever(search_kwargs={"k":3})