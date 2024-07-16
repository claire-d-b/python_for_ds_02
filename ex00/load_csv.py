from pandas import DataFrame


def load(path: str) -> DataFrame:
    num_rows, num_cols = 0, 0
    try:
        with open(path, 'r') as file:
            nlist = []

            """ Read the first line (header) """
            nlist.append(file.readline().strip().lstrip('\ufeff').split(','))
            j = len(nlist[0])
            i = 0
            for line in file:
                nlist.append(line.strip().split(','))
                i += 1

            df = DataFrame(nlist)

            num_rows = i
            num_cols = j

            size = (num_rows, num_cols)
            print("Loading dataset of dimensions ", size)

            return df

    except FileNotFoundError:
        print("File not found")
    except IOError:
        print("An IOError occurred")

    return None
