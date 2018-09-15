import setuptools
# wraps distutils.core.setup
# calls also _install_setup_requires(attrs) which calls
# distutils.core.Distribution(attrs) and runs methods on that.

with open("README.md", "r") as f:
    long_description = f.read()


setuptools.setup(
    name="tornado-console-2",
    version="2.0.0",
    author="dangerwillrobinsondanger",
    author_email="dangerwillrobinsondanger@gmail.com",
    description="Console for Tornado apps.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/dangerwillrobinsondanger/tornado-console",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    keywords='tornado console web python development pip',
    project_urls={
        'Documentation':
            'https://github.com/dangerwillrobinsondanger/tornado-console/wiki',
        # 'Funding': 'https://donate.pypi.org',
        # 'Say Thanks!': 'http://saythanks.io/to/example',
        'Source':
            'https://github.com/dangerwillrobinsondanger/tornado-console',
        'Tracker':
            'https://github.com/dangerwillrobinsondanger/tornado-console/issues',
    },
    install_requires=['tornado'],
    python_requires='>=3.7'
)


# import distutils.core

# distutils.core.setup(
#
# )
