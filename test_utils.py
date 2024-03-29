import os

from utils import find_file, format_result


def test_find_file_no_ex(tmp_path, s_file):
    dir_name = 'test-dir'
    filename = 'test'
    result = find_file(tmp_path, filename)
    assert result[0][0] == 'test.txt'
    assert result[0][1] == str(tmp_path / dir_name)


def test_find_multiple_files_no_ex(tmp_path, m_files):
    filename = 'test'

    result = find_file(tmp_path, filename)
    filenames = [file[0] for file in result]
    assert len(result) == 5
    assert filenames.count('test.txt') == 2
    assert filenames.count('test.py') == 1


def test_find_file_with_ex(tmp_path, s_file):
    dir_name = 'test-dir'
    filename = 'test.txt'

    result = find_file(tmp_path, filename)
    assert result[0][0] == 'test.txt'
    assert result[0][1] == str(tmp_path / dir_name)


def test_find_multiple_files_with_ex(tmp_path, m_files):
    filename = 'test'

    result = find_file(tmp_path, filename + '.txt')
    filenames = [file[0] for file in result]
    assert len(result) == 2
    assert filenames.count('test.txt') == 2


def test_find_file_if_file_dont_exist(tmp_path, m_files):
    filename = 'no_exist'

    result = find_file(tmp_path, filename)
    assert result is False


def test_format_result(tmp_path, s_file):
    filename = 'test'
    dir_name = 'test-dir'
    full_path = os.path.join(tmp_path, dir_name)

    result = format_result(find_file(tmp_path, filename))
    assert f'path: {full_path}' in result
    assert f'filename: {filename}' in result


def test_format_result_file_dont_exits(tmp_path):
    filename = 'no_exist'

    result = format_result(find_file(tmp_path, filename))
    assert result == 'No such file'
    