from pandas import DataFrame, read_csv


def load(path: str) -> DataFrame:
    try:
        assert not read_csv(path, encoding='utf-8-sig').empty, "Unable \
        to open file"

        frame = read_csv(path, encoding='utf-8-sig')

        print(type(frame))
        print(frame)

    except AssertionError as e:
        print(f"AssertionError: {e}")

    return frame
