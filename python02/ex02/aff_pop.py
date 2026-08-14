import matplotlib.pyplot as plt
from load_csv import load


def convert_population(value: str) -> float:
    """Convert an abbreviated population string to a numeric value."""
    multipliers = {
        "k": 1_000,
        "M": 1_000_000,
        "B": 1_000_000_000
    }

    suffix = value[-1]

    if suffix in multipliers:
        number = float(value[:-1])
        return number * multipliers[suffix]

    return float(value)


def main():
    """Display France and Belgium population projections from 1800 to 2050."""
    dataset = load("population_total.csv")
    if dataset is None:
        print("load failed")
        return
    countries = dataset.loc[dataset["country"].isin(["France", "Belgium"])]
    data = countries.loc[:, "country":"2050"].set_index("country")
    france = data.loc["France", "1800":]
    belgium = data.loc["Belgium", "1800":]
    fr_values = france.map(convert_population)
    bel_values = belgium.map(convert_population)

    years = data.columns.astype(int)
    plt.plot(years, fr_values, label="France")
    plt.plot(years, bel_values, label="Belgium")
    plt.xticks(range(1800, 2051, 40))
    plt.yticks(
        [20_000_000, 40_000_000, 60_000_000],
        ["20M", "40M", "60M"]
    )
    plt.title("Population Projections")
    plt.xlabel("Year")
    plt.ylabel("Population")
    plt.legend(loc="lower right")
    plt.show()


if __name__ == "__main__":
    main()
