import start_menu
import main_menu
import result
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget,QFileDialog
import sys
from PyQt5.QtGui import QPixmap
from keras.models import load_model
from tensorflow.keras.preprocessing import image
from PIL import Image 
from keras.applications.vgg16 import preprocess_input
import numpy as np

class start_menu_ui(QMainWindow,start_menu.Ui_MainWindow):
    def __init__(self):
        super(start_menu_ui,self).__init__()
        self.setupUi(self)
        self.mainmenu = main_menu_ui()
    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.close()
            self.mainmenu.show()

class main_menu_ui(QMainWindow,main_menu.Ui_MainWindow):
    def __init__(self):
        super(main_menu_ui,self).__init__()
        self.setupUi(self)
    def loadimg1(self):
        self.filename, self.filetype = QFileDialog.getOpenFileName(self, caption='開啟檔案') #get filename and filetype
        print(self.filename)
        self.mypixmap = QPixmap()
        self.mypixmap.load(self.filename)
        if self.mypixmap.isNull():
                print('load image failed')
                return
        self.label.setScaledContents(True)
        self.label.setPixmap(self.mypixmap)
    def predict(self):
        img_height=189
        img_width=240
        img = image.load_img(self.filename, target_size=(img_height,img_width))
        x = image.img_to_array(img)
        x = np.expand_dims(x, axis=0)
        x = preprocess_input(x)

        # 進行預測
        predictions = self.model.predict(x)
        predicted_class_index = np.argmax(predictions)
        self.listdir=['ferrari','hyundai', 'lexus', 'mazda', 'mercedes', 'opel', 'skoda', 'toyota', 'volkswagen']
        self.brand_intro={'ferrari':"Ferrari是一家世界知名的意大利豪華汽車製造商，成立於1947年，總部位於意大利馬拉內羅。Ferrari以其極高的性能、優雅的設計和卓越的工藝而聞名於世。該品牌專注於生產高性能跑車和超級跑車，並在賽車領域享有盛譽。Ferrari的車輛以其獨特的紅色外觀和具有優秀操控性能的特點而著名。它們搭載先進的引擎技術，以迅猛的加速和出色的極速而聞名。每輛Ferrari車輛都是精心打造的藝術品，融合了創新、精確和卓越的工藝，旨在提供極致的駕駛體驗。",
                          'hyundai':"Hyundai是一家總部位於韓國的汽車製造公司，成立於1967年。它是全球最大的汽車製造商之一，並且在全球各地擁有廣泛的市場份額。Hyundai以生產多種汽車類型而聞名，包括小型車、中型車、SUV、跨界車和電動車等。該公司注重創新和技術發展，在汽車設計、安全性能和燃油效率方面取得了顯著的成就。它的車輛設計具有現代感和流線型外觀，並提供豪華和實用性的結合。", 
                          'lexus':"Lexus是一個豪華汽車品牌，屬於豐田汽車旗下的子品牌。該品牌於1989年在日本成立，以生產高品質、豪華且舒適的汽車而聞名。Lexus著重於提供卓越的駕馭體驗和高級內部裝潢。其車輛設計獨特且富有辨識度，擁有流線型的外觀和精細的細節。內部空間注重細膩的工藝和舒適性，提供豪華的座椅、高級音響系統和先進的科技設施。", 
                          'mazda':"Mazda是一個日本汽車品牌，以其獨特的設計和卓越的駕馭性能而聞名。Mazda成立於1920年，迄今已有一個世紀的歷史。Mazda以其獨特的\"魂動\"設計理念而受到廣泛讚譽。該設計風格強調動感和流暢性，融合了精緻的細節和動態的線條，使其車型在道路上具有獨特的風格和辨識度。除了令人驚艷的外觀，Mazda車型還以卓越的駕馭體驗而聞名。品牌致力於提供優異的操控性能和平順的行駛感，融合了先進的底盤技術和動力系統，讓駕駛者享受到純粹、樂趣的駕駛體驗。", 
                          'mercedes':"Mercedes-Benz是一個德國汽車品牌，享有卓越的聲譽和豪華的形象。該品牌成立於1926年，至今已有近一個世紀的歷史。Mercedes-Benz以其高品質、創新和卓越的工藝而聞名。該品牌致力於製造精湛的汽車，以滿足對品質和豪華的高要求。每一輛Mercedes-Benz車型都代表著卓越的工程設計和精密的製造工藝。梅賽德斯-奔馳提供廣泛的車系，包括豪華轎車、SUV、跑車和敞篷車等多種類型。無論是商務用途還是休閒娛樂，Mercedes-Benz都有適合不同需求的車型。品牌的旗艦車型通常代表著最高水準的豪華和性能。", 
                          'opel':"Opel是一個德國汽車品牌，擁有悠久的歷史和豐富的汽車製造經驗。該品牌成立於1862年，最初是一家製造縫紉機的公司，後來轉型為汽車製造商。Opel以其出色的德國工程和可靠性而聞名。該品牌致力於提供高品質、實用和現代化的汽車，以滿足不同消費者的需求。Opel車型融合了創新技術、優雅設計和卓越性能，為駕駛者提供舒適、安全和令人愉悅的駕馭體驗。Opel提供多樣化的車型，包括小型車、家庭車、跨界車和SUV等。無論您是尋找經濟實惠的城市代步車還是舒適寬敞的家庭車，Opel都有適合的選擇。該品牌也推出了一些環保和節能的車型，以應對日益增長的環保意識和可持續發展的需求。", 
                          'skoda':"Skoda是一個捷克汽車品牌，擁有悠久的歷史和優良的汽車製造傳統。該品牌成立於1895年，起初是一家自行車製造公司，後來逐漸轉型為汽車製造商。Skoda以其可靠性、實用性和價值優勢而聞名。該品牌的車型注重功能性和經濟性，提供高品質的汽車，以滿足不同消費者的需求。Skoda車輛結合了先進的技術、優雅的設計和寬敞的內部空間，為駕駛者和乘客提供舒適、安全和愉悅的駕馭體驗。", 
                          'toyota':"Toyota是一個世界知名的日本汽車品牌，擁有悠久的歷史和卓越的汽車製造實力。該品牌成立於1937年，至今已成為全球最大的汽車製造商之一。Toyota以其出色的品質、可靠性和創新技術而聞名。該品牌的車型涵蓋了各個市場範疇，包括小型車、家庭車、SUV、豪華車和混合動力車等。無論是燃油車還是電動車，Toyota都致力於提供高效能、環保和節能的汽車解決方案。", 
                          'volkswagen':"Volkswagen是一個德國汽車品牌，享有廣泛的知名度和全球市場份額。該品牌成立於1937年，是世界上最大的汽車製造商之一。Volkswagen以其品質、可靠性和創新性而聞名。該品牌致力於提供高品質、功能豐富且經濟實惠的汽車。Volkswagen車型範圍廣泛，包括小型車、家庭車、SUV、豪華車和電動車等。無論是城市代步還是長途旅行，Volkswagen都能滿足不同用戶的需求。Volkswagen車輛的設計注重實用性和現代感。品牌的車型提供寬敞舒適的乘坐空間、優雅設計和先進的車輛功能。Volkswagen車輛的內部配置精良，提供豪華、舒適和便利的駕乘體驗。"
                          }
        self.result_name=self.listdir[predicted_class_index]
        print(self.result_name)
        self.result_ui = result_menu_ui()
        self.window1=QtWidgets.QMainWindow()
        self.result_ui.setupUi(self.window1)
        _translate = QtCore.QCoreApplication.translate
        self.result_ui.label.setText(_translate("result", self.result_name))
        self.result_ui.label_2.setText(_translate("result", self.brand_intro[self.result_name]))
        self.window1.show()

class result_menu_ui(result.Ui_MainWindow):
    def __init__(self):
        super(result_menu_ui,self).__init__()
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    startmenu = start_menu_ui()
    startmenu.show()
    
    sys.exit(app.exec_())
