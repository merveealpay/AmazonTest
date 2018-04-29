# AmazonTest
#Selenium Web Driver Nedir?
Yazılan test otomasyonları için yerel bilgisayarlarımızda kullandığımız bir Apı’dir.
Selenium WebDriver ile herhangi bir web sayfası üzerinde herhangi bir kullanıcının yapabileceği bütün işlemleri orta seviye kod bilgisi ile otomatize edebilir.
Selenium WebDriver'ı bütün işletim sistemlerinde kullanabilir.
Ayrıca, web sayfasının hangi teknoloji/teknolojiler ile yazılmış olduğunun da önemi bulunmamaktadır.

# Ayarlar
https://www.seleniumhq.org/download/ Bu linkten kullanacağınız dil için indirme gerçekleştirebilirsiniz. Bu testte Python 3.11.0 versiyon için kurulum yaptım.
Firefox ayarlaması için linkte bulunan size uygun driver'ı indirin ve path yoluna ekleyın ; https://github.com/mozilla/geckodriver/releases

# Test Case -Senaryo
1. http://www.amazon.com adresi ziyaret edilecek ve ana sayfanın açıldığı onaylanacak
2. Login ekranını açılarak daha önceden oluşturulmuş bir kullanıcı ile login olacak
3. Sayfanın üstündeki arama kutusuna “samsung” yazıp arama düğmesine tıklanacak
4. Gelen sonuçlarda Samsung için sonuçların listelendiği onaylanacak
5. Arama sonuçlarından 2. sayfaya tıklanarak açılan sayfada 2. sayfanın gösterildiği
onaylanacak
6. Üstten 3. ürüne tıklayıp detaylarına girilerek “Add to list” düğmesine tıklanacak
7. Açılan bilgi ekranından “View Your List” düğmesine tıklanarak wish list sayfası
görüntülenecek
8. Açılan sayfada bir önceki maddede listeye eklenmiş ürünün bulunduğu onaylanacak
9. Listeye eklenmiş bu ürünün yanındakki “Delete” düğmesine basılarak listeden
çıkartılacak
10. Ürünün listede yer almadığı onaylanacak.
