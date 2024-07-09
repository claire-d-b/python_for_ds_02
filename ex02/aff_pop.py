from matplotlib.pyplot import figure, plot, grid, xticks, yticks, title, xlabel, ylabel, legend, show, tight_layout
from pandas import DataFrame
from load_csv import load

def convert_to_int(value):
    """
    Convert a string with a suffix like 'M' (million) or 'K' (thousand) to an integer.
    """
    if not value:
        return 0
    if isinstance(value, int):
        return value
    
    value = value.strip().upper()
    if value.endswith('M'):
        return int(float(value[:-1]) * 1_000_000)
    elif value.endswith('K'):
        return int(float(value[:-1]) * 1_000)
    elif value.endswith('B'):
        return int(float(value[:-1]) * 1_000_000_000)
    else:
        return int(value)


def get_line(df: DataFrame, keyword: str):

    # Search for a keyword in the entire DataFrame
    nlist = df.iloc[0].tolist()
    ret = []
    i = 0
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

    # key = ''
    # value = ''

    # for item in klist[:1]:
    #     key = str(item)
    # for item in vlist[:1]:
    #     value = str(item)

    # key = klist[:1]
    # value = vlist[:1]
    
    # print(key)
    # print(value)

    nklist = []
    klist = klist[1:len(klist)]
    for k in klist:
        nklist.append(int(k))

    nvlist = []
    vlist = vlist[1:len(vlist)]
    for v in vlist:
        nvlist.append(convert_to_int(v))

    print(nklist)
    print(nvlist)

    return (nklist, nvlist)

def display_graph(x1: list, y1: list, x2: list, y2: list) -> None:
    figure(figsize=(8, 5))
    plot(x1, y1)
    plot(x2, y2)
    title('Population Total')
    xlabel('Year')
    ylabel('Population')
    min1, mid1, max1 = min(y1), (min(y1) + max(y1)) / 2, max(y1)
    min2, mid2, max2 = min(y2), (min(y2) + max(y2)) / 2, max(y2)
    nmin, nmid, nmax = (min1 + min2) / 2, (mid1 + mid2) / 2, (max1 + max2) / 2, 
    
    yticks([20000000, 40000000, 60000000], ['20M', '40M', '60M'])
    legend()
    tight_layout()
    show()


def main():

    x1, y1 = get_line(load("src/population_total.csv"), "France")
    x2, y2 = get_line(load("src/population_total.csv"), "Belgium")
    display_graph(x1, y1, x2, y2)

if __name__ == "__main__":
    main()
