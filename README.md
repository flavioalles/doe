### doe (Design Of Experiment)

Experiments design generator wrapped around [pyDOE](https://pythonhosted.org/pyDOE/).

At this point only [General Full-Factorial Designs](https://en.wikipedia.org/wiki/Factorial_experiment) are supported.

#### Usage

Usable by simply calling:

    python3 src/doe.py <yaml-conf-file>

The `<yaml-conf-file>` must follow the instructions defined in `conf/template.yaml`. An example can be located at `conf/example.yaml`.

#### Requirements

* Python 3.3
* pyDOE
