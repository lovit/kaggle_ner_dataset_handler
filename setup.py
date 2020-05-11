import kaggle_ner_dataset_handler
from setuptools import setup, find_packages

with open('README.md', encoding='utf-8') as f:
    long_description = f.read()

setup(
    name="kaggle_ner_dataset_handler",
    version=kaggle_ner_dataset_handler.__version__,
    author=kaggle_ner_dataset_handler.__author__,
    author_email='soy.lovit@gmail.com',
    url='https://github.com/lovit/kaggle_ner_dataset_handler',
    description="Easy-Handler for Kaggle Annotated Corpus for Named Entity Recognition",
    long_description=long_description,
    long_description_content_type='text/markdown',
    install_requires=["pandas>=0.25.3", "numpy>=1.15.2"],
    packages=find_packages()
)
