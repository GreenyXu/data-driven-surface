# Data-Driven Surface

## Overview

This project explores a data-driven approach to generating spatial design parameters by integrating text, image, and audio datasets.

Instead of treating these media separately, the system maps features from each modality into a unified parameter space that can be used for generative design.

---

## Data Sources

* **Text**: Literary text (Alice in Wonderland), segmented into chunks
* **Image**: Visual dataset with extracted features (brightness, saturation, edge density)
* **Audio**: Audio dataset with extracted features (RMS, spectral centroid, duration)

---

## Pipeline

### 1. Text Processing

* Cleaning and chunking
* TF-IDF / embedding clustering
* API-based tagging:

  * scene_label
  * emotion
  * spatial_keywords
  * motion_keywords
  * intensity

### 2. Image Feature Mapping

* brightness → height
* edge density → complexity
* saturation → color intensity
* image cluster → fragment family

### 3. Audio Feature Mapping

* RMS → motion amplitude
* spectral centroid → temporal sharpness
* duration → duration factor
* audio cluster → motion family

---

## Unified Parameter Table

All modalities are combined into a single dataframe:

* Semantic parameters (text)
* Spatial parameters (image)
* Temporal parameters (audio)

Additional derived parameters:

* width
* depth
* roughness
* animation speed

---

## Output

The final outputs include:

* `text_api_tagged.csv`
* `parameter_table.csv`

These files can be used for:

* generative geometry (Blender / C4D)
* animation systems (TouchDesigner)
* spatial simulations

---

## Key Idea

The system constructs a **distributed control space**, where spatial, temporal, and semantic parameters are not strongly correlated but jointly shape the final outcome.

---

## Status

Current version: working prototype
Next step: integration with generative design tools
