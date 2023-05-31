from utils import find_file


def test_find_file_no_ex(tmp_path):
    dir_name = 'test-dir'
    filename = 'test'

    file = tmp_path / f'{dir_name}/test.txt'
    file.parent.mkdir()
    file.touch()

    result = find_file(tmp_path, filename)
    assert result[0][0] == 'test.txt'
    assert result[0][1] == str(tmp_path / dir_name)


def test_find_multiple_files_no_ex(tmp_path):
    dir_name = 'test-dir'
    filename = 'test'

    extensions = ['.py', '.txt', '.jpg', '.theme', '.txt']
    for num, extension in enumerate(extensions, start=1):
        file = tmp_path / f'{dir_name + str(num)}/{filename + extension}'
        file.parent.mkdir()
        file.touch()

    result = find_file(tmp_path, filename)
    filenames = [file[0] for file in result]
    assert len(result) == 5
    assert filenames.count('test.txt') == 2
    assert filenames.count('test.py') == 1


def test_find_file_with_ex(tmp_path):
    dir_name = 'test-dir'
    filename = 'test.txt'

    file = tmp_path / f'{dir_name}/test.txt'
    file.parent.mkdir()
    file.touch()

    result = find_file(tmp_path, filename)
    assert result[0][0] == 'test.txt'
    assert result[0][1] == str(tmp_path / dir_name)
