#from playsound import playsound
import speech_recognition as sr
from googletrans import Translator
from gtts import  gTTS
import os
import nltk
import pandas as pd
import numpy as np
import sys

df=pd.read_csv("BadWordDataset.csv")
class BadWords:
    def matching(self,sent):
        new_sent=""
        repOrNot=True
        word_token=nltk.word_tokenize(sent)
        for i in range(0,len(word_token)):
            word2=word_token[i].lower()
            first_ele=word2[0]
            if len(word2)<=2:
                new_sent+=word2+" "
            elif word2 in df[first_ele].values.tolist():
                star=""
                repOrNot=False
                for j in range(0,len(word2)):
                    star+="*"
                new_sent+=star+" "
            else:
                new_sent+=word2+" "
        if new_sent.lower()==sent.lower()+" ":
            new_sent=sent 
        return new_sent,repOrNot
  
class LangConv():
    def __init__(self):
        dic=("hindi","hi","english","en","punjabi","pa")
  
    def input_from_mic(self,lang_input):
        r=sr.Recognizer()
        with sr.Microphone() as source:
            print("listening....")
            r.adjust_for_ambient_noise(source,duration=0.3)
            audio=r.record(source,duration=10)
        try:
            print("Recognizing....")
            query=r.recognize_google(audio,language=lang_input)
            print(f"User said : {query}")
        except Exception as e:
            print("say that again Please.....")
            return "none"
        return query
        # print("Enter sentence to translate")
    def call_to_mic(self,lang_input):
        obj2=LangConv()
        query=obj2.input_from_mic(lang_input)
        while(query=="none"):
                query=obj2.input_from_mic(lang_input)
                print(query)
        return query
            # language which user want to translate
    def destination_lang():
        print("Enter the language in which you want to convert")
        print("Exp, Hindi,English, Punjabi ,etc.")
        to_lang=input_from_mic()
        while(to_lang=="none"):
            lo_lang=input_from_mic()
        to_lang=to_lang.lower()
        return to_lang
    def call_to_destination(self):
            to_lang=destination_lang()
            while(to_lang not in dic):
                print("Language which you try to convert not availabe")
                to_lang=destination_lang()

            to_lang=dic[dic.index(to_lang)+1]
            #translating one language to another language form
            #translato=Translator(service_urls=['translate.googleapis.com'])
    def trans(self,query,lang):
            translate=Translator()
            text_to_translate=translate.translate(query,dest=lang)
            text_data=text_to_translate.text
            #print(text_data)
            # saving traslated files
            # google test to speak
            return text_data
    
def messageReceive(msg,lang,mic):
    obj=LangConv()
    if(lang=="English"):
        lang="en-in"
    elif(lang=="Hindi"):
        lang="hi-in"
    else:
        lang="pa"
    if(mic=="on"):
        query= obj.call_to_mic(lang)
    else:
        query=msg
    if lang=='pa' or lang=='hi-in':
        query=obj.trans(query,"en")
        
    BadWordObj=BadWords()
    new_sent,resp_check=BadWordObj.matching(query)
    return new_sent,resp_check  
# args[1] for message
# args[2] for language
# args[3] for mic         
x,y=messageReceive(sys.argv[1],sys.argv[2],sys.argv[3])
#x,y=messageReceive('hello you are lokk sexy','Eng','off')
print(x)
print(y)