from django.urls import path
from .views import *
# from .

urlpatterns = [
    path("category", CategoryView.as_view()),
    path("single_category/<int:pk>", CategoryView.as_view()),
    path("blogs-details/", BlogView.as_view()),
    path("blogs/<int:pk>", BlogDetailsView.as_view()),
    # path("techsyiq/", TechsyiqTeamView.as_view()),
    # path("techsyiq-details/<int:pk>", TechsyiqTeamDetails.as_view()),
    # path("application/", EnrollmentApplicationView.as_view()),
    # path("enroll_to_techsyiq/", enrollForTechsyicClass, name='application'),
    # path("application-details/<int:pk>", EnrollmentApplicationDetailsView.as_view()),
   
    
]