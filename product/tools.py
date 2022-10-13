import os


def load_images(instance: 'product.models.Product', filename: str) -> str:
    """Функция возвращает путь к файлу."""
    path: str = "product_images/"
    file_name: str = f'{instance.product.slug}_{instance.product.id}.{filename.split(".")[-1]}'
    return os.path.join(path, file_name)
