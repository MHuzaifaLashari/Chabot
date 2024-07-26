from tkinter import *
import tkinter as ttk
import random
from gtts import gTTS
import os
import playsound
import speech_recognition as sr  # Import speech_recognition library

class Chatbot:
    def __init__(self, root):
        self.root = root
        self.root.geometry('700x600+250+30')
        self.root.title('Welcome to Sindh Museum Hyderabad')
        self.root.bind('<Return>', self.ent_func)
        
        #===========title================
        lbl_title = Label(self.root, bg='White', text='Your personal AI Tourist GUIDE', font=('Calibri', 25, 'bold'))
        lbl_title.place(x=50, y=20)

        #========Main Frame with Text=========
        main_frame = Frame(self.root, relief=RAISED, bg='white')
        main_frame.place(x=0, y=60, width=700, height=400)

        # ===========Text area with scrollbar===
        self.scroll_y = ttk.Scrollbar(main_frame, orient=VERTICAL)
        self.text = Text(main_frame, width=65, height=20, font=('Calibiri', 14), relief=RAISED, yscrollcommand=self.scroll_y.set)
        self.scroll_y.pack(side=RIGHT, fill=Y)
        self.text.pack()

        #====Search label
        lbl_search = Label(self.root, text='Search Here', font=('Calibri', 18, 'bold'))
        lbl_search.place(x=20, y=480)

        #=====entry
        self.ent = StringVar()
        self.entry = ttk.Entry(self.root, textvariable=self.ent, bd=2, font=('Calibri', 16, 'bold'))
        self.entry.place(x=200, y=480, width=400, height=30)

        # =====btn send
        self.btn_send = ttk.Button(self.root, command=self.send, width=20, text='Submit', font=('Calibiri', 14,), bg='gray', fg='Black')
        self.btn_send.place(x=200, y=520, width=200, height=30)
        
        # =====btn clear
        self.btn_clr = ttk.Button(self.root, command=self.clear, width=20, text='Clear', font=('Calibiri', 14,), bg='gray', fg='Black')
        self.btn_clr.place(x=410, y=520, width=200, height=30)

        # =====btn speech-to-text
        self.btn_stt = ttk.Button(self.root, command=self.speech_to_text, width=20, text='Speak', font=('Calibiri', 14,), bg='gray', fg='Black')
        self.btn_stt.place(x=200, y=560, width=200, height=30)

        # ====label message
        self.msg = StringVar()
        self.lbl_msg = Label(self.root, textvariable=self.msg)
        self.lbl_msg.place(x=100, y=580)

        # Language selection
        self.language = StringVar(value='ur')  # Default language is Urdu
        self.language_menu = OptionMenu(self.root, self.language, 'ur', 'en')
        self.language_menu.place(x=600, y=480, width=100, height=30)

        self.recognizer = sr.Recognizer()  # Initialize the speech recognizer

    # ======================================functions=============

    def ent_func(self, event):
        self.btn_send.invoke()
        self.ent.set("")

    def clear(self):
        self.text.delete('1.0', END)
        self.ent.set("")

    def speak(self, text):
        lang = self.language.get()
        tts = gTTS(text=text, lang=lang)
        tts.save("response.mp3")
        playsound.playsound("response.mp3")
        os.remove("response.mp3")

    def send(self):
        user_input = "\t\t\t" + "You: " + self.entry.get()
        self.text.insert(END, "\n" + user_input)

        if self.entry.get() == "":
            self.msg.set("Please Type something")
            self.lbl_msg.config(fg='black')
        else:
            self.msg.set("")
            self.lbl_msg.config(fg='black')

        responses_urdu = {
            "hello": "سندھ میوزیم میں خوش آمدید   ہے۔ میں آج آپ کی کیسے مدد کرسکتا ہوں؟",
            "about museum": "سندھ میوزیم سندھ کی تاریخ اور ثقافت کی نمائش کے لیے ہے، جہاں مختلف دور کے قدیم نمونے، دستکاری اور ثقافتی اشیاء کی نمائش کی گئی ہے۔",
            "museum location": "سندھ میوزیم سندھ کے شہر حیدرآباد میں واقع ہے۔",
            "museum hours": "سندھ میوزیم پیر سے ہفتہ صبح 9 بجے سے شام 5 بجے تک کھلا رہتا ہے۔",
            "entry fee": "سندھ میوزیم میں داخلہ فیس بالغوں کے لیے 50 روپے اور بچوں کے لیے 20 روپے ہے۔",
            "historical artifacts": "سندھ میوزیم میں قدیم تاریخی اشیاء اور نوادرات کی بڑی تعداد موجود ہے، جن میں قدیم سککوں، برتنوں، اور ہنر کے نمونے شامل ہیں۔",
            "ancient jewelry": "میوزیم میں قدیم دور کے زیورات کی بھی نمائش کی گئی ہے، جو سندھ کی ثقافت کی عکاسی کرتے ہیں۔",
            "crafts": "یہاں مختلف قدیم دستکاری کے نمونے دیکھے جا سکتے ہیں جو سندھ کی ثقافت کی خوبصورتی کو ظاہر کرتے ہیں۔",
            "museum history": "سندھ میوزیم 1950 کی دہائی میں قائم ہوا تھا اور سندھ کی تاریخ اور ثقافت کی نمائندگی کرتا ہے۔",
            "special exhibitions": "میوزیم میں وقتاً فوقتاً خصوصی نمائشیں بھی منعقد کی جاتی ہیں، جو مختلف موضوعات پر مبنی ہوتی ہیں۔",
            "museum architecture": "سندھ میوزیم کی عمارت بھی اپنی خوبصورت فن تعمیر کے لیے مشہور ہے، جو کلاسیکی اور جدید طرز کی آمیزش کو ظاہر کرتی ہے۔",
            "visitor services": "میوزیم میں وزیٹرز کے لیے مختلف سہولتیں موجود ہیں، جیسے کہ گائیڈڈ ٹورز اور معلوماتی بروشرز۔",
            "museum collections": "سندھ میوزیم کی مجموعہ میں قدیم دور کے اہم تاریخی اور ثقافتی مواد شامل ہے۔",
            "photography rules": "میوزیم میں عام طور پر فوٹوگرافی کی اجازت نہیں ہوتی، مگر خصوصی اجازت کے لیے انتظامیہ سے رابطہ کیا جا سکتا ہے۔",
            "museum staff": "میوزیم میں تربیت یافتہ عملہ موجود ہوتا ہے جو وزیٹرز کی مدد اور معلومات فراہم کرتا ہے۔",
            "museum facilities": "میوزیم میں سیاحتی سہولتیں جیسے کہ کیفے، واش رومز، اور اسٹورز بھی موجود ہیں۔",
            "education programs": "میوزیم مختلف تعلیمی پروگرامز اور ورکشاپس بھی منعقد کرتا ہے جو اسکولوں اور کالجوں کے طلباء کے لیے ہیں۔",
            "museum restoration": "میوزیم میں تاریخی اشیاء کی مرمت اور بحالی کا عمل بھی جاری رہتا ہے تاکہ انہیں محفوظ رکھا جا سکے۔",
            "museum entrance": "میوزیم کے داخلی راستے پر عموماً ایک معلوماتی بورڈ نصب ہوتا ہے جو وزیٹرز کو معلومات فراہم کرتا ہے۔",
            "museum events": "میوزیم مختلف ثقافتی اور سماجی واقعات کی میزبانی بھی کرتا ہے جو عوام کے لیے کھلے ہوتے ہیں."
        }

        responses_english = {
            "hello": "Welcome to the Sindh Museum. How can I assist you today?",
            "about museum": "The Sindh Museum is dedicated to showcasing the history and culture of Sindh, featuring ancient artifacts, crafts, and cultural items from various periods.",
            "museum location": "The Sindh Museum is located in Hyderabad, Sindh.",
            "museum hours": "The Sindh Museum is open from 9 AM to 5 PM, Monday through Saturday.",
            "entry fee": "The entry fee for the Sindh Museum is 50 Rupees for adults and 20 Rupees for children.",
            "historical artifacts": "The museum houses a significant collection of ancient historical items and artifacts, including ancient coins, pottery, and craft samples.",
            "ancient jewelry": "The museum also displays ancient jewelry that reflects the culture of Sindh.",
            "crafts": "Various ancient craft samples can be seen here, showcasing the beauty of Sindhi culture.",
            "museum history": "The Sindh Museum was established in the 1950s and represents the history and culture of Sindh.",
            "special exhibitions": "The museum occasionally holds special exhibitions on different topics.",
            "museum architecture": "The museum building is also known for its beautiful architecture, reflecting a blend of classical and modern styles.",
            "visitor services": "The museum offers various facilities for visitors, such as guided tours and informational brochures.",
            "museum collections": "The museum's collection includes significant historical and cultural material from ancient times.",
            "photography rules": "Generally, photography is not allowed in the museum, but special permissions can be sought from the administration.",
            "museum staff": "Trained staff is available at the museum to assist visitors and provide information.",
            "museum facilities": "Visitor facilities such as a café, restrooms, and shops are also available at the museum.",
            "education programs": "The museum organizes various educational programs and workshops for school and college students.",
            "museum restoration": "The museum also carries out the restoration and preservation of historical items to keep them safe.",
            "museum entrance": "There is usually an informational board at the entrance of the museum to provide information to visitors.",
            "museum events": "The museum hosts various cultural and social events that are open to the public."
        }

        lang = self.language.get()
        responses = responses_urdu if lang == 'ur' else responses_english

        for question, answer in responses.items():
            if self.entry.get().lower() in [question.lower()]:
                self.text.insert(END, '\n\n' + "Bot :" + answer)
                self.speak(answer)
                return
        
        # If no match found
        self.text.insert(END, '\n\n' + "Bot: Sorry, I don’t have information on that topic.")
        self.speak("Sorry, I don’t have information on that topic.")

    def speech_to_text(self):
        with sr.Microphone() as source:
            self.text.insert(END, "\n\n" + "Listening...")
            audio = self.recognizer.listen(source)
            try:
                text = self.recognizer.recognize_google(audio, language=self.language.get())
                self.entry.delete(0, END)
                self.entry.insert(0, text)
                self.send()
            except sr.UnknownValueError:
                self.text.insert(END, "\n\n" + "Bot: Sorry, I could not understand the audio.")
            except sr.RequestError:
                self.text.insert(END, "\n\n" + "Bot: Sorry, there was an error with the speech recognition service.")

if __name__ == '__main__':
    root = Tk()
    obj = Chatbot(root)
    root.mainloop()

