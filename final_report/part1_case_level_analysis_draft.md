# Part 1 Case-Level Analysis Draft

Project: **Reconstructing Wonderland: A Data-Driven Spatial Narrative**

Purpose of this file: provide a stronger content base for the report before returning to a normal Word-style layout. The writing below is designed to be report-ready in English, but the notes also explain why each section matters.

---

## 1. Content Diagnosis

The current project has enough technical evidence for a strong Part 1. The weak point is not the amount of material, but the way the material is interpreted. A case-level report should not only state that datasets were collected, cleaned and vectorised. It should explain how the data describes **Alice's Adventures in Wonderland** as a design world: falling, scale-shifting, doors, rabbits, time anxiety, tea-party repetition, court authority, dream logic and unstable identity.

The strongest Part 1 argument should be:

> The project uses multimodal data to reconstruct Wonderland as a spatial and temporal system. Text captures narrative meaning and symbolic motifs. Images capture visual atmosphere and material qualities. Audio captures motion, rhythm and instability. Model comparison is used not as a generic machine-learning exercise, but as a way to decide which features can be trusted for design translation.

Key evidence already available:

| Evidence | Current result | Report meaning |
|---|---:|---|
| Cleaned text records | 288 | Enough narrative fragments to represent Wonderland motifs across chapters |
| Cleaned image records | 298 in cleaning summary; 278 in vectorisation summary | Need to explain filtering difference if using the 278 vectorised image count |
| Cleaned audio records | 270 | Enough sound segments to support temporal and behavioural mapping |
| TF-IDF dimensions | 300 | Interpretable keyword/motif layer |
| MiniLM dimensions | 384 | Semantic narrative similarity layer |
| Image feature dimensions | 35 | Visual atmosphere, colour and composition layer |
| Basic audio dimensions | 11 | Direct motion-control descriptors |
| MFCC dimensions | 26 | Timbral texture layer |
| Text silhouette, TF-IDF | -0.008620 | Keyword clusters are weak for dreamlike narrative ambiguity |
| Text silhouette, MiniLM | 0.038866 | Semantic embeddings improve narrative grouping but still show overlap |
| Image silhouette | 0.170996 | Visual descriptors form clearer groups than text |
| Audio silhouette, basic | 0.199004 | Broad audio descriptors are most coherent for motion mapping |
| Audio silhouette, MFCC | 0.107957 | Timbre features are useful but less directly separable |

---

## 2. Recommended Normal Word Structure

Use a normal Word report layout rather than two columns:

- A4 portrait
- Margins: 2.0 cm left/right, 2.0 cm top/bottom
- Body font: Arial / Aptos / Calibri, 10.5-11 pt
- Line spacing: 1.05 or 1.1
- Figure captions: 8.5-9 pt italic
- Headings: 14-16 pt bold italic for chapter headings, 12 pt bold italic for section headings
- Figures: full-width when detailed, half-width only for small plots or tables

Suggested report pagination:

1. Cover / Abstract / Workflow overview
2. Part 1. Dataset construction and Wonderland theme logic
3. Data cleaning and quality control
4. Text vectorisation and Wonderland motif retrieval
5. Image and audio vectorisation comparison
6. Model comparison and design interpretation
7. Parameter mapping from Part 1 to design workflows
8. Blender workflow
9. TouchDesigner workflow
10. Final animation and critical reflection
11. Appendix / links / credits

Part 1 should occupy about 4-5 pages because this is where the technical credibility of the whole report is established.

---

# Report-Ready Part 1 Draft

## Part 1. Multimodal Data Construction and Analysis

### 1.1 Aim of the Data Workflow

The first part of the project establishes the data foundation for **Reconstructing Wonderland**, a data-driven spatial narrative based on *Alice's Adventures in Wonderland*. The aim is not to illustrate the story literally, but to convert its narrative, visual and temporal qualities into a design system. Wonderland is defined by repeated transformations: Alice falls through the rabbit hole, changes scale, moves through locked doors, encounters unstable rules, and enters scenes where time, authority and identity behave strangely. These motifs make the story suitable for a multimodal workflow because they can be represented through semantic, visual and motion-related data.

The project therefore uses three complementary datasets. The text dataset captures narrative motifs and emotional logic. The image dataset captures visual atmosphere, colour, composition and texture. The audio dataset captures rhythm, intensity and temporal instability. Together, these datasets allow the design process to move from narrative evidence to spatial fragments and animation parameters. This is important because the final output should not appear as a purely manual fantasy scene; it should be traceable to analysed data.

### 1.2 Dataset Construction

