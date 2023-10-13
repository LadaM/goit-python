from setuptools import setup, find_namespace_packages

# to distribute the package to the PyPi
with open("README.md", 'r') as fh:
    long_description = fh.read()

setup(
    name="moskali",
    version="1.0",
    long_description=long_description,
    url="https://github.com/dummy_user/example_repo",
    author="Lada M",
    license="MIT",
    packages=find_namespace_packages,
    install_requires=["faker",],
    entry_points={'console_scripts': ['run_main = ']}
)