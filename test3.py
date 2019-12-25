import sys

# third-party imports
import requests
from bs4 import BeautifulSoup
from pyvirtualdisplay import Display
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtWidgets import QApplication


class Render(QWebEngineView):
    """Render HTML with PyQt5 WebKit."""

    def __init__(self, html):
        self.html = None
        self.app = QApplication(sys.argv)
        QWebEngineView.__init__(self)
        self.loadFinished.connect(self._loadFinished)
        self.mainFrame().setHtml(html)
        self.app.exec_()

    def _loadFinished(self, result):
        self.html = self.mainFrame().toHtml()
        self.app.quit()


url = 'https://impythonist.wordpress.com/2015/01/06/ultimate-guide-for-scraping-javascript-rendered-web-pages/'

# get the raw HTML
source_html = requests.get(url).text

# return the JavaScript rendered HTML
rendered_html = Render(source_html).html

# get the BeautifulSoup
soup = BeautifulSoup(rendered_html, 'html.parser')

print('title is %r' % soup.select_one('title').text)