import os
import openai

# Tap into API
os.environ['OPENAI_API_KEY'] = 'YOUR API KEY'
openai.api_key = (os.getenv('OPENAI_API_KEY'))

#Query the response
response = openai.Completion.create(
    model='text-davinci-003',
    prompt='Give me two reasons to learn OpenAI API with Python',
    max_tokens=300)


print(response['choices'][0]['text'])
