import click
import os

def get_user_slection(limit=5):
	message = "Enter selection [0-{}]".format(limit)
	selection = None
	while not selection:
		selection = click.prompt(message,type=click.IntRange(0,limit),default=0)
		if not selection:
			break
	return selection

def get_prompt_header(title):
	prompt = "Select your favorite article from " + title+"\n"
	prompt = prompt + len(prompt)*"="
	return prompt

def print_prompt(article_list, title):
	os.system('clear')
	header = get_prompt_header(title)
	print(header)
	for index, article in enumerate(article_list):
		print('{} | {}'.format(index,article.title))

def get_favorite_article(article_list, title):
	print_prompt(article_list,title)
	favorite = get_user_slection()
	return article_list[favorite]