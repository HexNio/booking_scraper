import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="booking_scraper",
    version="1.0.1",
    author="HexNio",
    author_email="",
    description="A scraper for the booking.com website",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/HexNio/booking_scraper",
    packages=setuptools.find_packages(),
    keywords=[
        "scarper",
        "web scraper"
        "beautifulsoup4"
        "automation"
    ],
    classifiers=[
        "Programming Language :: Python :: 3 :: Only",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: MacOS :: MacOS X",
        "Intended Audience :: Other Audience",
        "Intended Audience :: Education",
        "Topic :: Internet"
    ],
    install_requires=[
        'requests',
        'lxml',
        'beautifulsoup4'
    ],
    python_requires='>=3.6'
)