from lxml import html
import requests
import os
import errno


def get_number(number_as_string):
    actual_number = 0
    ns = (list(number_as_string.strip()[::-1]))
    for i in range(len(ns)):
        actual_number = actual_number + ((10 ** i) * int(ns[i]))
    return str(actual_number)


count = 0
xpath_sprites = "//a[@class='sprite-share-link']/img"
xpath_main_img_link = "//div[@class='col desk-span-4 lap-span-6 figure']/img/@src"
xpath_links = "//a[@class='ent-name']/@href"
xpath_numbers = "//td[@class='num cell-icon-string']/text()"
url = "https://pokemondb.net"
all = "/pokedex/all"
dir_name = "../images/"

page = requests.get(url + all)
tree = html.fromstring(page.content)
links = tree.xpath(xpath_links)
numbers = tree.xpath(xpath_numbers)

if len(links) == len(numbers):
    for index in range(len(links)):
        pokemon_page = requests.get(url + links[index])
        pokemon_tree = html.fromstring(pokemon_page.content)
        main_img_links = pokemon_tree.xpath(xpath_main_img_link)
        for main_img_link in main_img_links:
            try:
                os.makedirs(dir_name)
            except OSError as e:
                if e.errno != errno.EEXIST:
                    raise
            file_name = dir_name + get_number(numbers[index]) + "_" + os.path.basename(main_img_link)
            f = open(file_name, 'wb')
            f.write(requests.get(main_img_link).content)
            f.close()
            count = count + 1
            print "done - " + main_img_link + " , left: " + str(len(links) - count)
else:
    print str(len(links))
    print str(len(numbers))
