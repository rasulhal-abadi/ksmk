from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

edge_driver_path = "C:\\Users\\3bse\\Desktop\\al-zahraa\\MicrosoftEdgeSetup.exe"

# إعداد متصفح Microsoft Edge
edge_options = webdriver.EdgeOptions()
edge_options.use_chromium = True  # لضمان استخدام محرك Chromium

driver = webdriver.Edge(options=edge_options)

# فتح موقع ويب
driver.get('https://www.instagram.com/')

WebDriverWait(driver, 20).until(EC.title_contains("Instagram"))

# انتظر حتى يتم العثور على حقل اسم المستخدم
username_field = WebDriverWait(driver, 20).until(
    EC.presence_of_element_located((By.XPATH, '//input[@name="username"]'))
)

# أدخل اسم المستخدم
username_field.send_keys("x.qes")

# انتظر حتى يتم العثور على حقل كلمة المرور
password_field = WebDriverWait(driver, 20).until(
    EC.presence_of_element_located((By.XPATH, '//input[@name="password"]'))
)

# أدخل كلمة المرور
password_field.send_keys("1122334455saba")
login_button = WebDriverWait(driver, 20).until(
    EC.element_to_be_clickable((By.XPATH, "//button[contains(.,'Log in')]"))
)

# إزالة خاصية disabled
driver.execute_script("arguments[0].removeAttribute('disabled')", login_button)

# النقر على الزر بعد إزالة الخاصية
login_button.click()

save_button = WebDriverWait(driver, 20).until(
    EC.presence_of_element_located((By.XPATH, '//button[text()="Save Info"]'))
)

# انقر على زر "Save Info"
save_button.click()

not_now_button = WebDriverWait(driver, 20).until(
    EC.presence_of_element_located((By.XPATH, '//button[text()="Not Now"]'))
)
not_now_button.click()
# انتظر حتى يظهر العنصر الذي سنستخدمه للبحث
search_element = WebDriverWait(driver, 20).until(
    EC.presence_of_element_located((By.XPATH, '//span[contains(@class, "x1lliihq") and contains(text(), "Search")]'))
)

# النقر على عنصر البحث
# استخدم JavaScript لتنفيذ النقر على العنصر
driver.execute_script("arguments[0].click();", search_element)


search_field = WebDriverWait(driver, 20).until(
    EC.presence_of_element_located((By.XPATH, '//input[@aria-label="Search input"]'))
)

search_text = "g5rce"
search_field.send_keys(search_text)
search_field.send_keys(Keys.RETURN)
driver.execute_script("arguments[0].click();", search_field)

span_element = WebDriverWait(driver, 20).until(
    EC.presence_of_element_located((By.XPATH, f'//span[text()="{search_text}"]'))
)

# نفّذ النقر على العنصر
span_element.click()

follow_button = WebDriverWait(driver, 20).until(
    EC.presence_of_element_located((By.XPATH, '//button[contains(@class, "_acan") and contains(@class, "_acap")]'))
)

# نفّذ النقر على الزر
follow_button.click()


while True:
    try:
        # يمكنك إجراء أي عمليات إضافية هنا أثناء تشغيل المتصفح
        time.sleep(10)  # تأخير لبضع ثواني
    except KeyboardInterrupt:
        print("تم الضغط على Ctrl+C. إغلاق المتصفح.")
        break


driver.quit()

