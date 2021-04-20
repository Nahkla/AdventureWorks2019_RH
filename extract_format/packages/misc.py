import os

from extract_format import definitions


def load_rel_path(
        directory,
        filename,
        suffix
        # generate path string while directory, filename and suffix has to be handed manually // for now
):
    file_path = os.path.relpath(
        f'./{directory}/{filename}.{suffix}',
        start=definitions.root_dir())  # file path variable is generated via relpath and f string
    # .active directory is necessary to reach ~/extract_format/files

    return file_path


# returns file_path variable

def load_db_essentials():

    from os import listdir
    from os.path import isfile, join

    yml_directory = 'essentials'
    yml_path = os.path.relpath(f'./{yml_directory}')
    yml_filenames = [
        f for f in listdir(yml_path) if isfile(
            join(yml_path, f)
        )
    ]
    import yaml

    db_ls, driver_ls, user_ls = [
        yaml.load(
            open(os.path.relpath(f'./{yml_directory}/{essential}'), 'r'),
        Loader = yaml.FullLoader) for essential in yml_filenames
             ]

    print('connection details imported',*yml_filenames, sep='\n')

    return {
        'db_ls' : db_ls,
        'driver_ls' : driver_ls,
        'user_ls' : user_ls
    }
