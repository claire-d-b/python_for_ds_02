from load_csv import load


def main():
    print(load("src/life_expectancy_years.csv"))
    print(load("Wrong path"))


if __name__ == "__main__":
    main()
