import scraper
import sources
import argparse

parser = argparse.ArgumentParser()

parser.add_argument("-be", "--berries", help="scrape all berries resources", action="store_true")
parser.add_argument("-co", "--contests", help="scrape all contests resources", action="store_true")
parser.add_argument("-en", "--encounters", help="scrape all encounters resources", action="store_true")
parser.add_argument("-ev", "--evolution", help="scrape all evolution resources", action="store_true")
parser.add_argument("-ga", "--games", help="scrape games all resources", action="store_true")
parser.add_argument("-it", "--items", help="scrape items all resources", action="store_true")
parser.add_argument("-ma", "--machines", help="scrape all machines resources", action="store_true")
parser.add_argument("-mo", "--moves", help="scrape all moves resources", action="store_true")
parser.add_argument("-lo", "--locations", help="scrape all locations resources", action="store_true")
parser.add_argument("-po", "--pokemon", help="scrape all pokemon resources", action="store_true")
parser.add_argument("-ut", "--utility", help="scrape all utility resources", action="store_true")
parser.add_argument("-r", "--resources", help="resources to scrape", nargs="+")
parser.add_argument("-l", "--list", help="list all available scrape resources", action="store_true")
parser.add_argument("-a", "--all", help="scrape all resources", action="store_true")

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


def scrape_all():
    for resource_item in resources:
        scrape_group(resource_item)


def scrape_group(name):
    for group_item in resources[name]:
        scrape(name, group_item)


def scrape(resource, target):
    print "resource: " + resource
    print "target: " + target
    scraper.start(target, resource)


if args.resources:
    checked_resources = check_provided_resources(args.resources)
    for item in checked_resources:
        scrape(item["resource"], item["target"])
elif args.berries:
    scrape_group("berries")
elif args.contests:
    scrape_group("contests")
elif args.encounters:
    scrape_group("encounters")
elif args.evolution:
    scrape_group("evolution")
elif args.games:
    scrape_group("games")
elif args.items:
    scrape_group("items")
elif args.machines:
    scrape_group("machines")
elif args.moves:
    scrape_group("moves")
elif args.locations:
    scrape_group("locations")
elif args.pokemon:
    scrape_group("pokemon")
elif args.utility:
    scrape_group("utility")
elif args.list:
    list_all_resources()
elif args.all:
    scrape_all()
