import vimeo
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException


client = vimeo.VimeoClient(
    token='5ccfb477120f75f1d6e340488bc9821b',
    key='311a3529ba7c90ffcd62c60e17990a51ac82f25d',
    secret='BXLOjy/V91SwDJkn0ZFDMyJZG0RCQSasu6LzI3hjBQ5+lh11+HDEw9YXJloLvJJ4wCY4kXN2Edn+0EAqWFORBsCciozreg4/tTyuWXwGw8A87GjC7hEJ2N6qFUdiGAJc'
)

# 1 - Log in to vimeo API
response = client.get('/')
print(response.json())

# 2 - Comment on video
comment = client.post('https://api.vimeo.com/videos/746610211/comments', data={"text": "Nice"})
print(comment.json())

# 3 - WebUI
usernameStr = 'spotidas@gmail.com'
passwordStr = 'Aniview0922!'
browser = webdriver.Chrome()
browser.maximize_window()
browser.get('https://vimeo.com/')
try:
    logInButton = browser.find_element(By.XPATH, '//*[@id="__next"]/div[1]/header/div/div[2]/div/div[2]/div/div[1]/button[1]')
    logInButton.click()
    username = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.ID, 'login_email')))
    username.send_keys(usernameStr)
    username = browser.find_element(By.ID, 'password')
    username.send_keys(passwordStr)
    logInModalButton = browser.find_element(By.XPATH, '//*[@id="modal-root"]/div[2]/div[2]/form[1]/button')
    logInModalButton.click()

    whatsNewX = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="wrap"]/div[2]/main/div/div/div[1]/div[1]/div/div[2]/div/div[2]/div[2]/div/div[2]/button')))
    whatsNewX.click()

except NoSuchElementException:
    print("Exception Handled - Element not found")

# 4 - Navigate to video
browser.get('https://api.vimeo.com/videos/746610211')

# 5 - Find comment
commentId = (comment.json())['link']
print(commentId)
commentId = (commentId.split('#')[-1]).strip()
print(commentId)
print(type(commentId))
comment_url = 'https://api.vimeo.com/videos/746610211/comments/'+commentId
print(comment_url)
browser.get(comment_url)
