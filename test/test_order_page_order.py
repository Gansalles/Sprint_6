import time

import allure
import pytest

from data import Data
from locators.main_page_locators import MainPageLocators
from locators.order_page_locators import OrderPageLocators


class TestOrderPage:

    @allure.title('Проверка кнопки "Заказать"  в хедере на лендинге Яндекс Самоката')
    def test_check_open_order_page_tap_button_in_header(self, main_page):
        main_page.open_main_page()
        main_page.click_on_cookie()
        main_page.tap_order_header_button()
        assert Data.ORDER_PAGE == main_page.get_current_url()

    @allure.title('Проверка кнопки "Заказать" на лендинге Яндекс Самоката')
    def test_check_open_order_page_tap_midlle_button(self, main_page):
        main_page.open_main_page()
        main_page.click_on_cookie()
        main_page.scroll_to_middle_button()
        main_page.tap_order_middle_button()
        assert Data.ORDER_PAGE == main_page.get_current_url()

    person_data = [
            [MainPageLocators.ORDER_BUTTON, 'Александр', 'Янушкевич', 'Москва', 'Лубянка', '79900000000', '21', 'сутки',
             'чёрный жемчуг', 'Не звонить'],
            [MainPageLocators.ORDER_MIDDLE_BUTTON, 'Алексей', 'Сильченко', 'Москва', 'Черкизовская', '79955555555', '25', 'трое суток',
             'серая безысходность', 'Перед доставкой позвонить']
        ]
    @allure.title('Проверка флоу заказа самоката на сайте "Яндекс.Самоката"')
    @pytest.mark.parametrize('button, name, surname, address, station, phone, date_piker, rental_period, color, comment',
                             person_data)
    def test_check_pop_up_window_successful_order(self, main_page, order_page, button, name, surname, address, station, phone,
                                                  date_piker, rental_period, color, comment):
        main_page.open_main_page()
        main_page.click_on_cookie()
        main_page.click_button(button)
        order_page.order_about_person_page(name, surname, address, station, phone)
        order_page.tap_next_page_button()
        order_page.order_about_rental_page(date_piker, rental_period, color, comment)
        order_page.tap_order_final_button()
        assert order_page.find_element(OrderPageLocators.ORDER_MODAL_HEADER_SUCCESSFULLY_PLACED)
