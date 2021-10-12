from setuptools import setup, find_packages

VERSION = '0.0.3'
DESCRIPTION = 'Framework to generate an html file with python'
LONG_DESCRIPTION = 'Framework to generate an html file with python'

# Setting up
setup(
    name="camiseta",
    version=VERSION,
    author="Adrien (Adrien4g)",
    author_email="<adrien.de.adrien@gmail.com>",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=LONG_DESCRIPTION,
    packages=find_packages(),
    install_requires=[],
    keywords=['python', 'site', 'html', 'frontend', 'camiseta', 'brazil'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
    ]
)