# Reconstructing Wonderland

A data-driven spatial narrative project based on *Alice's Adventures in Wonderland*. The project collects, cleans, vectorises, compares and maps multimodal datasets into procedural 3D fragments, TouchDesigner point-cloud animation and AI-assisted final scene generation.

## Project Aim

The project does not simply illustrate the original story. It reconstructs Wonderland as a design system shaped by data: text contributes semantic and emotional structure, images contribute visual atmosphere and texture, and audio contributes rhythm, intensity and motion behaviour.

The final outcome is a short animation built from three connected workflows:

1. **Workflow 1: Blender data fragments** generated from mapped parameters.
2. **Workflow 2: TouchDesigner point-cloud transformation** using Alice-related objects and audio-driven motion.
3. **Workflow 3: AI-generated Wonderland scene** produced through structured prompt generation.

## Main Notebooks

The final Part 1 pipeline is documented in:

- `notebooks/PART1/01_data_collection_enhanced.ipynb`
- `notebooks/PART1/02_data_processing.ipynb`
- `notebooks/PART1/03_vectorisation_and_comparison_enhanced_final.ipynb`
- `notebooks/PART1/04_parameter_mapping.ipynb`

These notebooks cover data collection, cleaning, vectorisation, model comparison, cluster interpretation and parameter mapping.

## Data Overview

The project uses three main datasets:

- **Text:** cleaned and segmented chapters from *Alice's Adventures in Wonderland*.
- **Images:** curated Wonderland-related visual references for colour, texture and atmosphere.
- **Audio:** environmental and abstract sound samples used for motion and transformation parameters.

Processed datasets are stored under `data/cleaned/` and `data/processed/`. Raw media folders are excluded from GitHub because of file size.

## Key Outputs

- Final report: `final_report/Reconstructing_Wonderland_Case_Level_Report.docx`
- Report-generation script: `scripts/build_case_level_word_report.py`
- Corrected chapter figure script: `scripts/regenerate_text_chapter_figures.py`
- Part 1 figures: `outputs/figures/part1_data_collection/`, `outputs/figures/part1_data_processing/`, `outputs/figures/part1_vectorisation/`
- Mapping tables: `data/processed/parameters/`
- Final animation: `outputs/animation/3D_animation_combined.mp4`

## Reproducibility Notes

API keys are not included in the repository. The OpenAI placeholder cell in `04_parameter_mapping.ipynb` is intentionally left unexecuted.

Large raw datasets, design-package drafts, render QA folders and temporary report figures are ignored by `.gitignore`. The checked-in CSVs and final figures are the lightweight evidence needed to understand and review the workflow.

## Project Structure

```text
reconstructing-wonderland/
|-- blender/
|-- data/
|   |-- cleaned/
|   |-- processed/
|   `-- raw/              # heavyweight raw media ignored
|-- final_report/
|-- notebooks/
|   |-- PART1/
|   `-- PART2/
|-- outputs/
|   |-- animation/
|   |-- figures/
|   `-- tables/
|-- references/
|-- scripts/
|-- touchdesigner/
|-- README.md
`-- requirements.txt
```

## Tools

The workflow uses Python, Jupyter, pandas, scikit-learn, matplotlib, seaborn, Pillow, python-docx, Blender, TouchDesigner, FFmpeg/ImageIO and external APIs for data collection and prompt generation.
