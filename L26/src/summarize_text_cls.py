# summarize_text_cls.py
import os
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI
 
load_dotenv()

description = """
Spelunky 2 is the third installment in the Spelunky series of video games. In Spelunky 2 you play as Ana Spelunky, daughter of Guy Spelunky, as they venture into the moon. The Spelunky games are all 2D platformer action roguelikes with quite high difficulty and highly chaotic situations that it puts the player in. The games use extensive random generation with Spelunky 2 having easily both the most diverse and complex levels of any of the three.
In the story of the Spelunky series Guy Spelunky becomes a world renowned adventurer and before the start of Spelunky 2 Guy and his wife travel to the moon to search beneath its surface for treasure. Many years later, however, they still have not returned so their daughter travels to the moon as well to complete their quest and hopefully find them in the process.
Spelunky 2 features many diverse areas as beneath the surface of the moon things are wildly different from reality with underground temples, civilizations of cavemen, aliens cloning facilities, and many more diverse areas.
"""

summary_template = """
You are an excited assistant.
Respond to user's description of a video game with, for that game:
    1. A brief summary
    2. An exciting element of the game
    3. The main characters
Their description of the game was:
{description}
"""

prompt = PromptTemplate(
    input_variables=["description"],
    template=summary_template
)

def main():
    print("Hello from COP2080!")
  
    summary_prompt_template = PromptTemplate(
        input_variables=["description"], template=summary_template
    )

    llm = ChatGoogleGenerativeAI(
        model="gemini-2.5-flash",  temperature=0
    )
    chain = summary_prompt_template | llm

    response = chain.invoke(input={"description": description})
    print(response.content)

if __name__ == "__main__":
    main()
