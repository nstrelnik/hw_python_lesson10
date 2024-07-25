import allure
from selene import by, browser, be
from selene.support.shared.jquery_style import s


def test_decorator_steps():
    open_main_page()
    search_for_repository('eroshenkoam/allure-example')
    go_to_repository('eroshenkoam/allure-example')
    open_issue_tab()
    should_see_issue_with_number('#76')


@allure.step("Открытие главной страницы")
def open_main_page():
    browser.open("https://github.com")


@allure.step("Поиск репозитория {repo}")
def search_for_repository(repo):
    browser.element('.search-input').click()
    browser.element('#query-builder-test').send_keys(repo)
    browser.element('#query-builder-test').submit()


@allure.step("Переход по ссылке репозитория")
def go_to_repository(repo):
    browser.element(by.link_text(repo)).click()


@allure.step("Открытие таба Issues")
def open_issue_tab():
    browser.element('#issues-tab').click()


@allure.step("Проверка наличия Issue с номером {number}")
def should_see_issue_with_number(number):
    browser.element(by.partial_text(number)).should(be.visible)
