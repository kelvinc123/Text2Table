import os
import sys
import openai
import time

from table_utils import (
    extract_table_by_name,
    parse_text_to_table,
    is_empty_table,
)

from cli import parse_args

# Ada 4 epochs
# API_KEY="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"
# ENGINE_ID="ada:ft-personal-2023-04-04-18-21-16"

# Babbage 4 epochs
# API_KEY="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",
# ENGINE_ID="babbage:ft-personal-2023-03-30-18-52-41"


class Predictor:
    def __init__(self, api_key, engine_id):
        openai.api_key = api_key
        self.engine_id = engine_id

    def generate_pred(self, textpath, predpath):
        texts = []
        with open(textpath) as f:
            for line in f:
                line = line.strip()
                texts.append(line + "\n")

        for i in range(len(texts)):
            print(f"Working on {i}/{len(texts)} of {predpath}", end="\r")
            time.sleep(1)
            try:
                result = openai.Completion.create(model = self.engine_id, 
                                        prompt = texts[i],
                                        stop=[" |\n"])
                result = [res["text"].strip() for res in result["choices"]]
            except:
                result = [""]
            finally:
                with open(predpath, "a") as f:
                    f.write(f"{result[0]}\n")
        print("\n")

if __name__ == "__main__":
    args = parse_args()

    predictor = Predictor(
        api_key=args.api_key,
        engine_id=args.engine_id
    )

    if not os.path.exists(args.text_path):
        print(f"File {args.text_path} doesn't exists!")
        print("Exit...")
        sys.exit(1)
    
    if os.path.exists(args.output_path):
        print(f"File {args.output_path} already exists!")
        print("Exit...")
        sys.exit(1)

    predictor.generate_pred(args.text_path, args.output_path)