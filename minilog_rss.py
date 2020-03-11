import datetime
from bs4 import BeautifulSoup


def rss_make(items):
    pubdate = datetime.datetime.now().strftime("%a, %d %b %Y %H:%M:%S %z")
    template = """
<rss version="2.0">
<channel>
<title>POPL MINI LOG</title>
<link>https://popl.ml/minilog.html</link>
<description/>
<language>ko</language>
<pubDate>{pubdate}</pubDate>
<generator>minilog</generator>
<managingEditor>poplcode</managingEditor>
{item_content}
</channel>
</rss>
""".strip()

    item_template = """
<item>
<title>{title}</title>
<link>https://popl.ml/minilog.html#{link}</link>
<description>{title}</description>
<author>poplcode</author>
<guid>https://popl.ml/minilog.html#{link}</guid>
<pubDate>{pubdate}</pubDate>
</item>
""".strip() + "\n"

    item_content = ""
    for item in items:
        title = item['title']
        link = item['link']
        item_content += item_template.format(title=title, link=link, pubdate=pubdate)
    
    ret = template.format(pubdate=pubdate, item_content=item_content.strip())

    #print (ret)
    return ret


def load_html():
    html = ''
    with open("_book/minilog.html", 'r', encoding='utf-8') as f:
        html = f.read()

    soup = BeautifulSoup(html, "html.parser")
    h1_list = soup.find_all("h1")
    items = []
    for h1 in h1_list:
        try:
            h1_id = h1['id']
            txt = h1.text
            items.append({"link":h1_id, "title":txt})            
        except:
            pass
    
    ret = rss_make(items)
    return ret

def save_html():
    html = load_html()
    with open("_book/minilog.rss", 'w', encoding='utf-8') as f:
        f.write(html)

save_html()