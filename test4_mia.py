from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_contact_form_email_validation():
    edge_service = Service('msedgedriver.exe')
    driver = webdriver.Edge(service=edge_service)
    driver.maximize_window()

    try:
        driver.get("https://mia1.knute.edu.ua/contact")

        # Заповнюємо поле ПІБ
        name_input = WebDriverWait(driver, 5).until(
            EC.visibility_of_element_located((By.ID, "contactform-name"))
        )
        name_input.clear()
        name_input.send_keys("Тест Тестов")

        # Вводимо некоректний email
        email_input = driver.find_element(By.ID, "contactform-email")
        email_input.clear()
        email_input.send_keys("invalid-email")

        # Заповнюємо тему
        subject_input = driver.find_element(By.ID, "contactform-subject")
        subject_input.clear()
        subject_input.send_keys("Тестова тема")

        # Заповнюємо текст повідомлення
        body_input = driver.find_element(By.ID, "contactform-body")
        body_input.clear()
        body_input.send_keys("Це тестове повідомлення.")

        # Натискаємо кнопку "Відправити"
        submit_button = driver.find_element(By.NAME, "contact-button")
        submit_button.click()

        # Чекаємо появу повідомлення про помилку валідації email (div.invalid-feedback всередині поля email)
        error_message = WebDriverWait(driver, 5).until(
            EC.visibility_of_element_located(
                (By.CSS_SELECTOR, "#contactform-email + div.invalid-feedback, #contactform-email ~ div.invalid-feedback")
            )
        )

        expected_error = 'Значення "Email" не є правильною email адресою.'
        actual_error = error_message.text.strip()

        if expected_error == actual_error:
            print("Тест 4 пройшов: повідомлення про некоректний email відображено.")
        else:
            print(f"Тест 4 провалено: очікувано '{expected_error}', а отримано '{actual_error}'")

    except Exception as e:
        print(f"Тест 4 провалено: {e}")
    finally:
        driver.quit()

if __name__ == "__main__":
    test_contact_form_email_validation()
