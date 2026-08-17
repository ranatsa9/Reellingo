# ReelLingo

## Adaptive Language Learning Through Movies

ReelLingo is an AI-powered learning companion for Arabic-speaking students who want to improve a target language through movies. It recommends films using both the learner's entertainment preferences and an appropriate linguistic challenge.

Unlike streaming platforms that optimize only for entertainment, ReelLingo asks:

> Which movie will the learner enjoy **and** understand well enough to learn from?

The initial two-week prototype focuses on Arabic-speaking students learning English. The architecture can later support additional languages when suitable subtitle data and language-specific evaluation resources are available.

## Who It Serves

ReelLingo primarily serves Arabic-speaking university students who:

- Already watch English-language movies
- Want to improve conversational vocabulary and listening comprehension
- Find conventional language practice difficult to sustain
- Cannot access continuous personalized tutoring
- Need material matched to both their interests and current ability

## The Problem

Many students watch movies hoping to improve their English, but they often select films that are too difficult, depend completely on Arabic subtitles, or cannot measure whether they learned anything. Existing movie recommenders consider taste and popularity, not language-learning suitability.

## User Journey

### 1. Create a learner profile

The user provides:

- Native and target language
- Approximate language ability
- Favourite movies and genres
- Preferred subtitle setting
- Learning focus: vocabulary, listening, expressions, or idioms

An optional placement activity can refine the initial profile.

### 2. Select a learning mode

- **Relaxed:** easier language and high entertainment match
- **Balanced:** appropriate difficulty with useful new language
- **Challenge:** a stronger linguistic stretch without excessive overload

### 3. Receive movie recommendations

Each recommendation displays:

- Taste-match score
- Relative language difficulty
- Learning-fit score
- Dialogue density
- Vocabulary complexity
- Slang or idiom intensity
- A clear explanation of why the movie fits

### 4. Complete spoiler-free preparation

Before watching, the user receives a short pack containing:

- Five useful words or expressions
- Simple meanings and Arabic explanations
- A short contextual exercise
- No major plot information

### 5. Watch on the user's preferred platform

ReelLingo does not stream or redistribute movies. It functions as a companion application.

### 6. Complete a post-movie activity

The learner answers short vocabulary and comprehension questions and reports whether the movie felt too easy, suitable, or too difficult.

### 7. Update the learning path

The system updates the learner profile and adjusts the next recommendation. For example, it may keep vocabulary complexity stable while selecting slower dialogue if speech pace was difficult.

## Example

**Learner profile**

- Favourite films: *Interstellar*, *Inception*, *Arrival*
- English ability: Intermediate
- Goal: Conversational vocabulary
- Mode: Balanced

**Possible recommendation**

> **The Martian**
>
> Strong science-fiction and problem-solving taste match. Its important vocabulary is repeated and its dialogue is relatively more accessible than highly abstract science-fiction films.

**Spoiler-free preparation**

- figure something out
- run out of
- make it work
- against the odds
- keep someone posted

After the activity, the system uses the learner's performance to choose the next appropriate film.

## AI Architecture

```text
MovieLens ratings and tags ──> Taste model ───────────────┐
                                                          │
Movie summaries ────────────> Content and genre model ────┼─> Hybrid ranking
                                                          │
Subtitle-derived features ──> Language-difficulty model ──┘
                                                                   │
Learner profile and quiz history ──────────────────────────────────┘
                                                                   │
                                                                   v
                                              Personalized movie learning path
```

## Movie Language Profile

For every movie in the prototype catalogue, ReelLingo can derive:

- Average sentence length
- Vocabulary frequency and rarity
- Lexical diversity
- Relative word difficulty
- Dialogue density
- Estimated words per minute when timestamps are available
- Slang and idiom frequency
- Vocabulary repetition
- Named-entity density

The prototype reports **relative difficulty** such as low, medium, or high. It will not claim official CEFR levels without an appropriately labelled CEFR dataset.

