from setuptools import setup
from setuptools.command.test import test as TestCommand
import sys

try:
    import matplotlib
except ImportError:
    print('Building and running timplotlib requires matplotlib.')
    sys.exit(1)

requirements = [line.strip() for line in open('requirements.txt').readlines()]


class PyTest(TestCommand):
    def finalize_options(self):
        TestCommand.finalize_options(self)
        self.test_args = []
        self.test_suite = True

    def run_tests(self):
        import pytest
        errcode = pytest.main(['timplotlib'])
        sys.exit(errcode)


setup(name='timplotlib',
      version='0.0',
      description='Some functions I often use to make plots prettier',
      url='http://github.com/tcmoore3/timplotlib',
      author='Timothy C. Moore',
      author_email='timothy.c.moore@vanderbilt.edu',
      license='MIT',
      packages=['timplotlib'],
      install_requires=requirements,
      zip_safe=False,
      test_suite='tests',
      cmdclass={'test': PyTest},
      extras_require={'utils': ['pytest']},
)
