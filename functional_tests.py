from selenium import webdriver

browser = webdriver.Firefox()
browser.get('http://127.0.0.1:8000')

#HOW DAFUQ DO I WROIT TESTS I R DOM B HELP FBIWPNFO!!!!!!!
try:
    # Does the tab title have these expected words
    assert 'Robert' in browser.title

    # Can I enter the posts?
    browser.find_element_by_link_text('Test').click()

    # Can I go back to the homepage if I went into a post?
    browser.find_element_by_link_text("Robert's Blog").click()

    # Can I write posts? Can't, you're not logged in

    # Can I edit posts? Can't, you're not logged in   

    # Can I go back to the homepage if I am writing/editing a post? You can't even edit/write posts

    # Can I access the CV view?

    # Can I edit the CV form?

    # If no AssertionError has been raised, show this
    print("All functional tests succesfully completed!", end="\n")
except AssertionError:
    print("One or more of the tests failed!", end="\n")
except Exception:
    print("You may have fucked up one of your tests, so go rewrite it you dingus!", end="\n")
finally:
    browser.quit()