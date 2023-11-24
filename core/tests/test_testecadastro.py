# Generated by Selenium IDE
import pytest
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from django.test import TestCase
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities


class TestTestecadastro():
    def setup_method(self, method):
        self.driver = webdriver.Chrome()
        self.vars = {}

    def teardown_method(self, method):
        self.driver.quit()

    def test_testecadastro(self):
        # Test name: teste_cadastro
        # Step # | name | target | value
        # 1 | open | http://127.0.0.1:8000/ |
        self.driver.get("http://127.0.0.1:8000/")
        # 2 | setWindowSize | 1616x868 |
        self.driver.set_window_size(1616, 868)
        # 3 | click | id=nome |
        self.driver.find_element(By.ID, "nome").click()
        # 4 | type | id=nome | luiz
        self.driver.find_element(By.ID, "nome").send_keys("luiz")
        # 5 | click | id=email |
        self.driver.find_element(By.ID, "email").click()
        # 6 | type | id=email | luiz@gmail.com
        self.driver.find_element(By.ID, "email").send_keys("luiz@gmail.com")
        # 7 | click | css=.align-items-center |
        self.driver.find_element(By.CSS_SELECTOR, ".align-items-center").click()
        # 8 | click | id=telefone |
        self.driver.find_element(By.ID, "telefone").click()
        # 9 | type | id=telefone | 75992031081
        self.driver.find_element(By.ID, "telefone").send_keys("75992031081")
        # 10 | click | id=mensagem |
        self.driver.find_element(By.ID, "mensagem").click()
        # 11 | type | id=mensagem | teste selenium 3
        self.driver.find_element(By.ID, "mensagem").send_keys("teste selenium 3")
        # 12 | click | id=button |
        self.driver.find_element(By.ID, "button").click()
