from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework import permissions
from .models import Staff
from .serializers import StaffSerializer

# Create your views here.
class StaffListView(ListAPIView):
    permission_classes = (permissions.AllowAny, )
    queryset = Staff.objects.all()
    serializer_class = StaffSerializer
    pagination_class = None

class StaffView(RetrieveAPIView):
    queryset = Staff.objects.all()
    serializer_class = StaffSerializer

class TopStaffView(RetrieveAPIView):
    permission_classes = (permissions.AllowAny, )
    queryset = Staff.objects.filter(top_staff=True)
    serializer_class = StaffSerializer
    pagination_class = None
