from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException


from django.contrib.auth import authenticate

browser = webdriver.Firefox()

# Probably a very bad practice, but I don't know how else to do it
# Login in through admin, because site does not have another way to login
browser.get('http://127.0.0.1:8000/admin')
username_element = browser.find_element_by_name("username")
username_element.send_keys("robert")
password_element = browser.find_element_by_name("password")
password_element.send_keys("Landknecht222")
password_element.send_keys(Keys.RETURN)

# Find out if the elements we want are there
try:
    header_element = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.ID, "header"))
    )

    user_tools_element = WebDriverWait(browser, 20).until(
        EC.presence_of_element_located((By.ID, "user-tools"))
    )
except TimeoutException:
    print("No element found")

# I don't trust the first test, so here's another one
user_tools_is_present = False
try:
    user_tools_element = browser.find_element_by_id("user-tools")
    assert 2 + 2 is not 5 # Just for reference, to make sure that I know how to use assert
    user_tools_is_present = True
except NoSuchElementException:
    print("It can't see it, but why?")
except AssertionError:
    print("Nope")
finally:
    print("User tools found: ")
    print(user_tools_is_present)

# NOW we can get to business -  that is if the second test passed
# Click on view site because otherwise I can't access the site with admin priviliges 
if user_tools_is_present:
    user_tools_element = browser.find_element_by_id("user-tools")
    try:
        view_element = user_tools_element.find_element_by_tag_name('a')
        ActionChains(browser).move_to_element(view_element).click().perform()
    except NoSuchElementException:
        print("WHY DOES IT NOT SEE IT?!??!?!?!")

# Alright, we are in. With admin priviliges, we can test to see if the main features of the site actually work
try:
    # Does the tab title have these expected words
    tab_title_correct = WebDriverWait(browser, 10).until(
        EC.title_contains("Robert")
    )
    assert "Robert" in browser.title

    # Can I enter the posts?
    test_post_title_present = WebDriverWait(browser, 10).until(
        EC.visibility_of_element_located((By.LINK_TEXT, "Test"))
    )
    browser.find_element_by_link_text('Test').click()

    # Can I go back to the homepage if I went into a post?
    blog_title_present = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.PARTIAL_LINK_TEXT, "Robert"))
    )
    browser.find_element_by_link_text("Robert's Blog").click()

    # Can I write posts? 
    create_button_present = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.PARTIAL_LINK_TEXT, "Create"))
    )
    browser.find_element_by_partial_link_text('Create').click()

    post_title_field_present = WebDriverWait(browser, 10).until(
        EC.visibility_of_element_located((By.ID, "id_title"))
    )
    post_title_field_element = browser.find_element_by_id("id_title")
    post_title_field_element.send_keys("Repost ad nauseam")

    post_text_field_present = WebDriverWait(browser, 10).until(
        EC.visibility_of_element_located((By.ID, "id_text"))
    )
    post_text_field_element = browser.find_element_by_id("id_text")
    post_text_field_element.send_keys("This text shall appear in all the test posts. Soory for repost :P")

    post_button_present = WebDriverWait(browser, 10).until(
        EC.visibility_of_element_located((By.TAG_NAME, 'button'))
    )
    post_button_element = browser.find_element_by_tag_name('button')
    ActionChains(browser).move_to_element(post_button_element).click().perform()

    blog_title_present_2 = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.PARTIAL_LINK_TEXT, "Robert"))
    )
    browser.find_element_by_link_text("Robert's Blog").click()
    
    # Can I edit posts?
    repost_title_present = WebDriverWait(browser, 10).until(
        EC.visibility_of_element_located((By.PARTIAL_LINK_TEXT, "Repost"))
    )
    browser.find_element_by_partial_link_text('Repost').click()

    edit_button_present = WebDriverWait(browser, 10).until(
        EC.visibility_of_element_located((By.PARTIAL_LINK_TEXT, "Edit"))
    )
    browser.find_element_by_partial_link_text("Edit").click()

    repost_title_field_present = WebDriverWait(browser, 10).until(
        EC.visibility_of_element_located((By.ID, "id_title"))
    )
    repost_title_field_element = browser.find_element_by_id("id_title")
    repost_title_field_element.clear()
    repost_title_field_element.send_keys("Edited ad nauseam")

    repost_text_field_present = WebDriverWait(browser, 10).until(
        EC.visibility_of_element_located((By.ID, "id_text"))
    )
    repost_text_field_element = browser.find_element_by_id("id_text")
    repost_text_field_element.clear()
    repost_text_field_element.send_keys(
        "This text shall appear in all the test posts. Sorry for repost :P \n Edit: a word"
    )
    save_button_present = WebDriverWait(browser, 10).until(
        EC.visibility_of_element_located((By.TAG_NAME, 'button'))
    )
    save_button_element = browser.find_element_by_tag_name('button')
    ActionChains(browser).move_to_element(save_button_element).click().perform()

    edit_button_present_2 = WebDriverWait(browser, 10).until(
        EC.visibility_of_element_located((By.PARTIAL_LINK_TEXT, "Edit"))
    )
    blog_title_present_3 = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.PARTIAL_LINK_TEXT, "Robert"))
    )
    browser.find_element_by_link_text("Robert's Blog").click()
    
    # Alright, I admit my code has been rather "wet" - I repeated the same WebDriverWait a lot
    # However, I don't want to risk it. I want to make sure that elemenent is there before selenium uses it
    # Selenium works way too fast in order for me to observe what is going on
    # It's not a great way of doing it, but too bad!

    # Can I go back to the homepage if I am writing/editing a post?
    create_button_present_2 = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.PARTIAL_LINK_TEXT, "Create"))
    )
    browser.find_element_by_partial_link_text('Create').click()

    blog_title_present_4 = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.PARTIAL_LINK_TEXT, "Robert"))
    )
    browser.find_element_by_link_text("Robert's Blog").click()

    test_post_title_present_2 = WebDriverWait(browser, 10).until(
        EC.visibility_of_element_located((By.LINK_TEXT, "Test"))
    )
    browser.find_element_by_link_text("Test").click()

    edit_button_present_3 = WebDriverWait(browser, 10).until(
        EC.visibility_of_element_located((By.PARTIAL_LINK_TEXT, "Edit"))
    )
    browser.find_element_by_partial_link_text("Edit").click()

    save_button_present_2 = WebDriverWait(browser, 10).until(
        EC.visibility_of_element_located((By.TAG_NAME, 'button'))
    )
    blog_title_present_5 = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.PARTIAL_LINK_TEXT, "Robert"))
    )
    browser.find_element_by_link_text("Robert's Blog").click()

    # Can I access the CV view?
    cv_link_present = WebDriverWait(browser, 10).until(
        EC.visibility_of_element_located((By.LINK_TEXT, "CV"))
    )
    browser.find_element_by_link_text("CV").click()

    # Can I edit the CV form?

    # If no AssertionError has been raised, show this
    print("All functional tests succesfully completed!", end="\n")
except AssertionError:
    print("One or more of the tests failed!", end="\n")
except TimeoutException:
    print("Either a test failed, or you fucked up stellarly!", end="\n")
except Exception:
    print("You may have fucked up one of your tests, so go rewrite it you dingus!", end="\n")
finally:
    browser.quit()

