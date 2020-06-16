from selenium.webdriver.common.by import By


class DashboardPage:

    def __init__(self, driver):

        self.driver = driver
        self.profile_card = driver.find_element(By.CSS_SELECTOR, "div[data-testid='profile_card_id']")
        self.use_cases_card = driver.find_element(By.CSS_SELECTOR, "div[data-testid='use_cases_card_id']")
        self.playground_card = driver.find_element(By.CSS_SELECTOR, "div[data-testid='playground_card_id']")
        self.reports_card = driver.find_element(By.CSS_SELECTOR, "div[data-testid='reports_card_id']")

    def get_profile_card_title(self):

        return self.profile_card.find_element_by_class_name("card-title").text.encode(encoding='utf-8')
