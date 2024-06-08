from parsing import rag_chain

def chat(prompt: str):
    response = rag_chain.invoke(prompt)
    return { "BOT": f"""{response}"""}
print(chat('What is Hand reading?'))