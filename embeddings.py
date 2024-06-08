'''
Run this script to upload embeddings on Pinecone only.
'''

from langchain_community.document_loaders import PyPDFLoader
import os

PINECONE_API_KEY = os.environ.get('PINECONE_API_KEY')
OPENAI_API_KEY = os.environ.get('OPENAI_API_KEY')
INDEX_NAME = 'rag-pdf'


from langchain_pinecone import PineconeVectorStore
from langchain_openai import OpenAIEmbeddings
from langchain_text_splitters import CharacterTextSplitter


embeddings = OpenAIEmbeddings()

# path to an example text file
loader = PyPDFLoader("data/Cheiro.pdf")

documents = loader.load()
text_splitter = CharacterTextSplitter(chunk_size=500, chunk_overlap=50)
docs = text_splitter.split_documents(documents)

vectorstore_from_docs = PineconeVectorStore.from_documents(
    docs,
    index_name=INDEX_NAME,
    embedding=embeddings
)


