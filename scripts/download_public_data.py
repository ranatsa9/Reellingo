"""Download the small public datasets used by the ReelLingo prototype.

This script downloads MovieLens Latest Small and the CMU Movie Summary Corpus
from their official sources. OPUS OpenSubtitles requires the user to select a
language pair and format from its official dataset interface, so it is not
downloaded automatically here.

Review each dataset's terms before use or redistribution.
"""

from pathlib import Path
from urllib.request import urlretrieve


ROOT = Path(__file__).resolve().parents[1]
RAW = ROOT / "data" / "raw"

DOWNLOADS = {
    "movielens/ml-latest-small.zip": (
        "https://files.grouplens.org/datasets/movielens/ml-latest-small.zip"
    ),
    "cmu_movie_summaries/MovieSummaries.tar.gz": (
        "https://www.cs.cmu.edu/~ark/personas/data/MovieSummaries.tar.gz"
    ),
}


def download(relative_path: str, url: str) -> None:
    destination = RAW / relative_path
    destination.parent.mkdir(parents=True, exist_ok=True)

    if destination.exists():
        print(f"Already exists: {destination}")
        return

    print(f"Downloading {url}")
    urlretrieve(url, destination)
    print(f"Saved to {destination}")


def main() -> None:
    for relative_path, url in DOWNLOADS.items():
        download(relative_path, url)

    print("\nOpenSubtitles must be selected manually:")
    print("https://opus.nlpl.eu/datasets/OpenSubtitles")


if __name__ == "__main__":
    main()

