from flask import Flask, jsonify, request, abort
import os
import re
from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError

# 利用 handler 處理 LINE 觸發事件
from linebot.models import MessageEvent, TextMessage, TextSendMessage


app = Flask(__name__)

# get channel_secret and channel_access_token from your environment variable

channel_secret = os.getenv('LINE_CHANNEL_SECRET', None)
channel_access_token = os.getenv('LINE_CHANNEL_ACCESS_TOKEN', None)

if channel_secret is None:
    print('Specify LINE_CHANNEL_SECRET as environment variable.')
    sys.exit(1)

if channel_access_token is None:
    print('Specify LINE_CHANNEL_ACCESS_TOKEN as environment variable.')
    sys.exit(1)

line_bot_api = LineBotApi(channel_access_token)
parser = WebhookParser(channel_secret)
handler = WebhookHandler(channel_secret)

# 處理訊息
@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    print(event)
    text=event.message.text
    '''
        if (text=="Hi"):
            reply_text = "Hello"
            #Your user ID

        elif(text=="你好"):
            reply_text = "哈囉"
        elif(text=="機器人"):
            reply_text = "叫我嗎"
        else:
            reply_text = text
    #如果非以上的選項，就會學你說話
    '''
    '''
    if (re.match(r'^\d{4}([\/.-])(0?[1-9]|1[012])([\/.-])(0?[1-9]|[12][0-9]|3[01])$', text)):
        reply_text = '您輸入的為日期'
        #splitday = re.split(r'[\/.-]', inputday)
    else:
        reply_text = text
    '''
    reply_text = mooncal(text)

    message = TextSendMessage(text=f'{reply_text}')
    line_bot_api.reply_message(event.reply_token, message)

#@app.route('/')

@app.route("/callback", methods=['POST'])

def index():
    return jsonify({"Choo Choo": "Welcome to your Flask app 🚅"})

def callback():
    signature = request.headers['X-Line-Signature']

    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)

    return 'OK'

