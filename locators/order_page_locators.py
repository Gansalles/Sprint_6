from selenium.webdriver.common.by import By


class OrderPageLocators():
    COOKIE_BUTTON = By.XPATH, '//button[text() = "да все привыкли"]'  # Кнопка кукки
    ORDER_HEADER = By.XPATH, '//div[text() = "Для кого самокат"]'  # Страница заказа
    INPUT_NAME = By.XPATH, '//input[contains(@placeholder, "Имя")]'  # Плейсхолдер "Имя"
    INPUT_SURNAME = By.XPATH, '//input[contains(@placeholder, "Фамилия")]'  # Плейсхолдер "Фамилия"
    INPUT_ADDRESS = By.XPATH, '//input[contains(@placeholder, "Адрес")]'  # Плейсхолдер "Адрес"
    SELECT_SUBWAY = By.XPATH, '//input[contains(@placeholder, "Станция метро")]'  # Плейсхолдер "Станция метро"
    SELECT_LIST_SUBWAY = By.CLASS_NAME, "select-search__options"

    @staticmethod
    def select_station_subway(station):
        return By.XPATH, (f"//li[@class='select-search__row']//button[.//div[contains(@class, 'Order_Text__2broi') "
                          f"and text()='{station}']]")

    @staticmethod
    def complete_station(station):
        return By.XPATH, f"//input[@value='{station}']"

    INPUT_TELEPHONE = By.XPATH, '//input[contains(@placeholder, "Телефон")]'  # Плейсхолдер "Телефон"
    ORDER_NEXT_BUTTON = By.XPATH, '//button[text() = "Далее"]'  # Кнопка "Далее"
    ORDER_HEADER_ABOUT_RENT = By.XPATH, '//div[text() = "Про аренду"]'  # Название "Про аренду"
    INPUT_DATA_DELIVERY = By.CLASS_NAME, "react-datepicker__input-container" # "Когда привезти самокат"
    ORDER_DATA_RENTAL = By.CLASS_NAME, "react-datepicker" # "Срок аренды"

    @staticmethod
    def select_data_on_piker(date_piker):
        return By.XPATH, (f'//div[contains(@class, "react-datepicker")]//div[contains(@class, "react-datepicker__day")'
                          f'and text() = "{date_piker}"]')

    def select_data_in_input(date_piker):
        return By.XPATH, f'//div[@class = "react-datepicker__input-container"]//input[contains(@value, "{date_piker}")]'

    INPUT_DROPDOWN_RENTAL_PERIOD = By.CLASS_NAME, "Dropdown-control"
    MENU_DROPDOWN_RENTAL_PERIOD = By.CLASS_NAME, "Dropdown-menu"

    @staticmethod
    def select_dropdown_rental_period(rental_period):
        return By.XPATH, f'//div[@class = "Dropdown-option" and text() = "{rental_period}"]'

    @staticmethod
    def input_select_rental_period(rental_period):
        return By.XPATH, f'//div[contains(@class, "is-selected") and text() = "{rental_period}"]'

    @staticmethod
    def checkbox_color(color):
        return By.XPATH, f'//label[text() = "{color}"]'

    SELECT_CHECKBOX_COLOR = By.XPATH, '//div[contains(@class, "FilledContainer")]' # Блок "цвет самоката"
    INPUT_COMMENT = By.XPATH, '//input[contains(@placeholder, "Комментарий для курьера")]' # Плейсхолдер "Комментарий
                                                                                                        # для курьера"
    ORDER_FINAL_BUTTON = By.XPATH, '//div[3]/button[text() = "Заказать"]' # Кнопка "Заказать"
    ORDER_MODAL_HEADER = By.XPATH, '//div[text() = "Хотите оформить заказ?"]' # Название окна "Хотите оформить заказ?"
    ORDER_MODAL_SURE_BUTTON = By.XPATH, '//button[text() = "Да"]' # Кнопка "Да"
    ORDER_MODAL_HEADER_SUCCESSFULLY_PLACED = By.XPATH, '//div[text() = "Заказ оформлен"]' # Название окна
                                                                                            # "Заказ оформлен"
