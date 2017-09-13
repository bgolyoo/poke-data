import argparse
import glob
import os
import codecs
import sources
import errno

parser = argparse.ArgumentParser()

parser.add_argument("-l", "--list", help="list all available scrape resources", action="store_true")
parser.add_argument("-r", "--resources", help="resources to convert to mongoDb import format (space delimited list)", nargs="+")
parser.add_argument("-a", "--all", help="do merge on all resources", action="store_true")

args = parser.parse_args()

resources = sources.resources


def list_all_resources():
    print "\nAll available scrape resources:"
    for key in resources:
        print " - " + key + ": " + " ".join(resources[key])


def check_provided_resources(provided_resources):
    all_checked_resources = []
    for provided_resource in provided_resources:
        for key in resources:
            if provided_resource in resources[key]:
                all_checked_resources.append({"target": provided_resource, "resource": key})
    if len(all_checked_resources) > 0:
        return all_checked_resources
    else:
        print "Provided resources don't match with any available scrape resource!"


def convert(resource, target):
    print
    print "------------- start ------------"
    print "resource: " + resource
    print "target: " + target
    files = glob.glob("../data/" + resource + "/" + target + "/**.json")
    lines = []
    for f in files:
        with codecs.open(f, "r", "utf-8") as infile:
            data_str = infile.read()
            data_str = data_str.replace("\n", "")
            data_str = data_str.replace(" ", "")
            data_str = data_str.replace('"id"', '"_id"')
            data_str = data_str.replace("http://pokeapi.co/api/v2", "")
            lines.append(data_str)
    dir_name = "./converted_resources"
    try:
        os.makedirs(dir_name)
    except OSError as e:
        if e.errno != errno.EEXIST:
            raise
    with codecs.open(dir_name + "/" + target + ".json", "w", "utf-8") as outfile:
        line = ",\n".join(lines)
        outfile.write("[\n%s\n]" % line)
    print "------------- done -------------"
    print


def convert_all():
    for resource_item in resources:
        for group_item in resources[resource_item]:
            convert(resource_item, group_item)


if args.list:
    list_all_resources()
elif args.resources:
    checked_resources = check_provided_resources(args.resources)
    for item in checked_resources:
        convert(item["resource"], item["target"])
elif args.all:
    convert_all()
