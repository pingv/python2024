import os
import sys
from fastapi import FastAPI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_openai import ChatOpenAI
from langserve import add_routes

# Import credentials from config
try:
    from config import OPENAI_API_KEY
    os.environ["OPENAI_API_KEY"] = OPENAI_API_KEY
except ImportError:
    print("❌ ERROR: config.py not found!")
    print("📝 Please copy config.example.py to config.py and add your OpenAI API key")
    print("   cp config.example.py config.py")
    sys.exit(1)

# Create prompt template
system_template = "Translate the following into {language}:"
prompt_template = ChatPromptTemplate.from_messages([
    ('system', system_template),
    ('user', '{text}')
])

# Create model
model = ChatOpenAI()

# Create parser
parser = StrOutputParser()

# Create chain
chain = prompt_template | model | parser

# App definition
app = FastAPI(
  title="LangChain Server",
  version="1.0",
  description="A simple API server using LangChain's Runnable interfaces",
)

# Add chain route
add_routes(
    app,
    chain,
    path="/chain",
)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="localhost", port=8000)
