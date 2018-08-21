from base_test_case import BaseTestCase
from homepage_object import HomePageObject


class SeleniumTestCases(BaseTestCase):

    @classmethod
    def test_one(self):
        self.driver.navigate(self.url)
        self.homepage = HomePageObject(self.driver)
        print("You are currently on {}".format(self.driver.current_url()))

    def are_titles_in_articles(self):
        self.assertEqual(len(self.homepage.titles),self.homepage.number_of_articles,"Not all articles have title")

    def are_images_in_articles(self):
        self.assertEqual(len(self.homepage.images),self.homepage.number_of_articles,"Not all articles have images")

    def open_first_article(self):
        self.homepage.click_on_element(1)
        self.assertTrue(self.homepage.last_element_on_page.is_displayed())
