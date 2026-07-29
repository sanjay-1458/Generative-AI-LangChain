from dotenv import load_dotenv

load_dotenv()

from langchain_huggingface import HuggingFaceEmbeddings


embedding = HuggingFaceEmbeddings(model_name="BAAI/bge-small-en-v1.5")

vector = embedding.embed_query("What is Gen AI?")

print(len(vector))