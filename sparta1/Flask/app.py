from flask import Flask, render_template, request
import random
import requests
app = Flask(__name__)

@app.route('/')
def home():
    name = '윤수용'
    
    # 로또 번호 생성
    def generate_lotto_numbers():
        numbers = random.sample(range(1, 46), 6)
        return sorted(numbers)
    
    my_lotto = generate_lotto_numbers() # 내 로또 번호
    random_lotto = generate_lotto_numbers() # 당첨 로또 번호
    
    # 내 로또 번호와 당첨 로또 번호 비교 
    def count_common_elements(list1, list2):
        common_elements = set(list1) & set(list2)
        return len(common_elements)
    
    common_count = count_common_elements(my_lotto, random_lotto)
    
    context = {
        "name": name,
        "my_lotto": my_lotto,
        "random_lotto": random_lotto,
        "common_count": common_count
    }
    
    return render_template('index.html', data=context)

@app.route('/mypage')
def mypage():  
    return 'This is My Page!'

@app.route("/movie")
def movie():
    query = request.args.get('query') # 검색어
    URL = f"http://kobis.or.kr/kobisopenapi/webservice/rest/movie/searchMovieList.json?key=f5eef3421c602c6cb7ea224104795888&movieNm={query}" # URL

    res = requests.get(URL)
    rjson = res.json()
    movie_list = rjson["movieListResult"]["movieList"]
		
    return render_template("movie.html", data=movie_list)

if __name__ == '__main__':  
    app.run(debug=True)