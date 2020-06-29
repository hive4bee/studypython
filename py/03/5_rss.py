#pip install feedparser
import feedparser
#parse()함수에 파일경로, 파일객체, XML 문자열 등을 지정한다.
d=feedparser.parse('it.rss')
#parse()함수에 URL을 지정하면 피드를 파싱할 수 있다.
d=feedparser.parse("http://aladin.co.kr/rss/new_all/351")
d
d.version #피드의 버전을 추출한다.
type(d)
d.feed.title
d['feed']['title']
d.feed.link
d.feed.description
len(d.entries)#d.entries로 피드를 list자료형으로 추출한다.
d.entries[0].title
d.entries[0].link
d.entries[0].description
d.entries[0].updated
d.entries[0].updated_parsed


d=feedparser.parse("http://aladin.co.kr/rss/special_new/351")

for entry in d.entries:
    print("이름:",entry.title)
    print("타이틀:",entry.title)
    print()