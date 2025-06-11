from setuptools import setup, find_packages

setup(
    name='cold_gas_toolkit',
    version='1.0.0',
    author='Jaxsen Cheeks',
    author_email='jcheeks7@gatech.edu',
    description='A physics-based toolkit for sizing, modeling, and simulating cold gas propulsion systems.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/jcheeks7/cold-gas-thruster',
    packages=find_packages(include=['cold_gas_toolkit', 'cold_gas_toolkit.*']),
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Topic :: Scientific/Engineering :: Physics',
    ],
    python_requires='>=3.7',
    install_requires=[
        'matplotlib',
        'scipy',
    ],
    include_package_data=True,
)
