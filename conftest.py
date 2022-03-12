import pytest
from selenium import webdriver


@pytest.fixture(autouse=True)
def testing():
    pytest.driver = webdriver.Chrome('/chromedriver.exe')
    pytest.driver.set_window_size(1400, 1000)

    pytest.driver.get('http://petfriends1.herokuapp.com/login')

    yield

    pytest.driver.quit()


