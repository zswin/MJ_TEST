from requests_html import HTMLSession
import requests


session = HTMLSession()
re = session.get("http://www.win4000.com/wallpaper_2358_0_10_1.html")

images = re.html.find("ul.clearfix > li > a")
for image in images:
    print(image)

def save_img(url, title):
    html_res = requests.get(url)
    with open('c:/temp/wallpaper/' + title + '.jpg', 'wb') as f:
        f.write(html_res.content)


for image in images:
    image_url = image.attrs['href']
    if '/wallpaper_detail' in image_url:
        r = session.get(image_url)
        item_url = r.html.find("img.pic-large", first=True)
        url = item_url.attrs['src']
        title = item_url.attrs['title']
        print(title +'-' + url)
        save_img(url, title)
