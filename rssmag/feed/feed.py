from collections import namedtuple
from feedparser import parse

Feed = namedtuple("Feed",["title","article_list","substack_flag"])

'''
TODO: validate the f***ing feeds actually exist lmao
'''

def create_feed(url,n=5):
	feed_dict = parse(url)
	title = feed_dict.feed['title']
	entry_list = feed_dict.entries[0:n]
	substack_flag = "substack" in url
	return(Feed(title,entry_list,substack_flag))
