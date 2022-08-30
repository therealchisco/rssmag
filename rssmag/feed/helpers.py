import click
import os

def get_prompt_header(title):
	header = "Top Articles from " + title+"\n"
	header = header + len(header)*"="
	return header

def get_prompt_body(article_list):
	body = "\n"
	for index, article in enumerate(article_list):
		body = body +"{} | {}\n".format(index,article.title)
	return body

def get_prompt_message(article_list, title):
	header = get_prompt_header(title)
	body = get_prompt_body(article_list)
	separator = header.splitlines()[1]
	prompt = "\nChoose favorite"
	message = header + body + separator + prompt 
	return message

def get_favorite_article(article_list,title):
	message = get_prompt_message(article_list,title)
	cap = len(article_list)
	selection = click.prompt(message,type=click.IntRange(0,cap),default=0)
	click.clear()
	return article_list[selection]