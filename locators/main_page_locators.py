from selenium.webdriver.common.by import By

class MainPageLocators:

    COOKIE_BUTTON = By.XPATH, '//button[text() = "да все привыкли"]' # Кнопка кукки
    MAIN_PAGE = By.CLASS_NAME, "Home_HomePage__ZXKIX" # Стартовая страница
    ORDER_BUTTON = By.CLASS_NAME, "Button_Button__ra12g" # Кнопка заказать в шапке страницы
    ORDER_MIDDLE_BUTTON = By.XPATH, "//div[@class = 'Home_FinishButton__1_cWm']/button[text()='Заказать']" # Кнопка
                                                                             # заказать под блоком как это работает
    DROPDOWN_SECTION = By.CLASS_NAME, "accordion"  # Блок с вопросами
    OPEN_DROPDOWN_SECTION = By.XPATH, '//div[not(@hidden)]'

    @staticmethod
    def dropdown_element_question(id):
        return By.ID, f"accordion__heading-{id}"

    @staticmethod
    def dropdown_element_answer(id):
        return By.ID, f"accordion__panel-{id}"
