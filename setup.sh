pip install -r requirements.txt

git clone git@github.com:iuu-fishing-detection/training-data.git ../
sh ../training-data/prepare.sh

mkdir iuu-fishing-model/datasets/originals/
mkdir iuu-fishing-model/datasets/measures/
mkdir iuu-fishing-model/datasets/adjusted/

cp ../training-data/data/merged/kristina_*.npz \
datasets/originals/

python scripts/data_preprocessing.py

git clone git@github.com:iuu-fishing-detection/vessel-scoring.git ../

python ../vessel-scoring/scripts/add_measures.py \
datasets/adjusted/kristina_trawl.npz \
datasets/measures/kristina_trawl.measures.npz

python ../vessel-scoring/scripts/add_measures.py \
datasets/adjusted/kristina_ps.npz \
datasets/measures/kristina_ps.measures.npz

python ../vessel-scoring/scripts/add_measures.py \
datasets/adjusted/kristina_longliner.npz \
datasets/measures/kristina_longliner.measures.npz
