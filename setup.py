from setuptools import setup, find_packages

setup(
        name = 'pywm',
        author = 'JChien',
        author_email = 'jeffchien13@gmail.com',
        description = 'monitor filesystem event, and execute command.',
        version = '1.0.0',
        license = 'MIT License',
        packages = find_packages(),
        entry_points = {
            'console_scripts': ['pywm = src.pywm:main']
        },
        install_requires = [
            'pyinotify>=0.9'
        ]
)
