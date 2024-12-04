import allure
from allure_commons.types import Severity
from selene import browser, by, be
from selene.support.shared.jquery_style import s

browser.config.window_width = 1920
browser.config.window_height = 1080

@allure.tag("critical")
@allure.severity(Severity.CRITICAL)
@allure.label("owner", "alice")
@allure.feature('Задачи в репозитории №3')
@allure.story("Пользователь находит Issue под номером один")
@allure.link("https://github.com/home", name="Testing")
def test_dynamic_steps():
    with allure.step("Открываем главную страницу"):
        browser.open('https://github.com/home')
    with allure.step("Ищем репозиторий"):
        s('[class=search-input]').click()
        s('[id=query-builder-test]').send_keys("alicceea/lesson7_qa")
        s('[id=query-builder-test]').submit()

    with allure.step("Переходим по ссылке репозитория"):
        s(by.link_text('alicceea/lesson7_qa')).click()

    with allure.step("Открываем таб Issues"):
        s("#issues-tab").click()

    with allure.step("Проверяем наличие Issue с номером 76"):
        s(by.partial_text("Number one")).should(be.visible)