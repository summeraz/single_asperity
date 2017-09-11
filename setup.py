from setuptools import setup, find_packages

setup(
    name="single_asperity",
    version="0.1.0",
    long_description=__doc__,
    author='Andrew Z. Summers',
    author_email='andrew.z.summers@vanderbilt.edu',
    url='https://github.com/summeraz/single_asperity',
    packages=find_packages(),
    package_data={'single_asperity': ['lib/forcefields/*.xml',
                                      'lib/patterns/*.xyz',
                                      'lib/surfaces/*.pdb']},
    include_package_data=True,
    zip_safe=False,
)
