import json
import glob
import errno
import os
import requests


def get_urls(sprites_data):
    sprites_data_urls = []
    if sprites_data["back_female"] is not None:
        sprites_data_urls.append({"type": "back_female", "url": sprites_data["back_female"]})
    if sprites_data["back_shiny_female"] is not None:
        sprites_data_urls.append({"type": "back_shiny_female", "url": sprites_data["back_shiny_female"]})
    if sprites_data["back_default"] is not None:
        sprites_data_urls.append({"type": "back_default", "url": sprites_data["back_default"]})
    if sprites_data["front_female"] is not None:
        sprites_data_urls.append({"type": "front_female", "url": sprites_data["front_female"]})
    if sprites_data["front_shiny_female"] is not None:
        sprites_data_urls.append({"type": "front_shiny_female", "url": sprites_data["front_shiny_female"]})
    if sprites_data["back_shiny"] is not None:
        sprites_data_urls.append({"type": "back_shiny", "url": sprites_data["back_shiny"]})
    if sprites_data["front_default"] is not None:
        sprites_data_urls.append({"type": "front_default", "url": sprites_data["front_default"]})
    if sprites_data["front_shiny"] is not None:
        sprites_data_urls.append({"type": "front_shiny", "url": sprites_data["front_shiny"]})
    return sprites_data_urls


def download_sprites(sprite_urls):
    count = len(sprite_urls)
    for sprite_url in sprite_urls:
        make_dir(dir_name)
        types = sprite_url["urls"]
        for type_data in types:
            make_dir(dir_name + type_data["type"])
            file_name = dir_name + type_data["type"] + "/" + str(sprite_url["id"]) + ".png"
            f = open(file_name, 'wb')
            f.write(requests.get(type_data["url"]).content)
            f.close()
            count = count - 1
            print "done - " + file_name + " , left: " + str(count)


def make_dir(new_dir):
    try:
        os.makedirs(new_dir)
    except OSError as e:
        if e.errno != errno.EEXIST:
            raise


def get_data():
    files = glob.glob("../data/pokemon/pokemon/**.json")
    count = len(files)
    sprite_urls = []

    for f in files:
        print "\r" + str(count)
        with open(f, "rb") as infile:
            data = json.load(infile)
            urls = get_urls(data["sprites"])
            if len(urls) > 0:
                sprites = {"id": data["id"], "urls": urls}
                sprite_urls.append(sprites)
        count = count - 1

    download_sprites(sprite_urls)


dir_name = "../sprites/"
get_data()
