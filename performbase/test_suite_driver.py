import unittest
import sys
import os
import argparse

sys.path.append(os.path.sep.join(sys.path[0].split(os.path.sep)[:-1]))

from test_cases_driver import SeleniumTestCases
from automatedtester import AutomatedTester


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("--url", default="http://www.goal.com/en-gb")
    parser.add_argument("--browser", default="Chrome")
    parser.add_argument("--device", nargs='?', const=None, default=None)
    parser.add_argument("--test_level", default="all_tests")
    parser.add_argument("--resolution", default="1024x768")
    return parser.parse_args()


def suite():
    args = parse_args()
    SeleniumTestCases.browser_type = args.browser
    SeleniumTestCases.url = args.url
    SeleniumTestCases.device = args.device
    SeleniumTestCases.width, SeleniumTestCases.height = args.resolution.split('x')
    AutomatedTester.browser_type = args.browser
    AutomatedTester.url = "http://book.theautomatedtester.co.uk/chapter1"
    AutomatedTester.device = args.device
    AutomatedTester.width, AutomatedTester.height = args.resolution.split('x')

    # You can define test hierarchy here:
    smoke = unittest.TestSuite()
    functional = unittest.TestSuite()
    regression = unittest.TestSuite()
    all_tests = unittest.TestSuite([smoke, regression, functional])

    smoke.addTest(SeleniumTestCases('test_one'))
    smoke.addTest(SeleniumTestCases('are_titles_in_articles'))
    smoke.addTest(SeleniumTestCases('are_images_in_articles'))
    smoke.addTest(SeleniumTestCases('open_first_article'))
    smoke.addTest(AutomatedTester('page_load'))
    smoke.addTest(AutomatedTester('radio_button_click'))
    smoke.addTest(AutomatedTester('dropdown_change'))
    smoke.addTest(AutomatedTester('string_check'))
    smoke.addTest(AutomatedTester('load_text_to_page'))
    smoke.addTest(AutomatedTester('verify_if_there_is_no_ajax_text'))

    return locals()[args.test_level]

if __name__ == '__main__':
    result = unittest.TextTestRunner(verbosity=2).run(suite())
    sys.exit(not result.wasSuccessful())