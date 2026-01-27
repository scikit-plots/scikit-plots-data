import numpy as np
import pandas as pd

# from scikitplot import _data

# !python -m scikitplot._data._data_export \
#   --input autoscout24_dataset_20251108.csv \
#   --output-dir data/subsets \
#   --percentages 1 \
#   --rounding round \
#   --strategy hash \
#   --id-col id \
#   --dedup \
#   --required-cols id price make model registration_date mileage_km_raw vehicle_type fuel_category is_used country_code \
#   --keep-cols id price make model model_version registration_date mileage_km_raw vehicle_type body_type fuel_category primary_fuel \
#       transmission power_kw power_hp nr_seats nr_doors country_code zip city latitude longitude is_used seller_is_dealer offer_type \
#       description equipment_comfort equipment_entertainment  equipment_extra equipment_safety\
#   --format csv \
#   --write-manifest \
#   --write-profile
def main(*arg, **kwargs):

    # raw_data = "https://zenodo.org/records/17643343/files/autoscout24_dataset_20251108.csv"
    # raw_data = "data/subsets/subset_hash_11615.csv"
    # df = pd.read_csv(raw_data)
    # df.to_csv("autoscout24.csv", index=False)
    (
        pd.read_csv("data/subsets/subset_hash_11615.csv")
        # .query("...")
        # .dropna()
        .to_csv("autoscout24.csv", index=False)
    )


if __name__ == "__main__":
    main()