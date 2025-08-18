import argparse
import pypsa

import matplotlib.pyplot as plt

def main():
    parser = argparse.ArgumentParser(
        description="Generate plot from the model file."
    )
    
    parser.add_argument(
        "input_file",
        help="Path to the .nc input file"
    )
    parser.add_argument(
        "output_file",
        help="Path to save the output plot image",
        default="plot.pdf"
    )
    
    args = parser.parse_args()
    
    n = pypsa.Network(args.input_file)    
    n.plot()
    plt.savefig(args.output_file)

if __name__ == "__main__":
    main()