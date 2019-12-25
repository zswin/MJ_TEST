from selenium import webdriver
from selenium.webdriver import ChromeOptions
import sys

def tes():
    url="https://quark.1688.com/dashboard/view/cbu.htm?id=244226&QUARK_PARAMS=UL+hrbpqKrJaTx3XTM0OfP5znyMbjWA/Z0DFUAQrsNrE80vMjIR9aiyWHTbf/4nNr4sxXFyBpAGIb7O16D6mfmHxZapbLdNhQJ8nvSR6v4+VsEruDMsR+15aEfOLO/f6A5yk2oARP8W4eh6lcNi3AdQPNxRf/A/Zvqx4WdtpL1MoxS4D1p7+L9lG+i1v2FuHXann/nOL0x3qf3gBjjKIJ9kNLrxAGXgztC+BQ0n2ix7fBIH4o7aBWO1dv6/uSOMsTOTrFlKV7TvvRFblNRfPIFi24booEoIwZR1ufezZP1Uooh8bONkk9jBzzLMYf6i1vVPm9aVsmNozmGXR7FIhOg=="
    url2='https://zhuanlan.zhihu.com/c_1047791597869199360'
    options = ChromeOptions()
    options.add_argument('lang=zh-CN,zh,zh-TW,en-US,en')
    #options.add_argument('--headless')
    options.add_argument(
        'user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36')
    options.add_argument("--no-sandbox")
    options.add_argument('--disable-gpu')
    options.add_argument("--proxy-server=127.0.0.1:8080")

    options.add_experimental_option('excludeSwitches', ['enable-automation'])
    options.add_experimental_option("prefs", {"profile.managed_default_content_settings.images": 2})
    br = webdriver.Chrome(options=options)
    br.get(url)
    x= br.find_element_by_xpath('/html/body/div[1]/div/div/div[3]/div[1]/div/div/div/div[2]/div/div[1]/div/div[2]/div/div/div/div/div/span/span/div/div/div[1]/table/tbody').text
    br.quit()
    print(x)

if __name__ == '__main__':
    tes()