import allure

from data import Data
from locators.order_page_locators import OrderPageLocators
from pages.base_page import BasePage
from locators.main_page_locators import MainPageLocators


class MainPage(BasePage):

    @allure.step('Открываем сайт')
    def open_main_page(self):
        self.open_url(Data.MAIN_PAGE)
        self.wait_element_visibility_of_element_located(MainPageLocators.MAIN_PAGE)

    @allure.step('Принять кукки')
    def click_on_cookie(self):
        self.click_on_element(MainPageLocators.COOKIE_BUTTON)

    @allure.step('Скролим до выпадающего списка "Вопросы о важном"')
    def scroll_to_dropdown_section(self):
        element = self.find_element(MainPageLocators.DROPDOWN_SECTION)
        self.scroll_to_element(element)
        self.wait_element_element_to_be_clickable(MainPageLocators.DROPDOWN_SECTION)

    @allure.step('Найти вопрос')
    def find_dropdown_question(self, id):
        current_question = self.find_element(MainPageLocators.dropdown_element_question(id))
        self.wait_element_visibility_of(current_question)
        return current_question

    @allure.step('Тапнуть на вопрос')
    def tap_on_question(self, id):
        self.click_on_element(MainPageLocators.dropdown_element_question(id))
        self.wait_element_visibility_of_element_located(MainPageLocators.OPEN_DROPDOWN_SECTION)
        current_answer = self.find_element(MainPageLocators.dropdown_element_answer(id))
        self.wait_element_visibility_of_element_located(MainPageLocators.dropdown_element_answer(id))
        return current_answer

    @allure.step('Тапнуть на кнопку "Заказать" в шапке страницы')
    def tap_order_header_button(self):
        self.click_on_element(MainPageLocators.ORDER_BUTTON)
        self.wait_element_visibility_of_element_located(OrderPageLocators.ORDER_HEADER)

    @allure.step('Скролим до "Как это работает"')
    def scroll_to_middle_button(self):
        element = self.find_element(MainPageLocators.ORDER_MIDDLE_BUTTON)
        self.scroll_to_element(element)
        self.wait_element_element_to_be_clickable(element)

    @allure.step('Тапнуть на кнопку "Заказать" под блоком "Как это работает"')
    def tap_order_middle_button(self):
        self.click_on_element(MainPageLocators.ORDER_MIDDLE_BUTTON)
        self.wait_element_visibility_of_element_located(OrderPageLocators.ORDER_HEADER)
