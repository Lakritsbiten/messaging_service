import setuptools

setuptools.setup(
    name='messaging_service',
    version='0.1.7',
    author='Stefan Solender',
    author_email='stefan.solender@gmail.com',
    packages=setuptools.find_packages(),
    classifiers=[
        'Programming Language :: Python :: 3.7',
        'Intended Audience :: Developers',
    ],
    python_requires='>=3.7',
    install_requires=[
        'setuptools',
        'flask',
        'flask_restx',  # swagger doc
    ],
    include_package_data=True,
    zip_safe=False,
)