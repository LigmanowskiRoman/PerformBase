radio_button = "#radiobutton"
select = "#selecttype"
assertion_text = "#divontheleft"
load_text_button = "#secondajaxbutton"
text_box = "#html5div"
ajax_load = "#loadajax"
loaded_ajax_text = "#ajaxdiv"

class AutomatedTesterPageObject():
    def __init__(self, driver):
        self.driver = driver
        self.radiobutton = self.driver.find(radio_button)
        self.select_dropdown = self.driver.find(select)
        self.text_to_assert = self.driver.find(assertion_text).text()
        self.load_text_button = self.driver.find(load_text_button)
        self.textbox = self.driver.find(text_box)
        self.load_with_ajax = self.driver.find(ajax_load)
        self.ajaxtext = self.driver.find(loaded_ajax_text)




