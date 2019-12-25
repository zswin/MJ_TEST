#!/usr/bin/python3
# -*- coding: utf-8 -*-

'''
QNetworkAccessManager in PyQt

In this example we get a web page.

Author: Jan Bodnar
Website: zetcode.com
Last edited: September 2017
'''

from PyQt5 import QtNetwork
from PyQt5.QtCore import QCoreApplication, QUrl
import sys


class Example:

    def __init__(self):

        self.doRequest()

    def doRequest(self):
        url2 = "https://quark.1688.com/dashboard/view/cbu.htm?id=244226&QUARK_PARAMS=UL+hrbpqKrJaTx3XTM0OfP5znyMbjWA/Z0DFUAQrsNrE80vMjIR9aiyWHTbf/4nNr4sxXFyBpAGIb7O16D6mfmHxZapbLdNhQJ8nvSR6v4+VsEruDMsR+15aEfOLO/f6A5yk2oARP8W4eh6lcNi3AdQPNxRf/A/Zvqx4WdtpL1MoxS4D1p7+L9lG+i1v2FuHXann/nOL0x3qf3gBjjKIJ9kNLrxAGXgztC+BQ0n2ix7fBIH4o7aBWO1dv6/uSOMsTOTrFlKV7TvvRFblNRfPIFi24booEoIwZR1ufezZP1Uooh8bONkk9jBzzLMYf6i1vVPm9aVsmNozmGXR7FIhOg=="
        url = "http://www.baidu.com"
        req = QtNetwork.QNetworkRequest(QUrl(url2))

        self.nam = QtNetwork.QNetworkAccessManager()
        self.nam.finished.connect(self.handleResponse)
        self.nam.get(req)

    def handleResponse(self, reply):

        er = reply.error()

        if er == QtNetwork.QNetworkReply.NoError:

            bytes_string = reply.readAll()
            print(str(bytes_string, 'utf-8'))

        else:
            print("Error occured: ", er)
            print(reply.errorString())

        QCoreApplication.quit()


app = QCoreApplication([])
ex = Example()
sys.exit(app.exec_())