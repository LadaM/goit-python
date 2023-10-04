from setuptools import setup, find_namespace_packages

setup(
    name='package_practice',
    version='1',
    description='Practicing creating packages',
    url='http://github.com/dummy_user/useful',
    author='Me Myself and I',
    author_email='me@examplemail.com',
    license='MIT',
    packages=find_namespace_packages(),
    install_requires=['markdown'],
)