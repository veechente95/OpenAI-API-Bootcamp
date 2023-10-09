# We'll use a Kaggle data set consisting of StackOverflow Python questions and answers
# We will use StackSample, which is 10% of all StackOverflow questions from about 3 years ago
# 1GB of questions have been reduced to ~8MB csv file of top questions
# Then we'll fine tune the Babbage model to see how it affects the results
# We'll also explore the OpenAI tiktoken library to estimate costs

import os
import openai
import pandas as pd
import tiktoken
import json

openai.api_key = os.getenv("OPENAI_API_KEY")

qa_df = pd.read_csv("python_qa.csv")

# Get questions (body) and answers from csv
questions, answers = qa_df["Body"], qa_df["Answer"]

# Create a nested list with dict of question and response
qa_openai_format = [{"prompt": q, "completion": a} for q, a in zip(questions, answers)]
qa_sample_4 = qa_openai_format[4]['completion']


# Goal use a cheaper model to fine tune response and avoid hallucinations
response = openai.Completion.create(
    model="text-babbage-001",   # choose a poor model b/c it's cheaper to fine tune
    prompt=qa_sample_4,
    max_tokens=250,
    temperature=0
)

response_choices = response['choices'][0]['text']
# print(response_choices)


# Convert strings to tokens
def num_tokens_from_string(string, encoding_name):    # gpt2
    encoding = tiktoken.get_encoding(encoding_name)   # create encoding
    num_tokens = len(encoding.encode(string))         # get length / count of tokens
    return num_tokens


dataset_size = 500   # 4429 rows total in csv, but we are using 500 to save money on request
with open("example_training_data.json", "w") as f:
    for entry in qa_openai_format[:dataset_size]:   # grab from start to dataset size (500)
        f.write(json.dumps(entry))
        f.write('\n')

token_counter = 0   # REMEMBER: $0.0006 per 1k tokens * 4 epochs
for element in qa_openai_format:
    for prompt, completion in element.items():
        token_counter += num_tokens_from_string(prompt, 'gpt2')
        token_counter += num_tokens_from_string(completion, 'gpt2')


total_price = 0.0006 * 4 * token_counter / 1000
print(total_price)

fine_tuned_model = "ENTER_NUM"   # run this on terminal --> openai api fine_tunes.create -t "FullFilePath/training_data.json" -m babbage

response = openai.Completion.create(
    model=fine_tuned_model,
    prompt="What are good python books",
    max_tokens=128
)

print(response['choices'][0]['text'])
