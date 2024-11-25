import msvcrt,os
from selenium.webdriver.common.by import By 
from time import sleep

def SeConnecter(driver,email,mdp):
    

    driver.get("https://compte.groupe-voltaire.fr/login")

    driver.find_element(By.NAME, "email").send_keys(email)
    driver.find_element(By.NAME, "password").send_keys(mdp)
    driver.find_element(By.XPATH, "//button[@class='mainButton']").click() 

def LoginIncorrect(driver):
    driver.quit()
    os.system('cls')
    print("Identifiant incorrect, réessayer ...")
    
def AccesAcitviter(driver):
    driver.get("https://www.projet-voltaire.fr/voltaire/com.woonoz.gwt.woonoz.Voltaire/Voltaire.html?returnUrl=www.projet-voltaire.fr/choix-parcours/&applicationCode=pv")
    sleep(1)
    for i in range(10):
        try:
            driver.find_element(By.XPATH, f"//*[@id='btn_home_module_lancer_{i}' and @title='Lancer le programme d’entraînement personnalisé Niveau {i}' and @style='']").click()
            break
        except:pass
    sleep(3)
    PageCompris(driver)
    

def VerifDriver(driver):
    while True:
        try:
            driver.title  
        except : break         
        sleep(1)  
    driver.quit()

def PageCompris(driver):
    try:
        driver.find_element(By.XPATH, "//button[@class='understoodButton']").click()
        sleep(1)
        for i in range (3):
            driver.find_element(By.XPATH, "//button[@class='buttonKo']").click()
            sleep(1)
        try:
            driver.find_element(By.XPATH, "//button[@class='exitButton secondaryButton']").click()
        except: 
            driver.find_element(By.XPATH, "//button[@class='exitButton primaryButton']").click()
    except: 
        pass
    sleep(3)

def RecupereTexte(driver):
    texte = ""
    elements = driver.find_elements(By.CLASS_NAME, "pointAndClickSpan")
    for element in elements:
        if element.text == "":
            texte += " "
        texte += element.text
    return texte