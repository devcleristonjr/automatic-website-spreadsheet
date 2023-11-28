from selenium import webdriver
from selenium.webdriver.common.by import By
import openpyxl
import time

# acessar o site
driver = webdriver.Edge()
driver.get(
    "https://www.amazon.com.br/gp/browse.html?node=17351089011&ref_=nav_em__pc_gamer_0_2_17_5"
)

#pausa pra pensar

time.sleep(5)

# extrair todos os títulos
titulos = driver.find_elements(
    By.XPATH, "(//span[@class='a-size-base-plus a-color-base a-text-normal'])"
)
# extrair todos os preços
precos = driver.find_elements(By.XPATH, "(//span[@class='a-price-whole'])")

# Criando a planilha
workbook = openpyxl.Workbook()
# Criando a página 'produtos'
workbook.create_sheet("produtos")
# Seleciono a página produtos
sheet_produtos = workbook["produtos"]
sheet_produtos["A1"].value = "Produto"
sheet_produtos["B1"].value = "Preço"


# inserir os títulos e preços na planilha
for titulo, preco in zip(titulos, precos):
    sheet_produtos.append([titulo.text, preco.text])

workbook.save("produtos.xlsx")
