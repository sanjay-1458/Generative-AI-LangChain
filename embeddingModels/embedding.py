from dotenv import load_dotenv

load_dotenv()

from langchain_mistralai import MistralAIEmbeddings

embedding = MistralAIEmbeddings(
    model = "mistral-embed",
)

vector = embedding.embed_query("What is Gen AI")



print(vector[:6])


