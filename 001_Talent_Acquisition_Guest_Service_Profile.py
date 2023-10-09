import time
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

#------------------------------------------------------------------------------------
# Talent Acquisition - Guest Service Profile   (Tokens: 1) ------ RUN ON CHROME BROWSER
#------------------------------------------------------------------------------------

# Setting chrome driver object
driver = Chrome()
# launching the application URL
driver.get("https://www.fadvassessments.com/onlinetesting/gamma.html")

# Set account ID ----------- WebDriverWait ---------------->>
WebDriverWait(driver,20).until(EC.element_to_be_clickable((By.XPATH,"//input[@name='ID']"))).send_keys('QATEST')
# Set UserName
driver.find_element(By.XPATH,"//input[@name='username']").send_keys('administrator')
# Set Password
driver.find_element(By.XPATH,"//input[@name='password']").send_keys('Sk1llCheck!')
# Click Enter link
driver.find_element(By.XPATH,"//input[@value='Login']").click()

# Click Administer Testing link ----------- WebDriverWait ---------------->>
WebDriverWait(driver,20).until(EC.element_to_be_clickable((By.LINK_TEXT,"Administer Testing"))).click()
# driver.find_element(By.LINK_TEXT,"Administer Testing").click()
# Click Administer Tests link
driver.find_element(By.LINK_TEXT,"Administer Tests").click()

# select the test - Talent Acquisition - Guest Service Profile   (Tokens: 1) ---- WebDriverWait--------->>
WebDriverWait(driver,20).until(EC.element_to_be_clickable((By.XPATH,"//*[@id='all_tests']/option[1617]"))).click()
# driver.find_element(By.XPATH,"//*[@id='all_tests']/option[1617]").click()

# Click Add button
driver.find_element(By.XPATH,"//input[@name='add']").click()
# Click begin test button
driver.find_element(By.XPATH,"//input[@name='test']").click() #;time.sleep(7)
# feed first name ---- WebDriverWait--------->>
WebDriverWait(driver,20).until(EC.element_to_be_clickable((By.XPATH,"//input[@name='txtFirstName']"))).send_keys("Ganesan")

# driver.find_element(By.XPATH,"//input[@name='txtFirstName']").send_keys("Ganesan");time.sleep(2)
# feed last name
driver.find_element(By.XPATH,"//input[@id='txtLastName']").send_keys("Sivaraman") #;time.sleep(2)
# feed Email ID
driver.find_element(By.XPATH,"//input[@id='txtEmail']").send_keys("ganesan@symphonytalent.com") #;time.sleep(2)

gender = Select(driver.find_element(By.XPATH,'//*[@id="demo_gender"]'))
gender.select_by_value("Male") # select Male

age = Select(driver.find_element(By.XPATH,'//*[@id="demo_age"]'))
age.select_by_value("Under 40") # select under 10

age = Select(driver.find_element(By.XPATH,'//*[@id="demo_ethnicity"]'))
age.select_by_value("Prefer not to answer") # Prefered not to answer

driver.find_element(By.XPATH,"//*[@id='btnCompleteReg']").click()

# for start button --- WebDriverWait--------->>
WebDriverWait(driver,20).until(EC.element_to_be_clickable((By.XPATH,"//*[@id='btnBeginTest']"))).click()

# driver.find_element(By.XPATH,"//*[@id='btnBeginTest']").click();time.sleep(8)

# for first radio button and Answer Complete Button --- WebDriverWait--------->>
WebDriverWait(driver,20).until(EC.element_to_be_clickable((By.XPATH,"//*[@id='options_btn0']"))).click()

#driver.find_element(By.XPATH,"//*[@id='options_btn0']").click() # first radio button
driver.find_element(By.XPATH,"//*[@id='btnAnswerComplete']").click();time.sleep(8)

# for second radio button and Answer Complete Button --- WebDriverWait--------->>
WebDriverWait(driver,20).until(EC.element_to_be_clickable((By.XPATH,"//*[@id='button2']"))).click()
#driver.find_element(By.XPATH,"//*[@id='options_btn0']").click();time.sleep(5) # Second radio button
driver.find_element(By.XPATH,'//*[@id="btnAnswerComplete"]').click();time.sleep(5) #

