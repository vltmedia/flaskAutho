# Create setup.py file for uaiDiffusers.py that requires socket
#

from setuptools import setup, find_packages

# setup(name='uaiDiffusers', version='1.0', py_modules=['uaiDiffusers'],long_description=open('README.md').read(), requires=['socket'])
# Setup file for uaiDiffusers.py that requires socket and MediaItems.py and cv2
#
# setup(name='uaiDiffusers', version='1.1', py_modules=['uaiDiffusers'],long_description=open('README.md').read(), requires=['socket', 'MediaItems', 'cv2'])
setup(name='authovalidator', version='1.0.65', py_modules=['authovalidator'], 
    url="https://github.com/vltmedia/authovalidator", packages=find_packages(),)