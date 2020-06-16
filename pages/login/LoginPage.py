from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ExpectedConditions

class LoginPage:

    def __init__(self, driver):

        self.driver = driver
        self.submitButton = WebDriverWait(self.driver, 10).until(
            ExpectedConditions.visibility_of_element_located((By.CSS_SELECTOR, "button[data-testid='submit_btn']"))
        )
        self.usernameInputField = driver.find_element_by_name('email')
        self.passwordInputField = driver.find_element_by_name('password')

    def enter_login_credentials(self, username, password):

        self.usernameInputField.send_keys(username)
        self.passwordInputField.send_keys(password)

    def clear_inputs(self):

        self.usernameInputField.clear()
        self.passwordInputField.clear()

    def get_email_validation(self, expected_validation):

        # find expected validation
        WebDriverWait(self.driver, 10).until(
            ExpectedConditions.visibility_of_element_located((By.XPATH, "//*[text()='{}']".format(expected_validation)))
        )
        # return validation under email field
        return self.usernameInputField.find_element_by_xpath("./following-sibling::div").text

    def get_password_validation(self, expected_validation):

        # find expected validation
        WebDriverWait(self.driver, 10).until(
            ExpectedConditions.visibility_of_element_located((By.XPATH, "//*[text()='{}']".format(expected_validation)))
        )
        # return validation under password field
        return self.passwordInputField.find_element_by_xpath("./following-sibling::div").text