# For Next Button --- WebDriverWait--------->>
#WebDriverWait(driver,20).until(EC.element_to_be_clickable((By.XPATH,"//*[@id='btnAnswerComplete']"))).click()
driver.find_element(By.XPATH,"//*[@id='btnAnswerComplete']").click();time.sleep(5) # OK

# ---------------- Answering question with Think Time -------------------------

#Q1
# Wait for Q1 --- WebDriverWait--------->>
#WebDriverWait(driver,20).until(EC.element_to_be_clickable((By.XPATH,"//*[@id='options_btn0']")))

driver.find_element(By.XPATH,"//*[@id='options_btn0']").click();time.sleep(3)
driver.find_element(By.XPATH,"//*[@id='btnAnswerComplete']").click();time.sleep(4)

#Q2
# Wait for Q2 --- WebDriverWait--------->>
# WebDriverWait(driver,20).until(EC.element_to_be_clickable((By.XPATH,"//*[@id='options_btn0']")))
driver.find_element(By.XPATH,"//*[@id='options_btn0']").click()
driver.find_element(By.XPATH,"//*[@id='btnAnswerComplete']").click();time.sleep(4)

#Q3

# Wait for Q3 --- WebDriverWait--------->>
#WebDriverWait(driver,20).until(EC.element_to_be_clickable((By.XPATH,"//*[@id='button3']"))).click()
#time.sleep(2)
driver.find_element(By.XPATH,"//*[@id='options_btn0']").click()
driver.find_element(By.XPATH,"//*[@id='btnAnswerComplete']").click();time.sleep(4)

#Q4

# Wait for Q4 --- WebDriverWait--------->>
#WebDriverWait(driver,20).until(EC.element_to_be_clickable((By.XPATH,"//*[@id='button4']"))).click()
#time.sleep(2)
driver.find_element(By.XPATH,"//*[@id='options_btn0']").click()
driver.find_element(By.XPATH,"//*[@id='btnAnswerComplete']").click();time.sleep(4)

#Q5
driver.find_element(By.XPATH,"//*[@id='options_btn0']").click()
driver.find_element(By.XPATH,"//*[@id='btnAnswerComplete']").click();time.sleep(4)

#Q6
driver.find_element(By.XPATH,"//*[@id='options_btn0']").click()
driver.find_element(By.XPATH,"//*[@id='btnAnswerComplete']").click();time.sleep(4)

#Q7
driver.find_element(By.XPATH,"//*[@id='options_btn0']").click()
driver.find_element(By.XPATH,"//*[@id='btnAnswerComplete']").click();time.sleep(4)

#Q8
driver.find_element(By.XPATH,"//*[@id='options_btn0']").click()
driver.find_element(By.XPATH,"//*[@id='btnAnswerComplete']").click();time.sleep(4)

#Q9
driver.find_element(By.XPATH,"//*[@id='options_btn0']").click()
driver.find_element(By.XPATH,"//*[@id='btnAnswerComplete']").click();time.sleep(4)

#Q10
driver.find_element(By.XPATH,"//*[@id='options_btn0']").click()
driver.find_element(By.XPATH,"//*[@id='btnAnswerComplete']").click();time.sleep(4)

#Q11
driver.find_element(By.XPATH,"//*[@id='options_btn0']").click()
driver.find_element(By.XPATH,"//*[@id='btnAnswerComplete']").click();time.sleep(4)

#Q12
driver.find_element(By.XPATH,"//*[@id='options_btn0']").click()
driver.find_element(By.XPATH,"//*[@id='btnAnswerComplete']").click();time.sleep(4)

#Q13
driver.find_element(By.XPATH,"//*[@id='options_btn0']").click()
driver.find_element(By.XPATH,"//*[@id='btnAnswerComplete']").click();time.sleep(4)

