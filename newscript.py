import os
from pinecone import Pinecone, PodSpec
import logging
import sys
import os
from llama_index import VectorStoreIndex, SimpleDirectoryReader
from llama_index.vector_stores import PineconeVectorStore
from IPython.display import Markdown, display

logging.basicConfig(stream=sys.stdout, level=logging.INFO)
logging.getLogger().addHandler(logging.StreamHandler(stream=sys.stdout))

os.environ["PINECONE_API_KEY"] = "a0ada4d5-659d-494c-95da-b9018e8f4107"
os.environ["OPENAI_API_KEY"] = "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"
api_key = os.environ["PINECONE_API_KEY"]
pc = Pinecone(api_key=api_key)

pinecone_index = pc.Index("my-college-comparison-index")

documents = SimpleDirectoryReader("./data/paul_graham").load_data()

from llama_index.storage.storage_context import StorageContext

if "OPENAI_API_KEY" not in os.environ:
    raise EnvironmentError(f"Environment variable OPENAI_API_KEY is not set")

vector_store = PineconeVectorStore(pinecone_index=pinecone_index)
storage_context = StorageContext.from_defaults(vector_store=vector_store)
index = VectorStoreIndex.from_documents(
    documents, storage_context=storage_context
)

query_engine = index.as_query_engine()
response = query_engine.query("What did the author do growing up?")

display(Markdown(f"<b>{response}</b>"))