def mooncal(input):

    if (re.match(r'^\d{4}([\/.-])(0?[1-9]|1[012])([\/.-])(0?[1-9]|[12][0-9]|3[01])$', input)):
        #return '您輸入的為日期'
        splitday = re.split(r'[\/.-]', input)
        
        map_month = ( 0, 31, 59, 90, 120, 151, 181, 212, 243, 13, 44, 74)

        map_year = {}
        map_year = {
        ('2065', '2013', '1961', '1909'): 217,
        ('2064', '2012', '1960', '1908'): 112,
        ('2063', '2011', '1959', '1907'): 7,
        ('2062', '2010', '1958', '1906'): 162,
        ('2061', '2009', '1957', '1905'): 57,
        ('2060', '2008', '1956', '1904'): 212,
        ('2059', '2007', '1955', '1903'): 107,
        ('2058', '2006', '1954', '1902'): 2,
        ('2057', '2005', '1953', '1901'): 157,
        ('2056', '2004', '1952', '1900'): 52,
        ('2055', '2003', '1951', '1899'): 207,
        ('2054', '2002', '1950', '1898'): 102,
        ('2053', '2001', '1949', '1897'): 257,
        ('2052', '2000', '1948', '1896'): 152,
        ('2051', '1999', '1947', '1895'): 47,
        ('2050', '1998', '1946', '1894'): 202,
        ('2049', '1997', '1945', '1893'): 97,
        ('2048', '1996', '1944', '1892'): 252,
        ('2047', '1995', '1943', '1891'): 147,
        ('2046', '1994', '1942', '1890'): 42,
        ('2045', '1993', '1941', '1889'): 197,
        ('2044', '1992', '1940', '1888'): 92,
        ('2043', '1991', '1939', '1887'): 247,
        ('2042', '1990', '1938', '1886'): 142,
        ('2041', '1989', '1937', '1885'): 37,
        ('2040', '1988', '1936', '1884'): 192,
        ('2039', '1987', '1935', '1883'): 87,
        ('2038', '1986', '1934', '1882'): 242,
        ('2037', '1985', '1933', '1881'): 137,
        ('2036', '1984', '1932', '1880'): 32,
        ('2035', '1983', '1931', '1879'): 187,
        ('2034', '1982', '1930', '1878'): 82,
        ('2033', '1981', '1929', '1877'): 237,
        ('2032', '1980', '1928', '1876'): 132,
        ('2031', '1979', '1927', '1875'): 27,
        ('2030', '1978', '1926', '1874'): 182,
        ('2029', '1977', '1925', '1873'): 77,
        ('2028', '1976', '1924', '1872'): 232,
        ('2027', '1975', '1923', '1871'): 127,
        ('2026', '1974', '1922', '1870'): 22,
        ('2025', '1973', '1921', '1869'): 177,
        ('2024', '1972', '1920', '1868'): 72,
        ('2023', '1971', '1919', '1867'): 227,
        ('2022', '1970', '1918', '1866'): 122,
        ('2021', '1969', '1917', '1865'): 17,
        ('2020', '1968', '1916', '1864'): 172,
        ('2019', '1967', '1915', '1863'): 67,
        ('2018', '1966', '1914', '1862'): 222,
        ('2017', '1965', '1913', '1861'): 117,
        ('2016', '1964', '1912', '1860'): 12,
        ('2015', '1963', '1911', '1859'): 167,
        ('2014', '1962', '1910', '1858'): 62,
        }

        flat_year_dict = {element: value for key, value in map_year.items() for element in key}

        year_int = flat_year_dict[splitday[0]]
        month_int = map_month[int(splitday[1])-1]
        day_int = int(splitday[2])

        kin_num = year_int + month_int + day_int
        if kin_num > 260:
            kin_num = kin_num % 260

        tone = kin_num % 13
        tones = ['宇宙', '磁性', '月亮', '電力', '自我存在', '超頻', '韻律', '共鳴', '銀河星系', '太陽', '行星', '光譜', '水晶',]

        seal = kin_num % 20
        seals = ('黃太陽', '紅龍', '白風', '藍夜', '黃種子', '紅蛇', '白世界橋', '藍手', '黃星星', '紅月', '白狗', '藍猴', '黃人', '紅天行者', '白巫師', '藍鷹', '黃戰士', '紅地球', '白鏡', '藍風暴',)

        #print(f'您的輸入的日期 {splitday[0]} 年 {splitday[1] } 月 {splitday[2]} 日')
        #return ('星系印記 >> Kin' + kin_num + ' ' + tones[tone] + '的' + seals[seal])
        kin_text = '☆星系印記 >>\nKin' + str(kin_num) + ' ' + str(tones[tone]) + '的' + str(seals[seal])
        
        analog = 19 - seal
        antipode = (seal + 10) % 20
        occult = (21 - seal) % 20
        occult_tone = abs(tone - 14) #abs取絕對值
        guide_dict = {
        (1, 6, 11): 0,
        (2, 7, 12): 12,
        (3, 8, 0): 4,
        (4, 9): -4,
        (5, 10): 8,
        }
        flat_guide_dict = {element: value for key, value in guide_dict.items() for element in key}
        guide = (seal + flat_guide_dict[tone]) % 20

        #print(f'五大神諭 >> 支持： {seals[analog]}, 挑戰/強化： {seals[antipode]}, 隱藏／推動： {seals[occult]}, 指引： {seals[guide]}')
        fifth_text = '\n\n★五大神諭 >>\n支持： ' + seals[analog] + ',\n挑戰/強化： '+ seals[antipode] +',\n隱藏/推動： ' + seals[occult] + ',\n指引： ' + seals[guide]

        goddess_tone = (tone * 4 + occult_tone) % 13
        goddess_seal = (guide + 10) % 20 
        #print(f'內在女神 >> {tones[goddess_tone]}的{seals[goddess_seal]}')
        goddess_text = '\n\n♡內在女神 >>\n' + tones[goddess_tone] + '的' + seals[goddess_seal]

        wavespell = (kin_num -1) // 13 
        wavespells = ('紅龍波', '白巫師波', '藍手波', '黃太陽波', '紅天行者波', '白世界橋波', '藍風暴波', '黃人波', '紅蛇波', '白鏡波', '藍猴波', '黃種子波', '紅地球波', '白狗波', '藍夜波', '黃戰士波', '紅月波', '白風波', '藍鷹波', '黃種子波',)
        #print(f'波　　符 >> {wavespells[wavespell]}')
        wavspell_text = '\n\n⚭波　　符 >>\n' + wavespells[wavespell]

        return kin_text + fifth_text + goddess_text + wavspell_text

    else:
        return '請輸入欲查詢的日期（格式建議：2022.1.31）'




if __name__ == '__main__':
    app.run(debug=True, port=os.getenv("PORT", default=5000))
