from urllib import request

video_url=''

#下载进度函数
def report(a,b,c):
    '''
    a:已经下载的数据块
    b:数据块的大小
    c:远程文件的大小
    '''
    per=100.0*a*b/c
    if per>100:
        per=100

    print('%.2f%%'%per)

request.urlretrieve(url=video_url,filename='test.mp4',reporthook=report)