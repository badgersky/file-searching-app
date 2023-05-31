import pytest


@pytest.fixture
def m_files(tmp_path):
    dir_name = 'test-dir'
    filename = 'test'

    extensions = ['.py', '.txt', '.jpg', '.theme', '.txt']
    for num, extension in enumerate(extensions, start=1):
        file = tmp_path / f'{dir_name + str(num)}/{filename + extension}'
        file.parent.mkdir()
        file.touch()


@pytest.fixture
def s_file(tmp_path):
    dir_name = 'test-dir'

    file = tmp_path / f'{dir_name}/test.txt'
    file.parent.mkdir()
    file.touch()
