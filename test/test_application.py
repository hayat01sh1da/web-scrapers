from application import Application


def test_webdriver():
    application = Application(init_webdriver=False)
    if application.chrome is None:
        assert application.chrome is None
    else:
        assert str(type(application.chrome)) == \
            "<class 'selenium.webdriver.chrome.webdriver.WebDriver'>"


def test_base_url():
    assert Application(init_webdriver=False).base_url == 'https://scraping-for-beginner.herokuapp.com'
