# Create a prompt that generates a recipe from a list of ingredients

import os
import openai
import requests    # connects to the internet for image download
import shutil      # utilities that allows us to copy file object from a URL and save it as the file

openai.api_key = os.getenv('OPENAI_API_KEY')


def create_dish_prompt(list_of_ingredients):
    prompt = f"Create a detailed recipe based on only the following ingredients: {', '.join(list_of_ingredients)}.\n" \
             f"Additionally, assign a tittle starting with 'Recipe Title: ' to this recipe."
    return prompt


recipe = create_dish_prompt(['greek yogurt', 'cheese', 'eggs', 'bread', 'ground turkey'])

text_response = openai.Completion.create(
    engine='text-davinci-003',
    prompt=recipe,
    max_tokens=512,
    temperature=0.7
)

recipe_result = text_response['choices'][0]['text']
print(recipe_result)

image_response = openai.Image.create(
    prompt=recipe_result,
    n=1,   # num of images
    size='1024x1024',
)

print(image_response)

image_url = image_response['data'][0]['url']


# Download the image locally to your machine from URL to .png file
def save_image(image_url, filename):
    image_res = requests.get(image_url, stream=True)
    if image_res.status_code == 200:   # HTML code that means image is found
        with open(filename, 'wb') as f:
            shutil.copyfileobj(image_res.raw, f)
    else:
        print('Error Loading Image')

    return image_res.status_code


print(save_image(image_url, 'image.png'))
