import pandas as pd

df = pd.read_csv("sales_data_sample.csv")


# TODO: Pass in any pandas df and get back a table definition
def create_table_definition(df):
    prompt = """### sqlite SQL table, with it properties:
    #
    # Sales({})
    #
    """.format(",".join(str(col) for col in df.columns))  # long string of column names

    return prompt


print(create_table_definition(df))  # Sales(ORDERNUMBER,QUANTITYORDERED...CONTACTFIRSTNAME)


# TODO: Grab the Natural Language Request
def prompt_input():
    nlp_text = input("Enter the info you want: ")
    return nlp_text


# TODO: Combine the prompts
def combine_prompts(df, query_prompt):
    definition = create_table_definition(df)
    query_init_string = f"### A query to answer: {query_prompt}\nSELECT"
    return definition + query_init_string


nlp_text = prompt_input()   # Grabs the NLP
print(combine_prompts(df, nlp_text))   # inserts DF + "query that does..." + injects NLP