Three cleaned datasets were prepared for Part 1. The text dataset contains **288 cleaned narrative records**. The image dataset contains **298 cleaned image records** in the data-processing summary, with **278 records used in the vectorisation stage** after feature-level filtering. The audio dataset contains **270 cleaned audio records**, with one raw audio sample removed during validation. These dataset sizes satisfy the assignment requirement while remaining small enough for transparent inspection inside the notebooks.

The text dataset is the semantic core of the project. It contains fragments from the Wonderland narrative and preserves chapter-level context where possible. This is essential because the design process depends on symbolic and emotional relationships rather than isolated words alone. For example, motifs such as the rabbit hole, locked doors, the Queen, the Mad Tea-Party, time and dreaming are not just keywords; they define different spatial states. The rabbit hole suggests descent and transition. Doors suggest threshold and access. The Mad Tea-Party suggests circular repetition and broken time. The Queen of Hearts suggests authority, threat and unstable rules. These motifs later inform scene labels, emotional categories and fragment families.

The image dataset supports the visual world-building layer. Rather than treating images as reference pictures to copy, the workflow extracts measurable visual properties such as colour, size, aspect ratio and other handcrafted descriptors. These properties can be connected to material roughness, colour intensity, texture selection and atmosphere. This is especially relevant to Wonderland because the world is visually unstable: objects and spaces are recognisable but distorted, familiar but illogical.

The audio dataset supports the temporal layer. Wonderland is not only a visual world; it is full of urgency, interruption, rhythm and sudden shifts. Audio descriptors therefore become useful for animated behaviour. Basic audio features and MFCCs are compared to decide whether broad temporal descriptors or timbral features are more suitable for controlling motion amplitude, animation speed and temporal sharpness.

**Recommended figures for this section:**

- Dataset size overview chart
- Cleaned text table screenshot
- Cleaned image sample grid
- Cleaned audio duration or feature plot

### 1.3 Cleaning and Quality Control

The cleaning process is important because the project uses data as a design input. If an error remains in the dataset, it can become a visible error in the final animation. For example, a broken image path can produce a missing texture in Blender, an empty text fragment can weaken semantic clustering, and an invalid audio duration can distort motion parameters.

The text cleaning stage retained **288 valid text segments** after whitespace normalisation, word-count validation and short-fragment checks. The image cleaning stage retained **298 valid image records** after file existence, image validity, resolution and aspect-ratio validation. The audio cleaning stage retained **270 valid samples** after file existence and duration-based validation. This gives the project a stable foundation for vectorisation.

The retention rates also reveal different levels of dataset stability. Text and image records had a retention rate of **100%** in the cleaning summary, while audio retained **99.63%** of raw samples. This suggests that the raw text and image data were already structurally consistent, while the audio dataset required slightly more filtering. In the report, this should be framed as a quality-control step rather than a failure. It shows that the workflow checks whether data is usable before using it for design.

The cleaned datasets also preserve traceability. Each design parameter should be traceable backwards: from a generated fragment to a row in `parameter_table.csv`, from that row to cleaned features, and from the cleaned features back to a source record. This traceability is one of the main differences between a data-driven design workflow and a manually assembled visual collage.

**Recommended figures for this section:**

- `02_cleaned_dataset_summary.csv`
- `02_quality_check_summary.csv`
- Raw vs cleaned dataset count chart
- Screenshot from `02_data_processing.ipynb` showing validation results

### 1.4 Text Vectorisation: Keywords vs Semantic Meaning

The text dataset was vectorised using two methods: **TF-IDF** and **all-MiniLM-L6-v2 sentence embeddings**. TF-IDF generated a **300-dimensional** representation based on keyword importance. This method is useful because it is interpretable: the report can show which words and motifs dominate the dataset. The top TF-IDF terms include *alice*, *queen*, *time*, *king*, *gryphon*, *turtle*, *hatter*, *rabbit*, *head*, *duchess*, *mouse*, *dormouse*, *cat*, *door*, *caterpillar* and *white*. These terms clearly belong to the Wonderland world and support the thematic direction of the project.

However, TF-IDF is limited because it treats similarity mainly through shared vocabulary. This becomes a problem for Wonderland because many important themes are expressed indirectly. A passage about dream logic may not repeatedly use the word "dream"; a scene about time may involve the Hatter, tea-things and repetition rather than only the keyword "time". Therefore, TF-IDF is useful for identifying explicit motifs, but weaker for capturing the story's deeper semantic structure.

The sentence embedding model all-MiniLM-L6-v2 generated a **384-dimensional** semantic representation. This method is less transparent than TF-IDF, but it is better suited to narrative similarity because it can relate fragments that express similar ideas through different words. In the current comparison, MiniLM produced a higher silhouette score than TF-IDF: **0.038866** compared with **-0.008620**. Both scores are low, but the difference is meaningful. It suggests that Wonderland's narrative fragments do not form clean, separate categories, yet semantic embeddings provide a slightly more coherent structure than keywords alone.

