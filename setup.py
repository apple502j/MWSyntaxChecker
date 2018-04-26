from setuptools import setup, find_packages

setup(
    name="MWSyntaxChecker",
    version="1.0.0",
    description="Checker for MediaWiki syntax",
    long_description="Checks wikitext for common errors.",
    url="https://github.com/apple502j/MWSyntaxChecker",
    author="apple502j",
    license="GPLv3",
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content :: Wiki',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.6'
    ],
    keywords='mediawiki syntax checker',
    packages=find_packages(),
    python_requires='>=2.7',
)
