# @author: ww
import os
import pickle

import yaml


def read_yaml(yaml_file):
    """
    Read yaml file
    :param yaml_file:
    :return:

    >>> read_yaml('test_resource/test_read.yml')
    {'date': datetime.date(2019, 11, 6), 'pkg': {'python': {'version': '3.6.8', 'date': '{{ date }}'}, 'django': {'version': "{% if pkg.python.version|first == '2' %}1.8{% else %}2.2.6{% endif %}"}}}
    """
    with open(yaml_file) as f:
        data_str = f.read()
        data = yaml.safe_load(data_str)

    return data


def write_yaml(yaml_file, data):
    """
    Write yaml file
    :param yaml_file:
    :param data:
    :return:

    >>> import datetime
    >>> data = {'date': datetime.date(2019, 11, 6), 'pkg': {'python': {'version': '3.6.8', 'date': '{{ date }}'}, 'django': {'version': "{% if pkg.python.version|first == '2' %}1.8{% else %}2.2.6{% endif %}"}}}
    >>> write_yaml('test_resource/test_write.yaml', data)
    """
    with open(yaml_file, 'w') as f:
        yaml.dump(data, f)


def makedirs(path, verbose=True, stdout=print):
    """
    A wrap function for os.makedirs
    :param path:
    :param verbose: show message
    :param stdout:
    :return:

    >>> makedirs('build', True)
    make dir: build
    >>> makedirs('build', True)
    """
    if not os.path.exists(path):
        os.makedirs(path)
        if verbose:
            stdout(f'make dirs: {path}')


def read_pickle(pkl_path):
    with open(pkl_path, 'rb') as f:
        return pickle.load(f)


def save_pickle(data, pkl_path):
    os.system('mkdir -p {}'.format(os.path.dirname(pkl_path)))
    with open(pkl_path, 'wb') as f:
        pickle.dump(data, f)


if __name__ == '__main__':
    import doctest
    doctest.testmod()
    # print(read_yaml('test_resource/test_read.yml'))
    # makedirs('a')

