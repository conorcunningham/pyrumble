import setuptools
setuptools.setup(
    name='pyrumble',
    version='0.1',
    description='A simple client for working with the Rumble Run API',
    url='https://github.com/conorcunningham/pyrumble',
    author='Conor Cunningham',
    install_requires=['httpx'],
    author_email='conor@conorcunningham.net',
    packages=setuptools.find_packages(),
    zip_safe=False
)
