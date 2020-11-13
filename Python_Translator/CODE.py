from googletrans import *
from gtts import gTTS
import os

#text = '''The computer was born to solve problems that did not exist before'''
print("Langauges : ")
print('''
            af'--'Afrikaans', 'sq'--'Albanian','ar'--'Arabic','hy'--'Armenian',
            'bn'--'Bengali','ca'--'Catalan','zh'--'Chinese','zh-cn'--'Chinese (Mandarin/China)',
            'zh-tw'--'Chinese (Mandarin/Taiwan)','zh-yue'--'Chinese (Cantonese)','hr'--'Croatian',
            'cs'--'Czech','da'--'Danish','nl'--'Dutch','en'--'English','en-au'--'English (Australia)',
            'en-uk'--'English (United Kingdom)','en-us'--'English (United States)','fi'--'Finnish',
            'fr'--'French','de'--'German','el'--'Greek','hi'--'Hindi','hu'--'Hungarian','is'--'Icelandic',
            'id'--'Indonesian','it'--'Italian','ja'--'Japanese','ko'--'Korean','la'--'Latin','lv'--'Latvian',
            'mk'--'Macedonian','no'--'Norwegian','pl'--'Polish','pt'--'Portuguese',
            'pt-br'--'Portuguese (Brazil)','ro'--'Romanian','ru'--'Russian','sr'--'Serbian',
            'sk'--'Slovak','es'--'Spanish','es-es'--'Spanish (Spain)','es-us'--'Spanish (United States)',
            'sw'--'Swahili','sv'--'Swedish','ta'--'Tamil','th'--'Thai',
            'tr'--'Turkish','vi'--'Vietnamese','cy'--'Welsh''')
lang=input("\nEnter the langauge You want to convert into ")
text=input("Enter Word/phrase")
translator = Translator()            
temp= translator.detect(text)
print('-----------------------------------------------------------------------')
print('The Text is :')
print(text,"\n")
translated = translator.translate(text,dest=lang) #Change en into any langauge you want from below list

# 'af':'Afrikaans', 'sq':'Albanian','ar':'Arabic','hy':'Armenian','bn':'Bengali','ca':'Catalan','zh':'Chinese','zh-cn':'Chinese (Mandarin/China)',
# 'zh-tw':'Chinese (Mandarin/Taiwan)','zh-yue':'Chinese (Cantonese)','hr':'Croatian','cs':'Czech','da':'Danish','nl':'Dutch','en':'English','en-au':'English (Australia)',
# 'en-uk':'English (United Kingdom)','en-us':'English (United States)','fi':'Finnish','fr':'French','de':'German','el':'Greek','hi':'Hindi','hu':'Hungarian','is':'Icelandic',
# 'id':'Indonesian','it':'Italian','ja':'Japanese','ko':'Korean','la':'Latin','lv':'Latvian','mk':'Macedonian','no':'Norwegian','pl':'Polish','pt':'Portuguese',
# 'pt-br':'Portuguese (Brazil)','ro':'Romanian','ru':'Russian','sr':'Serbian','sk':'Slovak','es':'Spanish','es-es':'Spanish (Spain)','es-us':'Spanish (United States)',
# 'sw':'Swahili','sv':'Swedish','ta':'Tamil','th':'Thai','tr':'Turkish','vi':'Vietnamese','cy':'Welsh'

print("SOURCE Langauge : ",translated.src)
print("DESTINATION Langauge : ",translated.dest,"\n")

print("Translated :")
print(translated.text)
print("please wait...processing")
TTS = gTTS(text=translated.text, lang='en-in') #lang changes the accent

#Accents -

#en-au (Australia)
# en-gb (United Kingdom)
# en-in (India)
# en-us (United States)

# Save to mp3 in current dir.
TTS.save("voice.mp3")

# Plays the mp3 using the default app on your system
# that is linked to mp3s.
os.system("start voice.mp3")
