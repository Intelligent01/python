from threading import Thread
from time import sleep,perf_counter
from urllib import request

def file(url,file):


    data=request.urlopen(url,).read()
    with open(file,'w') as f:
        print('file is processing .....')
        f.write(str(data))
        sleep(1)

    print('file write done..')

url=['https://google.com/','https://youtube.com','https://linkedin.com']
filename='helo.html'
s=perf_counter()
threads=[]
for i in range(3):
    t=Thread(target=file,args=(url[i],filename))
    t.start()
    threads.append(t)


for t in threads:
    t.join()

e=perf_counter()
print(f'it tooks in {e-s:0.2f}second(s)')

