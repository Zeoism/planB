from django.shortcuts import render
from django.views.generic import CreateView, DetailView
from app.models import Lesson, LessonFile
from app.forms import LessonForm, LessonFileForm

class LessonCreateView(CreateView):
    model = Lesson
    form_class = LessonForm
    template_name = 'upload_lesson.html'
    success_url = '/'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['file_form'] = LessonFileForm()
        return context

    def form_valid(self, form):
        response = super().form_valid(form)
        lesson = form.instance
        file_form = LessonFileForm(self.request.POST, self.request.FILES)
        if file_form.is_valid():
            file = file_form.save(commit=False)
            file.lesson = lesson
            file.save()
        return response


class LessonDetailView(DetailView):
    model = Lesson
    template_name = 'lesson_detail.html'
    context_object_name = 'lesson'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['files'] = LessonFile.objects.filter(lesson=self.object)
        return context
