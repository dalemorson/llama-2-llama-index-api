from transformers import AutoTokenizer
from llama_index import (
    SimpleDirectoryReader,
    VectorStoreIndex,
    ServiceContext,
    set_global_tokenizer
)
from langchain.llms import LlamaCpp
from langchain.callbacks.manager import CallbackManager
from langchain.callbacks.streaming_stdout import StreamingStdOutCallbackHandler
import uvicorn
from fastapi import Request, FastAPI
from llama_cpp import Llama

app = FastAPI()

# for token-wise streaming so you'll see the answer gets generated token by token when Llama is answering your question
callback_manager = CallbackManager([StreamingStdOutCallbackHandler()])
llm = LlamaCpp(
    model_path="../models/7B/llama-2-7b-chat.Q8_0.gguf", # Download from Huggable Face - use TheBloke
    temperature=0.0,
    top_p=1,
    n_ctx=6000,
    verbose=True,
)

set_global_tokenizer(
    AutoTokenizer.from_pretrained("NousResearch/Llama-2-7b-chat-hf").encode
)

# use Huggingface embeddings
from llama_index.embeddings import HuggingFaceEmbedding

embed_model = HuggingFaceEmbedding(model_name="BAAI/bge-small-en-v1.5")

# create a service context
service_context = ServiceContext.from_defaults(
    llm=llm,
    embed_model=embed_model,
)

documents = SimpleDirectoryReader(
    "../storage"
).load_data()

# create vector store index
index = VectorStoreIndex.from_documents(
    documents, service_context=service_context
)

# set up query engine
query_engine = index.as_query_engine()

@app.get("/")
async def index():
   return {"message": "Llama Llama Llama"}

@app.get("/health")
async def health():
   return {"Health": "Up"}

# Use POST as it has a greater character limit than GET
@app.post("/ask")
async def prompt(req: Request):
   body = await req.json()
   prompt = body['question']
   response = query_engine.query(prompt)
   return {"answer": response}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)