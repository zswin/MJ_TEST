# -*- coding: utf-8 -*-


import sys
from PyQt5.QtCore import QUrl
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWebEngineWidgets import QWebEnginePage, QWebEngineView

class Render(QWebEngineView):
    def __init__(self, url):
        self.app = QApplication(sys.argv)
        QWebEngineView.__init__(self)
        self.loadFinished.connect(self._loadFinished)
        self.load(QUrl(url))
        self.app.exec_()

    def _loadFinished(self, result):
        # This is an async call, you need to wait for this
        # to be called before closing the app
        self.page().toHtml(self.callable)

    def callable(self, data):
        self.html = data
        # Data has been stored, it's safe to quit the app
        self.app.quit()



import lxml.html

#定义一个网页地址
url = 'https://www.baidu.com'
url2 = "https://quark.1688.com/dashboard/view/cbu.htm?id=244226&QUARK_PARAMS=UL+hrbpqKrJaTx3XTM0OfP5znyMbjWA/Z0DFUAQrsNrE80vMjIR9aiyWHTbf/4nNr4sxXFyBpAGIb7O16D6mfmHxZapbLdNhQJ8nvSR6v4+VsEruDMsR+15aEfOLO/f6A5yk2oARP8W4eh6lcNi3AdQPNxRf/A/Zvqx4WdtpL1MoxS4D1p7+L9lG+i1v2FuHXann/nOL0x3qf3gBjjKIJ9kNLrxAGXgztC+BQ0n2ix7fBIH4o7aBWO1dv6/uSOMsTOTrFlKV7TvvRFblNRfPIFi24booEoIwZR1ufezZP1Uooh8bONkk9jBzzLMYf6i1vVPm9aVsmNozmGXR7FIhOg=="
r = Render(url2)
result = r.html
print(result)
#tree = lxml.html.fromstring(result)
with open('d:/zs/mj/xx.txt', 'w', encoding='utf-8') as f:
    f.write(result)

