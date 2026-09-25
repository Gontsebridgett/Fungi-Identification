# Fungi Identification — Morphology-Based Key

A protocol for identifying common fungal genera from culture plate
observations, paired with a Python script that applies a simple decision-key
(colony colour, growth rate, texture, and microscopic spore-bearing structure)
to suggest a likely genus from recorded morphological characteristics.

## Overview

Preliminary fungal identification in a teaching or diagnostic microbiology lab
is typically based on macroscopic colony morphology (colour, texture, growth
rate, reverse-side pigmentation) combined with microscopic examination
(lactophenol cotton blue mount) of spore-bearing structures. This project
encodes a simplified identification key for several common genera
(*Aspergillus*, *Penicillium*, *Rhizopus*, *Candida*, *Trichophyton*) based on
these combined features — the kind of key used as a starting point before
confirmatory testing (e.g. molecular ID) in a real diagnostic setting.

## Principle

- **Colony morphology** — colour, texture (velvety, cottony, powdery), growth rate
- **Reverse pigmentation** — colour seen from the underside of the plate
- **Microscopic morphology** — hyphae type (septate vs. non-septate), spore
  structure (conidiophore shape, sporangia, budding yeast cells)
- Combining these features narrows identification to genus level; species-level
  and clinical identification requires further biochemical or molecular testing

## Materials

- Sabouraud Dextrose Agar (SDA) plates ± antibiotics
- Inoculating needle/loop
- Lactophenol cotton blue stain, microscope slides and coverslips
- Compound microscope (10×, 40× objectives)
- Incubator (25–30°C for moulds; 35–37°C for yeasts)

## Method (Summary)

| Step | Action |
|---|---|
| 1 | Inoculate SDA plate from sample; incubate at appropriate temperature |
| 2 | Observe colony daily for growth rate, colour, and texture (up to 7 days) |
| 3 | Record reverse-side pigmentation |
| 4 | Prepare a lactophenol cotton blue tease mount or tape-touch prep |
| 5 | Examine microscopically for hyphae type and spore-bearing structures |
| 6 | Apply identification key to combined macroscopic + microscopic features |

## Example Identification Key (Simplified)

| Genus | Colony colour | Texture | Growth rate | Key microscopic feature |
|---|---|---|---|---|
| *Aspergillus* | Green/black/yellow | Powdery | Fast (2–3 days) | Conidiophore with radiating conidial head |
| *Penicillium* | Blue-green | Velvety | Moderate (3–5 days) | Brush-like (penicillus) conidiophore |
| *Rhizopus* | White → grey-black | Cottony, fast-spreading | Very fast (1–2 days) | Non-septate hyphae, sporangia on sporangiophores |
| *Candida* | Cream/white | Smooth, yeast-like | Fast (1–2 days) | Budding yeast cells, pseudohyphae |
| *Trichophyton* | White/cream | Cottony/powdery | Slow (7–14 days) | Septate hyphae, microconidia along hyphae |

## Analysis Script

`fungi_identifier.py` takes recorded colony and microscopic observations
(from `sample_data/isolate_observations.csv`) and scores each isolate against
the identification key, returning the best-matching genus and a confidence
score based on how many key features matched.

### Usage

```bash
pip install -r requirements.txt
python fungi_identifier.py
```

### Sample output

```
Isolate_1: colour=green, texture=powdery, growth=fast, spore_structure=radiating_head
  -> Best match: Aspergillus (4/4 features matched)

Isolate_2: colour=white, texture=cottony, growth=very_fast, spore_structure=sporangia
  -> Best match: Rhizopus (4/4 features matched)

Isolate_3: colour=cream, texture=smooth, growth=fast, spore_structure=budding_yeast
  -> Best match: Candida (4/4 features matched)
```

## Repository Structure

```
fungi-identification/
├── README.md
├── fungi_identifier.py
├── requirements.txt
└── sample_data/
    └── isolate_observations.csv
```

## Disclaimer

This is a simplified educational key for common genera and is not a
substitute for clinical mycology diagnosis, which requires trained
expertise and, where relevant, molecular confirmation (e.g. ITS sequencing).