The retrieval results show this difference clearly. For the query **"mad tea party"**, TF-IDF incorrectly ranks a generic passage containing "party" from *The Pool of Tears* as the top result. In contrast, MiniLM retrieves the actual *A Mad Tea-Party* chapter as its top result, including passages about tea-time and the Hatter. This shows that semantic embeddings are better at capturing the scene-level meaning of Wonderland motifs. Another strong example is the query **"dream"**. TF-IDF returns zero-score results because the exact keyword is not distributed in a useful way, while MiniLM retrieves the final chapter where Alice wakes and describes her "curious dream". This is a strong argument for using semantic embeddings in a project about dream logic.

At the same time, TF-IDF should not be discarded. It remains valuable as an explanatory layer. Its top terms provide a readable motif map of Wonderland: Alice, Queen, Rabbit, Hatter, Door, Time, Caterpillar and Cat. A strong report should therefore present TF-IDF and MiniLM as complementary rather than simply declaring one "better". TF-IDF explains visible keywords; MiniLM supports semantic scene retrieval.

**Recommended figures for this section:**

- Top TF-IDF terms bar chart
- Text vectorisation comparison figure
- Text clustering comparison table
- Retrieval comparison table for `rabbit hole`, `mad tea party`, `queen of hearts`, `dream`, `door`, `time`, `mushroom`

### 1.5 PCA and Clustering Interpretation for Text

The PCA comparison also supports the interpretation above. For TF-IDF, PC1 explains **1.84%** of variance and PC2 explains **1.75%**. For MiniLM, PC1 explains **5.49%** and PC2 explains **4.61%**. The MiniLM components therefore capture more structure in the first two dimensions, although the values are still modest. This is expected for a literary dataset: Wonderland scenes overlap in mood, characters and motifs rather than forming rigid categories.

The low text silhouette scores should not be hidden. They are analytically useful because they reveal a property of the source material. *Alice's Adventures in Wonderland* is a story of ambiguity, repetition and unstable identity. Scenes often share characters and emotional tones. The rabbit appears in multiple chapters; doors recur as thresholds; authority and nonsense overlap in the Queen's court; dream logic frames the whole narrative. Therefore, weak cluster separation is not only a technical limitation. It also reflects the story's structure.

For design translation, this means the text model should not be used to create hard boundaries between scenes. Instead, it should support soft semantic mapping: emotional labels, scene tendencies and motif retrieval. This justifies the later use of categories such as `curious`, `dreamlike`, `anxious` and `chaotic`, rather than treating clusters as fixed architectural zones.

### 1.6 Image Vectorisation: Visual Atmosphere and Material Logic

The image dataset was vectorised using **35 handcrafted colour and size features**. The clustering silhouette score for image features is **0.170996**, which is stronger than the text scores. This suggests that visual descriptors form clearer groupings than narrative fragments. That result is useful for design because image features can be mapped more directly into visible outputs.

In the context of Wonderland, image features should be interpreted as atmosphere rather than literal representation. Colour intensity can influence material colour or lighting mood. Aspect ratio and size descriptors can suggest surface treatment, scaling or visual density. Feature correlation plots can reveal whether visual properties move together, for example whether brighter images also have lower contrast or whether certain image groups share similar proportions.

The limitation is that handcrafted features do not understand semantic content. They can describe colour and composition, but they cannot automatically recognise a rabbit, door, teacup, mushroom or playing card unless those features are separately labelled. This should be acknowledged in the report. It does not weaken the project if explained properly. The image model is useful for material and atmosphere, while the text model remains responsible for symbolic meaning.

This distinction is important for the final design workflow. If an object needs to represent the Queen of Hearts, text retrieval and semantic labels are more reliable. If a material needs to feel dark, bright, unstable or soft, image descriptors are more appropriate. This division of labour makes the multimodal workflow more convincing.

**Recommended figures for this section:**

- Image handcrafted feature cluster plot
- Image feature correlation heatmap
- Image feature distribution plot
- Cleaned image sample grid

### 1.7 Audio Vectorisation: Motion, Rhythm and Instability

The audio dataset was represented through **11 basic audio descriptors** and **26 MFCC features**. The basic descriptors achieved a silhouette score of **0.199004**, while MFCC features achieved **0.107957**. This means the basic audio features produced more coherent clusters for this dataset.

This result is important because it directly affects design mapping. Basic audio descriptors are easier to connect to motion: duration, intensity and broad spectral properties can become animation speed, motion amplitude and temporal sharpness. MFCCs may describe timbre more richly, but they are less immediately legible as design controls. Therefore, the report should argue that basic descriptors are preferred for motion parameters, while MFCCs remain useful as a secondary sound-texture analysis.

