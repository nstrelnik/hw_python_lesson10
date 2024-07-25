from selene import browser, by, be


def test_search_issue():
    browser.open('/')

    browser.element('.search-input').click()
    browser.element('#query-builder-test').type(
        'eroshenkoam/allure-example'
    ).press_enter()
    browser.element(by.link_text('eroshenkoam/allure-example')).click()
    browser.element('#issues-tab').click()

    browser.element(by.partial_text("#76")).should(be.visible)