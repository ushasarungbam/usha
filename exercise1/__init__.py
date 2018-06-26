import webbrowser
import time
#print("hello world by python")
#a="nielit"
#print (a)
url1="http://youtube.com"
url2="http://google.com"
url3="http://yahoo.com"
i=1
while(i<4):
    time.sleep(15)
    url=url+i
    webbrowser.open_new(url)
    i=i+1