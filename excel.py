import tkinter
from tkinter import filedialog
from tkinter import ttk
import os
import openai
from llama_index import download_loader, VectorStoreIndex, SimpleDirectoryReader

openai.api_key = "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"
os.environ["OPENAI_API_KEY"] = "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"

reader = SimpleDirectoryReader("pdfs").load_data()
index = VectorStoreIndex.from_documents(reader)
query_engine = index.as_query_engine(similarity_top_k=10)

root = tkinter.Tk()
root.title("College Comparison Application")

main_frame = ttk.Frame(root, padding=20) 
main_frame.pack(fill="both", expand=True)

query_box = ttk.Entry(main_frame, width=75) 
query_box.grid(row=1, column=0, padx=10, pady=10) 

result_label = ttk.Label(main_frame, text="", wraplength=500)
result_label.grid(row=2, column=0, columnspan=2) 

def process_query():
    query = query_box.get()
    response = query_engine.query(query)
    result_label.config(text=response)

query_button = ttk.Button(main_frame, text="Enter Prompt", command=process_query)
query_button.grid(row=3, column=0, columnspan=2)


root.mainloop()