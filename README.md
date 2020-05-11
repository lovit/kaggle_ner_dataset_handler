# Easy-Handler for Kaggle Annotated Corpus for Named Entity Recognition

It helps you load the kaggle dataset easily.
You first download it from https://www.kaggle.com/abhinavwalia95/entity-annotated-corpus

## Usage

`load` function partitions the dataset to `train`, `develop`, `test` with permutation.
The format of each dataset is `list of sentence` and the format of each sentence is `list of tuple`.
The tuple consists with (`word`, `POS`, `NER tag`).

```python
from kaggle_ner_dataset_handler import load

data_dir = 'path/to/entity-annotated-corpus/'
train, develop, test = load(data_dir)
train[0]  # select first sentence
```

```
[('Israel', 'NNP', 'B-geo'),
 ("'s", 'POS', 'O'),
 ('security', 'NN', 'O'),
 ('cabinet', 'NN', 'O'),
 ('has', 'VBZ', 'O'),
 ('approved', 'VBN', 'O'),
 ('a', 'DT', 'O'),
 ...
```
