from django.http import JsonResponse
from mysite.models import (
    Page
)


def page_title(request):
    page = Page()
    page.title = "Title test"
    page.contents = "Contents test"

    print(dir(request.POST.values))

    return JsonResponse(page.to_dict())
