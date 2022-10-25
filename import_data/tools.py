from config.celery import app

import importlib


@app.task
def import_data_to_db(data):
    module = importlib.import_module('product.models')
    module_class = getattr(module, 'Product')
    print(dir(module_class.objects))
    product = module_class(**data)
    product.save()
    print(product)
    return None
