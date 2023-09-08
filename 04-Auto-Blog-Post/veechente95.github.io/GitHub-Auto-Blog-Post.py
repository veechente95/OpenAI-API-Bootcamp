import os
import openai
from git import Repo
from pathlib import Path    # Allows us to set up paths & parent directories to the path files to that GitHub repository

openai.api_key = os.getenv('OPENAI_API_KEY')

PATH_TO_BLOG_REPO = Path("/Users/veechente/PycharmProjects/Work/Udemy/OpenAI API Bootcamp/OpenAI Notebooks and Files/04-Auto-Blog-Post/veechente95.github.io/.git")
PATH_TO_BLOG = PATH_TO_BLOG_REPO.parent

# subdirectory path with blog content
PATH_TO_CONTENT = PATH_TO_BLOG/"content"

# Make directory 'content' in python
PATH_TO_CONTENT.mkdir(exist_ok=True, parents=True)


# use Git to automate updates and push changes into my blog
def update_blog(commit_message='updates blog'):
    repo = Repo(PATH_TO_BLOG_REPO)       # Tells GitPython where to locate repo
    repo.git.add(all=True)               # git add command
    repo.index.commit(commit_message)    # git command with some message
    origin = repo.remote(name='origin')  # git push
    origin.push()


random_text_string = "This is a rando text string"

# This allows us to push text into HTML file
with open(PATH_TO_BLOG/"index.html", 'w') as f:
    f.write(random_text_string)

update_blog()
