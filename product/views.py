from django.shortcuts import render, HttpResponse

# Create your views here.

def homepage(request):
    html = Vegetables.objects.all()
    context = {'all_vegetables": html}
    return render(request, "product_list.html")


def cucumber(request):
    cucumber_object = Vegetables.object.get(id=1)
    description = cucumber_object.description
    return HttpResponse(description)

