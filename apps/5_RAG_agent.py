from dotenv import load_dotenv
load_dotenv()

from langchain_community.document_loaders import PyPDFLoader,PyPDFDirectoryLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_ollama import OllamaEmbeddings
from langchain_groq import ChatGroq
from langchain_chroma import Chroma
from langchain.agents import create_agent
from langchain.tools import tool
from langgraph.checkpoint.memory import InMemorySaver
import streamlit as st


if "document_uploaded" not in st.session_state:
    st.session_state.document_uploaded = False
    
if "agent" not in st.session_state:
    st.session_state.agent = None
    
if "vector_store" not in st.session_state:
    st.session_state.vector_store = None

if "messages" not in st.session_state:
    st.session_state.messages = []

def process_document(path):

    # load document

    loader = PyPDFDirectoryLoader(path)
    pdfs = loader.load()


    # split document 

    splitter = RecursiveCharacterTextSplitter(chunk_size= 100000, chunk_overlap = 20)
    split_chunk = splitter.split_documents(pdfs)



    # Embedding & vector store

    embedding = OllamaEmbeddings(model="nomic-embed-text:latest")
    vector_store = Chroma.from_documents(                                 
        documents = split_chunk,
        embedding = embedding
    )



    # agent - tools | llm | system_prompt


    llm = ChatGroq(model="openai/gpt-oss-20b")

    @tool
    def get_tool(query:str):
        """Retrieve documents relevant to a query from the knowledge base."""
    
        context = ""
        docs = vector_store.similarity_search(query= query, k=5)
    
        for doc in docs:
            context += doc.page_content + "\n\n"
        
        return "\n\n".join(doc.page_content for doc in docs)

        

    system_prompt = """ You are a PDF question-answering assistant.

You have access to an uploaded document knowledge base.

IMPORTANT RULES:

1. For every question related to the uploaded PDF,
   ALWAYS call the get_tool tool first.

2. Answer ONLY using the information returned by get_tool.

3. Do not use your general knowledge to answer PDF questions.

4. If the requested information is not present in the
   retrieved document context, say:
   "I could not find this information in the uploaded document."

5. Do not invent or guess information.

6. Give a short and direct answer.
"""
                
                
                
                
    memory = InMemorySaver()        

    agent = create_agent(
        model=llm,
        tools=[get_tool],
        system_prompt=system_prompt,
        checkpointer=memory
    )

    st.session_state.agent = agent
    st.session_state.document_uploaded = True
    


# upload ui

if not st.session_state.document_uploaded:
    uploaded = st.file_uploader(label="Select pdf Files", type=["pdf"], accept_multiple_files=True)
    
    if uploaded:
        with st.spinner("Processing..."):
           path= "./doc_files/"
           for file in uploaded:
                with open(path + file.name, "wb") as f:
                    f.write(file.getvalue())
                    
           process_document(path)
        st.rerun()
            
            
# chat messages

if st.session_state.document_uploaded and st.session_state.agent:
    for message in st.session_state.messages:
        role = message.get("role")
        content= message.get("content")
        st.chat_message(role).markdown(content)
    
    
    
    query = st.chat_input("Ask anything related to uploaded documents" )
    if query:
        st.session_state.messages.append({"role":"user", "content":query})
        
        st.chat_message("user").markdown(query)
        response = st.session_state.agent.invoke(
            {"messages":[{"role":"user", "content":query}]},
            {"configurable": {"thread_id":1}}
        )

        ans = response["messages"][-1].content
        st.chat_message("ai").markdown(ans)
        st.session_state.messages.append({"role":"ai", "content":ans})
  