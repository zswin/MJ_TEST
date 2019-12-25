
def render(source_url):
    """Fully render HTML, JavaScript and all."""

    import sys
    from PyQt5.QtWidgets import QApplication
    from PyQt5.QtCore import QUrl
    from PyQt5.QtWebEngineWidgets import QWebEngineView

    class Render(QWebEngineView):
        def __init__(self, url):
            self.html = None
            self.app = QApplication(sys.argv)
            QWebEngineView.__init__(self)
            self.loadFinished.connect(self._loadFinished)
            # self.setHtml(html)
            self.load(QUrl(url))
            self.app.exec_()

        def _loadFinished(self, result):
            # This is an async call, you need to wait for this
            # to be called before closing the app
            self.page().toHtml(self._callable)

        def _callable(self, data):
            self.html = data
            # Data has been stored, it's safe to quit the app
            self.app.quit()

    return Render(source_url).html

# url = 'http://webscraping.com'
# url='http://www.amazon.com'
if __name__ == '__main__':
    url ="https://www.ncbi.nlm.nih.gov/nuccore/CP002059.1"
    url2="https://quark.1688.com/dashboard/view/cbu.htm?id=244226&QUARK_PARAMS=UL+hrbpqKrJaTx3XTM0OfP5znyMbjWA/Z0DFUAQrsNrE80vMjIR9aiyWHTbf/4nNr4sxXFyBpAGIb7O16D6mfmHxZapbLdNhQJ8nvSR6v4+VsEruDMsR+15aEfOLO/f6A5yk2oARP8W4eh6lcNi3AdQPNxRf/A/Zvqx4WdtpL1MoxS4D1p7+L9lG+i1v2FuHXann/nOL0x3qf3gBjjKIJ9kNLrxAGXgztC+BQ0n2ix7fBIH4o7aBWO1dv6/uSOMsTOTrFlKV7TvvRFblNRfPIFi24booEoIwZR1ufezZP1Uooh8bONkk9jBzzLMYf6i1vVPm9aVsmNozmGXR7FIhOg=="
    txt = render(url2)
    print(txt)
    with open('d:/zs/mj/test2.txt', 'w', encoding='utf-8') as f:
        f.write(txt)