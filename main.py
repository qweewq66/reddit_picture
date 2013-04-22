import urllib,os,re

#define a null page sourse for a website
html=None
prompt = 'enter the URL adress in reddit you want to download!\n'
#get the html resouse from current website
def get_html(_url):
    if _url.startswith('http') or _url.startswith('HTTP'):
        url=_url
    else :
        url='http://'+_url
    try:
        page=urllib.urlopen(url)
        html=page.read()
        return html
    except:
        print('can not open the current website!\n')
        return
#search the target pictures
def get_urls(_html):
    url_reg='http:.{0,20}.thumbs\.reddit.{,40}.png'
    url_list=re.findall(url_reg,_html)
    return url_list

#download the target pictures
def downloadpic(url_list):
    num=0
    picdir= os.getcwd()+'/reddit_alien_pictures_from_'+url.split('/')[-1]
    if not os.path.exists(picdir):
        try:
            os.mkdir(picdir)
            for i in url_list:
                urllib.urlretrieve(i,picdir+'/'+str(num)+'.png')
                num+=1
            print('download successfully!')
        except:
            print('can not create the folder!')
    elif os.path.exists(picdir):
        print('the local folder has existed!')
        
if __name__ == '__main__':
    url=raw_input(prompt)
    if(url[-1] == '/'):
        url = url[0:-1]
    html=get_html(url) 
    urls=get_urls(html)
    downloadpic(urls)
