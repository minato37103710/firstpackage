from setuptools import setup


requires = ["requests>=2.14.2"]


setup(
    name='firstpackage',
    version='0.1',
    description='Awesome library',
    url='https://github.com/wminato37103710/firstpackage',
    author='minato37103710',
    author_email='arigatoudane@outlook.jp',
    license='MIT',
    keywords='sample setuptools development',
    packages=[
        "firstpackage",
    ],
    install_requires=requires,
    classifiers=[
        'Programming Language :: Python :: 3.10.4',
    ],
)