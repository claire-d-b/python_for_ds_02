from pandas import DataFrame, read_csv

def load(path: str) -> DataFrame:

    num_rows, num_cols = 0, 0

    try:
        # Open the file in read mode
        # assert read_csv('src/life_expectancy_years.csv', encoding='utf-8-sig'), "Unable to open file"
        assert not read_csv(path, encoding='utf-8-sig').empty, "Unable to open file"

        frame = read_csv(path, encoding='utf-8-sig')
        
        print(type(frame))
        print(frame)
        # with open('src/life_expectancy_years.csv', 'r') as frame:
        nlist = []

        # Read the first line (header)
        # nlist.append(frame.readline().strip().split(','))
        # nlist.append(frame.head())
        # j = len(nlist[0])

        # i = 0
        # # for line in frame:
        # #     nlist.append(line.strip().split(','))column_values = df['France']
        # #     i += 1
        
        # nlist.append(frame['France'])
        # df = DataFrame(nlist)

        # num_rows = i+1
        # num_cols = j

        # size = (num_rows, num_cols)

        # print("Loading dataset of dimensions ", size)

    except AssertionError as e:
        print(f"AssertionError: {e}")

    return frame