import allure
from allure_commons.types import Severity
from selene import browser, by, be
from selene.support.shared.jquery_style import s

browser.config.window_width = 1920
browser.config.window_height = 1080

@allure.tag("critical")
@allure.severity(Severity.CRITICAL)
@allure.label("owner", "alice")
@allure.feature('Задачи в репозитории №1')
@allure.story("Пользователь находит Issue под номером один")
@allure.link("https://github.com/home", name="Testing")
def test_github():
    browser.open('https://github.com/alicceea/lesson7_qa')

    s("#issues-tab").click()
    s(by.partial_text("Number one")).should(be.visible)