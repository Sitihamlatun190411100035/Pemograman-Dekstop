import sys 
from PyQt5.QtWidgets import QApplication,QWidget,QLabel,QPushButton

#membuat fungsi untuk menentukan layout window
def window_go():
    #inisialisai pyqt
    app = QApplication(sys.argv)
    window = QWidget()
    
    #menyiapkan label, menempelkan label ke window
    #settext dan posisi
    textLabel = QLabel(window)
    textLabel.setText("Kotak Angka")
    textLabel.move(10,5)
    for i in range(5):
        a = QPushButton(window)
        a.resize(50,50)
        a.setStyleSheet("background-color : #ADD8E6; color : red; font-size: 36px; font: bold")
        a.setText(str(i+1))
        a.move(30,40)
        a.move(60*(i),20)
        
    #menentukan ukuran window, title, dan menampilan window
    window.setGeometry(50,50,400,300)
    window.setWindowTitle("PyQt5 Example")
    window.show()
    sys.exit(app.exec_())
    
if __name__=='__main__':
    window_go()
