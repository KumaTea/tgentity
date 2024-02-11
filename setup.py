import tomllib
from setuptools import setup, find_packages


with open("pyproject.toml", 'rb') as f:
    config = tomllib.load(f)

with open("README.md", "r", encoding="utf-8") as f:
    readme = f.read()

setup(
    name=config["project"]["name"],
    version=config["project"]["version"],
    description=config["project"]["description"],
    long_description=readme,
    long_description_content_type=config['project']['readme']['content-type'],
    url=config['project']['urls']['Repository'],
    download_url=config['project']['urls']['Repository'] + "/releases/latest",
    author=config['project']['authors'][0]['name'],
    author_email=config['project']['authors'][0]['email'],
    license="MIT",
    packages=find_packages(),
    python_requires=config['project']['requires-python'],
    install_requires=[],  # no dependencies
    # extras_require={
    #     "dev": []
    # },
    classifiers=config['project']['classifiers'],
    keywords=" ".join(config['project']['keywords']),
    project_urls={
        "Source": config['project']['urls']['Repository'],
    },
    test_suite="tests",
    # zip_safe=True,
    ext_modules=[],
)
