import requests
import json
import io
import os
import errno
import time
import sys

scrape_data = ""
base_url = ""
directory_name = ""
resource_dir = ""
retry_times = 5
retry_count = 0
all_urls = []
expected_result_count = 0
actual_result_count = 0


def get_all_urls(url):
    my_response = requests.get(url, verify=True)
    print str(my_response.status_code) + " for " + url

    if str(my_response.status_code) == str(429):
        wait(int(my_response.headers["Retry-After"]) + 5)
        print "retry"
        get_all_urls(url)
    elif my_response.ok:
        json_data = json.loads(my_response.content)
        global expected_result_count
        if expected_result_count != json_data['count']:
            expected_result_count = json_data['count']
            print "\nexpected result count: " + str(expected_result_count) + "\n"
        results = json_data['results']
        for result in results:
            all_urls.append(result['url'])
        if json_data['next'] is not None:
            get_all_urls(json_data['next'])
    else:
        # my_response.raise_for_status()
        return


def get_all_data():
    global retry_count
    global actual_result_count
    global all_urls
    urls = all_urls
    retry_count = retry_count + 1
    to_removes = []
    for url in urls:
        ok = get_data(url)
        if ok is True:
            actual_result_count = actual_result_count + 1
            to_removes.append(url)
    for to_remove in to_removes:
        all_urls.remove(to_remove)
    if len(all_urls) > 0 and retry_count <= retry_times:
        get_all_data()
    elif len(all_urls) > 0 and retry_count > retry_times:
        print "tried times: " + str(retry_times)
        print "unable to parse urls: " + ', '.join(all_urls)
        failed_urls_data = {scrape_data: all_urls}
        write_json_data(failed_urls_data, time.strftime("%Y-%m-%d_%H:%M:%S_") + scrape_data + ".json", "./failed_urls/")


def get_data(url):
    my_response = requests.get(url, verify=True)
    print str(my_response.status_code) + " for " + url

    if str(my_response.status_code) == str(429):
        wait(int(my_response.headers["Retry-After"]) + 5)
        print "retry"
        get_data(url)
    elif my_response.ok:
        json_data = json.loads(my_response.content)
        write_json_data(json_data, get_file_name(json_data), directory_name)
        return True
    else:
        my_response.raise_for_status()
        return False


def wait(timeout):
    for sec in range(timeout):
        sys.stdout.write("\r%s" % "waited " + str(sec) + " / " + str(timeout) + " seconds")
        sys.stdout.flush()
        time.sleep(1)
    return


def write_json_data(json_data, file_name, dir_name):
    if dir_name is not None:
        try:
            os.makedirs(dir_name)
        except OSError as e:
            if e.errno != errno.EEXIST:
                raise
    else:
        dir_name = "./"
    out_file = dir_name + file_name
    with io.open(out_file, 'w', encoding='utf-8') as outfile:
        outfile.write(unicode(json.dumps(json_data, ensure_ascii=False)))


def get_file_name(json_data):
    if "name" in json_data:
        return str(json_data["id"]) + "_" + json_data["name"] + ".json"
    else:
        return str(json_data["id"]) + "_" + scrape_data + ".json"


def start(target, resource):
    global actual_result_count
    global expected_result_count
    global scrape_data
    global base_url
    global directory_name
    global resource_dir
    actual_result_count = 0
    expected_result_count = 0
    scrape_data = target
    resource_dir = resource
    base_url = "http://pokeapi.co/api/v2/" + target + "/"
    directory_name = "../data/" + resource_dir + "/" + target + "/"
    print "\n\n----------------- Scraping resource: " + scrape_data + " -----------------\n"
    get_all_urls(base_url)
    get_all_data()
    print
    print "data written: " + str(actual_result_count)
    print "expected: " + str(expected_result_count)
    print
