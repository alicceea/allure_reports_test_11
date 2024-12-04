import allure
from allure_commons.types import Severity
from selene import browser, by, be
from selene.support.shared.jquery_style import s

browser.config.window_width = 1920
browser.config.window_height = 1080

@allure.tag("critical")
@allure.severity(Severity.CRITICAL)
@allure.label("owner", "alice")
@allure.feature('Задачи в репозитории №2')
@allure.story("Пользователь находит Issue под номером один")
@allure.link("https://github.com/home", name="Testing")
def test_decorator_steps():
    open_main_page()
    search_for_repository()
    go_to_repository()
    open_issue_tab()
    should_see_issue_with_number()

@allure.step("Открываем главную страницу")
def open_main_page():
    browser.open('https://github.com/home')

@allure.step("Ищем репозиторий")
def search_for_repository():
    s('[class=search-input]').click()
    s('[id=query-builder-test]').send_keys("alicceea/lesson7_qa")
    s('[id=query-builder-test]').submit()

@allure.step("Переходим по ссылке репозитория")
def go_to_repository():
    s(by.link_text('alicceea/lesson7_qa')).click()

@allure.step("Открываем таб Issues")
def open_issue_tab():
    s("#issues-tab").click()
    # sleep(1)

@allure.step("Проверяем наличие Issue с номером 76")
def should_see_issue_with_number():
    s(by.partial_text("Number one")).should(be.visible)
