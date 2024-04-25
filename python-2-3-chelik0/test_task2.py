import pytest
import task2 as t


@pytest.fixture
def mock_csv_data():
    return [
        "Day,MxT,MnT,AvT,AvDP,1HrP TPcn,PDir,AvSp,Dir,MxS,SkyC,MxR,Mn,R AvSLP",
        "1,88,59,74,53.8,0,280,9.6,270,17,1.6,93,23,1004.5",
        "2,79,63,71,46.5,0,330,8.7,340,23,3.3,70,28,1004.5",
    ]


@pytest.fixture
def mock_csv_file(tmp_path, mock_csv_data):
    datafile = tmp_path / "weather.csv"
    datafile.write_text("\n".join(mock_csv_data))
    return str(datafile)


def test_no_lines():
    no_data = []
    for _ in t.get_next_day_and_avg(no_data):
        assert False


def test_trailing_blank_lines(mock_csv_data):
    mock_csv_data.append("")
    all_lines = [x for x in t.get_next_day_and_avg(mock_csv_data)]
    assert len(all_lines) == 2
    for line in all_lines:
        assert len(line) == 2


def test_mid_blank_lines(mock_csv_data):
    mock_csv_data.insert(1, "")
    all_lines = [x for x in t.get_next_day_and_avg(mock_csv_data)]
    assert len(all_lines) == 2
    for line in all_lines:
        assert len(line) == 2


def test_get_max_avg(mock_csv_file):
    assert t.get_max_avg(mock_csv_file) == (1, 73.5)


def test_get_next_day_and_avg(mock_csv_data):
    reader = t.get_next_day_and_avg(mock_csv_data)
    assert next(reader) == (1, 73.5)
    assert next(reader) == (2, 71)
    with pytest.raises(StopIteration):
        next(reader)
