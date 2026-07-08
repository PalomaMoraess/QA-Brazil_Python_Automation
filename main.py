import time

from selenium import webdriver
from selenium.webdriver import DesiredCapabilities

import data
import helpers
from pages import UrbanRoutesPage


class TestUrbanRoutes:

    @classmethod
    def setup_class(cls):
        capabilities = DesiredCapabilities.CHROME
        capabilities["goog:loggingPrefs"] = {'performance': 'ALL'}

        cls.driver = webdriver.Chrome()
        cls.driver.implicitly_wait(5)

        if helpers.is_url_reachable(data.URBAN_ROUTES_URL):
            print("Conectado ao servidor Urban Routes")
        else:
            print("Não foi possível conectar ao Urban Routes. Verifique se o servidor está ligado e ainda em execução.")

    def setup_method(self):
        self.driver.get(data.URBAN_ROUTES_URL)
        self.page = UrbanRoutesPage(self.driver)

    def test_set_route(self):
        self.page.enter_location(data.ADDRESS_FROM, data.ADDRESS_TO)
        assert self.page.get_from_location() == data.ADDRESS_FROM
        assert self.page.get_to_location() == data.ADDRESS_TO

    def test_select_plan(self):
        self.page.enter_location(data.ADDRESS_FROM, data.ADDRESS_TO)
        self.page.click_taxi_option()
        self.page.click_comfort_icon()
        assert self.page.is_comfort_active()

    def test_fill_phone_number(self):
        self.page.enter_location(data.ADDRESS_FROM, data.ADDRESS_TO)
        self.page.click_taxi_option()
        self.page.click_phone_button()

        self.page.enter_phone_number(data.PHONE_NUMBER)
        self.page.click_next_button()

        code = helpers.retrieve_phone_code(self.driver)

        self.page.enter_sms_code(code)
        self.page.click_confirm_button()

        assert self.page.get_registered_phone() == data.PHONE_NUMBER


    def test_fill_card(self):
        self.page.enter_location(data.ADDRESS_FROM, data.ADDRESS_TO)
        self.page.click_taxi_option()
        self.page.click_comfort_icon()
        self.page.click_payment_method()
        self.page.click_add_card()

        self.page.enter_card_number(data.CARD_NUMBER)
        self.page.enter_card_code(data.CARD_CODE)

        self.page.click_add_button()

        assert self.page.get_current_payment_method() == "Cartão"

    def test_comment_for_driver(self):
        self.page.enter_location(data.ADDRESS_FROM, data.ADDRESS_TO)
        self.page.click_taxi_option()
        self.page.click_comfort_icon()

        self.page.enter_message_for_driver(data.MESSAGE_FOR_DRIVER)

        assert self.page.get_message_for_driver() == data.MESSAGE_FOR_DRIVER

    def test_order_blanket_and_handkerchiefs(self):
        self.page.enter_location(data.ADDRESS_FROM, data.ADDRESS_TO)

        self.page.click_taxi_option()
        self.page.click_comfort_icon()

        self.page.click_blanket_switch()

        assert self.page.blanket_switch_is_selected()

    def test_order_2_ice_creams(self):
        numbers_of_ice_creams = 2

        self.page.enter_location(data.ADDRESS_FROM, data.ADDRESS_TO)
        self.page.click_taxi_option()
        self.page.click_comfort_icon()

        for _ in range(numbers_of_ice_creams):
            self.page.add_ice_cream()

        assert self.page.get_ice_cream_count() == numbers_of_ice_creams

    def test_car_search_model_appears(self):
        self.page.enter_location(data.ADDRESS_FROM, data.ADDRESS_TO)

        self.page.click_taxi_option()
        self.page.click_comfort_icon()

        self.page.click_payment_method()
        self.page.click_add_card()
        self.page.enter_card_number(data.CARD_NUMBER)
        self.page.enter_card_code(data.CARD_CODE)
        self.page.click_add_button()
        self.page.click_close_card_button()

        self.page.click_phone_button()
        self.page.enter_phone_number(data.PHONE_NUMBER)
        self.page.click_next_button()
        code = helpers.retrieve_phone_code(self.driver)
        self.page.enter_sms_code(code)
        self.page.click_confirm_button()

        self.page.enter_message_for_driver(data.MESSAGE_FOR_DRIVER)
        self.page.click_blanket_switch()

        self.page.click_order_taxi_button()

        assert self.page.order_header_is_displayed()

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()