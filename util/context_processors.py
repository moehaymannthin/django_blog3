from my_blog.models import CategoryModel

def allCategory(request):
    category = CategoryModel.objects.all()
    return {'categories':category}