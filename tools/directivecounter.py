# Copyright (C) ALbert Mietus;  2018. Part of DocIdeas project http://docideas.mietus.nl/
# Python3 code, use with IPYTHON

import re
import os, os.path
import collections
from logging import getLogger; logger = getLogger(__name__)
from pathlib import Path

class DirectiveCounterBase(collections.Counter):
    pass

    def info(self, top=5):
        return "No of Directive-kinds: %i.  Total no of Directives: %i.  Top(%i):\n%s" %(
            len(self), sum(c for n,c in self.most_common()), top,
            "\n".join("\t%-15s: %5i" % (n, c) for n,c in self.most_common(top)))


class FileDirectiveCounter(DirectiveCounterBase):
    """See: ``DirectiveCounter``; file-mode.

    Assumes the file is text-based, containing (mostly) documentation;
    including python-code with embedded documentation.
    """

    _directive_re = re.compile(r"^ *\.\. (?P<directive>\w+) *::")
    _debug = []                                                         # for development

    def __init__(self, filename):
        self.filename = filename
        self.scan()

    def scan(self):
        try:
            with open(self.filename, errors='replace') as f:
                for l in f.readlines():
                    for m in self._directive_re.finditer(l):
                        if m:
                            found = m['directive'].lower()
                            self[found] += 1
                            if self._debug and found in self._debug:
                                print(found, self.filename)
        except (IOError, UnicodeDecodeError) as e:
            logger.warning('ignored %s in %s: %s', type(e).__name__, self.filename, e)



class ProjectDirectiveCounter(DirectiveCounterBase):
    """See: ``DirectiveCounter``; dir-mode.

    Run ``FileDirectiveCounter`` for all (relevant) files in the given dir-tree.
    Stores the DirectiveCounter for each file, and in itself for the total.
    """

    _ext =("rst", "py")

    def __init__(self, dirname):
        self.dirname = dirname
        self.files = {}
        for f in self.rst_walk():
            self.files[f] = FileDirectiveCounter(f)
            self += self.files[f]

    def rst_walk(self):
        """Walk (like os.walk) over the specified directory and yield files that may contain rst-statements.
        This is determined by the extension: when it listed in _ext, it's used.
        """
        for (p, _d, fs) in os.walk(self.dirname):
            for f in [f for f in fs if os.path.splitext(f)[1] and os.path.splitext(f)[1][1:] in self._ext]:
                yield os.path.join(p, f)



class ListDirectiveCounter(DirectiveCounterBase):
    """Run (Project)DirectiveCounter for a list of projects
    """

    def __init__(self, list_of_prjs):
        self.prjCounts = {}
        for p in list_of_prjs:
            p = Path(p)
            self.prjCounts[p] = ProjectDirectiveCounter(p)
            self += self.prjCounts[p]



class DirectiveCounter(DirectiveCounterBase):
    """Scan and count all RST-directives in a single file, or a (project) directory.
    """

    def __new__(self, dir_or_file):
        if os.path.isdir(dir_or_file):
            return ProjectDirectiveCounter(dir_or_file)
        elif os.path.isfile(dir_or_file):
            return FileDirectiveCounter(dir_or_file)
        else:
            raise TypeError("No file, nor directory: %s"% dir_or_file)
