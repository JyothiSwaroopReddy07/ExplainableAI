import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

with open("requirements.txt") as f:
    required = f.read().splitlines()

"""
release checklist:
1. update version on `setup.py`
2. update `__version__` on `torch_dreams/__init__.py`
3. run tests with this command `pytest torch_dreams/tests/`
4. commit changes (`setup.py`, `torch_dreams/__init__.py`) and push
5. make release on PyPI. Run the following commands:
    5.1 `python3 setup.py sdist bdist_wheel`
    5.2 (optional) `python3 -m pip install --user --upgrade twine`
    5.3 `python3 -m twine upload dist/*`
6. make a new release on github with the latest version
"""

setuptools.setup(
    name="torch-dreams",
    version="4.0.0",
    author="Jyothi Swaroop Reddy",
    author_email="bjsreddy742002@gmail.com",
    description="Making neural networks more interpretable, for research and art",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/JyothiSwaroopReddy07/ExplainableAI",
    packages=setuptools.find_packages(),
    install_requires=required,
    python_requires=">=3.6",
    include_package_data=True,
    keywords=[
        "PyTorch",
        "machine learning",
        "neural networks",
        "convolutional neural networks",
        "feature visualization",
        "optimization",
    ],
    classifiers=[
        "Intended Audience :: Science/Research",
        "Intended Audience :: Education",
        "Natural Language :: English",
        "Programming Language :: Python :: 3.6",
        "Topic :: Scientific/Engineering",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
        "Topic :: Scientific/Engineering :: Mathematics",
        "Topic :: Scientific/Engineering :: Visualization",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    test_suite="nose.collector",
    tests_require=["nose"],
)
