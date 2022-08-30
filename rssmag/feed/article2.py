from collections import namedtuple
from .helpers import get_favorite_article

Article = namedtuple("Article",["title","body"])

class Article:

	def __init__(self, feed):
		self.feed_title = feed.title
		self.is_substack = feed.substack_flag
		article_list = feed.article_list
		self.article = get_favorite_article(article_list,self.feed_title)

	def _get_substack_content(self):
		content = self.article.content
		content_dict = content.pop()
		return content_dict['value']

	def _get_regular_content(self):
		return self.article.summary

	def _get_content(self):
		if self.is_substack:
			return self._get_substack_content()
		else:
			return self._get_regular_content()
	
	def __str__(self):
		title = self.article.title
		content = self._get_content()
		return "<h2>{}</h2> \n \n {}".format(title,content)

def create_article(feed):
	return Article(feed)
