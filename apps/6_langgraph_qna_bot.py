from dotenv import load_dotenv
load_dotenv()

from pydantic import BaseModel
from langchain_groq import ChatGroq
from langgraph.graph import StateGraph, START,END
from langgraph.graph.message import add_messages
from langgraph.checkpoint.memory import InMemorySaver
from typing import Annotated

class ChatState(BaseModel):
    messages : Annotated[list,add_messages]
    
llm = ChatGroq(model="openai/gpt-oss-20b")

def chatbotNode(state:ChatState):
     res = llm.invoke(state.messages)
     state.messages=[res]
     return state
 
memory = InMemorySaver()
 
 
graph= StateGraph(ChatState)
graph.add_node("chatbot",chatbotNode)

graph.add_edge( START, "chatbot")
graph.add_edge("chatbot",END)

graph = graph.compile(checkpointer=memory)
 
while True:
    query= input("user :")
    if query.lower() in ["quit", "Bye"]:
        print("Good Bye")
        break
    res = graph.invoke({"messages" :[{"role":"user", "content": query}]},
                       {"configurable":{"thread_id":"alok"}},
                       )
    print("AI:" ,res["messages"][-1].content)

