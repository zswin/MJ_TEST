#coding=utf-8
from selenium import webdriver
import requests

def tst():
    url = "https://quark.1688.com/dashboard/view/cbu.htm?id=244226&QUARK_PARAMS=UL+hrbpqKrJaTx3XTM0OfP5znyMbjWA/Z0DFUAQrsNrE80vMjIR9aiyWHTbf/4nNr4sxXFyBpAGIb7O16D6mfmHxZapbLdNhQJ8nvSR6v4+VsEruDMsR+15aEfOLO/f6A5yk2oARP8W4eh6lcNi3AdQPNxRf/A/Zvqx4WdtpL1MoxS4D1p7+L9lG+i1v2FuHXann/nOL0x3qf3gBjjKIJ9kNLrxAGXgztC+BQ0n2ix7fBIH4o7aBWO1dv6/uSOMsTOTrFlKV7TvvRFblNRfPIFi24booEoIwZR1ufezZP1Uooh8bONkk9jBzzLMYf6i1vVPm9aVsmNozmGXR7FIhOg=="
    headers = {
        "accept": "text / javascript, application / javascript, application / ecmascript, application / x - ecmascript, * / *; q = 0.01",
        "accept-encoding": "gzip, deflate, br",
        "accept-language": "zh-CN, zh; q=0.9",
        "content-type": "application / x-www-form-urlencoded;    charset = UTF-8",
        "cookie": "_csrf_token=1542699892655; cna=c4UWFNh73hQCAdrxruJblqwU; JSESSIONID=E0xY8Jo-DFhaA2nG92vN9E2B6J-1YXPv9R-3PMc1; cookie2=27bfff6799fde214c72faad7e43462ec; _tb_token_=577bbbe87ee37; _tmp_ck_0=Fllkyw0NULIEXAfWE5jQPEASZrjs5xQ%2Frawz33oBz5g5a5ul63Or2ZpTW1Uvzk6vts%2BlQCSRpPO%2BN4sXCf%2F732tNI2cHsjOsHPNmQasugzyTCcFaTlQksm%2FXZ1poLsZ%2FEMjNRRtyzn%2F%2Bv%2BRoexIQ758g2nrbz3A3XvjIfFL8WoETM9irx7fYxHGVtY%2FCdFbaOWFWXHwgQVj4bGkZUCJSEAkmQeZUzIZjCOByIdH%2F4q1nGfj6yOl1Odu7BB6qPBLvICAr%2FOhJWz0jzetj5fg2V5P9q2lQMD2aB3Zu%2FPxp%2Bw4YyOqaaLBJJRM5Tk4ljdRzBD7ksZ0ksWzwLyP9AE3whoJNcMpR9d4WStokieQijzpjhN3RDwNRf5F0BbGwGFufE3Haq%2B1%2BLLQ%3D; alicnweb=touch_tb_at%3D1542724002749; LOGIN_MODE=cbu; hng=CN%7Czh-CN%7CCNY%7C156; t=7ee99519e56022a5bf71b1a04bd3dbcd; lid=hzfickle; uc4=id4=0%40U2%2F3341MctffR2oan42KkMkp%2Fw%3D%3D&nk4=0%40CXB8XGU4FMS8RmjZMnBtcDEV6g%3D%3D; __cn_logon__=true; __cn_logon_id__=hzfickle; ali_apache_track=c_mid=b2b-25240914ddbaa|c_lid=hzfickle|c_ms=1; ali_apache_tracktmp=c_w_signed=Y; csg=18c24951; last_mid=b2b-25240914ddbaa; l=cBEvIOZnqwZDjuXaBOfNmuIRX87tnQRfc1Pzw4ZBGICPOpfXATPhWZUORBLWCnGVLspJ-3Wba70LB8T30yUIhMXxMmDSwFLN.; isg=BMnJKC2e8ABS-4x7SHE4LuKA2PXjvpZKy93Vx2s8w7DCsuTEsWfnGDOk9Fah7VWA",
        "origin": "https://quark.1688.com",
        "referer": "https://quark.1688.com/dashboard/view/cbu.htm?id=244226&QUARK_PARAMS=UL+hrbpqKrJaTx3XTM0OfP5znyMbjWA/Z0DFUAQrsNrE80vMjIR9aiyWHTbf/4nNr4sxXFyBpAGIb7O16D6mfmHxZapbLdNhQJ8nvSR6v4+VsEruDMsR+15aEfOLO/f6A5yk2oARP8W4eh6lcNi3AdQPNxRf/A/Zvqx4WdtpL1MoxS4D1p7+L9lG+i1v2FuHXann/nOL0x3qf3gBjjKIJ9kNLrxAGXgztC+BQ0n2ix7fBIH4o7aBWO1dv6/uSOMsTOTrFlKV7TvvRFblNRfPIFi24booEoIwZR1ufezZP1Uooh8bONkk9jBzzLMYf6i1vVPm9aVsmNozmGXR7FIhOg==",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-origin",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.75 Safari/537.36",
        "x-requested-with": "XMLHttpRequest"
    }
    params={
        "action": "WidgetAction",
        "event_submit_doGetWidgetData": "true",
        "callback": "fbi_m_k0f3coiw_10cz",
        "_ts_": "m_k0f3coix_cvyq",
        "callback": "jQuery331023762419635332366_1568194566552"
    }
    data = {
        "param": "{'conditionList':[{'conditionId':'371464','v1':'20190911','v2':'20190911'},{'conditionId':'371485','v1':'HZ01'},{'conditionId':'371470','v1':['天猫高']},{'conditionId':'371471','v1':[]},{'conditionId':'371484','v1':''}],'groupNo':'10304619'}",
        "groupNo": "10304619",
        "widgetId": "382161",
        "encryptWidgetId": "824d84073e671f82",
        "externalFlag": "true",
        "reportId": "244226",
        "env": "pro",
        "requestType": "view",
        "QUARK_PARAMS": "UL+hrbpqKrJaTx3XTM0OfP5znyMbjWA/Z0DFUAQrsNrE80vMjIR9aiyWHTbf/4nNr4sxXFyBpAGIb7O16D6mfmHxZapbLdNhQJ8nvSR6v4+VsEruDMsR+15aEfOLO/f6A5yk2oARP8W4eh6lcNi3AdQPNxRf/A/Zvqx4WdtpL1MoxS4D1p7+L9lG+i1v2FuHXann/nOL0x3qf3gBjjKIJ9kNLrxAGXgztC+BQ0n2ix7fBIH4o7aBWO1dv6/uSOMsTOTrFlKV7TvvRFblNRfPIFi24booEoIwZR1ufezZP1Uooh8bONkk9jBzzLMYf6i1vVPm9aVsmNozmGXR7FIhOg=="
    }
    re = requests.post(url=url, data=data, params = params, headers=headers)
    print(re.status_code)
    print(re.headers.get("content-encoding"))
    with open('d:/zs/test.txt', 'w') as f:
        f.write(re.content.decode('utf-8'))
        f.write(re.text)
    print(re.content)
if __name__ == '__main__':
    tst()
