from UrlMatch import Match

p = Match('https://youtube.com')
if p.UrlMatch() is True:
    print('오 이건 Url이넹')
else:
    print('오 이건 Url이 아니넹')