import os


def load_rel_path(
        directory,
        filename,
        suffix
):
    file_path = os.path.relpath(
        f'../{directory}/{filename}.{suffix}'
    )
    return file_path