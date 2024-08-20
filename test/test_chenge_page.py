import allure

from data import Data


class TestChengePage:

    @allure.title('Тап на логотип "Cамокат"')
    def test_check_open_main_page_tap_logo_scooter(self, order_page):
        order_page.open_order_page()
        order_page.tap_logo_scooter()
        assert Data.MAIN_PAGE == order_page.get_current_url()

    @allure.title('Тап на логотип "Яндекс"')
    def test_check_open_dzen_page_tap_logo_yandex(self, main_page):
        main_page.open_main_page()
        main_page.tap_logo_yandex()
        assert 'dzen.ru' in main_page.get_current_url()
