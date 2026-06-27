# teacher_summary.py
from langchain_chroma import Chroma
from langchain_ollama import OllamaEmbeddings, ChatOllama
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from config import DB_PATH, EMBEDDING_MODEL, LLM_MODEL, SEARCH_RESULTS_COUNT

def create_summary():
    embeddings = OllamaEmbeddings(model=EMBEDDING_MODEL)
    vectorstore = Chroma(persist_directory=DB_PATH, embedding_function=embeddings)
    docs = vectorstore.similarity_search("დოკუმენტის მთავარი იდეები, ძირითადი თემები და მნიშვნელოვანი ინფორმაცია", k=SEARCH_RESULTS_COUNT)
    context = "\n\n".join([doc.page_content for doc in docs])
    
    template = """შენ ხარ Teacher Assistant სისტემა. მოცემული ტექსტის მიხედვით შექმენი მოკლე summary.
    წესები:
      - გამოიყენე მხოლოდ მოცემული კონტექსტი.
      - summary უნდა იყოს ქართულად.
      - ტექსტი იყოს მოკლე, გასაგები და სასწავლო სტილის.
      - დაწერე 1 ან 2 აბზაცი.
      - არ დაამატო ისეთი ინფორმაცია, რომელიც კონტექსტში არ არის.

    კონტექსტი: {context}
    მოკლე summary: """
    
    prompt = ChatPromptTemplate.from_template(template)
    chain = prompt | ChatOllama(model=LLM_MODEL, temperature=0.2) | StrOutputParser()
    return chain.invoke({"context": context})
