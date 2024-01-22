#Individual College Comparison based on College Brochure
#Comparitive College Application

import tkinter as tk
import os
from pinecone import Pinecone
import logging
import sys
from llama_index import VectorStoreIndex, SimpleDirectoryReader
from llama_index.vector_stores import PineconeVectorStore

logging.basicConfig(stream=sys.stdout, level=logging.INFO)
logging.getLogger().addHandler(logging.StreamHandler(stream=sys.stdout))

os.environ["PINECONE_API_KEY"] = "a0ada4d5-659d-494c-95da-b9018e8f4107"
os.environ["OPENAI_API_KEY"] = "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"
api_key = os.environ["PINECONE_API_KEY"]
pc = Pinecone(api_key=api_key)

pinecone_index = pc.Index("my-college-comparison-index")

reader = SimpleDirectoryReader("files").load_data()
from llama_index.storage.storage_context import StorageContext

if "OPENAI_API_KEY" not in os.environ:
    raise EnvironmentError(f"Environment variable OPENAI_API_KEY is not set")

vector_store = PineconeVectorStore(pinecone_index=pinecone_index)
storage_context = StorageContext.from_defaults(vector_store=vector_store)
index = VectorStoreIndex.from_documents(reader, storage_context=storage_context
)

query_engine = index.as_query_engine(similarity_top_k=20)

root = tk.Tk()
root.title("College Comparison Application")

query_box = tk.Entry(root, width=75)
query_box.pack()

result_label = tk.Label(root, text="", wraplength=500)
result_label.pack()

def process_query():
    query = query_box.get()
    response = query_engine.query(query)
    result_label.config(text=response)

query_button = tk.Button(root, text="Enter Prompt", command=process_query)
query_button.pack()

root.mainloop()