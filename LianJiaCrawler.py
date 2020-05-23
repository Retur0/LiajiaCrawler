import requests
import csv
import time
import random
from bs4 import BeautifulSoup  # 网页解析


def askUrl(url):
    head = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36 Edg/81.0.416.77",
        "Cookie": "elect_city=110000; lianjia_uuid=2ad4c6a9-23ce-40c8-989d-d4a981c97e0b; Hm_lvt_9152f8221cb6243a53c83b956842be8a=1590140979; _smt_uid=5ec7a032.565e3a19; UM_distinctid=1723bc9c62867-093e95ee5c9704-70657c6e-1fa400-1723bc9c62915c; _jzqc=1; _jzqckmp=1; _qzjc=1; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%221723bc9c8e72c2-0c8588ca01b0d8-70657c6e-2073600-1723bc9c8e87fc%22%2C%22%24device_id%22%3A%221723bc9c8e72c2-0c8588ca01b0d8-70657c6e-2073600-1723bc9c8e87fc%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_referrer%22%3A%22%22%2C%22%24latest_referrer_host%22%3A%22%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%7D%7D; _gid=GA1.2.1778974911.1590140981; _ga=GA1.2.396896521.1590140981; Hm_lpvt_9152f8221cb6243a53c83b956842be8a=1590142574; lianjia_ssid=58aef8b3-721b-4a88-a1c4-47508b67a2fb; CNZZDATA1253477573=1800620365-1590137485-%7C1590225180; CNZZDATA1254525948=1196481690-1590137141-%7C1590223655; CNZZDATA1255633284=1477469989-1590139665-%7C1590226261; CNZZDATA1255604082=1534079261-1590139766-%7C1590226393; _jzqa=1.1627336090204837000.1590140979.1590140979.1590226467.2; login_ucid=2000000111931293; lianjia_token=2.0059613e843a4fbcf548cc17b591ea700c; lianjia_token_secure=2.0059613e843a4fbcf548cc17b591ea700c; security_ticket=si3KslN02zy6AfMjQpWQc74i/MVVnHzKNqzWXTKexxzmCn3RYzby1iF/agDMdTMvviEVmQmz97IvPfxACGZcaPRS2T0+9JWSfSBEhUysFmcNifekITxFc6Xmdep2oTB7tiYH7R9QIUZnh85DUmOwOAopj1nmaNNHSREeGIwKxbY=; _qzja=1.782221497.1590140978869.1590140978870.1590226467188.1590226467188.1590226560922.0.0.0.4.2; _qzjb=1.1590226467188.2.0.0.0; _qzjto=2.1.0; _jzqb=1.2.10.1590226467.1; srcid=eyJ0Ijoie1wiZGF0YVwiOlwiZGZmM2E4NTEwNjI1ZGQ0MDI5YWI5YTE0NmVhN2E5NzRkODg0ZDhiNDE1Y2UxYWI1MTRhM2I5NTBkY2M5ZWRlMTE0ZTIxMzBmZjhkYzVkYjIwMWVjYmQyMzZkMDRkNjczZGQyODlmYzI3MjUwODgwNmI4MDQ1ODk4MWZhYWU5YzhkMWZjNjRhYzU3YmZhM2VlZGEyMjI4YjFmYzNlMWE1ZGQyZDRhZDgyYmU5ZWZkMmI0ZjViMjY0MmU3ODg1MGZhNjcyMmQ4YjhiMjI1MTkxMjg1YmE3MjdiMGEyZGJmNzViMGY3ZjFkZTRkNTI3ZDU2MjFhYTMwY2U0ZDcxYzJiNGRkZTVkMTRhNWIwMmJkOTM2MWVhMmVhYmYyMjc2M2RjYWMwODRhNWQ2MGFjN2RlMjAxMzI3MDI3MDc1MWQ3MjkzODdkYzZjOTQ2YTJmNTllMzYyOWU3MWY1NWY5ZGJkOFwiLFwia2V5X2lkXCI6XCIxXCIsXCJzaWduXCI6XCJhOWI4Y2QzZlwifSIsInIiOiJodHRwczovL2JqLmxpYW5qaWEuY29tLyIsIm9zIjoid2ViIiwidiI6IjAuMSJ9; _gat=1; _gat_past=1; _gat_global=1; _gat_new_global=1; _gat_dianpu_agent=1",
        "Accept": "text / html, application / xhtml + xml, application / xml;q = 0.9, image / webp, image / apng, * / *;q = 0.8, application / signed - exchange;v = b3;q = 0.9",
        "Connection": "keep-alive"
    }
    try:
        response = requests.get(url, headers=head, timeout=10)
        return response.text
    except requests.exceptions.RequestException as e:
        print('第二次尝试获取 ', url)
        try:
            response = requests.get(url, headers=head, timeout=10)
            return response.text
        except requests.exceptions.RequestException as e:
            print('获取', url, '失败')
            return ''



