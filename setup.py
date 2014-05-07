from setuptools import setup, find_packages
import os

description = 'python wrapper for basecamp-next api'

def get_description():
    if os.path.exists('README.rst'):
        return open('README.rst','r').read()
    else:
        return description
        

config = {
        'name':'basehead',
        'version':'0.5.1',
        'description': description,
        'long_description': get_description(),
        'author': 'Kyle Roux',
        'author_email':'kyle@level2designs.com',
        'maintainer':'kyle@level2designs.com',
        'packages':find_packages(),
        # uncomment next line if packages not in top level dir
        #'package_dir':{'':'dir'}
        'include_package_data':True,
        'zip_safe':False,
        'install_requires':[],#,basehead]
}

setup(**config)