#Q14
driver.find_element(By.XPATH,"//*[@id='options_btn0']").click()
driver.find_element(By.XPATH,"//*[@id='btnAnswerComplete']").click();time.sleep(4)

#Q15
driver.find_element(By.XPATH,"//*[@id='options_btn0']").click()
driver.find_element(By.XPATH,"//*[@id='btnAnswerComplete']").click();time.sleep(4)

#Q16
driver.find_element(By.XPATH,"//*[@id='options_btn0']").click()
driver.find_element(By.XPATH,"//*[@id='btnAnswerComplete']").click();time.sleep(4)

#Q17
driver.find_element(By.XPATH,"//*[@id='options_btn0']").click()
driver.find_element(By.XPATH,"//*[@id='btnAnswerComplete']").click();time.sleep(4)

#Q18
driver.find_element(By.XPATH,"//*[@id='options_btn0']").click()
driver.find_element(By.XPATH,"//*[@id='btnAnswerComplete']").click();time.sleep(4)

#Q19
driver.find_element(By.XPATH,"//*[@id='options_btn0']").click()
driver.find_element(By.XPATH,"//*[@id='btnAnswerComplete']").click();time.sleep(4)

#Q20
driver.find_element(By.XPATH,"//*[@id='options_btn0']").click()
driver.find_element(By.XPATH,"//*[@id='btnAnswerComplete']").click();time.sleep(4)
# total 52

#Q21
driver.find_element(By.XPATH,"//*[@id='options_btn0']").click()
driver.find_element(By.XPATH,"//*[@id='btnAnswerComplete']").click();time.sleep(4)

#Q22
driver.find_element(By.XPATH,"//*[@id='options_btn0']").click()
driver.find_element(By.XPATH,"//*[@id='btnAnswerComplete']").click();time.sleep(4)

#Q23
driver.find_element(By.XPATH,"//*[@id='options_btn0']").click()
driver.find_element(By.XPATH,"//*[@id='btnAnswerComplete']").click();time.sleep(4)

#Q24
driver.find_element(By.XPATH,"//*[@id='options_btn0']").click()
driver.find_element(By.XPATH,"//*[@id='btnAnswerComplete']").click();time.sleep(4)

#Q25
driver.find_element(By.XPATH,"//*[@id='options_btn0']").click()
driver.find_element(By.XPATH,"//*[@id='btnAnswerComplete']").click();time.sleep(4)

#Q26
driver.find_element(By.XPATH,"//*[@id='options_btn0']").click()
driver.find_element(By.XPATH,"//*[@id='btnAnswerComplete']").click();time.sleep(4)

#Q27
driver.find_element(By.XPATH,"//*[@id='options_btn0']").click()
driver.find_element(By.XPATH,"//*[@id='btnAnswerComplete']").click();time.sleep(4)

#Q28
driver.find_element(By.XPATH,"//*[@id='options_btn0']").click()
driver.find_element(By.XPATH,"//*[@id='btnAnswerComplete']").click();time.sleep(4)

#Q29
driver.find_element(By.XPATH,"//*[@id='options_btn0']").click()
driver.find_element(By.XPATH,"//*[@id='btnAnswerComplete']").click();time.sleep(4)

#Q30
driver.find_element(By.XPATH,"//*[@id='options_btn0']").click()
driver.find_element(By.XPATH,"//*[@id='btnAnswerComplete']").click();time.sleep(4)

#Q31
driver.find_element(By.XPATH,"//*[@id='options_btn0']").click()
driver.find_element(By.XPATH,"//*[@id='btnAnswerComplete']").click();time.sleep(4)

#Q32
driver.find_element(By.XPATH,"//*[@id='options_btn0']").click()
driver.find_element(By.XPATH,"//*[@id='btnAnswerComplete']").click();time.sleep(4)

#Q33
driver.find_element(By.XPATH,"//*[@id='options_btn0']").click()
driver.find_element(By.XPATH,"//*[@id='btnAnswerComplete']").click();time.sleep(4)

