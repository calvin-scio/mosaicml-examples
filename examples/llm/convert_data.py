# Based on https://github.com/mosaicml/streaming
import argparse
import os
import numpy as np
from PIL import Image
from streaming import MDSWriter
import json


# A dictionary mapping input fields to their data types
columns = {
    'text': 'str'
}

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--input_data_dir', type=str, required=True, help='data directory')  
    parser.add_argument('--output_data_dir', type=str, required=True, help='data directory')  
    args = parser.parse_args()

    # Save the samples as shards using MDSWriter
    with MDSWriter(out=args.output_data_dir, columns=columns) as out:
        for filename in os.listdir(args.input_data_dir):
            with open(filename, 'r') as f:
                for line in f:
                    sample = json.loads(line.strip())
                    out.write(sample)

if __name__ == '__main__':
    main()
