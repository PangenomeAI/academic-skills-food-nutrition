# Agriculture journal coverage map (Q1 + Q2)

The **Q1 and Q2** journals of the seven JCR agriculture categories — Agronomy,
Agriculture Multidisciplinary, Agriculture Dairy & Animal Science, Soil Science,
Agricultural Economics & Policy, Horticulture, and Agricultural Engineering —
mapped to publisher-format skill folders. Source: JCR 2025 (retrieved 2026-07).
Verified by `scripts/check_journal_coverage.py`.

**230 journals** (109 Q1, 121 Q2), deduplicated across categories
(a journal listed in several categories appears once, at its best quartile). Q3 is
used only to fill gaps and **Q4 is avoided** — see `agri-research`.

**No duplicate formats:** these reuse the existing publisher-tier folders wherever
the format matches (an Elsevier agronomy journal follows the same Guide for Authors
as an Elsevier food journal). Journals already mapped in the food, nutrition, or
multidisciplinary lists **keep their existing folder** (e.g. Journal of Dairy
Science → `j-dairy-science`, Food Policy → `elsevier-food`). Only society and
regional publishers with no shared format fall to `agri-other`.

| # | Journal | JCR abbrev | Publisher | Category | Quartile (JIF) | Skill folder |
|---|---|---|---|---|---|---|
| 1 | Artificial Intelligence in Agriculture | ARTIF INTELL AGR | KEAI PUBLISHING LTD | Agri-Multidisciplinary | Q1 (16.1) | j-future-foods |
| 2 | Biochar | BIOCHAR | SPRINGER SINGAPORE PTE LTD | Soil Science | Q1 (15.1) | springer-food |
| 3 | Annual Review of Animal Biosciences | ANNU REV ANIM BIOSCI | ANNUAL REVIEWS | Dairy & Animal Science | Q1 (12.3) | annu-rev-food |
| 4 | SOIL BIOLOGY & BIOCHEMISTRY | SOIL BIOL BIOCHEM | PERGAMON-ELSEVIER SCIENCE LTD | Soil Science | Q1 (12.2) | elsevier-food |
| 5 | Agriculture Communications | AGR COMMUN-PRC | ELSEVIER | Agri-Multidisciplinary | Q1 (11.9) | elsevier-food |
| 6 | COMPUTERS AND ELECTRONICS IN AGRICULTURE | COMPUT ELECTRON AGR | ELSEVIER SCI LTD | Agri-Multidisciplinary | Q1 (10.3) | elsevier-food |
| 7 | Molecular Horticulture | MOL HORTIC | SPRINGERNATURE | Horticulture | Q1 (10.0) | springer-food |
| 8 | Horticulture Research | HORTIC RES-ENGLAND | OXFORD UNIV PRESS INC | Horticulture | Q1 (9.5) | food-quality-safety |
| 9 | Farming System | FARMING SYST | ELSEVIER | Agri-Multidisciplinary | Q1 (9.3) | elsevier-food |
| 10 | Advanced Agrochem | ADV AGROCHEM | KEAI PUBLISHING LTD | Agri-Multidisciplinary | Q1 (9.2) | j-future-foods |
| 11 | Information Processing in Agriculture | INFORM PROCESS AGR | ELSEVIER | Agri-Multidisciplinary | Q1 (8.9) | elsevier-food |
| 12 | Crop and Environment | CROP ENVIRON | ELSEVIER | Agronomy | Q1 (8.6) | elsevier-food |
| 13 | SOIL & TILLAGE RESEARCH | SOIL TILL RES | ELSEVIER | Soil Science | Q1 (8.4) | elsevier-food |
| 14 | Animal Nutrition | ANIM NUTR | KEAI PUBLISHING LTD | Dairy & Animal Science | Q1 (8.3) | j-future-foods |
| 15 | International Soil and Water Conservation Research | INT SOIL WATER CONSE | KEAI PUBLISHING LTD | Soil Science | Q1 (8.3) | j-future-foods |
| 16 | BIORESOURCE TECHNOLOGY | BIORESOURCE TECHNOL | ELSEVIER SCI LTD | Agri Engineering | Q1 (8.2) | elsevier-food |
| 17 | Plant Phenomics | PLANT PHENOMICS | ELSEVIER SCIENCE INC | Agronomy | Q1 (8.2) | elsevier-food |
| 18 | Agronomy for Sustainable Development | AGRON SUSTAIN DEV | SPRINGER FRANCE | Agronomy | Q1 (8.2) | springer-food |
| 19 | Journal of Animal Science and Biotechnology | J ANIM SCI BIOTECHNO | BMC | Dairy & Animal Science | Q1 (7.9) | agri-food-security |
| 20 | FIELD CROPS RESEARCH | FIELD CROP RES | ELSEVIER | Agronomy | Q1 (7.9) | elsevier-food |
| 21 | Geoderma | GEODERMA | ELSEVIER | Soil Science | Q1 (7.9) | elsevier-food |
| 22 | BIOSYSTEMS ENGINEERING | BIOSYST ENG | ACADEMIC PRESS INC ELSEVIER SCIENCE | Agri Engineering | Q1 (7.8) | elsevier-food |
| 23 | Animal Frontiers | ANIM FRONT | OXFORD UNIV PRESS INC | Dairy & Animal Science | Q1 (7.8) | food-quality-safety |
| 24 | Agricultural Water Management | AGR WATER MANAGE | ELSEVIER | Agronomy | Q1 (7.8) | elsevier-food |
| 25 | AGRICULTURE ECOSYSTEMS & ENVIRONMENT | AGR ECOSYST ENVIRON | ELSEVIER | Agri-Multidisciplinary | Q1 (7.7) | elsevier-food |
| 26 | PRECISION AGRICULTURE | PRECIS AGRIC | SPRINGER | Agri-Multidisciplinary | Q1 (7.6) | springer-food |
| 27 | Annual Review of Resource Economics | ANNU REV RESOUR ECON | ANNUAL REVIEWS | Agri Economics & Policy | Q1 (7.5) | annu-rev-food |
| 28 | Rice Science | RICE SCI | ELSEVIER | Agronomy | Q1 (7.4) | elsevier-food |
| 29 | POSTHARVEST BIOLOGY AND TECHNOLOGY | POSTHARVEST BIOL TEC | ELSEVIER | Agronomy | Q1 (7.3) | elsevier-food |
| 30 | Journal of Agriculture and Food Research | J AGR FOOD RES | ELSEVIER | Agri-Multidisciplinary | Q1 (7.2) | elsevier-food |
| 31 | Smart Agricultural Technology | SMART AGR TECHNOL | ELSEVIER | Agri Engineering | Q1 (7.1) | elsevier-food |
| 32 | Horticultural Plant Journal | HORTIC PLANT J | KEAI PUBLISHING LTD | Horticulture | Q1 (7.1) | j-future-foods |
| 33 | BIOMASS & BIOENERGY | BIOMASS BIOENERG | PERGAMON-ELSEVIER SCIENCE LTD | Agri Engineering | Q1 (7.0) | elsevier-food |
| 34 | PEDOSPHERE | PEDOSPHERE | SCIENCE PRESS | Soil Science | Q1 (7.0) | agri-other |
| 35 | FOOD POLICY | FOOD POLICY | ELSEVIER SCI LTD | Agri Economics & Policy | Q1 (6.8) | elsevier-food |
| 36 | BIOLOGY AND FERTILITY OF SOILS | BIOL FERT SOILS | SPRINGER | Soil Science | Q1 (6.8) | springer-food |
| 37 | JOURNAL OF AGRICULTURAL AND FOOD CHEMISTRY | J AGR FOOD CHEM | AMER CHEMICAL SOC | Agri-Multidisciplinary | Q1 (6.7) | jafc |
| 38 | EUROPEAN JOURNAL OF AGRONOMY | EUR J AGRON | ELSEVIER | Agronomy | Q1 (6.7) | elsevier-food |
| 39 | Crop Journal | CROP J | KEAI PUBLISHING LTD | Agronomy | Q1 (6.7) | j-future-foods |
| 40 | AGRICULTURAL AND FOREST METEOROLOGY | AGR FOREST METEOROL | ELSEVIER | Agronomy | Q1 (6.6) | elsevier-food |
| 41 | CATENA | CATENA | ELSEVIER | Soil Science | Q1 (6.6) | elsevier-food |
| 42 | INDUSTRIAL CROPS AND PRODUCTS | IND CROP PROD | ELSEVIER | Agri Engineering | Q1 (6.4) | elsevier-food |
| 43 | AGRICULTURAL SYSTEMS | AGR SYST | ELSEVIER SCI LTD | Agri-Multidisciplinary | Q1 (6.2) | elsevier-food |
| 44 | Agriculture & Food Security | AGR FOOD SECUR | BIOMED CENTRAL LTD | Agri-Multidisciplinary | Q1 (6.1) | agri-food-security |
| 45 | Frontiers in Soil Science | FRONT SOIL SCI | FRONTIERS MEDIA SA | Soil Science | Q1 (6.0) | frontiers-nutrition |
| 46 | International Journal of Agricultural Sustainability | INT J AGR SUSTAIN | TAYLOR & FRANCIS LTD | Agri-Multidisciplinary | Q1 (5.9) | crit-rev-food |
| 47 | Chemical and Biological Technologies in Agriculture | CHEM BIOL TECHNOL AG | SPRINGER | Agri-Multidisciplinary | Q1 (5.8) | springer-food |
| 48 | Asian Journal of Agriculture and Biology | ASIAN J AGR BIOL | LIFE SCIENCES SOC PAKISTAN | Agri-Multidisciplinary | Q1 (5.8) | agri-other |
| 49 | Rice | RICE | SPRINGER | Agronomy | Q1 (5.8) | springer-food |
| 50 | Journal of Integrative Agriculture | J INTEGR AGR | KEAI PUBLISHING LTD | Agri-Multidisciplinary | Q1 (5.7) | j-future-foods |
| 51 | APPLIED SOIL ECOLOGY | APPL SOIL ECOL | ELSEVIER | Soil Science | Q1 (5.6) | elsevier-food |
| 52 | JOURNAL OF AGRICULTURAL ECONOMICS | J AGR ECON | WILEY | Agri Economics & Policy | Q1 (5.5) | wiley-food |
| 53 | Agricultural and Food Economics | AGR FOOD ECON | SPRINGERNATURE | Agri Economics & Policy | Q1 (5.4) | springer-food |
| 54 | Animal Research and One Health | ANIM RES ONE HEALTH | WILEY | Dairy & Animal Science | Q1 (5.3) | wiley-food |
| 55 | Crop Design | CROP DES | ELSEVIER | Agronomy | Q1 (5.2) | elsevier-food |
| 56 | EUROPEAN REVIEW OF AGRICULTURAL ECONOMICS | EUR REV AGRIC ECON | OXFORD UNIV PRESS | Agri Economics & Policy | Q1 (5.1) | food-quality-safety |
| 57 | Soil | SOIL-GERMANY | COPERNICUS GESELLSCHAFT MBH | Soil Science | Q1 (5.1) | agri-other |
| 58 | AQUACULTURE ECONOMICS & MANAGEMENT | AQUACULT ECON MANAG | TAYLOR & FRANCIS INC | Agri Economics & Policy | Q1 (5.0) | crit-rev-food |
| 59 | AMERICAN JOURNAL OF AGRICULTURAL ECONOMICS | AM J AGR ECON | WILEY | Agri Economics & Policy | Q1 (4.9) | wiley-food |
| 60 | PLANT AND SOIL | PLANT SOIL | SPRINGER | Agronomy | Q1 (4.8) | springer-food |
| 61 | JOURNAL OF DAIRY SCIENCE | J DAIRY SCI | ELSEVIER SCIENCE INC | Dairy & Animal Science | Q1 (4.7) | j-dairy-science |
| 62 | AGRICULTURAL ECONOMICS | AGR ECON-BLACKWELL | WILEY | Agri Economics & Policy | Q1 (4.7) | wiley-food |
| 63 | SCIENTIA HORTICULTURAE | SCI HORTIC-AMSTERDAM | ELSEVIER | Horticulture | Q1 (4.6) | elsevier-food |
| 64 | POULTRY SCIENCE | POULTRY SCI | ELSEVIER | Dairy & Animal Science | Q1 (4.5) | elsevier-food |
| 65 | Agriculture-Basel | AGRICULTURE-BASEL | MDPI | Agronomy | Q1 (4.5) | foods-mdpi |
| 66 | GENETICS SELECTION EVOLUTION | GENET SEL EVOL | BMC | Dairy & Animal Science | Q1 (4.4) | agri-food-security |
| 67 | China Agricultural Economic Review | CHINA AGR ECON REV | EMERALD GROUP PUBLISHING LTD | Agri Economics & Policy | Q1 (4.4) | british-food-journal |
| 68 | British Food Journal | BRIT FOOD J | EMERALD GROUP PUBLISHING LTD | Agri Economics & Policy | Q1 (4.4) | british-food-journal |
| 69 | AGRICULTURE AND HUMAN VALUES | AGR HUM VALUES | SPRINGER | Agri-Multidisciplinary | Q1 (4.3) | springer-food |
| 70 | ANNALS OF AGRICULTURAL SCIENCES | ANN AGR SCI-CAIRO | ELSEVIER | Agri-Multidisciplinary | Q1 (4.3) | elsevier-food |
| 71 | PEST MANAGEMENT SCIENCE | PEST MANAG SCI | WILEY | Agronomy | Q1 (4.2) | wiley-food |
| 72 | Frontiers in Agronomy | FRONT AGRON | FRONTIERS MEDIA SA | Agronomy | Q1 (4.2) | frontiers-nutrition |
| 73 | SEED SCIENCE AND TECHNOLOGY | SEED SCI TECHNOL | ISTA-INT SEED TESTING ASSOC | Agronomy | Q1 (4.2) | agri-other |
| 74 | Animal | ANIMAL | ELSEVIER | Dairy & Animal Science | Q1 (4.1) | elsevier-food |
| 75 | THEORETICAL AND APPLIED GENETICS | THEOR APPL GENET | SPRINGER | Agronomy | Q1 (4.1) | springer-food |
| 76 | Agronomy-Basel | AGRONOMY-BASEL | MDPI | Agronomy | Q1 (4.1) | foods-mdpi |
| 77 | Vegetable Research | VEG RES | Maximum Academic Press | Horticulture | Q1 (4.1) | elsevier-food |
| 78 | Journal of Sustainable Agriculture and Environment | J SUST AGR ENV-AUST | WILEY | Agri-Multidisciplinary | Q1 (4.0) | wiley-food |
| 79 | JOURNAL OF THE SCIENCE OF FOOD AND AGRICULTURE | J SCI FOOD AGR | WILEY | Agri-Multidisciplinary | Q1 (4.0) | wiley-food |
| 80 | JOURNAL OF ANIMAL SCIENCE | J ANIM SCI | OXFORD UNIV PRESS INC | Dairy & Animal Science | Q1 (3.7) | food-quality-safety |
| 81 | CABI Agriculture and Bioscience | CABI AGR BIOSCI | CABI PUBLISHING | Agri-Multidisciplinary | Q1 (3.7) | agri-other |
| 82 | Applied Economic Perspectives and Policy | APPL ECON PERSPECT P | WILEY | Agri Economics & Policy | Q1 (3.6) | wiley-food |
| 83 | MOLECULAR BREEDING | MOL BREEDING | SPRINGER | Agronomy | Q1 (3.6) | springer-food |
| 84 | JOURNAL OF ANIMAL SCIENCE AND TECHNOLOGY | J ANIM SCI TECHNOL | KOREAN SOCIETY ANIMAL SCIENCE & TE… | Dairy & Animal Science | Q1 (3.4) | agri-other |
| 85 | WORLDS POULTRY SCIENCE JOURNAL | WORLD POULTRY SCI J | TAYLOR & FRANCIS LTD | Dairy & Animal Science | Q1 (3.4) | crit-rev-food |
| 86 | POTATO RESEARCH | POTATO RES | SPRINGER | Agronomy | Q1 (3.4) | springer-food |
| 87 | IRRIGATION SCIENCE | IRRIGATION SCI | SPRINGER | Agronomy | Q1 (3.4) | springer-food |
| 88 | Frontiers of Agricultural Science and Engineering | FRONT AGRIC SCI ENG | HIGHER EDUCATION PRESS | Agronomy | Q1 (3.4) | agri-other |
| 89 | Advances in Agriculture | ADV AGR | WILEY | Agronomy | Q1 (3.4) | wiley-food |
| 90 | Horticulturae | HORTICULTURAE | MDPI | Horticulture | Q1 (3.4) | foods-mdpi |
| 91 | Crop Protection | CROP PROT | ELSEVIER SCI LTD | Agronomy | Q1 (3.3) | elsevier-food |
| 92 | in silico Plants | IN SILICO PLANTS | OXFORD UNIV PRESS | Agronomy | Q1 (3.3) | food-quality-safety |
| 93 | JOURNAL OF PLANT NUTRITION AND SOIL SCIENCE | J PLANT NUTR SOIL SC | WILEY-V C H VERLAG GMBH | Agronomy | Q1 (3.3) | wiley-food |
| 94 | AUSTRALIAN JOURNAL OF GRAPE AND WINE RESEARCH | AUST J GRAPE WINE R | WILEY | Horticulture | Q1 (3.3) | wiley-food |
| 95 | Animals | ANIMALS-BASEL | MDPI | Dairy & Animal Science | Q1 (3.2) | foods-mdpi |
| 96 | ANIMAL FEED SCIENCE AND TECHNOLOGY | ANIM FEED SCI TECH | ELSEVIER | Dairy & Animal Science | Q1 (3.2) | elsevier-food |
| 97 | Animal Bioscience | ANIM BIOSCI | ASIAN-AUSTRALASIAN ASSOC ANIMAL PR… | Dairy & Animal Science | Q1 (3.2) | agri-other |
| 98 | JOURNAL OF AGRONOMY AND CROP SCIENCE | J AGRON CROP SCI | WILEY | Agronomy | Q1 (3.2) | wiley-food |
| 99 | AGROFORESTRY SYSTEMS | AGROFOREST SYST | SPRINGER | Agronomy | Q1 (3.2) | springer-food |
| 100 | Veterinary and Animal Science | VET ANIM SCI | ELSEVIER | Dairy & Animal Science | Q1 (3.0) | elsevier-food |
| 101 | Dairy | DAIRY-BASEL | MDPI | Dairy & Animal Science | Q1 (3.0) | foods-mdpi |
| 102 | Italian Journal of Agronomy | ITAL J AGRON | ELSEVIER | Agronomy | Q1 (3.0) | elsevier-food |
| 103 | Seeds | SEEDS-BASEL | MDPI | Agronomy | Q1 (3.0) | foods-mdpi |
| 104 | Annals of Animal Science | ANN ANIM SCI | WALTER DE GRUYTER GMBH | Dairy & Animal Science | Q1 (2.9) | agri-other |
| 105 | JOURNAL OF ANIMAL PHYSIOLOGY AND ANIMAL NUTRITION | J ANIM PHYSIOL AN N | WILEY | Dairy & Animal Science | Q1 (2.8) | wiley-food |
| 106 | Frontiers in Animal Science | FRONT ANIM SCI | FRONTIERS MEDIA SA | Dairy & Animal Science | Q1 (2.8) | frontiers-nutrition |
| 107 | ANIMAL REPRODUCTION SCIENCE | ANIM REPROD SCI | ELSEVIER | Dairy & Animal Science | Q1 (2.6) | elsevier-food |
| 108 | APPLIED ANIMAL BEHAVIOUR SCIENCE | APPL ANIM BEHAV SCI | ELSEVIER | Dairy & Animal Science | Q1 (2.6) | elsevier-food |
| 109 | Italian Journal of Animal Science | ITAL J ANIM SCI | TAYLOR & FRANCIS LTD | Dairy & Animal Science | Q1 (2.6) | crit-rev-food |
| 110 | AQUACULTURAL ENGINEERING | AQUACULT ENG | ELSEVIER SCI LTD | Agri Engineering | Q2 (4.4) | elsevier-food |
| 111 | EUROPEAN JOURNAL OF SOIL SCIENCE | EUR J SOIL SCI | WILEY | Soil Science | Q2 (4.3) | wiley-food |
| 112 | Soil Systems | SOIL SYST | MDPI | Soil Science | Q2 (4.1) | foods-mdpi |
| 113 | Soil Ecology Letters | SOIL ECOL LETT | SPRINGERNATURE | Soil Science | Q2 (4.0) | springer-food |
| 114 | LAND DEGRADATION & DEVELOPMENT | LAND DEGRAD DEV | WILEY | Soil Science | Q2 (4.0) | wiley-food |
| 115 | Rhizosphere | RHIZOSPHERE-NETH | ELSEVIER | Soil Science | Q2 (3.9) | elsevier-food |
| 116 | EUROPEAN JOURNAL OF SOIL BIOLOGY | EUR J SOIL BIOL | ELSEVIER FRANCE-EDITIONS SCIENTIFI… | Soil Science | Q2 (3.9) | elsevier-food |
| 117 | Geoderma Regional | GEODERMA REG | ELSEVIER | Soil Science | Q2 (3.9) | elsevier-food |
| 118 | Organic Agriculture | ORG AGR | SPRINGERNATURE | Agri-Multidisciplinary | Q2 (3.6) | springer-food |
| 119 | Journal of Soil Science and Plant Nutrition | J SOIL SCI PLANT NUT | SPRINGER INT PUBL AG | Soil Science | Q2 (3.6) | springer-food |
| 120 | SOIL USE AND MANAGEMENT | SOIL USE MANAGE | WILEY | Soil Science | Q2 (3.6) | wiley-food |
| 121 | Journal of Land Use Science | J LAND USE SCI | TAYLOR & FRANCIS LTD | Agri-Multidisciplinary | Q2 (3.5) | crit-rev-food |
| 122 | VADOSE ZONE JOURNAL | VADOSE ZONE J | WILEY | Soil Science | Q2 (3.5) | wiley-food |
| 123 | ACS Agricultural Science & Technology | ACS AGR SCI TECHNOL | AMER CHEMICAL SOC | Agri-Multidisciplinary | Q2 (3.4) | jafc |
| 124 | Agricultural & Environmental Letters | AGR ENV LETT | WILEY | Agri-Multidisciplinary | Q2 (3.3) | wiley-food |
| 125 | JOURNAL OF SOILS AND SEDIMENTS | J SOIL SEDIMENT | SPRINGER HEIDELBERG | Soil Science | Q2 (3.3) | springer-food |
| 126 | OUTLOOK ON AGRICULTURE | OUTLOOK AGR | SAGE PUBLICATIONS LTD | Agri-Multidisciplinary | Q2 (3.2) | agri-other |
| 127 | AgriEngineering | AGRIENGINEERING | MDPI | Agri Engineering | Q2 (3.1) | foods-mdpi |
| 128 | International Journal of Agricultural and Biological Engineering | INT J AGR BIOL ENG | CHINESE ACAD AGRICULTURAL ENGINEER… | Agri Engineering | Q2 (3.1) | agri-other |
| 129 | Journal of Agricultural Engineering | J AGRIC ENG-ITALY | PAGEPRESS PUBL | Agri Engineering | Q2 (3.1) | agri-other |
| 130 | Cogent Food & Agriculture | COGENT FOOD AGR | TAYLOR & FRANCIS LTD | Agri-Multidisciplinary | Q2 (3.1) | crit-rev-food |
| 131 | Ornamental Plant Research | ORNAM PLANT RES | Maximum Academic Press | Horticulture | Q2 (3.1) | elsevier-food |
| 132 | OENO One | OENO ONE | INT VITICULTURE & ENOLOGY SOC-IVES | Horticulture | Q2 (3.0) | agri-other |
| 133 | Journal of Biosystems Engineering | J BIOSYST ENG-KOR | SPRINGERNATURE | Agri Engineering | Q2 (2.9) | springer-food |
| 134 | EuroChoices | EUROCHOICES | WILEY | Agri Economics & Policy | Q2 (2.9) | wiley-food |
| 135 | Grass Research | GRASS RES | Maximum Academic Press | Agronomy | Q2 (2.9) | elsevier-food |
| 136 | Fruit Research | FRUIT RES | Maximum Academic Press | Horticulture | Q2 (2.9) | elsevier-food |
| 137 | Journal of Plant Diseases and Protection | J PLANT DIS PROTECT | SPRINGER HEIDELBERG | Agri-Multidisciplinary | Q2 (2.8) | springer-food |
| 138 | Gesunde Pflanzen | GESUNDE PFLANZ | SPRINGER | Agronomy | Q2 (2.8) | springer-food |
| 139 | Grassland Research | GRASSL RES | WILEY | Agronomy | Q2 (2.8) | wiley-food |
| 140 | Journal of Crop Health | J CROP HEALTH | SPRINGER | Agronomy | Q2 (2.8) | springer-food |
| 141 | PLANT PATHOLOGY | PLANT PATHOL | WILEY | Agronomy | Q2 (2.8) | wiley-food |
| 142 | Horticulture Environment and Biotechnology | HORTIC ENVIRON BIOTE | KOREAN SOC HORTICULTURAL SCIENCE | Horticulture | Q2 (2.8) | agri-other |
| 143 | Agricultural Engineering-Poland | AGR ENG-POL | Paradigm Publishing Services-De Gr… | Agri Engineering | Q2 (2.6) | agri-other |
| 144 | Wine Economics and Policy | WINE ECON POLICY | FIRENZE UNIV PRESS | Agri Economics & Policy | Q2 (2.6) | agri-other |
| 145 | Turkish Journal of Agriculture and Forestry | TURK J AGRIC FOR | Tubitak Scientific & Technological… | Agronomy | Q2 (2.6) | agri-other |
| 146 | GRASS AND FORAGE SCIENCE | GRASS FORAGE SCI | WILEY | Agronomy | Q2 (2.6) | wiley-food |
| 147 | International Journal of Plant Production | INT J PLANT PROD | SPRINGER | Agronomy | Q2 (2.6) | springer-food |
| 148 | EXPERIMENTAL AGRICULTURE | EXP AGR | CAMBRIDGE UNIV PRESS | Agronomy | Q2 (2.6) | cambridge-nutrition |
| 149 | Poultry | POULTRY-BASEL | MDPI | Dairy & Animal Science | Q2 (2.5) | foods-mdpi |
| 150 | Journal of Agribusiness in Developing and Emerging Economies | J AGRIBUS DEV EMERG | EMERALD GROUP PUBLISHING LTD | Agri Economics & Policy | Q2 (2.5) | british-food-journal |
| 151 | AGRONOMY JOURNAL | AGRON J | WILEY | Agronomy | Q2 (2.5) | wiley-food |
| 152 | MYCOBIOLOGY | MYCOBIOLOGY | TAYLOR & FRANCIS LTD | Agronomy | Q2 (2.5) | crit-rev-food |
| 153 | PLANT SOIL AND ENVIRONMENT | PLANT SOIL ENVIRON | CZECH ACADEMY AGRICULTURAL SCIENCES | Agronomy | Q2 (2.5) | agri-other |
| 154 | JDS Communications | JDS COMMUN | ELSEVIER | Dairy & Animal Science | Q2 (2.4) | elsevier-food |
| 155 | AUSTRALIAN JOURNAL OF AGRICULTURAL AND RESOURCE ECONOMICS | AUST J AGR RESOUR EC | WILEY | Agri Economics & Policy | Q2 (2.4) | wiley-food |
| 156 | Agribusiness | AGRIBUSINESS | WILEY | Agri Economics & Policy | Q2 (2.4) | wiley-food |
| 157 | NJAS-Impact in Agricultural and Life Sciences | NJAS-IMP AGR LIFE SC | TAYLOR & FRANCIS LTD | Agri-Multidisciplinary | Q2 (2.4) | crit-rev-food |
| 158 | RENEWABLE AGRICULTURE AND FOOD SYSTEMS | RENEW AGR FOOD SYST | CAMBRIDGE UNIV PRESS | Agri-Multidisciplinary | Q2 (2.4) | cambridge-nutrition |
| 159 | Agroecology and Sustainable Food Systems | AGROECOL SUST FOOD | TAYLOR & FRANCIS INC | Agri-Multidisciplinary | Q2 (2.4) | crit-rev-food |
| 160 | CROP SCIENCE | CROP SCI | WILEY | Agronomy | Q2 (2.4) | wiley-food |
| 161 | WEED SCIENCE | WEED SCI | CAMBRIDGE UNIV PRESS | Agronomy | Q2 (2.4) | cambridge-nutrition |
| 162 | JOURNAL OF APPLIED POULTRY RESEARCH | J APPL POULTRY RES | ELSEVIER | Dairy & Animal Science | Q2 (2.3) | elsevier-food |
| 163 | Veterinary World | VET WORLD | VETERINARY WORLD | Dairy & Animal Science | Q2 (2.3) | agri-other |
| 164 | Animal Reproduction | ANIM REPROD | BRAZILIAN COLL ANIMAL REPRODUCTION | Dairy & Animal Science | Q2 (2.3) | agri-other |
| 165 | Q Open | Q OPEN | OXFORD UNIV PRESS | Agri Economics & Policy | Q2 (2.3) | food-quality-safety |
| 166 | JOURNAL OF AGRICULTURAL SCIENCE | J AGR SCI-CAMBRIDGE | CAMBRIDGE UNIV PRESS | Agri-Multidisciplinary | Q2 (2.3) | cambridge-nutrition |
| 167 | WEED RESEARCH | WEED RES | WILEY | Agronomy | Q2 (2.3) | wiley-food |
| 168 | CEREAL RESEARCH COMMUNICATIONS | CEREAL RES COMMUN | SPRINGER HEIDELBERG | Agronomy | Q2 (2.3) | springer-food |
| 169 | Livestock Science | LIVEST SCI | ELSEVIER | Dairy & Animal Science | Q2 (2.2) | elsevier-food |
| 170 | ANIMAL GENETICS | ANIM GENET | WILEY | Dairy & Animal Science | Q2 (2.2) | wiley-food |
| 171 | CANADIAN JOURNAL OF AGRICULTURAL ECONOMICS-REVUE CANADIENNE D AGROECONOMIE | CAN J AGR ECON | WILEY | Agri Economics & Policy | Q2 (2.2) | wiley-food |
| 172 | Journal of Wine Economics | J WINE ECON | CAMBRIDGE UNIV PRESS | Agri Economics & Policy | Q2 (2.2) | cambridge-nutrition |
| 173 | International Journal of Wine Business Research | INT J WINE BUS RES | EMERALD GROUP PUBLISHING LTD | Agronomy | Q2 (2.2) | british-food-journal |
| 174 | Archives of Agronomy and Soil Science | ARCH AGRON SOIL SCI | TAYLOR & FRANCIS LTD | Agronomy | Q2 (2.2) | crit-rev-food |
| 175 | International Journal of Fruit Science | INT J FRUIT SCI | TAYLOR & FRANCIS INC | Horticulture | Q2 (2.2) | crit-rev-food |
| 176 | JOURNAL OF HORTICULTURAL SCIENCE & BIOTECHNOLOGY | J HORTIC SCI BIOTECH | TAYLOR & FRANCIS LTD | Horticulture | Q2 (2.2) | crit-rev-food |
| 177 | AMERICAN JOURNAL OF ENOLOGY AND VITICULTURE | AM J ENOL VITICULT | AMER SOC ENOLOGY VITICULTURE | Horticulture | Q2 (2.2) | agri-other |
| 178 | JOURNAL OF REPRODUCTION AND DEVELOPMENT | J REPROD DEVELOP | SOCIETY REPRODUCTION & DEVELOPMENT… | Dairy & Animal Science | Q2 (2.1) | agri-other |
| 179 | JOURNAL OF POULTRY SCIENCE | J POULT SCI | JAPAN POULTRY SCIENCE ASSOC | Dairy & Animal Science | Q2 (2.1) | agri-other |
| 180 | Agrekon | AGREKON | ROUTLEDGE JOURNALS, TAYLOR & FRANC… | Agri Economics & Policy | Q2 (2.1) | crit-rev-food |
| 181 | Journal of Agriculture Food Systems and Community Development | J AGRIC FOOD SYST CO | LYSON CENTER CIVIC AGRICULTURE & F… | Agri Economics & Policy | Q2 (2.1) | agri-other |
| 182 | ANNALS OF APPLIED BIOLOGY | ANN APPL BIOL | WILEY | Agri-Multidisciplinary | Q2 (2.1) | wiley-food |
| 183 | International Agrophysics | INT AGROPHYS | POLISH ACAD SCIENCES, INST AGROPHY… | Agronomy | Q2 (2.1) | agri-other |
| 184 | EUROPEAN JOURNAL OF PLANT PATHOLOGY | EUR J PLANT PATHOL | SPRINGER | Agronomy | Q2 (2.1) | springer-food |
| 185 | Agrosystems Geosciences & Environment | AGROSYS GEOSCI ENV | WILEY | Agronomy | Q2 (2.1) | wiley-food |
| 186 | Crops | CROPS-BASEL | MDPI | Agronomy | Q2 (2.1) | foods-mdpi |
| 187 | Paddy and Water Environment | PADDY WATER ENVIRON | SPRINGER HEIDELBERG | Agronomy | Q2 (2.1) | springer-food |
| 188 | PLANT PRODUCTION SCIENCE | PLANT PROD SCI | TAYLOR & FRANCIS LTD | Agronomy | Q2 (2.1) | crit-rev-food |
| 189 | International Journal of Agronomy | INT J AGRON | WILEY | Agronomy | Q2 (2.1) | wiley-food |
| 190 | Czech Journal of Genetics and Plant Breeding | CZECH J GENET PLANT | CZECH ACADEMY AGRICULTURAL SCIENCES | Agronomy | Q2 (2.1) | agri-other |
| 191 | Tree Genetics & Genomes | TREE GENET GENOMES | SPRINGER HEIDELBERG | Horticulture | Q2 (2.1) | springer-food |
| 192 | Technology in Horticulture | TECHNOL HORTIC | Maximum Academic Press | Horticulture | Q2 (2.1) | elsevier-food |
| 193 | TROPICAL ANIMAL HEALTH AND PRODUCTION | TROP ANIM HEALTH PRO | SPRINGER | Dairy & Animal Science | Q2 (2.0) | springer-food |
| 194 | JOURNAL OF APPLIED ANIMAL RESEARCH | J APPL ANIM RES | TAYLOR & FRANCIS LTD | Dairy & Animal Science | Q2 (2.0) | crit-rev-food |
| 195 | Ruminants | RUMINANTS-BASEL | MDPI | Dairy & Animal Science | Q2 (2.0) | foods-mdpi |
| 196 | ANIMAL BIOTECHNOLOGY | ANIM BIOTECHNOL | TAYLOR & FRANCIS INC | Dairy & Animal Science | Q2 (2.0) | crit-rev-food |
| 197 | CABI Reviews | CABI REV | CABI PUBLISHING | Dairy & Animal Science | Q2 (2.0) | agri-other |
| 198 | Agricultural and Resource Economics Review | AGRIC RESOUR ECON RE | CAMBRIDGE UNIV PRESS | Agri Economics & Policy | Q2 (2.0) | cambridge-nutrition |
| 199 | Folia Horticulturae | FOLIA HORTIC | Paradigm Publishing Services-De Gr… | Horticulture | Q2 (2.0) | agri-other |
| 200 | JOURNAL OF ANIMAL BREEDING AND GENETICS | J ANIM BREED GENET | WILEY | Dairy & Animal Science | Q2 (1.9) | wiley-food |
| 201 | Translational Animal Science | TRANSL ANIM SCI | OXFORD UNIV PRESS INC | Dairy & Animal Science | Q2 (1.9) | food-quality-safety |
| 202 | Archives Animal Breeding | ARCH ANIM BREED | COPERNICUS GESELLSCHAFT MBH | Dairy & Animal Science | Q2 (1.9) | agri-other |
| 203 | JOURNAL OF ANIMAL AND FEED SCIENCES | J ANIM FEED SCI | KIELANOWSKI INST ANIMAL PHYSIOLOGY… | Dairy & Animal Science | Q2 (1.9) | agri-other |
| 204 | Journal of Advanced Veterinary and Animal Research | J ADV VET ANIM RES | NETWORK VETERINARIANS BANGLADESH | Dairy & Animal Science | Q2 (1.9) | agri-other |
| 205 | JSFA Reports | JSFA REP | WILEY | Agri-Multidisciplinary | Q2 (1.9) | wiley-food |
| 206 | Journal of Agricultural Science and Technology | J AGR SCI TECH-IRAN | TARBIAT MODARES UNIV | Agri-Multidisciplinary | Q2 (1.9) | agri-other |
| 207 | BIOLOGICAL AGRICULTURE & HORTICULTURE | BIOL AGRIC HORTIC | TAYLOR & FRANCIS LTD | Agronomy | Q2 (1.9) | crit-rev-food |
| 208 | Sugar Tech | SUGAR TECH | SPRINGER INDIA | Agronomy | Q2 (1.9) | springer-food |
| 209 | GENETIC RESOURCES AND CROP EVOLUTION | GENET RESOUR CROP EV | SPRINGER | Agronomy | Q2 (1.9) | springer-food |
| 210 | IRRIGATION AND DRAINAGE | IRRIG DRAIN | WILEY | Agronomy | Q2 (1.9) | wiley-food |
| 211 | Meat and Muscle Biology | MEAT MUSCLE BIOL | Iowa State Univ Digital Press | Dairy & Animal Science | Q2 (1.8) | agri-other |
| 212 | Applied Animal Science | APPL ANIM SCI | ELSEVIER SCIENCE INC | Dairy & Animal Science | Q2 (1.8) | elsevier-food |
| 213 | SMALL RUMINANT RESEARCH | SMALL RUMINANT RES | ELSEVIER | Dairy & Animal Science | Q2 (1.8) | elsevier-food |
| 214 | BRAGANTIA | BRAGANTIA | INST AGRONOMICO | Agri-Multidisciplinary | Q2 (1.8) | agri-other |
| 215 | Crop & Pasture Science | CROP PASTURE SCI | CSIRO PUBLISHING | Agri-Multidisciplinary | Q2 (1.8) | agri-other |
| 216 | AIMS Agriculture and Food | AIMS AGRIC FOOD | AMER INST MATHEMATICAL SCIENCES-AI… | Agri-Multidisciplinary | Q2 (1.8) | agri-other |
| 217 | EUPHYTICA | EUPHYTICA | SPRINGER | Agronomy | Q2 (1.8) | springer-food |
| 218 | JOURNAL OF AGRICULTURAL & ENVIRONMENTAL ETHICS | J AGR ENVIRON ETHIC | SPRINGER | Agri-Multidisciplinary | Q2 (1.7) | springer-food |
| 219 | Chilean Journal of Agricultural Research | CHIL J AGR RES | INST INVESTIGACIONES AGROPECUARIAS… | Agri-Multidisciplinary | Q2 (1.7) | agri-other |
| 220 | Open Agriculture | OPEN AGRIC | DE GRUYTER POLAND SP Z O O | Agri-Multidisciplinary | Q2 (1.7) | agri-other |
| 221 | SCIENTIA AGRICOLA | SCI AGR | UNIV SAO PAULO, ESALQ | Agri-Multidisciplinary | Q2 (1.7) | agri-other |
| 222 | BREEDING SCIENCE | BREEDING SCI | JAPANESE SOC BREEDING | Agronomy | Q2 (1.7) | agri-other |
| 223 | CANADIAN JOURNAL OF PLANT SCIENCE | CAN J PLANT SCI | CANADIAN SCIENCE PUBLISHING | Agronomy | Q2 (1.7) | agri-other |
| 224 | COMMUNICATIONS IN SOIL SCIENCE AND PLANT ANALYSIS | COMMUN SOIL SCI PLAN | TAYLOR & FRANCIS INC | Agronomy | Q2 (1.7) | crit-rev-food |
| 225 | Egyptian Journal of Agronomy | EGYPT J AGRON | NATL INFORMATION DOCUMENTATION CEN… | Agronomy | Q2 (1.7) | agri-other |
| 226 | PLANT BREEDING | PLANT BREEDING | WILEY | Agronomy | Q2 (1.7) | wiley-food |
| 227 | WEED BIOLOGY AND MANAGEMENT | WEED BIOL MANAG | WILEY | Agronomy | Q2 (1.7) | wiley-food |
| 228 | International Journal of Sustainable Agricultural Management and Informatics | INT J SUST AGR MANAG | INDERSCIENCE ENTERPRISES LTD | Agri-Multidisciplinary | Q2 (1.6) | agri-other |
| 229 | Journal of Agricultural Sciences-Tarim Bilimleri Dergisi | J AGR SCI-TARIM BILI | ANKARA UNIV, FAC AGRICULTURE | Agri-Multidisciplinary | Q2 (1.5) | agri-other |
| 230 | JOURNAL OF AGRICULTURAL METEOROLOGY | J AGRIC METEOROL | SOC AGRICULTURAL METEOROLOGY JAPAN | Agri-Multidisciplinary | Q2 (1.5) | agri-other |
