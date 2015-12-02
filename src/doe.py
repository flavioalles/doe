import config
import design
import os.path
import sys

# check args
if len(sys.argv) != 2 or not os.path.isfile(sys.argv[1]):
    # flush keyword argument added in python 3.3
    print("Wrong usage.", flush=True)
    sys.exit(1)
# read conf. file
print("Loading & checking config. file...", flush=True)
conf = config.getconf(sys.argv[1])
# check if config is good
if not config.checkconf(conf):
    print("Poorly formatted config. file.", flush=True)
    sys.exit(2)
print("Generating design...", flush=True)
# generate base design
base = design.generate(conf)
# replicate it randomly
unnamed = design.replicate(base, conf["replications"])
# translate indexes to levels as described in conf
final = design.translate(unnamed, conf["factors"])
print("Outputting to file...", flush=True)
# output to file
location = design.emit(conf["factors"].keys(), final, os.path.dirname(sys.argv[1]))
print("Done. Design in " + location + ".", flush=True)
sys.exit(0)
