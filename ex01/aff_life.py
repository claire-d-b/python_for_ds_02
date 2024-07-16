from matplotlib.pyplot import figure, plot, title, xlabel, ylabel, legend
from matplotlib.pyplot import show, tight_layout
from pandas import DataFrame
from load_csv import load


def display_graph(df: DataFrame):
    try:
        assert isinstance(df, DataFrame), "Error"
        """ Search for a keyword in the entire DataFrame """
        keyword = "France"
        nlist = df.iloc[0].tolist()
        ret = []

        for item in nlist:
            ret.append(str(item).strip())

        data = df[df.map(lambda x: keyword.lower() in str(x).lower()).any(axis=1)]

        width, height = data.shape

        vlist = []
        klist = []

        row_data = data.iloc[0]

        keys = row_data.index
        klist = keys.tolist()

        for y in range(height):
            for x in range(width):
                vlist.append(data.iloc[x].iloc[y])

        x = klist
        y = vlist

        key = ''
        value = ''

        for item in klist[:1]:
            key = str(item)
        for item in vlist[:1]:
            value = str(item)

        nklist = []
        klist = klist[1:len(klist)]
        for k in klist:
            nklist.append(int(k))
        vlist = vlist[1:len(vlist)]

        figure(figsize=(8, 5))
        plot(nklist, vlist)
        title('Life Expectancy Years')
        xlabel(key)
        ylabel(value)
        legend()
        tight_layout()
        show()
    except AssertionError as e:
        print(f"An unexpected error occurred: {e}")


def main():

    display_graph(load("src/life_expectancy_years.csv"))
    display_graph(load("Wrong path"))


if __name__ == "__main__":
    main()
