import time

try:
    from selenium import webdriver

    driver = webdriver.Firefox()
    driver.get("https://www.amazon.com/")
    anasayfa=driver.title
    if "Amazon" in anasayfa:
        print("Başarıyla {} giriş yapıldı".format(anasayfa[0:10]))
        gir=driver.find_element_by_xpath('//*[@id="nav-link-accountList"]/span[2]')
        gir.click()
        time.sleep(5)
        
        posta=driver.find_element_by_xpath('//*[@id="ap_email"]')
        posta.send_keys("merveealpay@gmail.com")
        postabtn=driver.find_element_by_xpath('//*[@id="continue"]')
        postabtn.click()
        time.sleep(5)

        parola=driver.find_element_by_xpath('//*[@id="ap_password"]')
        parola.send_keys("123456789Merve")
        parolabtn=driver.find_element_by_xpath('//*[@id="signInSubmit"]')
        parolabtn.click()
        time.sleep(5)
        
        arama=driver.find_element_by_xpath('//*[@id="twotabsearchtextbox"]')
        arama.send_keys("samsung")
        aramabtn=driver.find_element_by_xpath('/html/body/div[1]/header/div/div[1]/div[3]/div/form/div[2]/div/input')
        aramabtn.click()
        time.sleep(5)
        if "samsung" in driver.title:
            print("Şuan 'samsung' araması yaptınız")
            sayfa2=driver.find_element_by_xpath('/html/body/div[1]/div[2]/div/div[3]/div[2]/div/div[5]/div[2]/div/span[3]/a')
            sayfa2.click()
            time.sleep(5)
            sayfa2t=driver.find_element_by_id('s-result-count')
            
            if "17-32" in sayfa2t.text:
                print("Şuan sayfa 2'de bulunmaktasınız")
                urun=driver.find_element_by_xpath('/html/body/div[1]/div[2]/div/div[3]/div[2]/div/div[4]/div[1]/div/ul/li[3]/div/div/div/div[1]/div/div')
                urun.click()
                time.sleep(3)
                urunonay=driver.find_element_by_id('productTitle')
                a=urunonay.text
                ekle=driver.find_element_by_xpath('//*[@id="add-to-wishlist-button-submit"]')
                ekle.click()
                time.sleep(2)
                liste=driver.find_element_by_id('WLHUC_viewlist')
                liste.click()
                time.sleep(5)
                urunonay2=driver.find_element_by_id('g-items')
                b=urunonay2.text
                if a in b:
                    print("Ürün başarıyla eklendi")
                    urunsil=driver.find_element_by_xpath('/html/body/div[1]/div[2]/div/div[1]/div/div/div/div[2]/div[2]/div[3]/div/div/div[1]/div/div/div[2]/div[3]/div/div[2]/div/div/div[1]/div[2]/form/span/span/span/input')
                    urunsil.click()
                    time.sleep(2)
                    urunsilonay=driver.find_element_by_id('g-items')
                    c=urunsilonay.text
                    if a in c:
                        print("Ürün başarıyla kaldırıldı")
                    else:
                        print("ürün kaldıralamadı")
                        driver.close()
                else:
                    print("ürün eklenemedi")
                    driver.close()
            else:
                print("Yanlış sayfa")
        else:
            print("Yanlış arama")
            driver.close()
            
  

        
    else:
        print("Yanlış sayfa")
        driver.close()
            
            
    time.sleep(10)
    driver.close()         
                
        
except ImportError:
    print("Lütfen selenium kütüphanesini kurunuz")
except:
    print("Bilinmeyen bir hata oluştu")
    
