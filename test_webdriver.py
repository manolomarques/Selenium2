# Bibliotecas

# Definição
import pytest
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By


class Test_Weddriver():
    # Método de Inicialização do Teste
    def setup_method(self, method):
        # criar um objeto chamado "driver" e instanciá-lo como Selenium para o
        # browser Chrome, indicando onde está o seu chrome driver
        self.driver = webdriver.Chrome('drivers/chrome/94/chromedriver.exe')
        # timeout
        self.driver.implicitly_wait(3)
        # maximizar a janela do navegador.
        self.driver.maximize_window()
        # Declaramos um atributo da classe chamado "vars" e ele é uma lista
        # self.vars = {}

    # Como se divide um script em Selenium
    # 1 - Preparativos  -  Antes do Teste
    # 2 - Execução do teste - Durante
    # 3 - Encerramento -  Depois do Teste



    # Método de Finanlização do teste
    def teardown_method(self, method):
        #encerrar o objeto do Selenium WebDriver
        self.driver.quit()

    # Método de Teste - Consultar um Curso
    def test_consultar_curso(self):
        # o Selenium acessa o endereço do site alvo
        self.driver.get('https://www.iterasys.com.br')
        # Clicar na caixa de pesquisa
        # todo: verificar find_elements para vários elementos
        # self.driver.find_elements(By.ID, 'searchtext',2)
        self.driver.find_element(By.ID, 'searchtext').click()
        # Limpar a caixa de pesquisa antes de começar a escrever
        self.driver.find_element(By.ID, 'searchtext').clear()
        # Escreve "mantis" na caixa de pesquisa
        self.driver.find_element(By.ID, 'searchtext').send_keys('mantis')
        # Como seria dar um TAB a partir da caixa de texto
        # self.driver.find_element(By.ID, 'searchtext').send_keys(Keys.TAB)
        # Clicar na lupa
        self.driver.find_element(By.ID, 'btn_form_search').click()

        # Página 2
        # Clicar no botão Matricule-se
        self.driver.find_element(By.CSS_SELECTOR, 'span.comprar').click()

        # Página 3
        assert self.driver.find_element(By.CSS_SELECTOR, 'span.item-title').text == 'Mantis'
        assert(self.driver.find_element(By.CSS_SELECTOR, 'span.item-title').text, 'Mantis')

        assert self.driver.find_element(By.CSS_SELECTOR, 'span.new-price').text == 'R$ 59,99'
        assert(self.driver.find_element(By.CSS_SELECTOR, 'span.new-price').text, 'R$ 59,99')

