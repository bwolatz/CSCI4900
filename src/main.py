#spdx-License-Identifier: MIT
'''Usage:
{0} FILE
{0} (--help | --version)
Arguments:
    FILE    path to pom.xml
'''
import shutil
import sys
import os
from dependency import Dependency
from docopt import docopt

__version__ = '0.0.1'

def main():
    argv = docopt(
        doc=__doc__.format(os.path.basename(sys.argv[0])),
        argv=sys.argv[1:],
        version=__version__
    )

    if argv['FILE']:
        dependency = Dependency()

        dependency.copyPom(os.path.abspath(argv['FILE']))
        dependency.getDependenciesandScan()

        shutil.rmtree(dependency.tempdir)

if __name__ == "__main__":
    sys.exit(main())