The PCA variance comparison supports this decision. Basic audio descriptors have PC1 variance of **39.99%** and PC2 variance of **28.26%**, while MFCC features have PC1 variance of **30.80%** and PC2 variance of **16.98%**. The first two components of the basic descriptor model therefore capture a larger share of structure. This makes them more suitable for visual explanation and mapping to TouchDesigner motion behaviour.

Within the Alice/Wonderland theme, audio should be framed as instability and rhythm. Wonderland is full of abrupt movement, urgency and repeated nonsense rhythms: the White Rabbit's lateness, the Mad Tea-Party's broken time, the Queen's commands, and Alice's sudden changes in scale. Audio descriptors become a way to translate this narrative instability into movement. In the later parameter table, values such as `motion_amp`, `temporal_sharpness` and `anim_speed` can be explained as the motion layer derived from this analysis.

**Recommended figures for this section:**

- Audio basic feature cluster plot
- Audio MFCC cluster plot
- Audio PCA explained variance chart
- Audio vectorisation comparison table

### 1.8 Cross-Modal Comparison and Design Decision

The model comparison shows that each modality has a different role. Text is semantically rich but difficult to cluster cleanly. Images cluster more clearly through visual descriptors and are useful for atmosphere and material. Audio descriptors produce the strongest clustering result and are most useful for motion mapping.

The final design decision should therefore be:

1. Use **TF-IDF** for readable Wonderland motif extraction.
2. Use **MiniLM sentence embeddings** for semantic scene retrieval and narrative similarity.
3. Use **handcrafted image features** for visual atmosphere, material and texture decisions.
4. Use **basic audio descriptors** as the main source for motion amplitude, speed and temporal behaviour.
5. Use **MFCC features** as a secondary descriptor for sound texture, not as the primary motion-control model.

This is a stronger conclusion than simply reporting silhouette scores. It explains how the models are used differently in the design workflow. The project does not need one model to "win" across all modalities. Instead, it uses the most useful representation for each design task.

### 1.9 From Part 1 to Parameter Mapping

The output of Part 1 becomes meaningful because it is converted into a parameter table. The current `parameter_table.csv` contains fields such as `fragment_id`, `text_id`, `scene_label`, `emotion`, `scene_order_param`, `narrative_family`, `motion_intensity`, `image_id`, `height`, `complexity`, `color_intensity`, `fragment_family`, `audio_id`, `motion_amp`, `temporal_sharpness`, `duration_factor`, `motion_family`, `width`, `depth`, `roughness` and `anim_speed`.

This table should be described as the design interface of the project. It is the point where Wonderland's narrative and multimodal data become spatial instructions. For example:

- `scene_label` connects text fragments to Wonderland scenes such as rabbit-hole, dream-fall or other narrative states.
- `emotion` translates semantic interpretation into material colour or atmosphere.
- `height`, `width` and `depth` turn image/text-derived variation into spatial scale.
- `complexity` and `roughness` connect visual features to geometry and material behaviour.
- `motion_amp`, `temporal_sharpness` and `anim_speed` translate audio analysis into animation behaviour.
- `scene_order_param` gives the design a temporal or narrative sequence instead of random placement.

This section is essential because it proves that Part 1 is not separate from Part 2. The data analysis directly prepares the Blender and TouchDesigner workflows. A strong report should show a short excerpt of the parameter table and then explain exactly which columns are read by the design scripts.

**Recommended figures for this section:**

- `parameter_table.csv` screenshot
- Data-to-fragment mapping diagram
- Parameter distribution grid
- Parameter correlation heatmap
- Blender script workflow diagram

---

## 3. Suggested Figure Order for Part 1

1. Dataset size overview chart
2. Cleaned data summary table
3. Text top TF-IDF terms
4. Text retrieval comparison table
5. Text clustering comparison plot/table
6. Image feature distribution or sample grid
7. Image feature correlation heatmap
8. Audio descriptor vs MFCC comparison
9. Feature dimension summary table
10. Data-to-design mapping summary
11. Parameter table excerpt
12. Parameter distribution / correlation chart

---

## 4. Key Sentences Worth Keeping

Use these as anchor sentences in the final Word report:

- The project treats Wonderland as a system of transformations rather than a set of illustrations.
- TF-IDF is useful for explicit motifs, while MiniLM is more useful for dreamlike semantic relationships.
- Low text cluster separation is not only a technical weakness; it reflects the narrative ambiguity of *Alice's Adventures in Wonderland*.
- Image features are used for atmosphere and material, not for symbolic recognition.
- Basic audio descriptors are preferred for motion mapping because they are more coherent and more directly interpretable than MFCC features in this dataset.
- The parameter table is the bridge between analysis and production.
- The final design workflow is multimodal: text controls meaning, image controls appearance, and audio controls behaviour.

