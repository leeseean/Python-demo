import urllib
import urllib.request
import re

def download_page(url):
    headers = {'User-Agent': 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'}
    request = urllib.request.Request(url,headers)
    response = urllib.request.urlopen(url)
    data = response.read()
    return data
def get_image(html):
    regx = r'"(\.\/sprites\/\w*?\.(png|jpg))"'

    pattern = re.compile(regx)

    get_img = re.findall(pattern,repr(html))

    for img in get_img:
        image = download_page('http://showcase.codethislab.com/games/horse_racing/'+img[0])
        with open(re.search(r"\w*?\.(png|jpg)",img[0]).group(),'wb') as fp:
            fp.write(image)
    for num in list(range(398)):
        image = download_page('http://showcase.codethislab.com/games/horse_racing/sprites/bg_track/bg_track_'+str(num)+'.jpg')
        with open('bg_track_'+str(num)+'.jpg', 'wb') as fp:
            fp.write(image)
    for num in list(range(9)):
        image = download_page('http://showcase.codethislab.com/games/horse_racing/sprites/cage_gates/gate_'+str(num)+'.png')
        print(image)
        with open('gate_'+str(num)+'.png', 'wb') as fp:
            fp.write(image)
    for num in list(range(9)):
        image = download_page('http://showcase.codethislab.com/games/horse_racing/sprites/cage_'+str(num)+'.png')
        with open('cage_'+str(num)+'.png', 'wb') as fp:
            fp.write(image)
    for num in list(range(8)):
        image = download_page('http://showcase.codethislab.com/games/horse_racing/sprites/bib_gui_'+str(num)+'.png')
        with open('bib_gui_'+str(num)+'.png', 'wb') as fp:
            fp.write(image)
    for num in list(range(1,9)):
        image_a = download_page('http://showcase.codethislab.com/games/horse_racing/sprites/horse_'+str(num)+'_a.png')
        image_b = download_page('http://showcase.codethislab.com/games/horse_racing/sprites/horse_' + str(num) + '_b.png')
        with open('horse_'+str(num)+'_a.png', 'wb') as fp:
            fp.write(image_a)
        with open('horse_' + str(num) + '_b.png', 'wb') as fp:
            fp.write(image_b)
    return
url = 'http://showcase.codethislab.com/games/horse_racing/js/main.js'
html = download_page(url)
get_image(html)