## Hybrid Recommendation

An example ranking formula is:

```text
Final Score =
    0.40 × Taste Match
  + 0.35 × Language Fit
  + 0.15 × Learning Value
  + 0.10 × Movie Quality
```

The weights can change based on relaxed, balanced, or challenge mode.

## AI and Data-Science Techniques

| Technique | Application |
|---|---|
| Exploratory data analysis | Examine ratings, genres, tags, and subtitle features |
| Statistics | Analyze vocabulary and linguistic-feature distributions |
| Supervised learning | Predict genres or ratings and compare baseline models |
| Unsupervised learning | Cluster movies by linguistic style and relative difficulty |
| Text embeddings | Represent movie summaries and subtitle language |
| Collaborative filtering | Learn entertainment preferences from ratings |
| Hybrid recommendation | Combine taste and learning suitability |
| Ensemble scoring | Combine multiple models and constraints |
| NLP | Analyze summaries, vocabulary, expressions, and subtitles |
| LLM support | Generate grounded explanations and short learning activities |

## Datasets

ReelLingo uses three complementary sources:

1. **MovieLens Latest Small** for ratings, tags, and taste modelling.
2. **CMU Movie Summary Corpus** for plot summaries, genres, runtime, and language metadata.
3. **A limited OPUS OpenSubtitles subset** for subtitle-language analysis.

See [docs/DATASETS.md](docs/DATASETS.md) for official links, licensing notes, and download instructions.

## Research Question

> Can combining linguistic suitability with entertainment preference produce a more useful movie-based learning path than recommendations based only on popularity or taste?

## Evaluation

### Recommendation baselines

Compare:

1. Popularity-based recommendation
2. Content-based recommendation
3. Collaborative filtering
4. Language-fit-only recommendation
5. ReelLingo hybrid recommendation

### Metrics

- RMSE or MAE for rating prediction
- Precision@K and Recall@K
- NDCG@K
- Silhouette score for linguistic clusters
- Genre-classification F1 score
- User-rated recommendation relevance
- User-rated difficulty fit
- Short-term vocabulary recall in a small pilot

### Small user pilot

Approximately 10–20 volunteer students can complete:

- A short pre-activity
- A ReelLingo vocabulary preparation activity
- A selected short viewing task or approved excerpt
- A post-activity vocabulary and comprehension check

Any result will be reported as a preliminary class-project finding, not proof of long-term language improvement.

## Two-Week MVP

### Week 1

- Prepare MovieLens and CMU data
- Select a catalogue of 100–300 movies
- Extract subtitle-derived linguistic features
- Conduct EDA
- Train recommendation and classification baselines
- Cluster movies by relative linguistic difficulty

### Week 2

- Build the hybrid ranking model
- Implement learner profiles and three learning modes
- Generate grounded vocabulary preparation
- Implement the post-movie activity and profile update
- Build a Streamlit interface
- Evaluate models and prepare the presentation

## Scope Boundaries

The prototype will not:

- Stream movies
- Redistribute full subtitles
- Support every movie or every language
- Claim official CEFR classification
- Train a large language model from scratch
- Guarantee language improvement

## Responsible and Legal Use

- Store only derived subtitle features where possible.
- Use limited excerpts only when permitted.
- Attribute OPUS and OpenSubtitles as required.
- Do not commit or redistribute MovieLens data contrary to its licence.
- Keep generated activities grounded in the selected vocabulary and metadata.
- Explain that recommendations are estimates, not formal educational assessment.

## Repository Structure

```text
reellingo/
├── README.md
├── PROJECT_PROPOSAL.md
├── requirements.txt
├── .gitignore
├── data/
│   ├── README.md
│   └── sample_movie_features.csv
├── docs/
│   ├── DATASETS.md
│   └── USER_FLOW.md
└── scripts/
    └── download_public_data.py
```

## Current Status

This repository contains the final-project proposal, reproducible data plan, and expected data schema. Application implementation begins after project approval.

