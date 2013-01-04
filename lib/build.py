#! /usr/bin/env python

import argparse
import contextlib
import fcntl
import os


@contextlib.contextmanager
def lock(filename):
    fd = os.open(filename, os.O_WRONLY | os.O_CREAT, 0600)
    fcntl.flock(fd, fcntl.LOCK_EX)
    yield
    fcntl.flock(fd, fcntl.LOCK_UN)
    os.close(fd)


def available_patterns():
    patterns = {'modernizr', 'less', 'prefixfree'}
    path = os.path.join(os.path.dirname(__file__), os.pardir, 'src', 'patterns')
    for fn in os.listdir(path):
        if fn.endswith('.js'):
            patterns.add(fn[:-3])
    return frozenset(patterns)


def list_type(value):
    return [v.strip() for v in value.split(',')]


class PatternList(argparse.Action):
    patterns = available_patterns()

    def __call__(self, parser, namespace, values, option_string=None):
        output = getattr(namespace, self.dest, [])
        for value in values:
            if value not in self.patterns:
                parser.error('Unknown pattern: %s' % value)
        output.extend(values)
        setattr(namespace, self.dest, output)


LOCKFILE = '.build.lock'


def main():
    parser = argparse.ArgumentParser(
            description="Build custom Pattern bundles.")
    parser.add_argument('-l', '--lock', metavar='LOCKFILE', default=LOCKFILE,
            help='Lock file to prevent parallel builds.')
    parser.add_argument('-c', '--compress', action='store_true',
            default=False,
            help='Generate a compressed bundle.')
    parser.add_argument('-p', '--pattern', dest='patterns',
            default=[], action=PatternList, type=list_type,
            help='Comma-separated list of patterns to include.')
    options = parser.parse_args()
    with lock(options.lock):
        print options.patterns


if __name__ == '__main__':
    main()
