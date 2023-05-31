from utils import find_file


def test_find_file_no_ex(tmp_path):
    dir_name = 'test-dir'
    filename = 'test'

    file = tmp_path / f"{dir_name}/test.txt"
    file.parent.mkdir()
    file.touch()

    result = find_file(tmp_path, filename)
    assert result[0][0] == 'test.txt'
    assert result[0][1] == str(tmp_path / dir_name)
