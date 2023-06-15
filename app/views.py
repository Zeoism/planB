from typing import Any, Dict
from django.db.models.query import QuerySet
from django.shortcuts import redirect
from django.views.generic import CreateView, DetailView, ListView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Grade, Class, Lesson
from django.shortcuts import render
from django.urls import reverse, reverse_lazy
class LessonCreateView(CreateView):
    model = Lesson
    #form_class = LessonForm
    fields = ['grade', 'class_name', 'course_name', 'teacher', 'teaching_plan']
    template_name = 'upload_lesson.html'

    def get_success_url(self):
         return reverse('lesson_class_view', args=[self.object.grade, self.object.class_name])
        # return reverse('lesson_detail', args=[self.object.id])
    
    def form_valid(self, form):
        form.instance.uploaded_by = self.request.user
        return super().form_valid(form)
        # form.instance.uploaded_by = self.request.user
        # lesson = form.save(commit=False)
        # lesson.uploaded_by = self.request.user
        # lesson.save()
        # self.lesson = lesson
        
        #return redirect('lesson_detail', lesson_id=lesson.id)

class LessonDetailView(DetailView):
    model = Lesson
    template_name = 'lesson_detail.html'
    context_object_name = 'lesson'
    pk_url_kwarg = 'lesson_id'

    # def get_context_data(self, **kwargs):
    #     super_dict = super().get_context_data
    #     super_dict['class_lesson'] = Lesson.objects.filter(lesson_id = self.object.id)
    #     return super_dict
 
class LessonClassView(ListView):
    model = Lesson
    template_name = 'class_lesson.html'

    def get_queryset(self):
        print(f"{self.kwargs['cid']:02d}")
        return Lesson.objects.filter(
            grade__name = self.kwargs['gid'], 
            class_name__name = self.kwargs['cid'], 
        )
    
    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['grade'] = self.kwargs['gid']
        ctx['class'] = self.kwargs['cid']
        return ctx

class HomePageView(ListView):
    model = Lesson
    template_name = 'startpage.html'

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['grade_list'] = [1, 2, 3, 7, 8, 9]
        ctx['class_list'] = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        return ctx

