'''
This script is meant to be used for RAG implimentation
You need to run embeddings.py first before running this script.
Running embeddings.py will upload embeddings to Pinecone vector db
'''



from langchain_pinecone import PineconeVectorStore
from langchain_openai import ChatOpenAI
from langchain_openai import OpenAIEmbeddings
from langchain.chains import RetrievalQAWithSourcesChain
import os

prompt = 'Answer the question asked.'

# embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/paraphrase-MiniLM-L6-v2")
embeddings = OpenAIEmbeddings()
docsearch = PineconeVectorStore(
    index_name="rag-pdf",
    embedding=embeddings,
    pinecone_api_key="80b270ea-3691-496e-ad85-a59076aff84e",
)


# llm = ChatGoogleGenerativeAI(
#     model="gemini-1.0-pro",
#     convert_system_message_to_human=False,
#     google_api_key="AIzaSyAdkCWjykz3IZlw0KIoZFqvBW5LZjLZm3k",
# """I was trying gemini here :)"""
# )


llm = ChatOpenAI(
    openai_api_key=os.environ.get('OPENAI_API_KEY'),
    model_name='gpt-3.5-turbo',
    temperature=0.2
)
retriever = docsearch.as_retriever()


rag_chain = RetrievalQAWithSourcesChain.from_chain_type(
    llm=llm,
    chain_type="stuff",
    retriever=docsearch.as_retriever()
)

