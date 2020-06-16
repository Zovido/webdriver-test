from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ExpectedConditions


class UseCasePage:

    def __init__(self, driver):

        self.driver = driver
        self.page_title = WebDriverWait(self.driver, 10).until(
            ExpectedConditions.visibility_of_element_located(
                (By.CLASS_NAME, "page-title"))
        ).text

        self.title = driver.find_element_by_name('title')
        self.description = driver.find_element_by_name('description')
        self.expected_result = driver.find_element_by_name('expected_result')
        self.add_step_btn = driver.find_element_by_class_name("addTestStep")
        self.submit_btn = driver.find_element_by_css_selector("button[data-testid='submit_btn']")
        self.return_to_dashboard_btn = driver.find_element_by_css_selector("a[href='/use-cases']")

    def set_title(self, input_value):
        self.title.send_keys(input_value)

    def get_title(self):

        return self.title.get_attribute("value")

    def edit_title(self, value):
        self.title.clear()
        self.title.send_keys(value)

    def set_description(self, input_value):
        self.description.send_keys(input_value)

    def get_description(self):
        return self.description.get_attribute("value")

    def edit_description(self, value):
        self.description.clear()
        self.description.send_keys(value)

    def set_expected_result(self, input_value):
        self.expected_result.send_keys(input_value)

    def get_expected_result(self):

        return self.expected_result.get_attribute("value")

    def edit_expected_result(self, value):
        self.expected_result.clear()
        self.expected_result.send_keys(value)

    def set_step_value(self, step_index, value):
        self.driver.find_element_by_name("testStepId-{}".format(step_index)).clear()
        self.driver.find_element_by_name("testStepId-{}".format(step_index)).send_keys(value)

    def get_step_value(self, step_index):

        return self.driver.find_element_by_name("testStepId-{}".format(step_index)).get_attribute("value")

    def set_steps(self, steps):

        for step_index in range(len(steps)):
            self.set_step_value(step_index, steps[step_index])
            if step_index < len(steps)-1:
                self.add_step_btn.click()

    def get_num_of_steps(self):

        return len(self.driver.find_elements_by_id('stepId'))

    def remove(self):
        if self.page_title == "Edit Use Case":
            self.driver.find_element_by_css_selector("button[data-testid='remove_usecase_btn']").click()
            self.driver.find_element_by_class_name("btn-danger").click()
        else:
            print "Nothing to remove"
