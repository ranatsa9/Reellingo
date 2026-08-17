# Dataset Guide

Third-party datasets should not be committed to this repository unless their licences explicitly permit redistribution. Use the official sources below and review their terms.

## 1. MovieLens Latest Small

Purpose:

- User ratings
- Movie titles and genres
- User-generated tags
- Collaborative-filtering and hybrid-recommendation experiments

Official page:

- https://grouplens.org/datasets/movielens/

Direct educational-size download:

- https://files.grouplens.org/datasets/movielens/ml-latest-small.zip

Approximate size: 1 MB compressed.

Important: read the included README and usage terms. Do not redistribute the downloaded dataset through this repository.

## 2. CMU Movie Summary Corpus

Purpose:

- 42,306 plot summaries
- Movie genres
- Runtime
- Release date
- Language and country metadata
- NLP and supervised genre-classification experiments

Official page:

- https://www.cs.cmu.edu/~ark/personas/

Direct download:

- https://www.cs.cmu.edu/~ark/personas/data/MovieSummaries.tar.gz

Approximate size: 46 MB compressed.

The official page states that the data is released under Creative Commons Attribution-ShareAlike. Preserve attribution and review the included README.

## 3. OPUS OpenSubtitles

Purpose:

- Subtitle-derived vocabulary and sentence features
- English–Arabic aligned text exploration
- Multilingual future expansion

Official selector:

- https://opus.nlpl.eu/datasets/OpenSubtitles

Select a manageable subset, such as:

- Corpus: OpenSubtitles
- Source language: English
- Target language: Arabic
- Format: Moses or TMX

Important:

- Use only the minimum subset required.
- Follow OPUS/OpenSubtitles attribution instructions.
- Do not commit the full corpus.
- Prefer committing derived numerical features rather than subtitle text.
- The corpus includes both film and television material, so title alignment may require additional cleaning.

## Recommended Download Order

1. MovieLens Latest Small
2. CMU Movie Summary Corpus
3. A carefully selected OPUS subtitle subset after confirming the prototype catalogue

## Expected Local Directories

```text
data/raw/movielens/
data/raw/cmu_movie_summaries/
data/raw/opus_subtitles/
data/processed/
```

The `data/raw` directory is ignored by Git.

