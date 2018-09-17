import requests
import requests.cookies


def get_video_data():
    url = 'http://v.zhibo.tv/ajax/appnesting/search'
    data = {
        "k": "羽毛球",
        "n": 2,
        "rnd": "0.19737283560050511",
        "_csrf": "WE9xeFlXc1g1IysfChMQMjwjJDJrMiQXB3o3CAE4FS40eBIMK28GLQ=="
    }
    headers = {
        'User-Agent': 'Mozilla/5.0 (Linux; Android 8.0.0; Mi Note 2 Build/OPR1.170623.032; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/62.0.3202.84 Mobile Safari/537.36'
    }
    cookies = requests.cookies.RequestsCookieJar()
    cookies.set('_csrf', 'mlZgSDcjdlUJ2eWO_5FpXofvl7ctr8uu')
    cookies.set('grwng_uid', 'fba2b068-c6f4-47c7-8066-60e8d7691e0e')
    cookies.set('gr_user_id', '683efa9b-4eb6-4283-aabd-b1286a8c135d')
    cookies.set('token', '038a0dcf66406659a64f77b5cfa2a3da%2A2883268')
    cookies.set('sign', 'b8b7b91f7fe5b69085e42821f3c8b1fe')
    cookies.set('ep', 'NjA0ODAw')
    cookies.set('oid', '34aac6ea287ac9e9c742aac1be450fc5')

    response = requests.post(url,  cookies=cookies, data=data).json()
    return response


result = get_video_data()
print(result)
