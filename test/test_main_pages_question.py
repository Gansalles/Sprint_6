import allure
import pytest

from data import Questions, Answers


class TestMainPage:

    @allure.title('Тест "вопрос- ответ"')
    @pytest.mark.parametrize(
        'question, answer, id',
        [
            [Questions.QUESTION_0, Answers.Answer_0, 0],
            [Questions.QUESTION_1, Answers.Answer_1, 1],
            [Questions.QUESTION_2, Answers.Answer_2, 2],
            [Questions.QUESTION_3, Answers.Answer_3, 3],
            [Questions.QUESTION_4, Answers.Answer_4, 4],
            [Questions.QUESTION_5, Answers.Answer_5, 5],
            [Questions.QUESTION_6, Answers.Answer_6, 6],
            [Questions.QUESTION_7, Answers.Answer_7, 7]
        ]
    )

    def test_check_question_in_dropdown_list(self, main_page, question, answer, id):
        main_page.open_main_page()
        main_page.click_on_cookie()
        main_page.scroll_to_dropdown_section()
        current_question = main_page.find_dropdown_question(id)
        current_answer = main_page.tap_on_question(id)
        assert question == current_question.text
        assert answer == current_answer.text
