# How to avoid Halluciante Responses using prompt engineering

import os
import openai

openai.api_key = os.getenv('OPENAI_API_KEY')

# This prompt specifically asks to avoid any Hallucinate response
prompt = "Give me details about the technology startup called Mimi and Pimo." \
         "Only answer if you are 100% sure that this company exists, otherwise specify, 'I dont know'"

response = openai.Completion.create(
    engine='text-davinci-003',
    prompt=prompt,
    max_tokens=256,
    temperature=0.7,
)

print(response['choices'][0]['text'])
