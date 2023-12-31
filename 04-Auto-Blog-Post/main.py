from pathlib import Path
import blog_utils
import openai_utils

# Define your paths here
PATH_TO_BLOG_REPO = Path("/Users/veechente/PycharmProjects/Work/Udemy/OpenAI API Bootcamp/OpenAI Notebooks and Files/04-Auto-Blog-Post/veechente95.github.io/.git")
PATH_TO_BLOG = PATH_TO_BLOG_REPO.parent
PATH_TO_CONTENT = PATH_TO_BLOG/"content"
PATH_TO_CONTENT.mkdir(exist_ok=True, parents=True)


# Get the blog content from OpenAI
title = "Easy healthy meal prep ideas"
print(openai_utils.create_prompt(title))
blog_content = openai_utils.get_blog_from_openai(title)

# Get the cover image and create the blog (Insert content to HTML)
_, cover_image_save_path = openai_utils.get_cover_image(title, "cover_image.png")
path_to_new_content = blog_utils.create_new_blog(PATH_TO_CONTENT, title, blog_content, cover_image_save_path)
blog_utils.write_to_index(PATH_TO_BLOG, path_to_new_content)

# Update the blog
blog_utils.update_blog(PATH_TO_BLOG_REPO)