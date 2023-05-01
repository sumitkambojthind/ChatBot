from playsound import playsound
import speech_recognition as sr
from googletrans import Translator
from gtts import  gTTS
import os
import nltk
import googletrans
import pandas as pd
import numpy as np
import chatBotDataset1 as tts
from chatBotLibrary import Chat, reflections
import sys
    
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
    def play_device(self,text_data):
        # slow keyword to read text more slowly
        from playsound import playsound
        speak=gTTS(text=text_data,lang='en',slow=False)
        speak.save("Translated_file.mp3")
        playsound("Translated_file.mp3")
        os.remove("Translated_file.mp3")
        print(text_data)


tts_chatbot=Chat(tts.pairs,tts.reflections)


def messageReply(new_sent,play,resp_check):
    obj2=LangConv()
    if resp_check==True:
        get_response=tts_chatbot.converse(new_sent)
    else:
        get_response="You are using irrelevant words in your sentence"
    if(play=="Yes"):
        obj2.play_device(get_response)
       
    #print(trans_data)
    return get_response

# args[4] for new sentence
#args[5] for play 
#args[6] for check message is bad or not
 
final_sen=messageReply(sys.argv[1],sys.argv[2],sys.argv[3])
#final_sen=messageReply('hello','Yes',True)
print(final_sen)
