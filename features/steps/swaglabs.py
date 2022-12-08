from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep


@given('I launch Chrome browser')
def step_impl(context):
    context.driver = webdriver.Chrome()


@when('I open SWAGLABS Homepage')
def step_impl(context):
    context.driver.get("https://www.saucedemo.com/")
    context.driver.maximize_window()

@when('User click on logout')
def step_impl(context):
    context.driver.find_element(By.ID, "react-burger-menu-btn").click()
    sleep(1)
    context.driver.find_element(By.ID, "logout_sidebar_link").click()
    sleep(1)

@then('user must be successully logout')
def step_impl(context):
    is_present = context.driver.find_element(By.ID, "login_button_container").is_displayed()
    sleep(1)
    assert is_present is True

@then('login form must be available')
def step_impl(context):
    is_present = context.driver.find_element(By.ID, "login_button_container").is_displayed()
    sleep(1)
    assert is_present is True

@given('Enter username "{name}" and password "{password}"')
def step_impl(context, name, password):

    if name == 'empty':
        name = ''

    if password == 'empty':
        password = ''
    context.driver.find_element(By.ID, "user-name").send_keys(name)
    sleep(1)
    context.driver.find_element(By.ID, "password").send_keys(password)
    sleep(1)


@given('Click on login button')
def step_impl(context):
    context.driver.find_element(By.ID, "login-button").click()
    sleep(1)

@then('close the bowser')
def step_impl(context):
    context.driver.quit()
    sleep(1)


# @then('Enter "{FirstName}","{LastName}" And "{PostalCode}"')
# def step_impl(context, FirstName, LastName, PostalCode):
#     for row in


@then('Adding all carts')
def step_impl(context):
    context.driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()
    sleep(1)
    context.driver.find_element(By.ID, "add-to-cart-sauce-labs-bike-light").click()
    sleep(1)
    context.driver.find_element(By.ID, "add-to-cart-sauce-labs-bolt-t-shirt").click()
    sleep(1)
    context.driver.find_element(By.ID, "add-to-cart-sauce-labs-fleece-jacket").click()
    sleep(1)
    context.driver.find_element(By.ID, "add-to-cart-sauce-labs-onesie").click()
    sleep(1)
    context.driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
    sleep(1)
    context.driver.find_element(By.ID, "checkout").click()
    sleep(1)


@then('shoping cart')
def step_impl(context):
    context.driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
    sleep(1)


@then('Checkout')
def step_impl(context):
    context.driver.find_element(By.ID, "checkout").click()
    sleep(1)

@then(u'Enter "{First}","{Last}" And "{Postal}"')
def step_impl(context, First, Last, Postal):
    if First == 'empty':
        First = ''
    if Last == 'empty':
        Last = ''
    if Postal == 'empty':
        Postal = ''
    context.driver.find_element(By.ID, "first-name").send_keys(First)
    sleep(2)
    context.driver.find_element(By.ID, "last-name").send_keys(Last)
    sleep(2)
    context.driver.find_element(By.ID, "postal-code").send_keys(Postal)
    sleep(2)



@then('click on Continue')
def step_impl(context):
    context.driver.find_element(By.ID, "continue").click()
    sleep(1)

@then('refresh browser')
def step_impl(context):
    context.driver.refresh()
    sleep(1)

@then('set of specific users')
def step_impl(context):
    for row in context.table:
        sleep(2)
        fname = row['FirstName']
        lname = row['LastName']
        code = row['PostalCode']

        context.execute_steps(f'''
        When Enter "{fname}","{lname}" And "{code}"
        Then click on Continue
        And refresh browser
         ''')


@then('User must succesfully login to Dashboard page')
def step_impl(context):
    pass_cass = False
    try:
        x = context.driver.find_element(By.ID, "inventory_container")
        pass_cass = True
    except:
        pass

    assert pass_cass

@then('User must not succesfully login to Dashboard page')
def step_impl(context):
    pass_cass = True
    try:
        x = context.driver.find_element(By.ID, "inventory_container")
        pass_cass = False
    except:
        pass

    assert pass_cass





