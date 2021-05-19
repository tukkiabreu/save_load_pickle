from setuptools import setup, find_packages
import pacotes_enel

setup(
    name='pacotes_enel',
    version=pacotes_enel.__version__,

    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'enel_pip = pacotes_enel.enel_pip.enel_pip:command_parser',
            'pip_enel = pacotes_enel.enel_pip.enel_pip:command_parser',
            #'enel_clone = enel_clone.main:run_commands',
            #'clone_enel = enel_clone.main:run_commands'
        ]
    }
)