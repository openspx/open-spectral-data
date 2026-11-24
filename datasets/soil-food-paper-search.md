# Further soil and food datasets

Research date: **23 November 2026**. This expands the preparation catalogue by **ten records: five soil and five food**. Eight have an explicit accompanying journal-paper link. CSIC is a project deposit; UWA is an institutional deposit with related doctoral research, without a verified accompanying journal article. These distinctions matter when reporting “paper-accompanied datasets”.

The catalogue now contains **66 records**, including **26 soil and eight food records**, across the same 16 fields. Counts describe catalogue resources, not independent sample collections. The original week-one 38-resource audit remains a separate historical scope.

## What was searched

Soil: moisture, fertility, carbon, field measurements and instrument comparisons. Food: fruit composition, dairy composition, adulteration, botanical authenticity and grain processing. Searches followed original papers to Zenodo, Mendeley Data, institutional repositories and author code deposits; existing catalogue entries and reused collections were checked before adding records. Coverage is targeted, not exhaustive.

Near-infrared spectroscopy measures light beyond visible red. Fourier-transform infrared spectroscopy (FTIR) measures an infrared fingerprint. A numerical target is a property attached to a spectrum; a recipe percentage is different from an independent laboratory assay.

## Soil additions

| New record / data | Accompanying paper | Numerical data and references | Evidence and selection issue |
|---|---|---|---|
| [Agroscope 2024](../../datasets/soil-science/agroscope-ssl-2024.md) · [deposit](https://zenodo.org/records/11204174) | [Nitrogen, active carbon and carbon-to-clay prediction](https://doi.org/10.1111/ejss.13508) | Reported 134 soils; two instruments and multiple scanning setups; separate laboratory CSV and spectral files. | Documentation reviewed. Laboratory units/joins need inspection. CC BY-NC-SA 4.0; overlaps LimeSoDa CV.98. |
| [CSIC ProbeField](../../datasets/soil-science/csic-probefield.md) · [deposit](https://zenodo.org/records/13744546) | No specific journal article established. | 2.8 MB workbook; 350–2500 nm spectra with carbon, nitrogen, moisture, pH and nutrient references. | Documentation reviewed; count unknown. Non-commercial/share-alike terms. Stored signal and sheet joins unverified. |
| [KarLy](../../datasets/soil-science/karly-soil-moisture.md) · [author data](https://github.com/felixriese/hyperspectral-soilmoisture-dataset) | [IGARSS 2018 paper](https://doi.org/10.1109/IGARSS.2018.8517812) | **Observed 679 rows × 125 bands**, 454–950 nm; measured moisture (%) and temperature (°C). | Selected CSV checked. **One soil specimen**, repeatedly observed. CC BY 4.0. |
| [Seven-LED moisture](../../datasets/soil-science/soil-seven-led-moisture.md) · [deposit](https://zenodo.org/records/21457181) | [2026 instrument paper](https://doi.org/10.1016/j.compag.2026.111948) | 92.5 kB CSV; seven channels, 970–1900 nm; gravimetric moisture (%), measured by drying/weighing. | Documentation reviewed. Attractive small candidate; download returned 403 here. Count and pairing remain unchecked. CC BY 4.0. |
| [Thailand homemade NIR](../../datasets/soil-science/thailand-homemade-soil-nir.md) · [deposit](https://data.mendeley.com/datasets/yt78nwnhbd/1) | [2025 data paper](https://doi.org/10.1016/j.dib.2025.111840) | Reported 190 topsoils; 900–1700 nm absorbance; named workbook combines spectra and chemical references for organic matter/total carbon. | Documentation reviewed; assay details, units and file joins unverified. CC BY 4.0. |

## Food additions

| New record / data | Accompanying paper | Numerical data and references | Evidence and selection issue |
|---|---|---|---|
| [Australian mango](../../datasets/food-feed-quality/mango-dry-matter-anderson.md) · [deposit v5](https://data.mendeley.com/datasets/46htwnp833/5) | [2020 robustness study](https://doi.org/10.1016/j.postharvbio.2020.111202) | Absorbance with dry-matter references; v5 retains the named v3 CSV and describes additional seasons/instruments. | Documentation reviewed. Select one file before counting; metadata has range/version typos. Original series: 309–1149 nm. CC BY 4.0. |
| [Coconut milk](../../datasets/food-feed-quality/coconut-milk-water-ftir.md) · [deposit](https://data.mendeley.com/datasets/byww6nrp2z/1) | [2021 data paper and supplement](https://doi.org/10.1016/j.dib.2021.107058) | **Observed 42 rows × 729 bands**, with added water at 0/10/20% and product-type labels. | Journal workbook checked. Water values are **formulation-based**. Paper says 43 samples; file has 42 plus header. CC BY 4.0. |
| [Milk composition](../../datasets/food-feed-quality/milk-composition-transmittance-nir.md) · [deposit](https://zenodo.org/records/8263430) | [2023 data paper](https://doi.org/10.1016/j.dib.2023.109767) | Reported 1,224 milk samples, 256 bands, 960–1690 nm; fat, protein, lactose, urea and somatic cell references in an 11.3 MB CSV. | Documentation reviewed. Exact reference methods/units require confirmation; repeated animals/time periods matter. CC BY 4.0. |
| [Honey botanical origin](../../datasets/food-feed-quality/honey-botanical-gc-ims.md) · [deposit](https://data.mendeley.com/datasets/jxj2r45t2x/1) | [2024 data paper](https://doi.org/10.1016/j.dib.2024.110532) | Numerical gas chromatography–ion mobility measurements (.mea); acacia/canola/honeydew labels, with pollen-based authenticity checks. | **Classification**, not numerical composition targets. Counts conflict in the paper; binary reader and label joins require checks. CC BY 4.0. |
| [UWA wheat sprouting](../../datasets/food-feed-quality/uwa-wheat-sprouting-ftir.md) · [deposit](https://doi.org/10.26182/w4ym-ta25) | [Related doctoral thesis](https://doi.org/10.26182/k8nr-sn89); exact journal link not established. | 14.1 MB workbook; controlled incubation durations and sprouted-grain percentages for Australian wheat. | Documentation reviewed. Treatment/formulation labels, **not independent quality assays**. CC BY-SA; version and workbook details unverified. |

## What the investigation established

- **An independent check changes the coconut count.** The journal supplement contains 42 spectra, each with a formulation label. Its 43 spreadsheet rows include the header. The two extra sheets contain predictions, not extra measurements. Wavelength headers run approximately 2501–4000; the provider labels them nm. Instrument interpretation still needs confirmation.
- **KarLy is suitable for studying moisture changes in one specimen.** It does not establish performance across soil types. The downloaded dates span 16–26 May 2017, which needs reconciling with the author's five-day campaign description.
- **Aggregates can hide overlap and different licences.** [LimeSoDa CV.98](https://limesoda.readthedocs.io/en/latest/datasets/CV_98.html) reuses 98 Agroscope soils. Its stated CC BY-SA terms do not establish permission to redistribute the original Agroscope release under those terms.
- **Australian relevance is now concrete.** Mango adds an Australian fruit-composition study; UWA adds Australian grain-processing experiments. Their targets have different meanings and should stay separate.

## Other leads investigated, not added

| Lead | Why it remains outside the new records |
|---|---|
| [Western Highveld soil](https://doi.org/10.5281/zenodo.17510653) · [data paper](https://doi.org/10.1016/j.dib.2026.113160) | Primary DOI metadata says **803** samples; paper says **790**. File download returned 403. Resolve release and matching reference table before admission. |
| [Beef patties with plant protein](https://zenodo.org/records/21639596) · [paper](https://doi.org/10.1016/j.foodcont.2025.111793) | Reported 240 patties; 8.1 GB ZIP. Five point-spectrometer replicates per patty. Recipe labels are documented, but the usable file-level pairing has not been established here; no giant download performed. |
| [Olive-oil FTIR/Raman](https://zenodo.org/records/14651816) | Explicit 2017 paper relationship and 37.7 MB RAR containing CSV spectra, but a ready independently usable target table was not established. |
| [Commercial-honey NMR](https://zenodo.org/records/11341174) | Raw and processed spectra exist, but a sufficiently defined target/label table and accompanying-paper link were not established. |
| [Other UWA flour data](https://doi.org/10.26182/pv21-ar16) | Potential overlap with related UWA experiments; target mapping not established. Non-commercial/no-derivatives terms also differ from the sprouting deposit. |
| [Surface-orientation soil data](https://doi.org/10.6086/D15091) | 2.16 GB total, with large RData files. A practical spectral/reference subset and its joins were not established. |

Previously catalogued Corn, Tecator, Sugar, OSSL, LUCAS, NeoSpectra/KSSL and tropical-soil measurements were not added again. Derivatives, versions and repeated spectra are not independent samples. Unresolved numerical target mappings remain outside the admitted shortlist.

## Recommendation and remaining work

Start **soil moisture exploration with KarLy**, because the complete selected CSV has clear same-row pairings and manageable size. For broader soil chemistry, prioritise the Agroscope laboratory/spectral join or Thailand workbook once accessible. Start **food adulteration exploration with the coconut supplement**; its recipe labels are directly visible. For independently obtained food-composition references, **Australian mango and Belgian milk** are stronger discovery leads, pending method/unit and file checks.

Only **two new numerical artifacts** were inspected: the complete selected KarLy CSV and the complete selected coconut journal workbook (basic checks on its raw sheet; structure checks on prediction sheets). Neither has missing raw-table cells or exact duplicate spectra/rows. These checks do not establish scientific accuracy, sample independence or all-file validity. Eight additions are documentation-only. Several direct public downloads returned 403 and Mendeley file-list requests returned 404 in this environment; those are retrieval failures here, not proof the data are unavailable.

Before cleaning: obtain remaining selected files through permitted provider routes, check licences, confirm specimen IDs and joins, resolve units/reference methods, and retain repeat-measurement groups. Detailed retrieval logs, SHA-256 hashes, source snapshots and inspection results are retained separately in the workspace; original raw data and the Git checkout were not modified.

Local research archive: moved here on 24 November 2026 under AGENTS.md. Historical counts and findings describe the earlier catalogue scope; this file is not a current catalogue index.
