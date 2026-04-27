from pydantic import BaseModel, Field
from typing import List, Optional

class Ingredient(BaseModel):
    name: str = Field(description="Name of the ingredient.")
    quantity: str = Field(description="Quantity including units.")

class Recipe(BaseModel):
    recipe_name: str = Field(description="The name of the recipe.")
    prep_time_minutes: Optional[int] = Field(description=\
        "Optional prep time in minutes.")
    ingredients: List[Ingredient]
    instructions: List[str]

from google import genai
from dotenv import load_dotenv
import os

load_dotenv()
api_key = os.getenv("GOOGLE_API_KEY")
client = genai.Client(api_key=api_key)

def extract_recipe(text: str) -> Recipe:
    response = client.models.generate_content(
        model="gemini-2.5-flash-lite",
        contents=f"Extract the recipe from this text.\n{text}",
        config={
            "response_mime_type": "application/json",
            "response_json_schema": Recipe.model_json_schema()
        }
    )
    return Recipe.model_validate_json(response.text)

if __name__ == "__main__":
    sample = "Prepare oatmeal by heating water to a boil. "\
        "Combine water with half the volume of water in dry instant oatmeal. "\
        "Add roughly a quarter teaspoon of salt per half cup of dry oatmeal to taste."
    recipe = extract_recipe(sample)
    print(recipe)