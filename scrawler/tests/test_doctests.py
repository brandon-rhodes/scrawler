import doctest
import pkgutil

import scrawler

def load_tests(loader, tests, ignore):
    """Create a DocTestSuite for every module in the main package."""

    it = pkgutil.iter_modules(scrawler.__path__, scrawler.__name__ + '.')
    for importer, name, ispkg in it:
        if not ispkg:
            module = __import__(name, fromlist='dummy')
            tests.addTests(doctest.DocTestSuite(module))
    return tests
