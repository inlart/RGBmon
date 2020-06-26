import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="rgbmon",
    version="0.0.1",
    author="inlart",
    author_email="g@inlart.com",
    description="System monitoring tool that colors your hardware",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/inlart/RGBmon",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.7',
    install_requires=[
        'openrgb-python',
    ],
    entry_points = {
        'console_scripts': ['rgbmon=rgbmon.rgbmon:main'],
    },
)