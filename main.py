from selenium import webdriver
from time import sleep 
import fonction,navigation,threading
from selenium.webdriver.common.by import By

while True:
    email,mdp = "mohamedamine.delhem@limayrac.fr","Mazouna2004!"#fonction.login()
    driver = webdriver.Chrome()
    navigation.SeConnecter(driver,email,mdp)
    if driver.current_url != "https://compte.groupe-voltaire.fr/login": 
        break
    else:
        navigation.LoginIncorrect(driver)

        

threading.Thread(target=navigation.VerifDriver, args=(driver,)).start()

navigation.AccesAcitviter(driver)

texte = navigation.RecupereTexte(driver).strip()
texte_corrige = fonction.Correction(texte).strip()

print("Texte : ", texte)
print("Texte corrigé : ", texte_corrige)
print(fonction.TrouveLErreur(texte,texte_corrige))



    
