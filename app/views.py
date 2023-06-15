from django.shortcuts import redirect
from django.views.generic import CreateView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Grade, Class, Lesson
from django.shortcuts import render
from django.urls import reverse
class LessonCreateView(CreateView):
    model = Lesson
    #form_class = LessonForm
    fields = ['grade', 'class_name', 'course_name', 'teacher', 'teaching_plan']
    template_name = 'upload_lesson.html'

    def get_success_url(self):
         return reverse('lesson_detail', args=[self.object.id])
    
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
 