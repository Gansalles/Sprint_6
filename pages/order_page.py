import allure

import generators
from data import Data
from locators.main_page_locators import MainPageLocators
from locators.order_page_locators import OrderPageLocators
from pages.base_page import BasePage


class OrderPage(BasePage):

    @allure.step('Открываем страницу заказа самоката')
    def open_order_page(self):
        self.open_url(Data.ORDER_PAGE)
        self.wait_element_visibility_of_element_located(OrderPageLocators.ORDER_HEADER)

    @allure.step('Заполняем поле "Имя"')
    def set_name(self):
        name = generators.generate_name()
        self.send_keys(OrderPageLocators.INPUT_NAME, name)

    @allure.step('Заполняем поле "Фамилия"')
    def set_surname(self):
        surname = generators.generate_surname()
        self.send_keys(OrderPageLocators.INPUT_SURNAME, surname)

    @allure.step('Заполняем поле "Адрес"')
    def set_address(self):
        address = generators.generate_address()
        self.send_keys(OrderPageLocators.INPUT_ADDRESS, address)

    @allure.step('Выбираем станцию метро')
    def set_station(self):
        station = generators.generate_station()
        self.click_on_element(OrderPageLocators.SELECT_SUBWAY)
        self.wait_element_presence_of_element_located(OrderPageLocators.select_station_subway(station))
        self.click_on_element(OrderPageLocators.select_station_subway(station))
        self.wait_element_visibility_of_element_located(OrderPageLocators.complete_station(station))

    @allure.step('Заполняем поле "Телефон"')
    def set_phone(self):
        telephone = generators.generate_telephone()
        self.send_keys(OrderPageLocators.INPUT_TELEPHONE, telephone)

    @allure.step('Заполнение персональными данными')
    def order_about_person_page(self):
        self.set_name()
        self.set_surname()
        self.set_address()
        self.set_station()
        self.set_phone()

    @allure.step('Тап на кнопку "Далее" на первой странице')
    def tap_next_page_button(self):
        self.click_on_element(OrderPageLocators.ORDER_NEXT_BUTTON)
        self.wait_element_visibility_of_element_located(OrderPageLocators.ORDER_HEADER_ABOUT_RENT)

    @allure.step('Заполняем поле "Когда привезти самокат"')
    def set_data_delivery(self, date):
        self.click_on_element(OrderPageLocators.INPUT_DATA_DELIVERY)
        self.wait_element_presence_of_element_located(OrderPageLocators.ORDER_DATA_RENTAL)
        self.click_on_element(OrderPageLocators.select_data_on_piker(date))
        self.wait_element_presence_of_element_located(OrderPageLocators.select_data_in_input(date))

    @allure.step('Заполняем поле "Срок аренды"')
    def set_rental_period(self):
        rental_period = generators.generate_rental_period()
        self.click_on_element(OrderPageLocators.INPUT_DROPDOWN_RENTAL_PERIOD)
        self.wait_element_presence_of_element_located(OrderPageLocators.MENU_DROPDOWN_RENTAL_PERIOD)
        self.click_on_element(OrderPageLocators.select_dropdown_rental_period(rental_period))
        self.wait_element_presence_of_element_located(OrderPageLocators.input_select_rental_period(rental_period))

    @allure.step('Заполняем поле "Цвет самоката"')
    def set_color(self):
        color = generators.generate_color()
        self.click_on_element(OrderPageLocators.checkbox_color(color))
        self.wait_element_visibility_of_element_located(OrderPageLocators.SELECT_CHECKBOX_COLOR)

    @allure.step('Заполняем поле "Комментарии для курьера"')
    def set_comment_delivery(self):
        comment = generators.generate_comment()
        self.send_keys(OrderPageLocators.INPUT_COMMENT, comment)

    @allure.step('Заполнение формы "Про аренду"')
    def order_about_rental_page(self, date):
        self.set_data_delivery(date)
        self.set_rental_period()
        self.set_color()
        self.set_comment_delivery()

    @allure.step('Тап на кнопку "Заказать"')
    def tap_order_final_button(self):
        self.click_on_element(OrderPageLocators.ORDER_FINAL_BUTTON)
        self.wait_element_visibility_of_element_located(OrderPageLocators.ORDER_MODAL_HEADER)
        self.click_on_element(OrderPageLocators.ORDER_MODAL_SURE_BUTTON)
        assert self.find_element(OrderPageLocators.ORDER_MODAL_HEADER_SUCCESSFULLY_PLACED)

    @allure.step('Тапаем на логотип "Самокат" в форме заказа')
    def tap_logo_scooter(self):
        self.click_on_element(MainPageLocators.LOGO_SCOOTER)
