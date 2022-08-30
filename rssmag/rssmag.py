from feed.feed import create_feed
from feed.article import create_article
from pypandoc import convert_file
import click

def load_feeds(filename):
	f = open(filename,'r')
	return(f.readlines())

def unload_list_to_file(l1, filename):
	with open(filename, 'w') as f:
		for article in l1:
			print(article,file=f)
	del l1[:]

def html_to_md(filename):
	out = filename.removesuffix(".html")
	out = out +".md"
	''' 
	TODO: Pypandoc is trash from the few tests i've run
	it has crashed at least 40% of the times, ideally i'd call
	proper pandoc from here, i haven't looked into how to achieve that tho
	
	'''	
	convert_file(filename,"markdown",outputfile=out)


def main_loop():
	feed_list = click.prompt("Enter feeds file")
	feeds = load_feeds(feed_list)
	outputfile = click.prompt("Enter path for output file")
	click.clear()
	article_list = [create_article(create_feed(url)) for url in feeds]
	unload_list_to_file(article_list,outputfile)
	html_to_md(outputfile)
	click.echo(click.style('YOUR MAGAZINE IS READY BITCH!!!', fg='green', blink=True))
# TEST
main_loop()
