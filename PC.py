import requests
import time


def bian():
    cookies = {
        '_ga': 'GA1.2.781920884.1685725901',
        '_gid': 'GA1.2.1602389429.1685725901',
        'bnc-uuid': '23a1a435-fe2a-4d4b-b5b0-77e7dd079cdc',
        'c2c-menu-ssbt': 'true',
        'c2c-menu-ssct': 'false',
        'sys_mob': 'no',
        'common_fiat': 'VND',
        'userPreferredCurrency': 'USD_USD',
        'BNC_FV_KEY': '33bd62f75e92aa818374c29c27cf56fa9fe7f2da',
        'sajssdk_2015_cross_new_user': '1',
        'sensorsdata2015jssdkcross': '%7B%22distinct_id%22%3A%221887d17ff8037c-0c5716d366e442-26031d51-2073600-1887d17ff811265%22%2C%22first_id%22%3A%22%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%2C%22%24latest_referrer%22%3A%22%22%7D%2C%22identities%22%3A%22eyIkaWRlbnRpdHlfY29va2llX2lkIjoiMTg4N2QxN2ZmODAzN2MtMGM1NzE2ZDM2NmU0NDItMjYwMzFkNTEtMjA3MzYwMC0xODg3ZDE3ZmY4MTEyNjUifQ%3D%3D%22%2C%22history_login_id%22%3A%7B%22name%22%3A%22%22%2C%22value%22%3A%22%22%7D%2C%22%24device_id%22%3A%221887d17ff8037c-0c5716d366e442-26031d51-2073600-1887d17ff811265%22%7D',
        'OptanonAlertBoxClosed': '2023-06-02T17:11:54.957Z',
        'source': 'referral',
        'campaign': 'p2p.binance.com',
        'BNC_FV_KEY_EXPIRE': '1685824995036',
        'OptanonConsent': 'isGpcEnabled=0&datestamp=Sat+Jun+03+2023+23%3A19%3A11+GMT%2B0800+(%E4%B8%AD%E5%9B%BD%E6%A0%87%E5%87%86%E6%97%B6%E9%97%B4)&version=202211.1.0&isIABGlobal=false&hosts=&consentId=34f8c220-9c73-4ae9-830d-33bb7d5819ce&interactionCount=1&landingPath=NotLandingPage&groups=C0001%3A1%2CC0003%3A0%2CC0004%3A0%2CC0002%3A0&geolocation=PH%3B00&AwaitingReconsent=false',
    }

    headers = {
        'authority': 'p2p.binance.com',
        'accept': '*/*',
        'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8',
        'bnc-uuid': '23a1a435-fe2a-4d4b-b5b0-77e7dd079cdc',
        'c2ctype': 'c2c_merchant',
        'clienttype': 'web',
        'content-type': 'application/json',
        # 'cookie': '_ga=GA1.2.781920884.1685725901; _gid=GA1.2.1602389429.1685725901; bnc-uuid=23a1a435-fe2a-4d4b-b5b0-77e7dd079cdc; c2c-menu-ssbt=true; c2c-menu-ssct=false; sys_mob=no; common_fiat=VND; userPreferredCurrency=USD_USD; BNC_FV_KEY=33bd62f75e92aa818374c29c27cf56fa9fe7f2da; sajssdk_2015_cross_new_user=1; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%221887d17ff8037c-0c5716d366e442-26031d51-2073600-1887d17ff811265%22%2C%22first_id%22%3A%22%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%2C%22%24latest_referrer%22%3A%22%22%7D%2C%22identities%22%3A%22eyIkaWRlbnRpdHlfY29va2llX2lkIjoiMTg4N2QxN2ZmODAzN2MtMGM1NzE2ZDM2NmU0NDItMjYwMzFkNTEtMjA3MzYwMC0xODg3ZDE3ZmY4MTEyNjUifQ%3D%3D%22%2C%22history_login_id%22%3A%7B%22name%22%3A%22%22%2C%22value%22%3A%22%22%7D%2C%22%24device_id%22%3A%221887d17ff8037c-0c5716d366e442-26031d51-2073600-1887d17ff811265%22%7D; OptanonAlertBoxClosed=2023-06-02T17:11:54.957Z; source=referral; campaign=p2p.binance.com; BNC_FV_KEY_EXPIRE=1685824995036; OptanonConsent=isGpcEnabled=0&datestamp=Sat+Jun+03+2023+23%3A19%3A11+GMT%2B0800+(%E4%B8%AD%E5%9B%BD%E6%A0%87%E5%87%86%E6%97%B6%E9%97%B4)&version=202211.1.0&isIABGlobal=false&hosts=&consentId=34f8c220-9c73-4ae9-830d-33bb7d5819ce&interactionCount=1&landingPath=NotLandingPage&groups=C0001%3A1%2CC0003%3A0%2CC0004%3A0%2CC0002%3A0&geolocation=PH%3B00&AwaitingReconsent=false',
        'csrftoken': 'd41d8cd98f00b204e9800998ecf8427e',
        'device-info': 'eyJzY3JlZW5fcmVzb2x1dGlvbiI6IjE5MjAsMTA4MCIsImF2YWlsYWJsZV9zY3JlZW5fcmVzb2x1dGlvbiI6IjE5MjAsMTAzMiIsInN5c3RlbV92ZXJzaW9uIjoiV2luZG93cyAxMCIsImJyYW5kX21vZGVsIjoidW5rbm93biIsInN5c3RlbV9sYW5nIjoiemgtQ04iLCJ0aW1lem9uZSI6IkdNVCs4IiwidGltZXpvbmVPZmZzZXQiOi00ODAsInVzZXJfYWdlbnQiOiJNb3ppbGxhLzUuMCAoV2luZG93cyBOVCAxMC4wOyBXaW42NDsgeDY0KSBBcHBsZVdlYktpdC81MzcuMzYgKEtIVE1MLCBsaWtlIEdlY2tvKSBDaHJvbWUvMTE0LjAuMC4wIFNhZmFyaS81MzcuMzYiLCJsaXN0X3BsdWdpbiI6IlBERiBWaWV3ZXIsQ2hyb21lIFBERiBWaWV3ZXIsQ2hyb21pdW0gUERGIFZpZXdlcixNaWNyb3NvZnQgRWRnZSBQREYgVmlld2VyLFdlYktpdCBidWlsdC1pbiBQREYiLCJjYW52YXNfY29kZSI6IjI5NGRjNWIyIiwid2ViZ2xfdmVuZG9yIjoiR29vZ2xlIEluYy4gKEludGVsKSIsIndlYmdsX3JlbmRlcmVyIjoiQU5HTEUgKEludGVsLCBJbnRlbChSKSBVSEQgR3JhcGhpY3MgNjMwIERpcmVjdDNEMTEgdnNfNV8wIHBzXzVfMCwgRDNEMTEpIiwiYXVkaW8iOiIxMjQuMDQzNDc1Mjc1MTYwNzQiLCJwbGF0Zm9ybSI6IldpbjMyIiwid2ViX3RpbWV6b25lIjoiQXNpYS9TaGFuZ2hhaSIsImRldmljZV9uYW1lIjoiQ2hyb21lIFYxMTQuMC4wLjAgKFdpbmRvd3MpIiwiZmluZ2VycHJpbnQiOiI4YjY4ODFlNzgwYzllZDYyMzQ3ZmJjMzcxNjgyZTY2MiIsImRldmljZV9pZCI6IiIsInJlbGF0ZWRfZGV2aWNlX2lkcyI6IiJ9',
        'fvideo-id': '33bd62f75e92aa818374c29c27cf56fa9fe7f2da',
        'lang': 'zh-CN',
        'origin': 'https://p2p.binance.com',
        'referer': 'https://p2p.binance.com/zh-CN/trade/sell/USDT?fiat=VND&payment=ALL&asset=USDT',
        'sec-ch-ua': '"Not.A/Brand";v="8", "Chromium";v="114", "Google Chrome";v="114"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36',
        'x-passthrough-token': '',
        'x-trace-id': 'd6d00a98-e609-4fc5-a243-d49fa64442f1',
        'x-ui-request-trace': 'd6d00a98-e609-4fc5-a243-d49fa64442f1',
    }

    json_data = {
        'fiat': 'VND',
        'page': 1,
        'rows': 10,
        'tradeType': 'sell',
        'asset': 'USDT',
        'countries': [],
        'proMerchantAds': False,
        'publisherType': None,
        'payTypes': [],
    }

    response = requests.post(
        'https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search',
        cookies=cookies,
        headers=headers,
        json=json_data,
    )

    r = response.json()
    U2V = []
    U2Vprice = []
    U2V.append('币安 [USDT TO VND]\n')
    U2V.append(time.strftime("%m-%d %H:%M:%S ", time.localtime()) + '实时汇率 \n \n')
    for i in range(0, 10):
        HS = r['data'][i]['adv']['price'] + '  ' + r['data'][i]['advertiser']['nickName']
        HLprice = r['data'][i]['adv']['price']
        U2Vprice.append(float(HLprice))
        U2V.append(HS + '\n')
        i = i + 1
    U2VMAX = max(U2Vprice)
    U2VABG = round(sum(U2Vprice) / len(U2Vprice), 2)
    U2V.append('\n最高价:' + str(U2VMAX) + '\n平均价:' + str(U2VABG))
    USDT_TO_VND = ''.join(U2V)
    print(USDT_TO_VND)
    return USDT_TO_VND



