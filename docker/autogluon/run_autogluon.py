import argparse
import os
import pandas as pd
from autogluon.tabular import TabularPredictor


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", default="/data/train.csv")
    parser.add_argument("--label", default="target")
    parser.add_argument("--output", default="/data/models")
    args = parser.parse_args()

    os.makedirs(args.output, exist_ok=True)
    print("Loading", args.input)
    df = pd.read_csv(args.input)
    print("Fitting predictor...")
    predictor = TabularPredictor(label=args.label).fit(df)
    predictor.save(os.path.join(args.output, "predictor"))
    print("Done")


if __name__ == "__main__":
    main()
