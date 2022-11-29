
from django.urls import path,register_converter,include
from django.conf import settings
from django.conf.urls.static import static
from . import views

from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

from django.urls import path
from .views import PatientRegistrationView, DoctorRegistrationView
app_name = 'Counsellingapp'



schema_view = get_schema_view(
   openapi.Info(
      title="Counselling API",
      default_version='v1',
      description="A restful api for counselling",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="josephkamore084@gmail.com"),
      license=openapi.License(name="MIT"),
   ),
   public=True,
   permission_classes=[permissions.AllowAny],
)


urlpatterns = [

    # swagger ui
    path('', schema_view.with_ui('swagger', cache_timeout=0),
         name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc',
         cache_timeout=0), name='schema-redoc'),
    
    path('api/counselor/',views.CounselorList.as_view()),#list
    path('api/counselor/<int:pk>/',views.CounselorDetail.as_view()),#detail
    path('api/client/',views.ClientList.as_view()),#list
    path('api/client/<int:pk>/',views.ClientDetail.as_view()),
    path('api/supportgroup/',views.SupportGroupList.as_view()),
    path('api/supportgroup/<int:pk>/',views.SupportGroupDetail.as_view()),
    path('api/session/',views.SessionList.as_view()),
    path('api/session/<int:pk>/',views.SessionDetail.as_view()),
    path('api/medication/',views.MedicationList.as_view()),
    path('api/medication/<int:pk>/',views.MedicationDetail.as_view()),
    path('api/medicationdosage/',views.MedicationDosageList.as_view()),
    path('api/medicationdosage/<int:pk>/',views.MedicationDosageDetail.as_view()),
    #Registration Urls
    path('registration/patient/', PatientRegistrationView.as_view(), name='register-patient'),
    path('registration/doctor/', DoctorRegistrationView.as_view(), name='register-doctor'),
   
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

