"""

Reference
    - Build a simple LLM application with chat models and prompt templates  https://python.langchain.com/docs/tutorials/llm_chain/
"""

import os
import getpass
from langchain_core.messages import SystemMessage, HumanMessage
from langchain_openai import ChatOpenAI

os.environ["LANGSMITH_TRACING"] = "true"

if not os.environ.get("OPENAI_API_KEY"):
    os.environ["OPENAI_API_KEY"] = getpass.getpass("OpenAI API Key: ")
if not os.environ.get("LANGSMITH_API_KEY"):
    os.environ["LANGSMITH_API_KEY"] = getpass.getpass("LangSmith API Key: ")



model = ChatOpenAI(model="gpt-3.5-turbo")

messages = [
    SystemMessage("Translate the following from English into Korean"),
    HumanMessage("hi!"),
]

print(model.invoke(messages))


# Prompt Templates

from langchain_core.prompts import ChatPromptTemplate

system_template = "Translate the following from English into {language}"
prompt_template = ChatPromptTemplate.from_messages([
    ("system", system_template),
    ("user", "{text}"),
])

prompt = prompt_template.invoke({"language": "Korean", "text": "Where are you from?"})
print(model.invoke(prompt))

