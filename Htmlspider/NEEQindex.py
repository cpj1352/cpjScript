from Clib.http import _http
from Clib import db
import re,json
def index():
    url='http://www.neeq.com.cn/neeqController/getNeeqList.do?callback=jQuery18303443067020250625_1468897955504'
    http=_http()
    content=http.get_data(req_url=url,num=3)
    pattern = re.compile(r'\[.*\]', re.DOTALL).findall(content)
    htmljson = json.loads("".join(pattern))
    data=db.select(content='SELECT * FROM `neeq_index` ',type=1)
    text=htmljson
    for i in range(2):
        for k,v in htmljson[i].items():
            if k not in data:
                htmljson[i].pop(k)
        print htmljson[i]
        db.insert_dict(table='neeq_index',repeat=3,**htmljson[i])

index()
