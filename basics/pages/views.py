from django.shortcuts import render
from django.views import View
from .forms import PageForm
from .models import Page
from django.http import HttpResponseRedirect


class PageView(View):

    template = "pages_home.html"

    def get(self, request):
        all_pages = Page.objects.all()
        return render(request, self.template, {'page': all_pages})


class AddPageView(View):

    form_class = PageForm
    template = "shared/staff_home.html"

    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template, {'form': form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            edited_page = form.save(commit=False)
            try:
                page = Page.objects.get(title=form.cleaned_data['title'])
                edited_page.page = page
            except Exception as e:
                print(e)
                pass
            edited_page.save()
            return HttpResponseRedirect('/')
        return render(request, self.template, {'form': form})
