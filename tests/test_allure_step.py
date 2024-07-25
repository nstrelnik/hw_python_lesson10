import allure
from selene import browser, by, be


def test_search_issue():
    with allure.step("Открытие главной страницы"):
        browser.open('/')

    with allure.step("Поиск репозитория"):
        browser.element('.search-input').click()
        browser.element('#query-builder-test').type(
            'eroshenkoam/allure-example'
        ).press_enter()

    with allure.step("Переход по ссылке репозитория"):
        browser.element(by.link_text('eroshenkoam/allure-example')).click()

    with allure.step("Открытие таба Issues"):
        browser.element('#issues-tab').click()

    with allure.step("Проверка начилия Issues с номером 76"):
        browser.element(by.partial_text("#76")).should(be.visible)
