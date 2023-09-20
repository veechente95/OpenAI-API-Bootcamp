import os
import openai
import inspect  # transform python code into a string

openai.api_key = os.getenv("OPENAI_API_KEY")


def docstring_prompt(code):
    prompt = f"{code}\n # A high quality python docstring of the above python function:\n\"\"\""
    return prompt


def hello(name):
    """
    param: name

    this function prints out hello and then the name
    :return:
    """
    print(f"Hello {name}")

def create_docstring(function):
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=docstring_prompt(inspect.getsource(function)),
        temperature=0,
        max_tokens=100,
        top_p=1.0,
        stop=["\"\"\""]  # Corresponds to """, the end of the docstring
    )
    return merge_docstring_and_function(function, response['choices'][0]['text'])


# TODO: Follow this format
# fist line of function --- def myfunc():
    # """
    # DOCSTRING (Completion API)
    # """
    # Rest of the function


def merge_docstring_and_function(original_function, doctring):
    function_string = inspect.getsource(original_function)
    split = function_string.split('\n')   # splits on first line
    first_part, second_part = split[0], split[1:]   # split between first part and everything after first part

    merged_function = first_part + '\n    """' + doctring + '    """' + '\n' + '\n'.join(second_part)

    return merged_function

