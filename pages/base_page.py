import allure

from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:
    @allure.step('Создание драйвера')
    def __init__(self, driver):
        self.driver = driver

    @allure.step('Открытие страницы')
    def open_url(self, url):
        self.driver.get(url)

    @allure.step('Поиск элемента')
    def find_element(self, locator):
        return self.driver.find_element(*locator)

    @allure.step('Клик по элементу')
    def click_on_element(self, locator):
        self.find_element(locator).click()

    @allure.step('Скролл до элемента')
    def scroll_to_element(self, locator):
        self.driver.execute_script("arguments[0].scrollIntoView();", locator)

    @allure.step('Ожидание элемента на странице и его видимость')
    def wait_element_visibility_of_element_located(self, locator):
        WebDriverWait(self.driver, 3).until(expected_conditions.visibility_of_element_located(locator))

    @allure.step('Ожидание наличия элемента на странице')
    def wait_element_presence_of_element_located(self, locator):
        WebDriverWait(self.driver, 3).until(expected_conditions.presence_of_element_located(locator))

    @allure.step('Ожидание кликабельности элемента')
    def wait_element_element_to_be_clickable(self, locator):
        WebDriverWait(self.driver, 3).until(expected_conditions.element_to_be_clickable(locator))

    def wait_element_visibility_of(self, locator):
        WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of(locator))

    @allure.step('Получение текста элемента')
    def get_text(self, locator):
        return self.find_element(locator).text

    @allure.step('Переход на другую вкладку браузера')
    def witch_to_window(self, number):
        self.driver.switch_to.window(self.driver.window_handles[number])

    @allure.step('Получение url')
    def get_current_url(self):
        return self.driver.current_url

    @allure.step('Ввод текста')
    def send_keys(self, locator, text):
        self.find_element(locator).send_keys(text)
