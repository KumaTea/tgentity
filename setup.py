import tomllib
from setuptools import setup, find_packages


with open("pyproject.toml", 'rb') as f:
    config = tomllib.load(f)


with open("README.md", encoding="utf-8") as f:
    readme = f.read()


setup(
    name="TgEntity",
    version=config["project"]["version"],
    description="Telegram entity parser",
    long_description=readme,
    long_description_content_type="text/markdown",
    url="https://github.com/KumaTea/tgentity",
    download_url="https://github.com/KumaTea/tgentity/releases/latest",
    author="KumaTea",
    author_email="mail@kmtea.eu",
    license="MIT",
    packages=find_packages(),
    python_requires=">=3.10",  # match-case
    install_requires=[],  # no dependencies
    # extras_require={
    #     "dev": []
    # },
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Programming Language :: Python :: Implementation",
        "Programming Language :: Python :: Implementation :: CPython",
        "Programming Language :: Python :: Implementation :: PyPy",
        "Topic :: Communications",
        "Topic :: Communications :: Chat",
        "Topic :: Software Development :: Libraries",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    keywords="telegram entity entities parser html markdown v2",
    project_urls={
        "Source": "https://github.com/KumaTea/tgentity",
    },
    test_suite="tests",
    # zip_safe=True,
    ext_modules=[],
)
