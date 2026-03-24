from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# -------- POSITIVE TEST --------
def positive_login():
    driver = webdriver.Chrome()
    wait = WebDriverWait(driver, 10)

    driver.get("https://the-internet.herokuapp.com/login")

    username = wait.until(
        EC.visibility_of_element_located((By.ID, "username"))
    )
    username.send_keys("tomsmith")

    password = driver.find_element(By.ID, "password")
    password.send_keys("SuperSecretPassword!")

    login = driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
    login.click()

    message = wait.until(
        EC.visibility_of_element_located((By.ID, "flash"))
    ).text

    print("Positive message:", message)

    assert "secure area" in message.lower()
    print("✅ Positive Login Test Passed")

    driver.quit()


# -------- NEGATIVE TEST --------
def negative_login():
    driver = webdriver.Chrome()
    wait = WebDriverWait(driver, 10)

    driver.get("https://the-internet.herokuapp.com/login")

    username = wait.until(
        EC.visibility_of_element_located((By.ID, "username"))
    )
    username.send_keys("wronguser")

    password = driver.find_element(By.ID, "password")
    password.send_keys("wrongpass")

    login = driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
    login.click()

    message = wait.until(
        EC.visibility_of_element_located((By.ID, "flash"))
    ).text

    print("Negative message:", message)

    assert "invalid" in message.lower()
    print("✅ Negative Login Test Passed")

    driver.quit()


# -------- RUN TESTS --------
positive_login()
negative_login()