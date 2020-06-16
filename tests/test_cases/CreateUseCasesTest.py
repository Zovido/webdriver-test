import unittest
from selenium import webdriver
from pages.login.LoginPage import LoginPage
from pages.dashboard.DashboardPage import DashboardPage
from pages.usecases.UseCasesPage import UseCasesPage
from pages.usecase.UseCasePage import UseCasePage
from tests.tests_data.UseCaseMockData import UseCaseDataMock
from selenium.webdriver.support import expected_conditions as ExpectedConditions
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By


class CreateUseCasesTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.get("https://qa-sandbox.apps.htec.rs/dashboard")
        loginFromContainer = self.driver.find_element_by_class_name('btn-secondary')
        loginFromContainer.click()
        WebDriverWait(self.driver, 10).until(
            ExpectedConditions.visibility_of_element_located((By.CSS_SELECTOR, "button[data-testid='submit_btn']"))
        )
        loginPage = LoginPage(self.driver)
        loginPage.enter_login_credentials("stancicmilan06@gmail.com", "lINKINpARK06")
        loginPage.submitButton.click()

    def testCreateUseCases(self):
        WebDriverWait(self.driver, 10).until(
            ExpectedConditions.visibility_of_element_located((By.CSS_SELECTOR, "div[data-testid='use_cases_card_id']"))
        )
        dashboard_page = DashboardPage(self.driver)
        dashboard_page.use_cases_card.click()

        mock_data = UseCaseDataMock()

        for test_case_index in range(len(mock_data.all_use_cases)):
            #ovo ili je nepotrebno ili trerba izmeniti da gadja stranicu
            WebDriverWait(self.driver, 10).until(
                ExpectedConditions.visibility_of_element_located(
                    (By.CSS_SELECTOR, "a[data-testid='create_use_case_btn']"))
            )
            use_cases_page = UseCasesPage(self.driver)
            use_cases_page.create_use_case_btn.click()

            data = mock_data.all_use_cases[test_case_index]

            self.create_new_use_case(data)

            use_cases_page = UseCasesPage(self.driver)
            saved_use_case = use_cases_page.get_first_use_case()

            self.assertEqual(data.title, saved_use_case.get_title())
            self.assertEqual(data.description, saved_use_case.get_description())
            self.assertEqual(data.expected_result, saved_use_case.get_expected_result())
            self.assertEqual(len(data.steps), saved_use_case.get_num_of_steps())

            for step_index in range(len(data.steps)):
                self.assertEqual(data.steps[step_index], saved_use_case.get_step_value(step_index))

            saved_use_case.return_to_dashboard_btn.click()

    def create_new_use_case(self, mock_data):

        new_use_case = UseCasePage(self.driver)
        new_use_case.set_title(mock_data.title)
        new_use_case.set_description(mock_data.description)
        new_use_case.set_expected_result(mock_data.expected_result)
        new_use_case.set_steps(mock_data.steps)
        new_use_case.submit_btn.click()

    def tearDown(self):
        # close the browser window
        self.driver.quit()