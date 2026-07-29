from langchain_core.messages import HumanMessage, AIMessage
from langchain_mistralai import ChatMistralAI
from dotenv import load_dotenv

load_dotenv()

# from langchain_huggingface import ChatHuggingFace, HuggingFacePipeline

# llm = HuggingFacePipeline.from_model_id(
#     model_id ="TinyLlama/TinyLlama-1.1B-Chat-v1.0",
#     task="text-generation",
#     pipeline_kwargs=dict(
#         max_new_tokens=512,

#         # When it is disabled we use grredy decoding
#         do_sample=False,

#         # Avoid repeating the same words or phrases too often.
#         repetition_penalty=1.03,
#     ),
# )


# chat_model = ChatHuggingFace(llm=llm)

chat_model = ChatMistralAI(
    model="mistral-small-latest",
)


messages = []

print("Pess Ctrl ^ C to exit")

while True:

    prompt = input("You: ")

    if(prompt == "0"):
        break

    messages.append(HumanMessage(content=prompt))

    response=chat_model.invoke(messages)
    print("Bot: ", response.content)

    messages.append(response)
