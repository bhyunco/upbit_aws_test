# 모든 함수를 한번에 실행

# 거래소 구조 설명 https://docs.upbit.com/docs
# 원화거래 / BTC 거래 / USDT 거래
# 1.업비트의 코인 종류 체크

from urllib.parse import urlencode
import hashlib
import uuid
import jwt
import os
import pandas as pd
import time
import requests
import json


def coins(current):
    url = "https://api.upbit.com/v1/market/all"
    querystring = {"isDetails": "true"}
    response = requests.request("GET", url, params=querystring)
    response_json = json.loads(response.text)

    KRWticker = []
    BTCticker = []
    USDTticker = []

    for a in response_json:
        #     print(a['market'])
        if "KRW-" in a['market']:
            KRWticker.append(a['market'])
        elif "BTC-" in a['market']:
            BTCticker.append(a['market'])
        elif "USDT-" in a['market']:
            USDTticker.append(a['market'])
    ticker = {
        "KRW": KRWticker,
        "BTC": BTCticker,
        "USDT": USDTticker
    }
#     print(ticker)
    if current == "ALL":
        ticker = ticker
    else:
        ticker = ticker[current]
    return ticker


# 암호화폐 시세조회


def coin_price(coin):
    url = "https://api.upbit.com/v1/orderbook"
    querystring = {"markets": coin}
    response = requests.request("GET", url, params=querystring)
    response_json = json.loads(response.text)
    coin_now_price = response_json[0]["orderbook_units"][0]["ask_price"]
    return coin_now_price
# 시세 호가 정보(Orderbook) 조회 // 호가 정보 조회


def coin_history(coin, time1='minute', time2=""):
    url = f"https://api.upbit.com/v1/candles/{time1}/{time2}"

    querystring = {"market": coin, "count": "200"}

    response = requests.request("GET", url, params=querystring)
    response_json = json.loads(response.text)
    # print(type(response_json))
    df = pd.DataFrame(response_json)
    return df

# 로그인


def login():
    global access_key
    global secret_key
    access_key = input("access_key : ")
    secret_key = input("secret_key : ")


# 나의 계좌 잔액 조회


def balance():
    global server_url
    server_url = 'https://api.upbit.com'

    payload = {
        'access_key': access_key,
        'nonce': str(uuid.uuid4()),
    }

    jwt_token = jwt.encode(payload, secret_key)
    authorize_token = 'Bearer {}'.format(jwt_token)
    headers = {"Authorization": authorize_token}

    res = requests.get(server_url + "/v1/accounts", headers=headers)
    return res.json()


# 매수(지정가)


# access_key = os.environ['UPBIT_OPEN_API_ACCESS_KEY']
# secret_key = os.environ['UPBIT_OPEN_API_SECRET_KEY']
# server_url = os.environ['UPBIT_OPEN_API_SERVER_URL']

def buy_limit(coin, volume, price):
    query = {
        'market': coin,
        'side': 'bid',
        'volume': volume,
        'price': price,
        'ord_type': 'limit',
    }
    query_string = urlencode(query).encode()

    m = hashlib.sha512()
    m.update(query_string)
    query_hash = m.hexdigest()

    payload = {
        'access_key': access_key,
        'nonce': str(uuid.uuid4()),
        'query_hash': query_hash,
        'query_hash_alg': 'SHA512',
    }

    jwt_token = jwt.encode(payload, secret_key)
    authorize_token = 'Bearer {}'.format(jwt_token)
    headers = {"Authorization": authorize_token}

    res = requests.post(server_url + "/v1/orders",
                        params=query, headers=headers)
    print(res.json())
    return res.json()


# 매수(시장가)


# access_key = os.environ['UPBIT_OPEN_API_ACCESS_KEY']
# secret_key = os.environ['UPBIT_OPEN_API_SECRET_KEY']
# server_url = os.environ['UPBIT_OPEN_API_SERVER_URL']

def buy_market(coin, price):
    query = {
        'market': coin,
        'side': 'bid',
        'volume': '',
        'price': price,
        'ord_type': 'price',
    }
    query_string = urlencode(query).encode()

    m = hashlib.sha512()
    m.update(query_string)
    query_hash = m.hexdigest()

    payload = {
        'access_key': access_key,
        'nonce': str(uuid.uuid4()),
        'query_hash': query_hash,
        'query_hash_alg': 'SHA512',
    }

    jwt_token = jwt.encode(payload, secret_key)
    authorize_token = 'Bearer {}'.format(jwt_token)
    headers = {"Authorization": authorize_token}

    res = requests.post(server_url + "/v1/orders",
                        params=query, headers=headers)
    print(res.json())
    return res.json()


# 매도(지정가)


# access_key = os.environ['UPBIT_OPEN_API_ACCESS_KEY']
# secret_key = os.environ['UPBIT_OPEN_API_SECRET_KEY']
# server_url = os.environ['UPBIT_OPEN_API_SERVER_URL']

