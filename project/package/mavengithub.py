import argparse
import json
import os
import os.path
import subprocess
import xml.etree.ElementTree as et

from . import maven
from jl95terceira.batteries import *

class DepsInstaller:

    def __init__(self, project_dir:str):

        self._pom = maven.Pom(os.path.join(project_dir if project_dir is not None else os.getcwd(), 'pom.xml'))

    def install_deps_by_map(self, deps_map:dict[tuple[str,str],str]):

        for dep in self._pom.dependencies():



    def install_deps_by_mapfile_path(self, deps_mapfile_path:str|None=None):

        with open(deps_mapfile_path, mode='r') as fr:

            deps_map_raw:dict[str,str] = json.load(fr)
            deps_map = dict((k.split(':')[:2],v) for k,v in deps_map_raw.items())

        self.install_deps_by_map(deps_map)

if __name__ == '__main__':

    p = argparse.ArgumentParser(formatter_class=argparse.RawTextHelpFormatter,
                                description='Download and build Maven dependencies from their corresponding Github projects')
    class A:
        DEPS_MAPFILE = 'mapfile'
        PROJECT_DIR  = 'wd'
    class Defaults:
        DEPS_MAPFILE = 'depsmapfile'
    p.add_argument(f'--{A.PROJECT_DIR}',
                   help=f'Project / working dir\nDefault: current directory')
    p.add_argument(f'--{A.DEPS_MAPFILE}',
                   help=f'Path of dependencies map file to consider, relative to working directory, if different than the default ({Defaults.DEPS_MAPFILE})')
    # parse
    get = p.parse_args().__getattribute__
    project_dir       = get(A.PROJECT_DIR)
    deps_mapfile_path = get(A.DEPS_MAPFILE)
    # do it
    DepsInstaller(project_dir).install_deps_by_mapfile_path(deps_mapfile_path=deps_mapfile_path)
