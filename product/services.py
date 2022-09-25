from .models import Product
from .forms import AddReviewForm


class ProductService:

    @staticmethod
    def current_user_has_review(user_id, product_id):
        reviews = Product.objects.get(id=product_id).reviews.all()
        curr_usr_review = reviews.filter(user_id=user_id).exists()
        if curr_usr_review:
            return True
        else:
            return False

    @staticmethod
    def review_form_save(instance, request):
        if not ProductService.current_user_has_review(instance.request.user, instance.kwargs['pk']):
            review_form = AddReviewForm(request.POST)
            if review_form.is_valid():
                review = review_form.save(commit=False)
                review.product = instance.object
                review.user = request.user
                review.save()
