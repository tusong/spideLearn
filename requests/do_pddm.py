import requests
import urllib3
urllib3.disable_warnings()

import json

import pandas as pd

header = {
    "Accept": "application/json, text/javascript, */*; q=0.01",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
    "Authorization": "",
    "Cache-Control": "no-cache",
    "Connection": "keep-alive",
    "Content-Length": "242",
    "Content-Type": "application/json",
    "Host": "pddm.tydic.com",
    "Pragma": "no-cache",
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "same-origin",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36 Edg/119.0.0.0",
    "sec-ch-ua": "\"Microsoft Edge\";v=\"119\", \"Chromium\";v=\"119\", \"Not?A_Brand\";v=\"24\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\"",
    "x-requested-with": "XMLHttpRequest, XMLHttpRequest"
    }
cookie = {
    "JSESSIONID": "f8fda30f-51cd-403b-930c-f6a2bc6e04fc"
    # "JSESSIONID":"8768cfc5-5348-43e2-9404-0e87f5fa47c1"
}
#verify = False 去掉ssl证书校验

def getP(item,dataIn):
    prdId = item.get('prdId')
    url = 'https://pddm.tydic.com/pddm/project/find'
    param = {"prdId":prdId,"prdExtId":""}
    response = requests.post(url,headers=header,cookies=cookie,verify = False,json=param)
    if response.status_code == 200:
        data = json.loads(response.text)
        if data.get('success') == True:
            result = data.get('result')
            mainProductId = result.get('mainProductId')
            dataIn['包含产品']=result.get('productNames')
            tbProducts = result.get('tbProducts')
            dataIn['包含产品'] = []
            if(tbProducts):
                for p in tbProducts:
                    d = {
                    '产品名称':p.get('productName'),
                    '产品简称':p.get('productSname'),
                    '所属产品线':p.get('tbPlName'),
                    '产品经理':p.get('managerUserName'),
                    '是否主产品':'是' if p.get('productId')==mainProductId else '否'
                    }
                    dataIn['包含产品'].append(d)
            else:
                if dataIn['包含产品'] == []:
                    dataIn['包含产品'].append({
                        '产品名称':'',
                        '产品简称':'',
                        '所属产品线':'',
                        '产品经理':'',
                        '是否主产品':''
                    })


def getD(pageno,dataList):
    urlList = 'https://pddm.tydic.com/pddm/project/list'
    param = {
        "pagesize": 15,
        "pageno": pageno,
        "sortname": "prdId",
        "sortorder": "desc",
        "keyWord": "",
        "projectApprovalStart": "",
        "projectApprovalEnd": "",
        "projectTypeName": "",
        "projectStateName": "",
        "projectAreaName": "",
        "proProductLines": "",
        "oaProductIds": "",
        "orgIds": ""
        }
    response = requests.post(urlList,headers=header,cookies=cookie,verify = False,json=param)
    if response.status_code == 200:
        data = json.loads(response.text)
        if data.get('success') == True:
            result = data.get('result')
            rowTotal = result.get('rowTotal')
            totalPage = result.get('totalPage')
            if(pageno==1):
                print('总记录数:%s,总页数：%s' % (rowTotal,totalPage) )
            infoList = result.get('infoContent')
            
            #pd.DataFrame(infoList).to_excel("pddm.xls")
            #loop infoList
            for item in infoList:
                data = {}
                data['项目名称']=item.get('prdName')
                data['日期']=item.get('projectApproval')
                data['编号']=item.get('projectCoding')
                data['开始日期']=item.get('projectStart')
                data['结束日期']=item.get('projectEnd')
                data['部门经理']=item.get('orgManagerNames')
                data['项目经理']=item.get('projectManagerName')
                data['项目类型']=item.get('projectTypeName')
                data['项目状态']=item.get('projectStateName')
                data['部门名称']=item.get('orgName')
                data['项目所属产品线']=item.get('productLineName')

                dataList.append(data)
                getP(item,data)
            # pd.DataFrame(infoList).to_excel("pddm.xls")

            if(pageno<totalPage):
                getD(pageno+1,dataList)

if __name__ == '__main__':
    dataList = []
    getD(1,dataList)
    #pd.DataFrame(dataList).to_excel("pddm.xls")

    # 展平数据
    df_nested_list = pd.json_normalize(
        dataList,
        record_path =['包含产品'],
        meta=['项目名称', '日期','编号', '开始日期','结束日期', '部门经理','项目经理', '项目类型','项目状态', '部门名称','项目所属产品线']
    )
    pd.DataFrame(df_nested_list).to_excel("pddm.xls")



