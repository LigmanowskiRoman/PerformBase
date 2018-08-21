from base_test_case import BaseTestCase
from the_automated_tester_object import AutomatedTesterPageObject

class AutomatedTester(BaseTestCase):

    @classmethod
    def page_load(cls):
        cls.driver.navigate(cls.url)
        cls.aut_test_obj = AutomatedTesterPageObject(cls.driver)
        print("You are currently on {}".format(cls.driver.current_url()))

    def radio_button_click(self):
        self.aut_test_obj.radiobutton.click()
        self.assertTrue(self.aut_test_obj.radiobutton.attribute("checked"), "Radio button wasn't clicked")

    def dropdown_change(self):
        self.aut_test_obj.select_dropdown.select(text="Selenium RC")
        self.assertEqual(self.aut_test_obj.select_dropdown.value(), "Selenium RC", "Wrong option selected")

    def string_check(self):
        self.assertTrue("Assert that this text" in self.aut_test_obj.text_to_assert, "There is no text visible")

    def load_text_to_page(self):
        before = self.aut_test_obj.textbox.text()
        self.aut_test_obj.load_text_button.click()
        self.assertTrue(before != self.aut_test_obj.textbox.text(), "Text is not loaded to textbox")

    def verify_if_there_is_no_ajax_text(self):
        self.assertFalse(self.aut_test_obj.ajaxtext.is_displayed(), "Ajax text is visible, but it shouldn't")