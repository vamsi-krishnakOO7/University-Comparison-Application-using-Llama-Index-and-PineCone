#Individual College Comparison based on College Brochure
#Comparitive College Application

import tkinter as tk
from tkinter import filedialog
import os
import openai
from llama_index import VectorStoreIndex, SimpleDirectoryReader


openai.api_key = "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"
os.environ["OPENAI_API_KEY"] = "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"

reader = SimpleDirectoryReader("files").load_data()
index = VectorStoreIndex.from_documents(reader)
query_engine = index.as_query_engine(similarity_top_k=10)

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