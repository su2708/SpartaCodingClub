from flask import Flask, render_template
from bs4 import BeautifulSoup
import requests

app = Flask(__name__)

@app.route('/')
def index():
    # 멜론 크롤링
    url = "https://www.melon.com/chart/"
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
    data = requests.get(url, headers=headers)
    soup = BeautifulSoup(data.text, 'html.parser')

    trs = soup.select('table > tbody > tr')
    
    context = {}
    for tr in trs:
        rank = tr.select_one('.rank').text
        title = tr.select_one('.rank01 > span > a').text
        artist = tr.select_one('.rank02 > a').text
        image = tr.select_one('img')['src']
        song = {
            "title": title,
            "artist": artist,
            "image": image
        }
        context[f"{rank}"] = song
        
    
    return render_template('index.html', data=context)

if __name__ == '__main__':
    app.run()