import requests
from bs4 import BeautifulSoup
import urllib.request

class MovieInfo:

    def __init__(self):
        self.name = ''
        self.like = ''
        self.poster = ''
        self.ticket = ''

    def __str__(self):
        return 'title:{}, like:{}, 예매링크:{}'.format(self.name, self.like, self.ticket)

url = 'https://movie.naver.com/movie/running/current.nhn?view=list&tab=normal&order=likeCount'
data = requests.get(url)
soup = BeautifulSoup(data.content, 'html.parser')
ul = soup.select('.lst_wrap .lst_detail_t1')
movies = ul[0].findAll('li')

i = 0
li = list()
#li = []
while i < 20:
    movie = movies[i]
    info = MovieInfo()

    movieName = movie.select('.tit a')[0].text
    #print('영화 이름:',movieName)
    info.name = movieName

    movieLike = movie.findAll('em', class_ = 'num_likeit')[0].text.strip()
    #print('좋아요 수:',movieLike)
    info.like = movieLike

    moviePoster = movie.select('.thumb img')[0]['src']
    #print('영화 포스터:',moviePoster)
    info.poster = moviePoster
    #urllib.request.urlretrieve(moviePoster, movieName + '.png')

    movieTicket = movie.select('.btn_area a')[0]['href']
    info.ticket = movieTicket
    #print('예매 링크: ','https://ticket.movie.naver.com' + movieTicket)
    
    #print(info)
    li.append(info)
    i = i + 1

print(len(li))
for movie in li:
    print(movie.name)
    print(movie.like)