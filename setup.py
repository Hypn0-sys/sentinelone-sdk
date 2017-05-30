from setuptools import setup, find_packages
setup(
    name="Sentinelone",
    version="0.1",
    packages=find_packages(),
    scripts=['sentinelone.py'],
    install_requires=['requests>=2.12.4'],

    author='Jacolon Walker',
    author_email='jacolon.walker@collectivehealth.com',
    description='SentinelOne SDK which helps IT administrators and security teams help automate management of their Sentinelone fleet',
    license='Apache License 2.0',
    keywords='anti-malware anti-virus security management sentinelone sdk api',
    url='http://collectivehealth.com/security',
)
