import time

link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_add_to_cart(browser):
    browser.get(link)
    add_tocart = browser.find_element_by_css_selector('.btn-add-to-basket')
    assert add_tocart