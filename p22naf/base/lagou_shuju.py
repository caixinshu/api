#!/usr/bin/env python
# -*- coding=utf-8 -*-
import requests

url = "https://www.lagou.com/jobs/positionAjax.json?needAddtionalResult=false"

def getheaders():
    headers = {
        "Content-Type":"application/x-www-form-urlencoded; charset=UTF-8",
        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36",
        "Cookie":"user_trace_token=20190819151430-dd125515-085f-4aed-83ef-f6f981c1f3be; _gat=1; PRE_UTM=m_cf_cpc_baidu_pc; PRE_HOST=www.baidu.com; PRE_SITE=https%3A%2F%2Fwww.baidu.com%2Fbaidu.php%3Fsc.000000jk39biGWe9FCeMD3RPabNrW2OGSbYFK_pAahH8r6QYxJyHXBSxcJdPYnO1kvjhhD3s9SpmLU-DNiBpX8MxDtPqx2ghkSy36bfdu_zYQNO3BdD4owGwAiiDk6oN7PKm3gXNsnfBiinmT6aigTOfk6uFcRFzxPzdJPa-YKHYD5oZeu_d-QtrcbHaNXvFoQEpQN5BykhJWtpmi0.DR_NR2Ar5Od663rj6tJQrGvKD77h24SU5WudF6ksswGuh9J4qt7jHzk8sHfGmYt_rE-9kstVerQKz33X8M-eXKBqM764mTT5QZstJplePXO-8zNqrw5Q9tSMj_qTr1x9tqvZul3xg1sSxW9qx-9LdoDkE3tUPh1x84phgT85R_nYQZuubtX260.U1Yk0ZDqs2v4VnL30ZKGm1Ys0Zfqs2v4VnL30A-V5HcsP0KM5gK1n6KdpHdBmy-bIykV0ZKGujYY0APGujY4nsKVIjYknjDLg1DsnH-xnW0vn-tknjc1g1nvnjD0pvbqn0KzIjYvP1R0uy-b5fKBpHYkPH9xnW0Y0AdW5HD3n1nsP1DdP19xnH0snNtznj64rHb3rHRzg17xn0KkTA-b5H00TyPGujYs0ZFMIA7M5H00mycqn7ts0ANzu1Ys0ZKs5H00UMus5H08nj0snj0snj00Ugws5H00uAwETjYs0ZFJ5H00uANv5gKW0AuY5H00TA6qn0KET1Ys0AFL5HDs0A4Y5H00TLCq0A71gv-bm1dsTzdMXh93XfKGuAnqiD4a0ZwdT1YznjmLnHT4PjbYrjbLrjfsrHb30ZF-TgfqnHRvPWD4rj6vPjm3PsK1pyfqmHIBryFBPAcsnj04uyc3mfKWTvYqPWRdnjfLwbmzf19jwW6kw6K9m1Yk0ZK85H00TydY5H00Tyd15H00XMfqn0KVmdqhThqV5HKxn7tsg1Kxn0Kbmy4dmhNxTAk9Uh-bT1Ysg1Kxn7tsg100TA7Ygvu_myTqn0Kbmv-b5H00ugwGujYVnfK9TLKWm1Ys0ZNspy4Wm1Ys0Z7VuWYs0AuWIgfqn0KlTAkdT1Ys0A7buhk9u1Yk0Akhm1Ys0AqY5H00ULFsIjYsc10Wc10Wnansc108nj0snj0sc10Wc100mLFW5HckPW6Y%26word%3D%25E6%258B%2589%25E5%258B%25BE%25E7%25BD%2591%26ck%3D9118.1.86.401.357.401.354.193%26shh%3Dwww.baidu.com%26sht%3D93308895_hao_pg%26us%3D1.0.1.0.2.828.0%26bc%3D110101; PRE_LAND=https%3A%2F%2Fwww.lagou.com%2Flanding-page%2Fpc%2Fsearch.html%3Futm_source%3Dm_cf_cpc_baidu_pc%26m_kw%3Dbaidu_cpc_sz_e110f9_d2162e_%25E6%258B%2589%25E5%258B%25BE%25E7%25BD%2591; LGUID=20190819151430-fcde6f2c-c250-11e9-8a9c-525400f775ce; JSESSIONID=ABAAABAAAFCAAEG1156FB2643210EB72D7B93A5EDB573A9; WEBTJ-ID=20190819151435-16ca8ba4639815-0026f31bfa6074-5e4f2b18-1049088-16ca8ba463a864; index_location_city=%E5%85%A8%E5%9B%BD; SEARCH_ID=d22c74cf279b4474bbe5a7daa67d236e; X_HTTP_TOKEN=d84cf5d217cd7aa45888916651792f70dc5b473688; _gid=GA1.2.1803498514.1566198877; Hm_lvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1565747931,1566198873; Hm_lpvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1566198887; _ga=GA1.2.1709271687.1566198873; LGSID=20190819151430-fcde6d17-c250-11e9-8a9c-525400f775ce; LGRID=20190819151445-05940d98-c251-11e9-8a9c-525400f775ce",
        "Referer":"https://www.lagou.com/jobs/list_%E6%B5%8B%E8%AF%95%E5%B7%A5%E7%A8%8B%E5%B8%88?labelWords=sug&fromSearch=true&suginput=ceshi"
    }
    return headers

def laGou(page=2):
    r = requests.post(url=url,
                      headers=getheaders(),
                      data={'first':False,'pn':page,'kd':'测试'})
    print(r.text)
    # for i in range(15):
    #     city = r.json()["content"]["positionResult"]["result"][i]["city"]
    #     print(city)

laGou()

