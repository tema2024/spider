import time
import csv
from selenium import webdriver
from selenium.webdriver.common.by import By

# Настройка веб-драйвера
driver = webdriver.Chrome()

# URL для парсинга
url = 'https://www.divan.ru/category/krovati-i-matrasy'

# Переход на страницу
driver.get(url)

# Ожидание загрузки страницы
time.sleep(3)

# Найдите контейнеры кроватей
beds = driver.find_elements(By.CLASS_NAME, 'WdR1o')

# Проверка, что элементы найдены
print(f'Найдено кроватей: {len(beds)}')

parsed_data = []

for bed in beds:
    try:
        # Найдите элементы внутри контейнера
        name = bed.find_element(By.CSS_SELECTOR, 'span[itemprop="name"]').text
        price = bed.find_element(By.CSS_SELECTOR, 'span.ui-LD-ZU').text
        link = bed.find_element(By.CSS_SELECTOR, 'link[itemprop="url"]').get_attribute('href')
        parsed_data.append([name, price, link])
    except Exception as e:
        print(f'Произошла ошибка при парсинге: {e}')
        continue

# Закрытие веб-драйвера
driver.quit()

# Сохранение данных в CSV файл
with open("beds.csv", mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['Название кровати', 'Цена', 'Ссылка на кровать'])
    writer.writerows(parsed_data)

print(f'Данные сохранены в файл beds.csv')







