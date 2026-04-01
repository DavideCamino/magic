import pandas as pd
import json
import os
import argparse

parser = argparse.ArgumentParser(
                    prog='excel_to_json',
                    description='converts an excel table into a json config file')

parser.add_argument('file')

args = parser.parse_args()

# Load Excel file
df = pd.read_excel(args.file)

print(df)

# Convert rows to desired structure
data = {
    "card": df[["id", "card_color", "text_color", "frame_type", "border", "crown_type", "title", "cost", "image", "type", "subtype", "watermark", "body", "caption", "stats", "rarity", "number"]].to_dict(orient="records")
}

# Export to JSON file
with open("output.json", "w", encoding="utf-8") as f:
    json.dump(data, f, indent=4)

print("JSON file created successfully.")

with open("output.json", "r") as f_i:
    with open("cards.json", "w") as f_o:
        cards = f_i.read().replace('NaN', '""')
        f_o.write(cards)

os.system("mv cards.json template/cards.json")
os.system("rm output.json")