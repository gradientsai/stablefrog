import os

from setuptools import find_packages, setup

REQUIRED_PKGS = ["numpy>=1.17"]

TEMPLATE_REQUIRE = [
    # to populate metric template
    "cookiecutter"]
TESTS_REQUIRE = [
    "absl-py",
    "nltk",
    "pytest",
    "tensorflow>=2.3,!=2.6.0,!=2.6.1, <=2.10",
    "torch",
    "scipy",
    # to speed up pip backtracking
    "toml>=0.10.1",
    "requests_file>=1.5.1",
    "tldextract>=3.1.0",
    "texttable>=1.6.3",
    "unidecode>=1.3.4",
    "Werkzeug>=1.0.1",
    "six~=1.15.0",
]
EVALUATION_REQUIRE = [
   "transformers",
   "scipy>=1.7.1",
]
QUALITY_REQUIRE = ["black~=22.0", "flake8>=3.8.3", "isort>=5.0.0", "pyyaml>=5.3.1"]
EXTRAS_REQUIRE = {
    "tensorflow": ["tensorflow>=2.2.0,!=2.6.0,!=2.6.1"],
    "tensorflow_gpu": ["tensorflow-gpu>=2.2.0,!=2.6.0,!=2.6.1"],
    "torch": ["torch"],
    "dev": TESTS_REQUIRE + QUALITY_REQUIRE,
    "tests": TESTS_REQUIRE,
    "quality": QUALITY_REQUIRE,
    "docs": [
        # Might need to add doc-builder and some specific deps in the future
        "s3fs",
    ],
    "template": TEMPLATE_REQUIRE,
    "evaluation": EVALUATION_REQUIRE
}
setup(
    name="stablefrog",
    version="0.0.1",  # x.y.z
    description="Gradients open-source library of large language model evaluation",
    long_description=open("README.md", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    author="Sharad Varshney@Gradients",
    author_email="sharad@gradients.ai",
    url="https://github.com/gradients/stablefrog",
    download_url="https://github.com/gradients/stablefrog/tags",
    license="MIT",
    package_dir={"": "src"},
    packages=find_packages("src"),
    entry_points={"console_scripts": ["evaluate-cli=stablefrog.commands.evaluate_cli:main"]},
    install_requires=REQUIRED_PKGS,
    extras_require=EXTRAS_REQUIRE,
    python_requires=">=3.9.0",
    classifiers=[
        "Development Status :: 1 - Production/Stable",
        "Intended Audience :: Developers",
        "Intended Audience :: Education",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.9",
        "Topic :: Engineering/Generative AI/Large Language Model/Data Science/AI :: Artificial Intelligence",
    ],
    keywords="metrics machine learning model evaluation llm",
    zip_safe=False,  # Required for mypy to find the py.typed file
)