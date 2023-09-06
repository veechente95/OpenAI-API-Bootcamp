# Create a prompt that generates a recipe from a list of ingredients

import os
import openai

openai.api_key = os.getenv('OPENAI_API_KEY')


def create_dish_prompt(list_of_ingredients):
    prompt = f"Create a detailed recipe based on only the following ingredients: {', '.join(list_of_ingredients)}.\n" \
             f"Additionally, assign a tittle starting with 'Recipe Title: ' to this recipe."
    return prompt


recipe = create_dish_prompt(['greek yogurt', 'cheese', 'eggs', 'bread', 'ground turkey'])

response = openai.Completion.create(
    engine='text-davinci-003',
    prompt=recipe,
    max_tokens=512,
    temperature=0.7
)

recipe_result = response['choices'][0]['text']
print(recipe_result)
