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
        time.sleep(10)

    def test_order_2_ice_creams(self):
        numbers_of_ice_creams = 2
        for count in range(numbers_of_ice_creams):
            # Adicionar em S8
            pass
        print("Função criada para adicionar quantidade de sorvetes")

    def test_select_plan(self):
        # Adicionar em S8
        pass
        print("Função criada para selecionar o plano")

    def test_fill_phone_number(self):
        # Adicionar em S8
        pass
        print("Função criada para preencher o número de telefone")

    def test_fill_card(self):
        # Adicionar em S8
        pass
        print("Função criada para preencher os dados do cartão")

    def test_comment_for_driver(self):
        # Adicionar em S8
        pass
        print("Função criada para adicionar comentário para o motorista")

    def test_order_blanket_and_handkerchiefs(self):
        # Adicionar em S8
        pass
        print("Função criada para solicitar cobertor e lenços")

    def test_car_search_model_appears(self):
        # Adicionar em S8
        pass
        print("Função criada para verificar se o modelo do carro aparece")

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()