def getData(url):
    datalist = []
    html = askUrl(url)
    if html == '':
        return ''
    bs = BeautifulSoup(html, "html.parser")
    list = bs.find_all("div", class_="content__list--item--main")

    for item in list:
        try:
            info1 = item.contents[1].contents[1].string.strip()
            info2 = item.contents[3].contents[1].string.strip() + "-" + item.contents[3].contents[3].string.strip() + "-" + \
                    item.contents[3].contents[5].string.strip()
            info3 = item.contents[3].contents[8].string.strip()
            info4 = item.contents[3].contents[10].string.strip()
            if '南' in info4 or '北' in info4 or '东' in info4 or '西' in info4:
                info5 = item.contents[3].contents[12].string.strip()
                info6 = item.contents[3].contents[13].contents[2].string.replace(" ", "").replace("\n", "")
            else:
                info4 = ''
                info5 = item.contents[3].contents[10].string.strip()
                info6 = item.contents[3].contents[11].contents[2].string.replace(" ", "").replace("\n", "")
            info7 = item.contents[9].contents[0].contents[0]
        except:
            print(url, '数据筛选出现了问题')
            continue

        datalist.append([info1, info2, info3, info4, info5, info6, info7])

    return datalist


def saveData(datalist):
    headers = ['摘要', '位置', '大小', '朝向', '户型', '楼层', '价格（元/月）']
    file = open('data.csv', 'a', newline='', encoding='UTF-8')
    csvf = csv.writer(file)
    csvf.writerows(datalist)


def getBigAreaList(url):
    bigAreaList = []
    html = askUrl(url)
    bs = BeautifulSoup(html, "html.parser")
    list = bs.find_all("li", class_="filter__item--level2")

    for item in list:
        href = item.contents[1].get('href')
        if 'ditie' in href or href == "/zufang/":
            continue
        bigAreaList.append(href)

    return bigAreaList


def getSamllAreaList(bigAreaList):
    samllAreaList = []
    for bhref in bigAreaList:
        url = "https://bj.lianjia.com" + bhref
        html = askUrl(url)
        bs = BeautifulSoup(html, "html.parser")
        list = bs.find_all("li", class_="filter__item--level3")
        for item in list:
            href = item.contents[1].get("href")
            if href == bhref:
                continue
            samllAreaList.append(href)

    return samllAreaList


if __name__ == "__main__":
    baseurl = "https://bj.lianjia.com/zufang"
    counter = 0
    start = time.time()
    failedUrls = []

    print('开始获取网页列表')
    list = getSamllAreaList(getBigAreaList(baseurl))
    print('获取网页列表结束')

    for href in list:
        url = "https://bj.lianjia.com" + href
        print(url, '开始获取房数')
        html = askUrl(url)
        if html == '':
            failedUrls.append(url)
            continue
        bs = BeautifulSoup(html, "html.parser")
        num = int(bs.find("span", class_="content__title--hl").string)
        print('共有 ', num, ' 套')

        if num == 0:
            continue

        for i in range(1, num // 30 + 2):
            counter = counter + 1
            print('开始获取', url + "pg" + str(i))
            datalist = getData(url + "pg" + str(i))
            if datalist == '':
                print('没有获取到')
                failedUrls.append(url + "pg" + str(i))
                counter = counter - 1
                continue
            saveData(datalist)
            print('第 ' + str(counter) + ' 个页面数据已保存')
        time.sleep(random.random())

    end = time.time()
    print('总共用时：', int((end - start) // 60), ' 分钟', int((end - start) % 60), '秒')
    print('请求失败连接数：', len(failedUrls))

