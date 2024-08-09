from django.urls import path
from .views import UploadFileView, SuccessView
from .api_views import QueryCompanyDataView

urlpatterns = [
    path('upload/', UploadFileView.as_view(), name='upload'),
    path('success/', SuccessView.as_view(), name='success'),
    path('api/query/', QueryCompanyDataView.as_view(), name='query_company_data')
    # path('api/query/', QueryCompanyDataView.as_view()
]
