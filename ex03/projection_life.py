from matplotlib.pyplot import figure, plot, grid, xticks, yticks, title, xlabel, ylabel, legend, show, tight_layout, scatter, subplots
from pandas import DataFrame
from load_csv import load

def get_values(df: DataFrame, keyword: str):

    # Search for a keyword in the entire DataFrame
    nlist = df.iloc[0].tolist()
    ret = []
    i = 0
    for item in nlist:
        ret.append(str(item).strip())
    
    # data = df[df.map(lambda x: keyword.lower() in str(x).lower()).any(axis=1)]

    # width, height = data.shape

    vlist = []
    klist = []

    row_data = df[keyword]
    print("raw data", row_data)
    height, width = row_data.shape[0], 1
    print("shape", row_data.shape)

    keys = row_data.index
    klist = keys.tolist()

    data = row_data

    for d in data:
        vlist.append(d)
    
    # print("VLISTTTTT", vlist)
    
    # x = klist
    # y = vlist

    # nklist = []
    # klist = klist[1:len(klist)]
    # for k in klist:
    #     nklist.append(int(k))

    # nvlist = []
    # vlist = vlist[1:len(vlist)]
    # for v in vlist:
    #     nvlist.append(convert_to_int(v))

    # print(nklist)
    # print(nvlist)

    return (vlist)


def display_points(frame_x: DataFrame, frame_y: DataFrame) -> None:

    list_x = get_values(frame_x, '1900')
    list_y = get_values(frame_y, '1900')

    # Custom positions and labels for the x-axis
    x_positions = [300, 1000, 10000]
    x_labels = ['300', '1k', '10k']

    fig, ax = subplots()
    ax.scatter(list_y, list_x)

    # Set the x-axis to logarithmic scale
    ax.set_xscale('log')

    # Set custom ticks and labels for the x-axis
    ax.set_xticks(x_positions)
    ax.set_xticklabels(x_labels)

    # x_labels = ['300', '1k', '10k']
    # # Set custom labels for the x-axis
    # ax.set_xticklabels(x_labels)
    # ax.set_xticks([0, 1000, 10000])

    # Customize the plot
    ax.set_title("1900")
    ax.set_xlabel("Gross Domestic product")
    ax.set_ylabel("Life Expectancy")

    # Display the plot
    legend()
    tight_layout()
    show()

def main():

    frame_x = load("src/life_expectancy_years.csv")
    frame_y = load("src/income_per_person_gdppercapita_ppp_inflation_adjusted.csv")
    display_points(frame_x, frame_y)

if __name__ == "__main__":
    main()