import argparse

parser = argparse.ArgumentParser(description="Convert hourly wage to annual salary.")

parser.add_argument("rate", metavar="RATE", type=int,
                    help="hourly rate for wage")
parser.add_argument("-wk", "--weeks", type=int, default=52,
                    help="number of weeks worked in a year, default 52")
parser.add_argument("-hr", "--hours", type=int, default=40,
                    help="number of hours worked per week, default 40")

if __name__ == "__main__":
    args = parser.parse_args()
    print(args.rate * args.weeks * args.hours)