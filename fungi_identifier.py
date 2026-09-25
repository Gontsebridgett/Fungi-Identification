"""
fungi_identifier.py

Applies a simplified morphology-based identification key to recorded fungal
isolate observations (colony colour, texture, growth rate, and microscopic
spore-bearing structure) and returns the best-matching genus for each isolate.
"""

import csv
from pathlib import Path

DATA_PATH = Path(__file__).parent / "sample_data" / "isolate_observations.csv"

# Reference identification key: genus -> expected feature values
KEY = {
    "Aspergillus": {
        "colour": "green",
        "texture": "powdery",
        "growth_rate": "fast",
        "spore_structure": "radiating_head",
    },
    "Penicillium": {
        "colour": "blue_green",
        "texture": "velvety",
        "growth_rate": "moderate",
        "spore_structure": "penicillus",
    },
    "Rhizopus": {
        "colour": "white",
        "texture": "cottony",
        "growth_rate": "very_fast",
        "spore_structure": "sporangia",
    },
    "Candida": {
        "colour": "cream",
        "texture": "smooth",
        "growth_rate": "fast",
        "spore_structure": "budding_yeast",
    },
    "Trichophyton": {
        "colour": "white",
        "texture": "cottony",
        "growth_rate": "slow",
        "spore_structure": "microconidia",
    },
}


def load_isolates(path: Path):
    with open(path, newline="") as f:
        return list(csv.DictReader(f))


def score_match(observation: dict, reference: dict) -> int:
    features = ["colour", "texture", "growth_rate", "spore_structure"]
    return sum(1 for feat in features if observation.get(feat) == reference.get(feat))


def identify(observation: dict):
    scores = {genus: score_match(observation, ref) for genus, ref in KEY.items()}
    best_genus = max(scores, key=scores.get)
    return best_genus, scores[best_genus]


def main():
    isolates = load_isolates(DATA_PATH)
    total_features = 4

    for row in isolates:
        genus, score = identify(row)
        obs_summary = (f"colour={row['colour']}, texture={row['texture']}, "
                        f"growth={row['growth_rate']}, spore_structure={row['spore_structure']}")
        print(f"{row['isolate_id']}: {obs_summary}")
        print(f"  -> Best match: {genus} ({score}/{total_features} features matched)\n")


if __name__ == "__main__":
    main()
