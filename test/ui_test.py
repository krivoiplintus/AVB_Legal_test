import allure
from page.main_page import MainPage
from page.cart_page import CartPage
from page.novelty_page import NoveltyPage
from test_data.data_provider import DataProvider


@allure.title("Регистрация с валидным номером")
def test_reg_pos(browser):
    number = DataProvider().get_number()
    class_button = "app-button auth-modal__sms-button blue"
    with allure.step("Открыть главную страницу"):
        main_page = MainPage(browser)
    main_page.authorization_click()
    main_page.say_number(number)
    with allure.step("Проверить, что кнопка 'получить код' активна"):
        assert main_page.find_atribyte_button() == class_button


@allure.title("Регистрация с невалидным номером")
def test_reg_neg(browser):
    fake_number = DataProvider().get_fake_number()
    class_button = "app-button auth-modal__sms-button blue disabled"
    with allure.step("Открыть главную страницу"):
        main_page = MainPage(browser)
    main_page.authorization_click()
    main_page.say_number(fake_number)
    with allure.step("Проверить, что кнопка 'получить код' не активна"):
        assert main_page.find_atribyte_button() == class_button


@allure.title("Добавление книги в корзину")
def test_add_to_cart(browser):
    with allure.step("Открыть страницу новинки"):
        novelty_page = NoveltyPage(browser)
    novelty_page.add_book_from_novelty_page()
    with allure.step("Перейти в корзину"):
        cart_page = CartPage(browser)
    total_book = cart_page.total_book_in_cart()
    with allure.step("Проверить, что книга добавлена в корзину"):
        assert total_book == "1 товар"
    cart_page.clear_cart()


@allure.title("Удаление книги из корзины")
def test_del_to_cart(browser):
    with allure.step("Открыть страницу новинки"):
        novelty_page = NoveltyPage(browser)
    novelty_page.add_book_from_novelty_page()
    with allure.step("Перейти в корзину"):
        cart_page = CartPage(browser)
    cart_page.clear_cart()
    with allure.step("Перейти в корзину"):
        cart_page = CartPage(browser)
    read_empty_cart_messege = cart_page.empty_cart()
    with allure.step("Проверить, что книга удалена из корзины"):
        assert read_empty_cart_messege == "В корзине ничего нет"


@allure.title("Поиск на латинице с валидными данными")
def test_search(browser):
    search_data = DataProvider().get_search_data()
    with allure.step("Открыть главную страницу"):
        main_page = MainPage(browser)
    main_page.search(search_data)
    with allure.step("Проверить, что количество найденных книг больше 0"):
        assert main_page.total_book_search() > 0


@allure.title("Поиск длинной строки 1024 символа")
def test_search_1024str(browser):
    fake_search_data = DataProvider().get_fake_search_data()
    with allure.step("Открыть главную страницу"):
        main_page = MainPage(browser)
    main_page.search(fake_search_data)
    with allure.step("Проверить, что ничего не найдено"):
        assert main_page.not_founded_search() == "Похоже, у нас такого нет"
