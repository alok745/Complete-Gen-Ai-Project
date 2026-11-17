
# Lec- 15 & 16------------------------------------

from dotenv import load_dotenv
load_dotenv()

from langchain_community.utilities import GoogleSerperAPIWrapper
from langchain_groq import ChatGroq
from langchain.agents import create_agent
from langgraph.checkpoint.memory import MemorySaver

llm = ChatGroq(model="openai/gpt-oss-20b")
search = GoogleSerperAPIWrapper()

agent = create_agent(
    model=llm,
    tools=[search.run],
    system_prompt="You are a Google Search agent who give a answer of user",
    checkpointer = MemorySaver()
)
while True:
    query= input("user :")
    if query.lower() in ["quit", "Bye"]:
        print("Good Bye")
        break
    res = agent.invoke({"messages" :[{"role":"user", "content": query}]},
                       {"configurable":{"thread_id":"alok"}},
                       )
    print("AI:" ,res["messages"][-1].content)