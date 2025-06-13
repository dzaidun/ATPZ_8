from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def test_google_play_link_opens_new_tab():
    edge_service = Service('msedgedriver.exe')
    driver = webdriver.Edge(service=edge_service)
    driver.maximize_window()

    try:
        driver.get("https://mia1.knute.edu.ua/")

        # Знаходимо посилання на Google Play за href
        google_play_link = WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable(
                (By.CSS_SELECTOR, 'a[href="https://play.google.com/store/apps/details?id=com.mkr.shedule_app"]')
            )
        )

        # Запам’ятовуємо поточні вкладки
        original_windows = driver.window_handles

        # Клікаємо по посиланню (відкривається в новій вкладці через target="_blank")
        google_play_link.click()

        # Чекаємо поки з’явиться нова вкладка
        WebDriverWait(driver, 5).until(
            lambda d: len(d.window_handles) > len(original_windows)
        )

        # Перемикаємося на нову вкладку
        new_window = [w for w in driver.window_handles if w not in original_windows][0]
        driver.switch_to.window(new_window)

        # Чекаємо завантаження URL у новій вкладці
        WebDriverWait(driver, 10).until(
            EC.url_contains("play.google.com/store/apps/details?id=com.mkr.shedule_app")
        )

        current_url = driver.current_url
        if "play.google.com/store/apps/details?id=com.mkr.shedule_app" in current_url:
            print("Тест 5 пройшов: посилання відкриває правильну сторінку Google Play.")
        else:
            print(f"Тест 5 провалено: відкрито неправильну URL: {current_url}")

    except Exception as e:
        print(f"Тест 5 провалено: {e}")
    finally:
        driver.quit()

if __name__ == "__main__":
    test_google_play_link_opens_new_tab()
