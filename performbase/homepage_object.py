TOP_STORIES_MODULE = "section.widget-top-stories"
ARTICLE = "article"
TITLE = "div.title"
IMAGE = "div.picture.article-image"
LAST_ELEMENT = "p.widget-footer__copyright"

class HomePageObject(object):
    def __init__(self, driver):
        self.driver = driver
        self.top_stories = self.driver.find(TOP_STORIES_MODULE)
        self.articles = self.top_stories.find(ARTICLE)
        self.titles = [article.attribute(TITLE) for article in self.articles]
        self.images = [article.attribute(IMAGE) for article in self.articles]
        self.last_element_on_page = self.driver.find(LAST_ELEMENT)

    @property
    def number_of_articles(self):
        return len(self.articles)

    def click_on_element(self, element):
        self.articles[element-1].click()