bian()


def ox():
    cookies = {
        'devId': 'a16ce3c4-441e-4857-95a0-cb3ae69b3bcc',
        'intercom-id-ny9cf50h': '931973a6-cb18-4e26-9a88-d9afbd90403b',
        'intercom-device-id-ny9cf50h': '7dc9f15c-eda6-4e7b-bcaa-eb3352029811',
        'G_ENABLED_IDPS': 'google',
        'preferLocale': 'zh_CN',
        '_okcoin_legal_currency': 'CNY',
        'amp_21c676': 'VEVf_JjpfogqJQ9WW466kN.bk1COHdEOXBVS0FXbThYc3BUR1pkZz09..1h0vjv6q6.1h0vk3p1i.3.1.4',
        'first_ref': 'https%3A%2F%2Fwww.okx.com%2Fcn',
        '__zlcmid': '1Fylq1gURSkr8sf',
        'locale': 'zh_CN',
        'isLogin': '1',
        'connectedWallet': '1',
        '_ga': 'GA1.1.8923041860.9213780525',
        'intercom-session-ny9cf50h': 'SGEzTjR1eEltWm9JVnVjWHZBU0tGSmZxdEZldW1ibEhaVlVMdFIvQnc1VGd2RnVZdkQvRysvYXNTUHlCT01TTS0ta1dvSGJJTVlpdXRGeGFLdFJaZUdBdz09--8a8c4b69ed23987c347d18aee940e4e7e68e3db4',
        '_ga_G0EKWWQGTZ': 'GS1.1.1685851187.11.0.1685851187.60.0.0',
        '__cf_bm': 'VRqdP02jwOzQ36DW2kxqQtkUBorDVOhd0HR.a6fz7Pg-1685965026-0-AWyiSr0q4Dstz4Y6luUX67ICUmJHxt4zXlHNiTb736Vs7li2WpzbxaM42wTi/985FBGW0hP67UZpOw6MKzIiOFc=',
        'token': 'eyJhbGciOiJIUzUxMiJ9.eyJqdGkiOiJleDExMDE2ODU1MzM1Mjk1NDA2RjFGNEU4NTgwQjI0OENGMVBqdVYiLCJ1aWQiOiIrbm5QWXRVNFAzcVdTTnd2UHdFRjRBPT0iLCJzdGEiOjAsIm1pZCI6IitublBZdFU0UDNxV1NOd3ZQd0VGNEE9PSIsImlhdCI6MTY4NTk2NTAzOCwiZXhwIjoxNjg2NTY5ODM4LCJiaWQiOjAsImRvbSI6Ind3dy5va3guY29tIiwiZWlkIjoxLCJpc3MiOiJva2NvaW4iLCJzdWIiOiI2NkM2N0JCODFDNDEyREI3RkUxOUU3RjdDNUZCQTcxQSJ9.wrBIBJfHDFM9icB5EEbDFOYo3g2iV4gNCTlZauHyYxM_kZ4m89Kna3oiMmlZ6xVeRgNy9gsoqtoJoftj29UrTQ',
        'ok-ses-id': 'StgCm5MHdh6zCVlmx7kRa2jpDJHvELQLFFlOPJDzytvH+ssntZP6OagnWp3yRYpGnhsWC95I/hu51DnRoumaDOdIQW7PZkt6Ele0Kf1N7add46eLW8Y15dO5FPFTSr0r',
        'okg.currentMedia': 'lg',
        '_monitor_extras': '{"deviceId":"kaMpRblDoPpP_PBmurpoHS","eventId":1218,"sequenceNumber":1218}',
        'amp_56bf9d': 'D1pinx8_6FvP4FTY5aNYPg.M3hpUlZDTXFXdVZtWWJFeWhqcUpadz09..1h25li0dl.1h25li54q.nt.2n.qk',
    }

    headers = {
        'authority': 'www.okx.com',
        'accept': 'application/json',
        'accept-language': 'zh-CN',
        'app-type': 'web',
        'authorization': 'eyJhbGciOiJIUzUxMiJ9.eyJqdGkiOiJleDExMDE2ODU1MzM1Mjk1NDA2RjFGNEU4NTgwQjI0OENGMVBqdVYiLCJ1aWQiOiIrbm5QWXRVNFAzcVdTTnd2UHdFRjRBPT0iLCJzdGEiOjAsIm1pZCI6IitublBZdFU0UDNxV1NOd3ZQd0VGNEE9PSIsImlhdCI6MTY4NTk2NTAzOCwiZXhwIjoxNjg2NTY5ODM4LCJiaWQiOjAsImRvbSI6Ind3dy5va3guY29tIiwiZWlkIjoxLCJpc3MiOiJva2NvaW4iLCJzdWIiOiI2NkM2N0JCODFDNDEyREI3RkUxOUU3RjdDNUZCQTcxQSJ9.wrBIBJfHDFM9icB5EEbDFOYo3g2iV4gNCTlZauHyYxM_kZ4m89Kna3oiMmlZ6xVeRgNy9gsoqtoJoftj29UrTQ',
        # 'cookie': 'devId=a16ce3c4-441e-4857-95a0-cb3ae69b3bcc; intercom-id-ny9cf50h=931973a6-cb18-4e26-9a88-d9afbd90403b; intercom-device-id-ny9cf50h=7dc9f15c-eda6-4e7b-bcaa-eb3352029811; G_ENABLED_IDPS=google; preferLocale=zh_CN; _okcoin_legal_currency=CNY; amp_21c676=VEVf_JjpfogqJQ9WW466kN.bk1COHdEOXBVS0FXbThYc3BUR1pkZz09..1h0vjv6q6.1h0vk3p1i.3.1.4; first_ref=https%3A%2F%2Fwww.okx.com%2Fcn; __zlcmid=1Fylq1gURSkr8sf; locale=zh_CN; isLogin=1; connectedWallet=1; _ga=GA1.1.8923041860.9213780525; intercom-session-ny9cf50h=SGEzTjR1eEltWm9JVnVjWHZBU0tGSmZxdEZldW1ibEhaVlVMdFIvQnc1VGd2RnVZdkQvRysvYXNTUHlCT01TTS0ta1dvSGJJTVlpdXRGeGFLdFJaZUdBdz09--8a8c4b69ed23987c347d18aee940e4e7e68e3db4; _ga_G0EKWWQGTZ=GS1.1.1685851187.11.0.1685851187.60.0.0; __cf_bm=VRqdP02jwOzQ36DW2kxqQtkUBorDVOhd0HR.a6fz7Pg-1685965026-0-AWyiSr0q4Dstz4Y6luUX67ICUmJHxt4zXlHNiTb736Vs7li2WpzbxaM42wTi/985FBGW0hP67UZpOw6MKzIiOFc=; token=eyJhbGciOiJIUzUxMiJ9.eyJqdGkiOiJleDExMDE2ODU1MzM1Mjk1NDA2RjFGNEU4NTgwQjI0OENGMVBqdVYiLCJ1aWQiOiIrbm5QWXRVNFAzcVdTTnd2UHdFRjRBPT0iLCJzdGEiOjAsIm1pZCI6IitublBZdFU0UDNxV1NOd3ZQd0VGNEE9PSIsImlhdCI6MTY4NTk2NTAzOCwiZXhwIjoxNjg2NTY5ODM4LCJiaWQiOjAsImRvbSI6Ind3dy5va3guY29tIiwiZWlkIjoxLCJpc3MiOiJva2NvaW4iLCJzdWIiOiI2NkM2N0JCODFDNDEyREI3RkUxOUU3RjdDNUZCQTcxQSJ9.wrBIBJfHDFM9icB5EEbDFOYo3g2iV4gNCTlZauHyYxM_kZ4m89Kna3oiMmlZ6xVeRgNy9gsoqtoJoftj29UrTQ; ok-ses-id=StgCm5MHdh6zCVlmx7kRa2jpDJHvELQLFFlOPJDzytvH+ssntZP6OagnWp3yRYpGnhsWC95I/hu51DnRoumaDOdIQW7PZkt6Ele0Kf1N7add46eLW8Y15dO5FPFTSr0r; okg.currentMedia=lg; _monitor_extras={"deviceId":"kaMpRblDoPpP_PBmurpoHS","eventId":1218,"sequenceNumber":1218}; amp_56bf9d=D1pinx8_6FvP4FTY5aNYPg.M3hpUlZDTXFXdVZtWWJFeWhqcUpadz09..1h25li0dl.1h25li54q.nt.2n.qk',
        'devid': 'a16ce3c4-441e-4857-95a0-cb3ae69b3bcc',
        'ftid': '521052002519135.0116dba12774b5890184d6035b8cf672eb191.1010L8o0.92C0BD105BB3DCC5',
        'referer': 'https://www.okx.com/cn/p2p-markets/cny/buy-usdt',
        'sec-ch-ua': '"Not.A/Brand";v="8", "Chromium";v="114", "Google Chrome";v="114"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'timeout': '10000',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36',
        'x-cdn': 'https://static.okx.com',
        'x-locale': 'zh_CN',
        'x-utc': '8',
    }

    params = {
        't': '1685965052444',
        'quoteCurrency': 'cny',
        'baseCurrency': 'usdt',
        'side': 'sell',
        'paymentMethod': 'bank',
        'userType': 'all',
        'showTrade': 'false',
        'receivingAds': 'false',
        'showFollow': 'false',
        'showAlreadyTraded': 'false',
        'isAbleFilter': 'false',
    }

    response = requests.get('https://www.okx.com/v3/c2c/tradingOrders/books', params=params, cookies=cookies,
                            headers=headers)
    r = response.json()
    U2C = []
    U2Cprice = []
    U2C.append('欧易 [USDT TO CNY]\n')
    U2C.append(time.strftime("%m-%d %H:%M:%S ", time.localtime()) + '实时汇率 \n \n')
    for i in range(0, 10):
        HS = r['data']['sell'][i]['price'] + '  ' + r['data']['sell'][i]['nickName']
        HLprice = r['data']['sell'][i]['price']
        U2Cprice.append(float(HLprice))
        U2C.append(HS + '\n')
        i = i + 1
    U2CMAX = max(U2Cprice)
    U2CABG = round(sum(U2Cprice) / len(U2Cprice), 2)
    U2C.append('\n最高价:' + str(U2CMAX) + '\n平均价:' + str(U2CABG))
    USDT_TO_CNY = ''.join(U2C)
    print(USDT_TO_CNY)
    return USDT_TO_CNY

ox()
