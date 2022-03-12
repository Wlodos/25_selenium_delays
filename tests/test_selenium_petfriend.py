import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By


def test_show_my_pets():
    """ Check if all user`s pets present, have names, ages and breeds, at least half of pets have a photo,
     all pets have different names, there is no identical pets """

    # Enter email
    email = WebDriverWait(pytest.driver, 5).until(ec.presence_of_element_located((By.ID, 'email')))
    email.send_keys('sottestoss@gmail.com')

    # Enter password
    password = WebDriverWait(pytest.driver, 5).until(ec.presence_of_element_located((By.ID, 'pass')))
    password.send_keys('password')

    # Click on submit button
    submit_btn = WebDriverWait(pytest.driver, 5).until(ec.presence_of_element_located(
        (By.CSS_SELECTOR, 'button[type="submit"]')))
    submit_btn.click()

    # Click on "Мои питомцы"
    my_pets_btn = WebDriverWait(pytest.driver, 5).until(ec.presence_of_element_located(
        (By.CSS_SELECTOR, 'a[href="/my_pets"]')))
    my_pets_btn.click()

    # implicitly_wait
    pytest.driver.implicitly_wait(10)
    images = pytest.driver.find_elements_by_css_selector('th>img')
    names = pytest.driver.find_elements_by_css_selector('tr>td:nth-of-type(1)')
    breeds = pytest.driver.find_elements_by_css_selector('tr>td:nth-of-type(2)')
    age = pytest.driver.find_elements_by_css_selector('tr>td:nth-of-type(3)')

    # amount of pets in statistic field
    quantity = int(pytest.driver.find_element_by_xpath('//div[@class=".col-sm-4 left"]').text.split('\n')[1].split(' ')[1])

    count_images = 0
    list_names = []
    pet_list = []
    assert len(images) == quantity

    for i in range(len(images)):
        if images[i].get_attribute('src') != '':
            count_images += 1
        list_names.append(names[i].text)
        pet_list.append((names[i].text, breeds[i].text, age[i].text))
        assert names[i].text != ""
        assert breeds[i].text != ""
        assert age[i].text != ""
    assert count_images >= quantity / 2  # at least half of pets have an image
    assert len(list_names) == len(set(list_names))  # true if all pets have different names
    assert len(pet_list) == len(set(pet_list))  # true if there is no identical pets