def sell_limit(coin, volume, price):
    query = {
        'market': coin,
        'side': 'ask',
        'volume': volume,
        'price': price,
        'ord_type': 'limit',
    }
    query_string = urlencode(query).encode()

    m = hashlib.sha512()
    m.update(query_string)
    query_hash = m.hexdigest()

    payload = {
        'access_key': access_key,
        'nonce': str(uuid.uuid4()),
        'query_hash': query_hash,
        'query_hash_alg': 'SHA512',
    }

    jwt_token = jwt.encode(payload, secret_key)
    authorize_token = 'Bearer {}'.format(jwt_token)
    headers = {"Authorization": authorize_token}

    res = requests.post(server_url + "/v1/orders",
                        params=query, headers=headers)
    print(res.json())
    return res.json()

# 매도(시장가)


# access_key = os.environ['UPBIT_OPEN_API_ACCESS_KEY']
# secret_key = os.environ['UPBIT_OPEN_API_SECRET_KEY']
# server_url = os.environ['UPBIT_OPEN_API_SERVER_URL']

def sell_market(coin, volume):
    query = {
        'market': coin,
        'side': 'ask',
        'volume': volume,
        'price': '',
        'ord_type': 'market',
    }
    query_string = urlencode(query).encode()

    m = hashlib.sha512()
    m.update(query_string)
    query_hash = m.hexdigest()

    payload = {
        'access_key': access_key,
        'nonce': str(uuid.uuid4()),
        'query_hash': query_hash,
        'query_hash_alg': 'SHA512',
    }

    jwt_token = jwt.encode(payload, secret_key)
    authorize_token = 'Bearer {}'.format(jwt_token)
    headers = {"Authorization": authorize_token}

    res = requests.post(server_url + "/v1/orders",
                        params=query, headers=headers)
    print(res.json())
    return res.json()


login()


def price_trim(price_trim):

    # ~10원 미만[소수점 둘째자리]
    if price_trim < 10:
        price_trim = round(price_trim, 2)

    # 10~100원 미만 - [소수점첫째자리]
    elif price_trim < 100:
        price_trim = round(price_trim, 1)

    # 100~1,000원 미만 - [1원단위]
    elif price_trim < 1000:
        price_trim = round(price_trim)

    # 1,000~10,000원 미만[5원단위]
    elif price_trim < 10000:
        price_trim = round(price_trim*2, -1)/2

    # 10,000~100,000원 미만[10원단위]
    elif price_trim < 100000:
        price_trim = round(price_trim, -1)

    # 100,000~500,000원 미만 [50원단위]
    elif price_trim < 500000:
        price_trim = round(price_trim*2, -2)/2

    # 500,000원~1,000,000원 미만[100원단위]
    elif price_trim < 1000000:
        price_trim = round(price_trim, -2)

    # 1,000,000~2,000,000 [500원단위]
    elif price_trim < 2000000:
        price_trim = round(price_trim*2, -3)/2

    # 2,000,000 이상 [1000원단위]
    else:
        price_trim = round(price_trim, -3)

    return price_trim


print("진행9")
while True:

    try:
        # 1분봉으로 200분 안에 제일 하락을 많이 한 코인을 찾기
        # coin_history("KRW-BTC","minutes",30)
        tickers = coins("KRW")
        decrease_top_score = 0.001
        # ticker = "KRW-BTC"
        print("진행10")
        for ticker in tickers:
            coin_1_m = coin_history(ticker, 'minutes', 1)
#             print(coin_1_m)

            max_high_price = coin_1_m["high_price"].max()
            now_price = coin_price(ticker)
        #     print(ticker)
        #     print(max_high_price)
        #     print(now_price)
        #     print("하락률 : " + str(round(((1-(now_price/max_high_price))*100),3)) + "%")
            decrease_percent = round(((1-(now_price/max_high_price))*100), 3)
            if decrease_percent > decrease_top_score:
                decrease_top_score = decrease_percent
                decrease_top_score_ticker = [
                    ticker, max_high_price, now_price, (-1)*decrease_percent]

        print(decrease_top_score_ticker)
        print("진행11")
        for a in balance():
            if a['currency'] == 'KRW':
                print(a['balance'])
                buy_amount = float(a['balance'])*0.10
                print(round(buy_amount, -2))
                buy_amount = round(buy_amount, -2)

        # 해당 코인을 시장가에 구매
        # buy_market()
        buy_market(decrease_top_score_ticker[0], buy_amount)
        time.sleep(3)

        # 구매한 코인이 2% 상승했을 때 판매
        # 판매해야하는 가격
        sell_price = price_trim(coin_price(decrease_top_score_ticker[0])*1.02)
        # 가지고있는 코인갯수
        for a in balance():
            if a['currency'] == decrease_top_score_ticker[0].replace("KRW-", ""):
                sell_balance = a['balance']
        # 지정가에 판매
        sell_limit(decrease_top_score_ticker[0], sell_balance, sell_price)
        print("진행12")
        time.sleep(10)
    except:
        print("진행13")
        time.sleep(10)
    # 30분단위로 반복
