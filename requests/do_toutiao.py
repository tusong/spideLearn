import requests

import urllib3
urllib3.disable_warnings()

import pymysql
import datetime
import json
import sys
import getopt
import traceback

task_id = 1
def dealResponse(item):
    try:
        con = pymysql.connect(host='192.168.161.139', user='vk_sz1', password='vk_sz1', db='yq_base', port=3306, charset='utf8')
        con.autocommit(1)
        cursor = con.cursor()
        sql = "insert into crawl_data_com (taks_id,create_time,data_topic,data_level" 
        for i in range(1,8):
            sql = sql + ",key%d" % i
        sql = sql + ") values "

        # keys = ('title','abstract','article_url','source','tag','comment_count','behot_time')
        
        v = "(" + str(task_id) + "," + "now(),'toutiaoAticle','1'"
        v = v + ",'" + item.get("title") + "'"
        v = v + ",'" + item.get("abstract") + "'"
        v = v + ",'" + item.get("article_url") + "'"
        v = v + ",'" + item.get("source") + "'"
        v = v + ",'" + item.get("tag","") + "'"
        v = v + "," + str(item.get("comment_count") )
        #单位是秒
        time = datetime.datetime.fromtimestamp(item.get("behot_time"))
        time = time.strftime('%Y-%m-%d %H:%M:%S')
        v = v + ",'" + time + "'"
        v = v +")"
        sql = sql + v
        print(sql)
        cursor.execute( sql )
        print(".")
    except Exception as e:
        stacktrace = traceback.format_exc()
        print(stacktrace)
        sys.exit(2)
    finally:
        cursor.close()
        con.close()

userId = ""
url=r'https://www.toutiao.com/api/pc/list/user/feed'

header = {
    "Connection": "keep-alive",
    "Cache-Control": "max-age=0",
    "sec-ch-ua": "\"Microsoft Edge\";v=\"119\", \"Chromium\";v=\"119\", \"Not?A_Brand\";v=\"24\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\"",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36 Edg/119.0.0.0",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "Sec-Fetch-Site": "none",
    "Sec-Fetch-Mode": "navigate",
    "Sec-Fetch-User": "?1",
    "Sec-Fetch-Dest": "document",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6"
    }
cookie = {
    "ttcid": "5b825568c1144e2d9c58a6f1e7147fb638",
    "csrftoken": "486aa65d4b91d22f6e5de38c5894ed88",
    "ttwid": "1%7CzsAocct-O5arZb-0hdb1bjJ-STTEKNomZXNEmneA6Q0%7C1680756186%7Cfd0f66e3a89677d4752b072c8a11c05d298983153878f56922b6eceb4b34bb7e",
    "tt_webid": "7218792800531138108",
    "_ga": "GA1.1.12220769.1696732456",
    "s_v_web_id": "verify_lngup7hx_USE5O2Vb_E7pL_4TpL_9u8a_P09UxxorktoT",
    "tt_scid": ".PYX9o7yyaneSU.5-lse3rzehyzDQHQ6Zygzwk6wjSqg46aoUTMxbqgn7i6rQAwL692b",
    "local_city_cache": "%E5%B9%BF%E5%B7%9E",
    "_ga_QEHZPBE5HH": "GS1.1.1701243460.19.1.1701243504.0.0.0"
}

def dealRequest(params):
    response = requests.get(url=url,headers=header,cookies=cookie,params=params,verify = False)
    result = json.loads(response.text)
    if result.get('message') == 'success':
        data = result.get("data")
        for item in data:
            dealResponse(item)
        if True==result.get("has_more"):
                max_behot_time = result.get("next").get("max_behot_time")
                params.update({"max_behot_time":max_behot_time})
                dealRequest(params=params)
    else:
        print(result.get('message'))
        sys.exit(2)
        

if __name__ == '__main__':
    argv = sys.argv
    print (argv)
    try:
        opts, args = getopt.getopt(argv[1:], "t:", ["token="])
        for opt, arg in opts:
            if opt in ("-t","--token"):
                userId = arg
        if userId == "":
            print("token is null")
            sys.exit(2)
        params = {"category":"pc_profile_article","token":userId,"max_behot_time":"0","aid":"24","app_name":"toutiao_web"}
        dealRequest(params=params)
    except getopt.GetoptError as e:
        print(e)
        sys.exit(2)
