# NYC Taxi Trip Duration Prediction

I built a model that predicts how long a Manhattan taxi trip will take, represented with a range, not just a single number. The idea is that a good ETA system should tell you "between 11 and 16 minutes" rather than just "14 minutes."

## What I did

Took NYC TLC yellow taxi data from January to March 2025, cleaned it, engineered features like rolling congestion proxies and cyclical time encoding, and trained a LightGBM quantile regression model that outputs three predictions: optimistic, median, and pessimistic.

## Results

- MAE of 0.8 minutes on the median prediction
- 79.8% of actual trips fell inside the predicted interval (target was 80%)
- Median interval width of 1.5 minutes

## Stack

Python, LightGBM, pandas, scikit-learn, matplotlib, seaborn

## Project structure
```
notebooks/       — data cleaning, feature engineering, model training
src/             — bolt_theme.py for consistent plot styling
website/         — single page project writeup
data/            — not included (too large), download from NYC TLC website
```

## Data source

NYC TLC Yellow Taxi Trip Records: https://www.nyc.gov/site/tlc/about/tlc-trip-record-data.page