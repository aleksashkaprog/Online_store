from .models import Category


class CategoryService:

    @staticmethod
    def get_categories():
        categories = Category.objects.all()
        return categories
