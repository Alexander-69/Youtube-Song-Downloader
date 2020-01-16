import youtube_dl
def download(url,title):
  options = {
    'format': 'bestaudio/best',
    'outtmpl': title+".music",
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '192',
    
    }],
  }

#'outtmpl': title+".music",
  with youtube_dl.YoutubeDL(options) as ydl:
      ydl.download(['http://www.youtube.com'+url])

  

import requests
from lxml import html
import threading
def get_Music(q):
  page = requests.get('https://www.youtube.com/results?search_query='+str(q))

  tree = html.fromstring(page.content)

  #This will create a list of buyers:
  #buyers = tree.xpath('//div[@title="buyer-name"]/text()')
  #This will create a list of prices
  urls = tree.xpath('//*[@class="yt-uix-tile-link yt-ui-ellipsis yt-ui-ellipsis-2 yt-uix-sessionlink      spf-link "]')
  for x in range(0,10):
    #print(urls[x].get("href"))
    print(str(x)+"."+urls[x].text)
  choice=int(input("Enter the number "))
  
  x = threading.Thread(target=download, args=(urls[choice].get("href"),urls[choice].text))
  x.start()
  

while True:
  song_name=input("Enter the name of the song ")
  if song_name=="x":
    exit()
  get_Music(song_name)

 