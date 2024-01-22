import os
import openai
from pathlib import Path
from llama_index import download_loader, VectorStoreIndex, SimpleDirectoryReader

openai.api_key = "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"
os.environ["OPENAI_API_KEY"] = "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"

reader = SimpleDirectoryReader("pdfs").load_data()
index = VectorStoreIndex.from_documents(reader)

query_engine = index.as_query_engine(similarity_top_k=10)  # Adjust top_k as needed

while True:
    user_query = input("Enter Your Prompt (or type STOP to exit the bot):\n ")

    if user_query.lower() == "Stop":
        break
    
    response = query_engine.query(user_query)
    print(response)