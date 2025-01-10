# urls.py
from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings



urlpatterns = [
    path('directions/', views.crud_view_directions, name='crud_view_directions'),
    path('modifier/<int:id>/', views.modifier_direction, name='modifier_direction'),
    path('supprimer/<int:id>/', views.supprimer_direction, name='supprimer_direction'),


   
    path('poles/', views.pole_crud_view, name='pole_crud_view'),
    path('poles/<int:id>/', views.pole_crud_view, name='pole_crud_view'),

    path('sites/', views.site_crud_view, name='site_crud_view'),
    path('sites/<int:id>/', views.site_crud_view, name='site_crud_view'),

   
    path('sousdirections/', views.sousdirection_crud_view, name='sousdirection_crud_view'),
    path('sousdirections/<int:id>/', views.sousdirection_crud_view, name='sousdirection_crud_view'),
   
    path("login/", views.login_view, name="login"),
    path("", views.login_view, name="home"),  # Exemple de redirection après connexion réussie
    path('acceuil/', views.acceuil_view, name='acceuil'),  # Vue pour la page d'accueil
   
    path('upload/', views.upload_file, name='upload_file'),

    path('extract_all/', views.extract_data_from_all_files, name='extract_data_from_all_files'),
    path('generer/', views.generate_astreinte_and_download, name='generer_astreinte'),

]

from django.conf import settings
from django.conf.urls.static import static

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

   







   
    
