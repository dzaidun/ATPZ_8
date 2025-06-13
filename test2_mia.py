from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_invalid_login():
    edge_service = Service('msedgedriver.exe')
    driver = webdriver.Edge(service=edge_service)
    driver.maximize_window()

    try:
        driver.get("https://mia1.knute.edu.ua/login")

        # Вводимо неправильний логін
        username_input = WebDriverWait(driver, 5).until(
            EC.visibility_of_element_located((By.NAME, "LoginForm[username]"))
        )
        username_input.clear()
        username_input.send_keys("wronguser")

        # Вводимо неправильний пароль
        password_input = driver.find_element(By.NAME, "LoginForm[password]")
        password_input.clear()
        password_input.send_keys("wrongpassword")

        # Натискаємо кнопку входу
        submit_button = driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
        submit_button.click()

        # Очікуємо появу сторінки з помилкою сервера (перевіряємо текст у <p> з класом text-danger)
        error_header = WebDriverWait(driver, 5).until(
            EC.visibility_of_element_located(
                (By.CSS_SELECTOR, "p.text-danger")
            )
        )

        error_text = error_header.text.strip()
        expected_error = "Виникла внутрішня помилка сервера."

        if error_text == expected_error:
            print("Тест 2 пройшов: помилка сервера відображена правильно.")
        else:
            print(f"Тест 2 провалено: очікувано '{expected_error}', а отримано '{error_text}'")
    except Exception as e:
        print(f"Тест 2 провалено: {e}")
    finally:
        driver.quit()

if __name__ == "__main__":
    test_invalid_login()
