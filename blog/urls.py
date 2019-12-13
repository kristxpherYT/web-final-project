from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from . import views

urlpatterns = [
                  path("", views.index, name="index"),
                  path("projects", views.projects, name="projects"),
                  path("studies", views.studies, name="studies"),
                  path("hobbies", views.hobbies, name="hobbies"),
                  path("store_project", views.store_project, name="store_project"),
                  path("remove_project", views.remove_project, name="remove_project"),
                  path("store_hobby", views.store_hobby, name="store_hobby")
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
