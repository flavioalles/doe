import os.path
import pyDOE
import random

SEP = ","

def generate(conf):
    """Generate base design by calling pyDOE"""
    # build list containing number levels for each factor (argument to pyDOE)
    levels = list()
    for factor in conf["factors"].keys():
        levels.append(len(conf["factors"][factor]))
    # call pyDOE method corresponding to conf["design"]
    if conf["design"] == "fullfact":
        base = pyDOE.fullfact(levels)
    return base

def replicate(base, replications):
    """Randomly Replicates `replications` times each experiment in `base`"""
    # build list that will contain final design
    unnamed = list()
    # tracker of times each experiment has been replicated
    tracker = [replications for e in base]
    while sum(tracker) > 0:
        # randomly select experiment index (in base)
        exp = random.randint(0, len(base)-1)
        # check if experiment selected has been replicated enough
        if tracker[exp] != 0:
            # append selected experiment to final design
            unnamed.append(list(map(int, base[exp])))
            # subtract from experiment tracker
            tracker[exp] -= 1
    return unnamed

def translate(unnamed, factors):
    """Translates unnamed, integer-based levels to names as described in config. file"""
    # create final design container
    final = list()
    # iterate over every line of unnamed `unnamed`
    for line in unnamed:
        exp = list()
        # perform translation from index to appropriate name
        for (level, factor) in zip(line, factors):
            exp.append(str(factors[factor][level]))
        final.append(exp)
    return final

def emit(factors, final, path):
    """Outputs as `csv` the design in `final` to the dir. specified by `path`"""
    location = os.path.join(path, "design.csv")
    with open(location, "w") as output:
        # write header
        header = str()
        for (index, factor) in enumerate(factors):
            if index != len(factors) - 1:
                header += factor + SEP
            else: header += factor + "\n"
        output.write(header)
        # write experiments
        for line in final:
            exp = str()
            for (index, factor) in enumerate(line):
                if index != len(line) - 1:
                     exp += factor + SEP
                else: exp += factor + "\n"
            output.write(exp)
    return location
