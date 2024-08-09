from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import CompanyData
from .serializers import CompanyDataSerializer

class QueryCompanyDataView(APIView):
    def get(self, request):
        
        filters = request.query_params
        data = CompanyData.objects.filter(**filters)
        serializer = CompanyDataSerializer(data, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)
