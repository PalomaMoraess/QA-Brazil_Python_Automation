Afrom selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys


class UrbanRoutesPage:

    # Seção DE e PARA
    from_field = (By.ID, 'from')
    to_field = (By.ID, 'to')

    # Fluxo do Táxi
    taxi_option = (By.XPATH, '//button[contains(text(),"Chamar")]')
    comfort_icon = (By.XPATH, '//img[contains(@src, "kids")]')
    comfort_active = (By.XPATH, '//*[@id="root"]//div[contains(@class,"active") and contains(@class,"tcard")]')

    # Cartão
    card_number = (By.ID, "number")
    card_code = (By.ID, "code")
    add_button = (By.XPATH, "//button[text()='Adicionar']")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    # Metodo de pagamento
    payment_method = (By.CLASS_NAME, "pp-button")
    add_card = (By.XPATH, "//div[contains(text(),'Adicionar cartão')]")
    current_payment_method = (
        By.XPATH,
        "//div[contains(@class,'pp-value-text')]"
    )

    # Telefone
    phone_button = (By.CLASS_NAME, "np-button")
    phone_input = (By.ID, "phone")
    next_button = (By.XPATH, "//button[text()='Próximo']")
    sms_code = (By.ID, "code")
    confirm_button = (By.XPATH, "//button[text()='Confirmar']")
    registered_phone = (By.XPATH, "//div[contains(@class,'np-text')]")

    # Comentário
    message_field = (By.ID, "comment")

    # Cobertor e lençóis
    blanket_switch = (
        By.XPATH,
        "//div[text()='Cobertor e lençóis']/following::input[@type='checkbox'][1]"
    )

    blanket_switch_slider = (
        By.XPATH,
        "//div[text()='Cobertor e lençóis']/following::span[contains(@class,'slider')][1]"
    )

    # Sorvete
    ice_cream_plus = (By.CLASS_NAME, "counter-plus")
    ice_cream_count = (By.CLASS_NAME, "counter-value")

    # Pedir táxi
    order_taxi_button = (By.XPATH, "//span[text()='Pedir']")
    order_header = (By.XPATH, "//div[text()='Buscar carro']")


    # Métodos auxiliares (POM)

    def _find(self, locator):
        return self.wait.until(
            EC.visibility_of_element_located(locator)
        )

    def _click(self, locator):
        self.wait.until(
            EC.element_to_be_clickable(locator)
        ).click()

    def _type(self, locator, text):
        element = self._find(locator)
        element.clear()
        element.send_keys(text)

    def _get_text(self, locator):
        return self._find(locator).text

    def _get_value(self, locator):
        return self._find(locator).get_attribute('value')

    # Endereços

    def enter_location(self, from_text, to_text):
        self._type(self.from_field, from_text)
        self._type(self.to_field, to_text)

    def get_from_location(self):
        return self._get_value(self.from_field)

    def get_to_location(self):
        return self._get_value(self.to_field)

    # Fluxo do Táxi

    def click_taxi_option(self):
        self._click(self.taxi_option)

    def click_comfort_icon(self):
        self._click(self.comfort_icon)

    def is_comfort_active(self):
        active_button = self._find(self.comfort_active)
        
        return "active" in active_button.get_attribute("class")

    def click_payment_method(self):
        self._click(self.payment_method)

    def click_add_card(self):
        self._click(self.add_card)

    def get_current_payment_method(self):
        return self._get_text(self.current_payment_method)

    def enter_card_number(self, number):
        element = self._find(self.card_number)
        element.clear()
        element.send_keys(number)
        element.send_keys(Keys.TAB)

    def enter_card_code(self, code):
        element = self.driver.find_element(
            By.XPATH,
            "//input[@id='code' and contains(@class,'card-input')]"
        )
        element.click()
        element.clear()
        element.send_keys(code)
        element.send_keys(Keys.TAB)

    def click_add_button(self):
        self._click(self.add_button)

    def click_close_card_button(self):
        buttons = self.driver.find_elements(
            By.CSS_SELECTOR,
            "button.close-button.section-close"
        )

        for button in buttons:
            if button.is_displayed() and button.is_enabled():
                self.driver.execute_script(
                    "arguments[0].click();",
                    button
                )
                return


    # Telefone
    def click_phone_button(self):
        self._click(self.phone_button)

    def enter_phone_number(self, phone):
        self._type(self.phone_input, phone)

    def click_next_button(self):
        self._click(self.next_button)

    def enter_sms_code(self, code):
        self._type(self.sms_code, code)

    def click_confirm_button(self):
        self._click(self.confirm_button)

    def get_registered_phone(self):
        return self._get_text(self.registered_phone)

    # Comentário

    def enter_message_for_driver(self, message):
        self._type(self.message_field, message)

    def get_message_for_driver(self):
        return self._get_value(self.message_field)

    # Cobertor e lençóis
    def click_blanket_switch(self):
        self._click(self.blanket_switch_slider)

    def blanket_switch_is_selected(self):
        element = self.driver.find_element(By.CLASS_NAME, "switch-input")
        return element.is_selected()

    # Sorvete

    def add_ice_cream(self):
        self._click(self.ice_cream_plus)

    def get_ice_cream_count(self):
        return int(self._get_text(self.ice_cream_count))


    # Pedir táxi

    def click_order_taxi_button(self):
        self._click(self.order_taxi_button)

    def order_header_is_displayed(self):
        return self._find(self.order_header).is_displayed()
