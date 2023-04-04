import argparse

def parse_args():
    parser = argparse.ArgumentParser()

    # General settings
    parser.add_argument("--api_key", required=True, help="OPEN AI API KEY")
    parser.add_argument("--engine_id", required=True, help="OPEN AI Engine ID for a fine tuned model")
    parser.add_argument("--text_path", required=True, help="Filepath containing texts to make prediction")
    parser.add_argument("--output_path", required=True, help="Output filepath for the prediction")
    args = parser.parse_args()
    return args 
