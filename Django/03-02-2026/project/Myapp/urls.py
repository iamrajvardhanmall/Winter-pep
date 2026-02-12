from .views import RajTemplateView, RajView, saveDetails, base
from django.urls import path

urlpatterns = [
    path('', RajView),
    path('raj/', RajTemplateView),
    path('save/', saveDetails, name='save_data'),
    # path('base/', base),
]
