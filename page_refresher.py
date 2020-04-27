import sys
import time
from PyQt5.QtCore import QUrl
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtWidgets import QApplication, QGridLayout, QWidget
from qtconsole.qt import QtCore


class MainWindow(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        self.setGeometry(100, 100, 300, 200)
        self.show()
        self.grid = QGridLayout(self)
        self.grid.setContentsMargins(0, 0, 0, 0)
        self.web = QWebEngineView()
        self.web.load(QUrl(link))
        self.grid.addWidget(self.web, 0, 0)

        self.web2 = QWebEngineView()
        self.web2.hide()
        self.web2.load(QUrl(link))
        self.grid.addWidget(self.web2, 0, 0)

        timer = QtCore.QTimer(self)
        timer.timeout.connect(self.refresh)
        timer.start(int(sys.argv[-1]))

    def refresh(self):
        print(int(time.time()))

        def finished():
            browser, another = self.web, self.web2
            if another.isHidden():
                browser, another = another, browser
            time.sleep(1)
            browser.show()
            another.hide()

        if self.web2.isHidden():
            self.web2.reload()
            self.web2.loadFinished.connect(finished)
        else:
            self.web.reload()
            self.web.loadFinished.connect(finished)


if __name__ == "__main__":
    if len(sys.argv) == 3:
        link = sys.argv[-2]
        app = QApplication(sys.argv)
        main_window = MainWindow()
        main_window.showFullScreen()
        sys.exit(app.exec_())
    else:
        print('Use page_refresher.exe <url> <delay in ms>')
