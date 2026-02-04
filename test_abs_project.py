import pytest
from selenium.webdriver.common.by import By


class TestMainPage1():

#    @pytest.mark.first
    @pytest.mark.parametrize('language', ["ru", "en"])
    def test_guest_should_see_login_link(self, browser, language):
        print("start test1")
        link = f"https://{language}.wikipedia.org/wiki/%D0%A1%D1%82%D1%80%D0%B0%D0%BD%D0%B8%D1%86%D0%B0_(%D0%BF%D0%BE%D0%BB%D0%B8%D0%B3%D1%80%D0%B0%D1%84%D0%B8%D1%8F)"
        browser.get(link)
        browser.find_element(By.CSS_SELECTOR, "#searchInput")
        print("finish test1")

#    @pytest.mark.second
    def test_guest_should_see_basket_link_on_the_main_page(self, browser):
        print("start test2")
        link = "https://ru.wikipedia.org/wiki/%D0%A1%D1%82%D1%80%D0%B0%D0%BD%D0%B8%D1%86%D0%B0_(%D0%BF%D0%BE%D0%BB%D0%B8%D0%B3%D1%80%D0%B0%D1%84%D0%B8%D1%8F)"
        browser.get(link)
        browser.find_element(By.CSS_SELECTOR, "#n-content")
        print("finish test2")

#    @pytest.mark.xfail(reason="trulala")
    def test_guest_should_see_search_button_on_the_main_page(self, browser):
        browser.get(link)
        browser.find_element(By.XPATH, '//*[text()="Пожертвовать"]')