#Q34
driver.find_element(By.XPATH,"//*[@id='options_btn0']").click()
driver.find_element(By.XPATH,"//*[@id='btnAnswerComplete']").click();time.sleep(4)

#Q35
driver.find_element(By.XPATH,"//*[@id='options_btn0']").click()
driver.find_element(By.XPATH,"//*[@id='btnAnswerComplete']").click();time.sleep(4)

#Q36
driver.find_element(By.XPATH,"//*[@id='options_btn0']").click()
driver.find_element(By.XPATH,"//*[@id='btnAnswerComplete']").click();time.sleep(4)

#Q37
driver.find_element(By.XPATH,"//*[@id='options_btn0']").click()
driver.find_element(By.XPATH,"//*[@id='btnAnswerComplete']").click();time.sleep(4)

#Q38
driver.find_element(By.XPATH,"//*[@id='options_btn0']").click()
driver.find_element(By.XPATH,"//*[@id='btnAnswerComplete']").click();time.sleep(4)

#Q39
driver.find_element(By.XPATH,"//*[@id='options_btn0']").click()
driver.find_element(By.XPATH,"//*[@id='btnAnswerComplete']").click();time.sleep(4)

#Q40
driver.find_element(By.XPATH,"//*[@id='options_btn0']").click()
driver.find_element(By.XPATH,"//*[@id='btnAnswerComplete']").click();time.sleep(4)

#Q41
driver.find_element(By.XPATH,"//*[@id='options_btn0']").click()
driver.find_element(By.XPATH,"//*[@id='btnAnswerComplete']").click();time.sleep(4)

#Q42
driver.find_element(By.XPATH,"//*[@id='options_btn0']").click()
driver.find_element(By.XPATH,"//*[@id='btnAnswerComplete']").click();time.sleep(4)

#Q43
driver.find_element(By.XPATH,"//*[@id='options_btn0']").click()
driver.find_element(By.XPATH,"//*[@id='btnAnswerComplete']").click();time.sleep(4)

#Q44
driver.find_element(By.XPATH,"//*[@id='options_btn0']").click()
driver.find_element(By.XPATH,"//*[@id='btnAnswerComplete']").click();time.sleep(4)

#Q45
driver.find_element(By.XPATH,"//*[@id='options_btn0']").click()
driver.find_element(By.XPATH,"//*[@id='btnAnswerComplete']").click();time.sleep(4)

#Q46
driver.find_element(By.XPATH,"//*[@id='options_btn0']").click()
driver.find_element(By.XPATH,"//*[@id='btnAnswerComplete']").click();time.sleep(4)

#Q47
driver.find_element(By.XPATH,"//*[@id='options_btn0']").click()
driver.find_element(By.XPATH,"//*[@id='btnAnswerComplete']").click();time.sleep(4)

#Q48
driver.find_element(By.XPATH,"//*[@id='options_btn0']").click()
driver.find_element(By.XPATH,"//*[@id='btnAnswerComplete']").click();time.sleep(4)

#Q49
driver.find_element(By.XPATH,"//*[@id='options_btn0']").click()
driver.find_element(By.XPATH,"//*[@id='btnAnswerComplete']").click();time.sleep(4)

#Q50
driver.find_element(By.XPATH,"//*[@id='options_btn0']").click()
driver.find_element(By.XPATH,"//*[@id='btnAnswerComplete']").click();time.sleep(4)

#Q51
driver.find_element(By.XPATH,"//*[@id='options_btn0']").click()
driver.find_element(By.XPATH,"//*[@id='btnAnswerComplete']").click();time.sleep(4)

#Q52
driver.find_element(By.XPATH,"//*[@id='options_btn0']").click()
driver.find_element(By.XPATH,"//*[@id='btnAnswerComplete']").click();time.sleep(10)

# button continue
driver.find_element(By.XPATH,"//*[@id='btnContinue']").click();time.sleep(10)

# Button Exist
driver.find_element(By.XPATH,"//*[@id='btnExitTestSession']").click();time.sleep(7)
time.sleep(3)