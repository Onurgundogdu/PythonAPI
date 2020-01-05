###  ! Komut ekranında  pip/pip3 install googletrans paketi yükleme
#### Googletrans ile hangi dil olduğunu gösterme
from googletrans import Translator
translate=Translator()
lang=translate.detect('Detect')
print(lang)
lang2=translate.detect('Dili Belirle')
print(lang2)
#### Dil çeviri işlemi
ceviri=translate.translate('İyi günler',dest='en')
print(ceviri)
ceviri2=translate.translate("Good night",dest='ja')
print(ceviri2)
ceviri3=translate.translate("Googletrans is a free and unlimited python library that implemented Google Translate API. This uses the Google Translate Ajax API"
"to make calls to such methods as detect and translate.",dest='tr')
print(ceviri3)
