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
    # can list executable files .exe, bash files, cmd or other files that can be executed by the system
    entry_points={'console_scripts': ['helloworld = package_practice.some_code:hello_world']}
)