import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

pkgs = setuptools.find_packages()
print('found these packages:', pkgs)

pkg_name = "getArenaParameters"

setuptools.setup(
    name=pkg_name,
    version="1.0.0",
    author="Geoffrey Barrett",
    author_email="geoffrey.m.barrett@gmail.com",
    description="getArenaParameters - GUI designed to acquire arena parameters (pixels-per-meter, and center position).",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/GeoffBarrett/getArenaParameters.git",
    packages=pkgs,
    install_requires=
    [
        'numpy',
        'matplotlib',
        'scipy',
    ],
    package_data={'getArenaParamters': ['img/*.png']},
    classifiers=[
        "Programming Language :: Python :: 3.7 ",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3) ",
        "Operating System :: OS Independent",
    ],
)
