import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'programming.settings')
import django
django.setup()

from webtoon.models import Episode

from urllib.parse import urljoin
import requests
from bs4 import BeautifulSoup

def main():
    url_set = { ep.url for ep in Episode.objects.all()}

    episode_list = []

    for page in range(1,10000):
        params = {
            'titleId' : 679519,
            'page' : page,
        }
        page_url = 'http://comic.naver.com/webtoon/list.nhn'
        html =requests.get(page_url, params=params).text
        soup =BeautifulSoup(html, 'html.parser')
        for a_tag in soup.select('.viewList .title a'):
             title = a_tag.text
             link = urljoin(page_url, a_tag['href'])

            if link in url_set :
                print('End')
                return episode_list

            url_set.add(link)

            print(title, link)

            episode_list.append(Episode(title=title, url=link))

if __name__ == '__main__':
    #__name__은 시작한 파일의 이름이 __main__으로 기본적으로 설정되어있다.
    #이 기능은 다른 파일에서 함수를 가져오려고 할때
    from django.db import connection

    episode_list = main()
    Episode.objects.bulk_create(episode_list)

    for idx, query in enumerate(connection.queries, 1): #인자로 1을 주면 1부터 시작할 수 있음. enumerate함수는 값이 인덱스와 함께 나온다.
        print(idx, query)
