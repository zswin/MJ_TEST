from PyQt5.QtWidgets import QApplication
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtCore import QUrl
from PyQt5.QtWebEngineWidgets import QWebEnginePage
from lxml import etree
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *


class WebRender(QWebEnginePage):
    def __init__(self, url):
        self.app = QApplication(sys.argv)
        QWebPage.__init__(self)
        self.loadFinished.connect(self.__loadFinished)
        self.mainFrame().load(QUrl(url))
        self.app.exec_()

    def __loadFinished(self, result):
        self.frame = self.mainFrame()
        self.app.quit()

url = 'www.baidu.com'
r = WebRender(url)
html = r.frame.toHtml()
p = etree.HTML(html.encode('utf-8'))
print(p)

'''app = QApplication([])
view = QWebEngineView()
view.load(QUrl("http://www.baidu.com/"))
view.show()
page = view.page()

def test():
	#page.runjavascript("your javascript")
    print('ok')

view.loadFinished.connect(test)

app.exec_()'''