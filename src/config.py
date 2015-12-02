import yaml

KEYS = ["design", "replications", "factors"]
DESIGNS = ["fullfact"]

def getconf(path):
    """Returns associate container (i.e. Dict) holding the elements in path"""
    with open(path, "r") as stream:
        conf = stream.read()
    return yaml.load(conf)

def checkconf(conf):
    """Check whether conf is well formatted."""
    # check keys
    if len(conf.keys()) != len(KEYS):
        return False
    for key in KEYS:
        if key not in conf.keys():
            return False
    # check design
    if not isinstance(conf["design"], str) or conf["design"] not in DESIGNS:
        return False
    # check replications
    if not isinstance(conf["replications"], int) or int(conf["replications"]) < 1:
        return False
    # check factors
    if isinstance(conf["factors"], dict) and len(conf["factors"].keys()) > 0:
        for key in conf["factors"].keys():
            if not isinstance(conf["factors"][key], list) or len(conf["factors"][key]) == 0:
                return False
    else: return False
    # if execution got here, conf is ok
    return True
