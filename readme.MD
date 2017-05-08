# Data Analytics

Setup environment: [Environment Setup Wiki](https://github.com/iuu-fishing-detection/data-analytics/wiki)

Setup data after environment is prepared. It is recommended to view the script before running:

    sh iuu-fishing-models/setup.sh

## Download Geos if Geopy does not work
For Mac, download Homebrew, then run

    brew install geos

For Ubuntu, run

    sudo apt-get install libgeos-dev

## Derive data (1 - 3 hours)
sh iuu-fishing-models/derive_data.sh
