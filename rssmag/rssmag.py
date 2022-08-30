from feed.feed import create_feed
from feed.article2 import create_article

def load_feeds(filename):
	f = open(filename,'r')
	return(f.readlines())

def unload_list_to_file(l1, filename):
	with open(filename, 'w') as f:
		for article in l1:
			print(article,file=f)
	del l1[:]

def main_loop():
	feed_list = input("feeds file: ")
	feeds = load_feeds(feed_list)
	outputfile = input("Enter path for outputfile: ")
	article_list = [create_article(create_feed(url)) for url in feeds]
	unload_list_to_file(article_list,outputfile)
# TEST
main_loop()
