import os
from .. import scraper

target = os.path.basename(__file__).split(".")[0]
resource = os.path.basename(os.path.dirname(os.path.realpath(__file__)))
print
print "resource: " + resource
print "target: " + target
print
scraper.start(target, resource)
