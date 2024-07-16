from pandas import DataFrame, read_csv


def load(path: str) -> DataFrame:
    try:
        frame = read_csv(path, encoding='utf-8-sig')

        print(type(frame))
        print(frame)
        return frame

    except FileNotFoundError:
        """ This is raised when the specified file does not exist. """
        print(f"File does not exist")

    except EmptyDataError:
        """ This is raised when the file is empty. """
        print(f"Empty file")

    except ParserError:
        """ This is raised when there is a problem parsing the data
        (e.g., malformed CSV). """
        print(f"There was a problem parsing the file")

    except UnicodeDecodeError:
        """ This is raised when there is an issue with the file's encoding. """
        print(f"There was an issue with the file encoding")
    return None

