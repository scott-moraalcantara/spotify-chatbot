from langchain.chat_models import ChatOpenAI
from langchain.prompts import PromptTemplate
import os

oa_api = os.getenv("OPENAI_API_KEY")

llm = ChatOpenAI(model='gpt-4', temperature=0, openai_api_key= oa_api)

spotify_prompt = PromptTemplate(
    input_variables=["query"],
    template="You are a chatbot that interacts with Spotify. Take in user query, to output the action (play ,search) and the details."

)

def parse_user_query(query):
    response = llm.predict(spotify_prompt.format(query=query))
    return response