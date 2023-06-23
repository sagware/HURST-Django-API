from rest_framework import status, generics
from rest_framework.response import Response
from .serializers import ReportSerializer
from .models import Report


class ReportAPI(generics.GenericAPIView):
    serializer_class=ReportSerializer
    def post(self,request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        createdreport = Report(
            longitude=serializer.data["longitude"],
            latitude=serializer.data["latitude"],
            time=serializer.data["time"],
            incident=serializer.data["incident"],
            sy=serializer.data["sy"]

        )
        createdreport.save()
        return Response(ReportSerializer(createdreport).data,status=status.HTTP_201_CREATED)