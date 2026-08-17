import matplotlib.pyplot as plt
from load_csv import load


def main():
    """Display life expectancy vs GDP per capita for the year 1900."""
    life_expectancy = load("life_expectancy_years.csv")
    inflation = load(
        "income_per_person_gdppercapita_ppp_inflation_adjusted.csv"
    )
    if life_expectancy is None or inflation is None:
        return

    life_expectancy_year = life_expectancy.loc[:, "1900"]
    inflation_year = inflation.loc[:, "1900"]

    plt.scatter(inflation_year, life_expectancy_year)
    plt.xscale("log")
    plt.xticks([300, 1_000, 10_000], ["300", "1k", "10k"])
    plt.title("1900")
    plt.ylabel("Life Expectancy")
    plt.xlabel("Gross domestic product")
    plt.show()


if __name__ == "__main__":
    main()
