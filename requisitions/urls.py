# requisitions/urls.py

from django.urls import path
from .views import requisition_detail

app_name = 'requisitions'

urlpatterns = [
    path('<int:requisition_id>/', requisition_detail, name='requisition_detail'),
    # Add more URLs as needed
]
