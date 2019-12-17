

import requests
data1 = {'token':'a724636d6dba10a8e92d351e9d783ebcc3a4de79','id':9}
r=requests.post('http://127.0.0.1:8000/ltcs/api/book/lend',json=data1)
print r.content
