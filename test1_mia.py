from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_navigation_to_login():
    edge_service = Service('msedgedriver.exe')
    driver = webdriver.Edge(service=edge_service)
    driver.maximize_window()

    try:
        driver.get("https://mia1.knute.edu.ua/")

        # Клікнути саме на посилання "Авторизація" за текстом
        auth_dropdown = WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable(
                (By.XPATH, "//a[contains(@class, 'nav-link') and contains(@class, 'dropdown-toggle') and contains(text(), 'Авторизація')]")
            )
        )
        auth_dropdown.click()

        # Дочекатись появи "Увійти"
        login_link = WebDriverWait(driver, 5).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "div.dropdown-menu a.dropdown-item[href='/login']"))
        )
        login_link.click()

        # Перевірити, що URL змінився на /login
        WebDriverWait(driver, 5).until(EC.url_contains("/login"))

        print("Тест 1 пройшов: перехід на /login успішний.")
    except Exception as e:
        print(f"Тест 1 провалено: {e}")
    finally:
        driver.quit()

if __name__ == "__main__":
    test_navigation_to_login()
