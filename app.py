import os
import sys
import openai


from cli import parse_args_app
from generate_gpt_prediction import Predictor

if __name__ == "__main__":
    args = parse_args_app()
    predictor = Predictor(
        api_key=args.api_key,
        engine_id=args.engine_id
    )
    
    while True:
        text = input("Please enter the input/text (q to quit):\n")
        if text == "q":
            break
        result = predictor.predict(text)
        print("\nResult:")
        print(result)
        print()