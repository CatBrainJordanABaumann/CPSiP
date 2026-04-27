# prompt_cls.py
## You will need to replace all #PLACEHOLDER# lines  
from langchain_core.prompts import PromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv

load_dotenv()

# Define a prompt template with placeholders

template = """
You are an excited assistant.
Respond to user's description of a video game with, for that game:
    1. A brief summary
    2. An exciting element of the game
    3. The main characters
Their description of the game was:
{text}
"""


# Create the PromptTemplate object
prompt = PromptTemplate(
    input_variables=["text"],  # placeholders in the template
    template=template
)
# Initialize the Gemini LLM
llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",  temperature=1.0
)

#Function to get user input and generate response
def chat_to_llm():
    while True:
        user_input = input("Enter text to summarize of favorite video game or quit to exit ")
        if user_input.lower().strip() == "quit":
            break

        filled_prompt = prompt.format(text=user_input)
        print(filled_prompt)

        response = llm.invoke(filled_prompt)

        print("Summary:", response.content)        

if __name__ =="__main__":
    chat_to_llm()