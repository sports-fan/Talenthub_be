from rest_framework.filters import SearchFilter
from rest_framework.generics import ListAPIView
from .serializers import SearchUserSerializer
from user.models import User


class SearchUserView(ListAPIView):
    """
    search User by username, first_name, last_name field start with given keyword
    """
    queryset = User.objects.all()
    serializer_class = SearchUserSerializer
    filter_backends = [SearchFilter]
    search_fields = ['username', 'first_name', 'last_name']
