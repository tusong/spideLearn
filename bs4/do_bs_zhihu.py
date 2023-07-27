import requests
import re
 
def get_zhihu_question(question_id):
    url = f'https://www.zhihu.com/question/{question_id}'
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
 
    r = requests.get(url, headers=headers)
    if r.status_code == 200:
        pattern = re.compile('<h1 class="QuestionHeader-title">(.*?)</h1>.*?<button class="Button QuestionMainAction.*?>(.*?)</button>', re.S)
        result = pattern.search(r.text)
        if result:
            title = result.group(1).strip()
            answer_count = result.group(2).strip()
            print(f"问题标题：{title}")
            print(f"回答数：{answer_count}")
        else:
            print("无法匹配问题标题和回答数")
 
        pattern = re.compile('<div class="RichContent-inner">(.*?)</div>', re.S)
        result = pattern.search(r.text)
        if result:
            answer = result.group(1).strip()
            print(f"回答内容：{answer}")
        else:
            print("无法匹配回答内容")
    else:
        print(f"请求失败，错误代码：{r.status_code}")

if __name__ == '__main__':
    keyword = '30576324'
    get_zhihu_question(keyword)