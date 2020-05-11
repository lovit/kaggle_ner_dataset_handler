import os
import numpy as np
import pandas as pd


installpath = os.path.abspath(os.path.dirname(__file__))


def load(data_dir=None, random_seed=42):
    """
    Args:
        data_dir: str or None
            Directory path containing `ner.csv` and `ner_dataset.csv`
            If None, it assume that `ner.csv` path is 'path/to/kaggle_ner_dataset_handler/entity-annotated-corpus/ner.csv'
            If you downloaded the dataset to other path, set `data_dir`
        random_seed: int
            Random seed for partitioning `train`, `develop`, `evaluation` set
    """
    if data_dir is None:
        data_dir = f'{installpath}/entity-annotated-corpus/'
    df = pd.read_csv(f'{data_dir}/ner.csv', encoding = 'ISO-8859-1', error_bad_lines=False)

    # modified from https://www.kaggle.com/akshay235/bert-implementation-on-ner-corpus
    def get(sub_df):
        words = sub_df['word'].values.tolist()
        poses = sub_df['pos'].values.tolist()
        tags = sub_df['tag'].values.tolist()
        return list(zip(words, poses, tags))

    grouped = df.groupby("sentence_idx").apply(get)
    sentences = [s for s in grouped]
    n = len(sentences)

    # fix random seed
    np.random.seed(random_seed)
    permuted_indices = np.random.permutation(n)
    last_train = int(0.8 * n)
    last_develop = int(0.9 * n)

    def samples(indices, sentences):
        return [sentences[i] for i in indices]

    train_set = samples(permuted_indices[:last_train], sentences)
    develop_set = samples(permuted_indices[last_train: last_develop], sentences)
    evaluation_set = samples(permuted_indices[last_develop:], sentences)

    return train_set, develop_set, evaluation_set


def write_as_tsv(data, path):
    """Save tap separated value file. Each sentence is separated with empty line."""
    with open(path, 'w', encoding='utf-8') as f:
        for sent in data:
            for w, pos, t in sent:
                f.write(f'{w}\t{pos}\t{t}\n')
            f.write('\n')