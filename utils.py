import os


def find_file(path, filename, extension=None):
    if not extension:
        result = []
        for paths, dirs, files in os.walk(path):
            file_no_ex = [os.path.splitext(file)[0] for file in files]

            if filename in file_no_ex:
                result.append((files[file_no_ex.index(filename)], paths))
    else:
        filename = filename + '.' + extension
        result = [(files[files.index(filename)], paths) for paths, dirs, files in os.walk(path) if filename in files]

    if not result:
        return f'No such file: {filename}'
    return result


if __name__ == '__main__':
    print('-' * 40)
    print(find_file(os.environ.get('HOME'), 'empire_invaders'))
    print('-' * 40)
    print(find_file(os.environ.get('HOME'), 'empire_invaders', 'py'))
    print('-' * 40)
    print(find_file(os.environ.get('HOME'), 'test'))
    print('-' * 40)
    print(find_file(os.environ.get('HOME'), 'test', 'txt'))
