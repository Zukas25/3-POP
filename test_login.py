import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By

class TestLoginLogout(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()  # Użyj odpowiedniego sterownika
        self.driver.get("https://www.edu.goit.global/account/login")

    def tearDown(self):
        self.driver.quit()

    def test_login_logout_case1(self):
        driver = self.driver
        # Wprowadź dane logowania
        email_field = driver.find_element(By.ID, "email")  # Zaktualizuj selektor, jeśli potrzebne
        email_field.send_keys("użytkownik888@gmail.com")
        password_field = driver.find_element(By.ID, "password")  # Zaktualizuj selektor, jeśli potrzebne
        password_field.send_keys("1234567890")
        login_button = driver.find_element(By.ID, "loginButton")  # Zaktualizuj selektor, jeśli potrzebne
        login_button.click()

        # Sprawdź, czy użytkownik jest zalogowany
        menu_button = driver.find_element(By.ID, "menuButton")  # Zaktualizuj selektor, jeśli potrzebne
        menu_button.click()
        logout_button = driver.find_element(By.ID, "logoutButton")  # Zaktualizuj selektor, jeśli potrzebne
        logout_button.click()

        # Sprawdź, czy użytkownik wrócił na stronę logowania
        self.assertIn("https://www.edu.goit.global/account/login", driver.current_url)

    def test_login_logout_case2(self):
        driver = self.driver
        # Wprowadź dane logowania
        email_field = driver.find_element(By.ID, "email")  # Zaktualizuj selektor, jeśli potrzebne
        email_field.send_keys("testoweqa@qa.team")
        password_field = driver.find_element(By.ID, "password")  # Zaktualizuj selektor, jeśli potrzebne
        password_field.send_keys("QA!")
        login_button = driver.find_element(By.ID, "loginButton")  # Zaktualizuj selektor, jeśli potrzebne
        login_button.click()

        # Sprawdź, czy użytkownik jest zalogowany
        menu_button = driver.find_element(By.ID, "menuButton")  # Zaktualizuj selektor, jeśli potrzebne
        menu_button.click()
        logout_button = driver.find_element(By.ID, "logoutButton")  # Zaktualizuj selektor, jeśli potrzebne
        logout_button.click()

        # Sprawdź, czy użytkownik wrócił na stronę logowania
        self.assertIn("https://www.edu.goit.global/account/login", driver.current_url)

if __name__ == "__main__":
    unittest.main()

