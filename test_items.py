import pytest
import time
from selenium import webdriver
link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
def test_button_add_to_basket_is_visible(browser):
    browser.get(link)
    time.sleep(30)
    assert browser.find_element_by_css_selector("[class='btn btn-lg btn-primary btn-add-to-basket']")