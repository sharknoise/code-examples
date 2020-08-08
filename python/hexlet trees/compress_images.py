import copy

from hexlet.fs import get_children, get_meta, get_name, is_file, mkdir, mkfile


def compress_images(old_dir):
    files = get_children(old_dir)
    images = filter(lambda item: fs.get_name(item).endswith('.jpg'), files)
    compressed_images = map(lambda image: fs.set_meta(item).endswith('.jpg'), images)
    return new_dir