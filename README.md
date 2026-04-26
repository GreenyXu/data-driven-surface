# Reconstructing Wonderland: A Data-Driven Spatial Narrative

## Overview

This project explores a data-driven workflow that transforms multimodal datasets into dynamic 3D visualisations and animations, using *Alice’s Adventures in Wonderland* as a conceptual framework.

Rather than directly illustrating the original narrative, the project reconstructs a data-driven interpretation of Wonderland, where characters, objects and environments emerge through transformation, fragmentation, and recomposition.

The workflow combines data collection, vectorisation, pretrained machine learning models, procedural modelling, real-time audiovisual interaction, and AI-assisted scene generation.

The final outcome is a >1 minute animation composed of three workflows:

1. **Workflow 1 – Blender 3D Fragments**  
2. **Workflow 2 – TouchDesigner Point Cloud Transformation**  
3. **Workflow 3 – AI-Generated Wonderland Scene**

---

## Data Sources

Three datasets were collected and processed from multiple sources:

- **Text dataset**  
  Literary text from *Alice’s Adventures in Wonderland* (public domain).  
  This dataset provides the conceptual and narrative foundation of the project.  
  The text was cleaned, segmented, and vectorised to extract thematic and semantic features used later for prompt generation and conceptual mapping.

- **Image dataset**  
  Visual references collected using APIs from platforms such as **Flickr** and **Pexels**.  
  The dataset focuses on surreal, dreamlike and Wonderland-like imagery.  
  These images were used for pretrained visual feature extraction, influencing texture selection, fragment generation, and overall visual style in the 3D workflows.

- **Audio dataset**  
  Environmental and abstract sound samples collected using the **Freesound API**.  
  The audio data was processed into basic descriptors and MFCC features, which were later mapped to real-time parameters in TouchDesigner to control point cloud vibration, transformation, and switching behaviours.

---

The datasets are organised as:

```
text
data/raw/
data/cleaned/
data/processed/
```
raw/ contains the original collected data
cleaned/ contains filtered and structured data
processed/ contains vectorised features and parameters used in later workflows

Each dataset contains approximately 200–300 elements, following the assignment requirements.

## Data-to-Design Pipeline

The project transforms data into visual and spatial outputs through the following pipeline:

Text → semantic features → prompt generation & narrative structure
Images → visual features → texture, form and style influence
Audio → feature vectors → real-time motion and transformation control

This multimodal mapping allows the datasets to actively shape the final 3D animation rather than simply being represented.

Each dataset contains approximately 200–300 elements, following the assignment requirement.

## Data Processing and Vectorisation

The datasets were transformed into machine-readable representations:

Text → TF-IDF vectors and pretrained sentence embeddings
Images → pretrained visual feature vectors
Audio → basic audio descriptors and MFCC features

The main processed files are stored in:
data/processed/

Vectorisation and comparison are documented in:
notebooks/PART1/03_vectorisation_and_comparison.ipynb

This notebook also includes Matplotlib and Seaborn visualisations saved to:
outputs/figures/

## Machine Learning and Pretrained Models

The project uses pretrained machine learning models to extract semantic and visual features from the datasets.

Pretrained models are used because they provide meaningful feature representations without requiring full model training from scratch. These extracted features are then mapped into design parameters for 3D generation and animation.

The workflow includes:

text embeddings for semantic analysis
image feature extraction for visual similarity and atmosphere
audio feature extraction using MFCCs and basic descriptors
parameter mapping for procedural 3D generation

## Workflow 1 — Blender 3D Fragments

Vectorised data and mapped parameters are used to generate abstract 3D fragments in Blender.

The data informs:

scale
spatial distribution
density
material / texture selection
fragment variation

Main file: blender/wf1_data_fragments.blend

## Workflow 2 — TouchDesigner Point Cloud Transformation

Nine Alice in Wonderland objects are generated as 3D meshes and converted into standardised point cloud CSV files.

The point clouds are then used in TouchDesigner to create:

point cloud reconstruction
fragmentation
vibration
audio-reactive switching
transformation between Alice-related objects

TouchDesigner project: touchdesigner/final_pointcloud/alice_pointcloud.toe
Relevant point cloud data: data/processed/alice_pointclouds/

Duplicate runtime assets are also stored inside the TouchDesigner folder to improve file stability and avoid path dependency issues.

## Workflow 3 — AI-Generated Wonderland Scene

The final scene uses AI-assisted prompt generation to compose the nine Alice-related elements into a cinematic Wonderland environment.

OpenAI API is used to generate structured prompts and narrative text. MidJourney is then used to produce the final visual scene.

Notebook: notebooks/PART2/08_final_animation_prompt_generation.ipynb

## Final Animation

The final animation combines all three workflows:

Blender data fragments appear
TouchDesigner point clouds break, vibrate and transform
The sequence resolves into an AI-generated Wonderland scene

Final output: outputs/animation/3D_animation_combined.mp4

## Project Structure
```data-driven-surface/
├── blender/
├── data/
│   ├── raw/
│   ├── cleaned/
│   └── processed/
├── notebooks/
│   ├── PART1/
│   └── PART2/
├── outputs/
├── touchdesigner/
├── scripts/
├── references/
├── README.md
└── requirements.txt
```

## Notes on File Size and Reproducibility

Some raw datasets are excluded from GitHub through .gitignore because of file size limitations. The full datasets, animation outputs, and design tool files are provided through the submitted OneDrive folder.

API keys are not included in the repository. They should be provided manually when running the relevant notebooks.

## Credits and Attribution

This project uses external datasets, pretrained models, OpenAI API, MidJourney, Tripo, Blender, TouchDesigner, Python libraries and FFmpeg as part of the workflow.

Generated and processed outputs are documented in the notebooks and final report.

## Conclusion

## Conclusion

This project explores how data can be used not only as input, but as a generative force in shaping visual and spatial narratives.

Using *Alice’s Adventures in Wonderland* as a conceptual framework, the project translates literary themes, visual references, and sound data into a series of interconnected workflows. Rather than directly representing the original story, the system reinterprets Wonderland through data-driven transformations, where characters, objects and environments emerge through transformation, fragmentation, and recomposition.

Across Blender, TouchDesigner and AI-generated imagery, data is continuously reinterpreted:
- text informs narrative structure and prompt generation  
- images influence visual style and spatial composition  
- audio drives motion, rhythm and transformation behaviour  

The final animation demonstrates a transition from abstract data fragments to a coherent Wonderland scene, revealing how meaning can emerge through multimodal data processing.

This approach positions data not as a static resource, but as an active agent in constructing dynamic, experiential spatial narratives.