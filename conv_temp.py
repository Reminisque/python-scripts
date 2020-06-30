import argparse

parser = argparse.ArgumentParser(
    description="Convert temperature between farenheit and celsius. "
                "Converts from farenheit to celsius by default")

parser.add_argument("temperature", metavar="TEMP", type=float,
                    help="degrees of temperature")
parser.add_argument("-f", "--farenheit", action="store_true",
                    help="flag to convert from celsius to farenheit")

if __name__ == "__main__":
    args = parser.parse_args()
    temperature = args.temperature

    
    if args.farenheit:      # Convert to farenheit
        temperature *= 1.8
        temperature += 32
    else:                   # Convert to celsius
        temperature -= 32
        temperature /= 1.8

    print("{:.2f}".format(temperature))