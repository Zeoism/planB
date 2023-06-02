from django.shortcuts import render, redirect
from .models import Grade, Class, Lesson
from .forms import LessonForm

def upload_lesson(request):
    if request.method == 'POST':
        form = LessonForm(request.POST)
        if form.is_valid():
            lesson = form.save(commit=False)
            lesson.uploaded_by = request.user
            lesson.save()
            return redirect('lesson_detail', lesson_id=lesson.id)
    else:
        form = LessonForm()
    
    return render(request, 'upload_lesson.html', {'form': form})


def lesson_detail(request, lesson_id):
    lesson = Lesson.objects.get(id=lesson_id)
    return render(request, 'lesson_detail.html', {'lesson': lesson})
