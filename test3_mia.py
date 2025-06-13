from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_navigation_to_contact():
    edge_service = Service('msedgedriver.exe')
    driver = webdriver.Edge(service=edge_service)
    driver.maximize_window()

    try:
        driver.get("https://mia1.knute.edu.ua/")

        # Знаходимо посилання "Зворотній зв'язок" за href і текстом (щоб бути точними)
        contact_link = WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable(
                (By.XPATH, "//a[@href='/contact' and contains(., \"Зворотній зв'язок\")]")
            )
        )
        contact_link.click()

        # Чекаємо, що URL містить "/contact"
        WebDriverWait(driver, 5).until(EC.url_contains("/contact"))

        print("Тест 3 пройшов: перехід на сторінку зворотного зв’язку успішний.")
    except Exception as e:
        print(f"Тест 3 провалено: {e}")
    finally:
        driver.quit()

if __name__ == "__main__":
    test_navigation_to_contact()
