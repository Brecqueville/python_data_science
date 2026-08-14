from load_csv import load
import matplotlib.pyplot as plt


def main():
    """Display France's life expectancy over time."""
    dataset = load("life_expectancy_years.csv")
    if dataset is None:
        print("Load failed")
        return
    france = dataset[dataset["country"] == "France"]
    years = dataset.columns[1:].astype(int)
    fr_values = france.iloc[0, 1:]

    print(fr_values.shape)
    print(years.shape)

    plt.plot(years, fr_values)
    plt.xticks(range(1800, 2081, 40))
    plt.title("France Life expectancy Projections")
    plt.xlabel("Year")
    plt.ylabel("Life expectancy")
    plt.show()


if __name__ == "__main__":
    main()
