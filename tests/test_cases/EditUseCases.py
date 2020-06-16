import unittest
from selenium import webdriver
from pages.login.LoginPage import LoginPage
from pages.dashboard.DashboardPage import DashboardPage
from pages.usecases.UseCasesPage import UseCasesPage
from tests.tests_data.UseCaseMockData import UseCaseDataMock
from selenium.webdriver.support import expected_conditions as ExpectedConditions
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By


class EditUseCasesTest(unittest.TestCase):

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

            data = mock_data.all_use_cases[test_case_index]
            use_cases_page = UseCasesPage(self.driver)
            use_case_by_title = use_cases_page.get_use_case(data.title)

            expected_value = "This field previously had {} characters"
            self.edit_use_case(use_case_by_title, expected_value)

            use_cases_page = UseCasesPage(self.driver)
            edited_use_case = use_cases_page.get_use_case(expected_value.format(len(data.title)))

            self.assertEqual(expected_value.format(len(data.title)), edited_use_case.get_title())
            self.assertEqual(expected_value.format(len(data.description)), edited_use_case.get_description())
            self.assertEqual(expected_value.format(len(data.expected_result)), edited_use_case.get_expected_result())
            self.assertEqual(len(data.steps), edited_use_case.get_num_of_steps())

            for step_index in range(len(data.steps)):
                self.assertEqual(expected_value.format(len(data.steps[step_index])), edited_use_case.get_step_value(step_index))

            edited_use_case.return_to_dashboard_btn.click()

    def edit_use_case(self, use_case, new_value):

        new_title = new_value.format(len(use_case.get_title()))
        new_description = new_value.format(len(use_case.get_description()))
        new_expected_result = new_value.format(len(use_case.get_expected_result()))
        use_case.edit_title(new_title)
        use_case.edit_description(new_description)
        use_case.edit_expected_result(new_expected_result)
        for step_index in range(use_case.get_num_of_steps()):
            step_value_length = len(use_case.get_step_value(step_index))
            use_case.set_step_value(step_index, new_value.format(step_value_length))
        use_case.submit_btn.click()

    def tearDown(self):
        # close the browser window
        self.driver.quit()