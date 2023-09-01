# from melon_top100 import get_songs()
# 1. https://www.melon.com/chart/index.htm
# 1-1. requests 설치 => get 함수 => text로 변환
# 1-2. beautifulsoup4 설치
# 2. <tbody> -> <tr>을 가지고 오면 뭔가를 가져올 수 있음
# 3. 100번 반복
# 4. 리스트로 변경
# 5. 결과 반환
# 6. 화면 출력

import requests
from bs4 import BeautifulSoup

headers = {
    "User-Agent": (
        "Chrome/72.0.3626.121 Safari/537.36"
    )
}

def get_songs():
    res = requests.get('https://www.melon.com/chart/index.htm', headers=headers)
    html = res.text
    soup = BeautifulSoup(html, 'html.parser')
    tbody_tr_tag = soup.select("tbody tr")
    song_list = []
    for rank, tr_tag in enumerate(tbody_tr_tag, 1):
        song_no = tr_tag["data-song-no"]
        song_title = tr_tag.select_one("a[href*=playSong]")
        album_title = tr_tag.select_one(".wrap_song_info a[href*=goAlbumDetail]")
        artist_title = tr_tag.select_one("a[href*=goArtistDetail]")

        song = {
            "rank": rank,
            "song_no": song_no,
            "song_title": song_title.text,
            "album_title": album_title.text,
            "artist_title": artist_title.text
        }

        song_list.append(song)

    return song_list

if __name__ == "__main__":
    for song in get_songs():
        print(song)