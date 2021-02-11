from rest_framework import viewsets
from rest_framework.generics import ListAPIView

from user.models import User, Team, Profile, Account
from .serializers import UserAdminSerializer
from ...permission import IsAdmin
from ...common.serializers import TeamSerializer, UserDetailSerializer, UserDetailUpdateSerializer, ProfileSerializer, AccountSerializer


class UserAdminViewSet(viewsets.ModelViewSet):
    # serializer_class = UserAdminSerializer
    permission_classes = [IsAdmin]
    queryset = User.objects.all()

    def get_serializer_class(self):
        if self.action == 'list':
            return UserAdminSerializer
        elif self.request.method == 'PUT' or self.request.method == 'POST':
            return UserDetailUpdateSerializer
        else:
            return UserDetailSerializer


class TeamListViewSet(viewsets.ModelViewSet):
    serializer_class = TeamSerializer
    permission_classes = [IsAdmin]
    queryset = Team.objects.all()


class ProfileListAdminView(ListAPIView):
    serializer_class = ProfileSerializer
    permission_classes = [IsAdmin]
    
    def get_queryset(self):
        return Profile.objects.filter(user_id=self.kwargs['pk'])

class ProfilesAdminViewSet(viewsets.ModelViewSet):
    serializer_class = ProfileSerializer
    permission_classes = [IsAdmin]
    queryset = Profile.objects.all()


class AccountListByProfileIdView(ListAPIView):
    serializer_class = AccountSerializer
    permission_classes = [IsAdmin]

    def get_queryset(self):
        return Account.objects.filter(profile_id=self.kwargs['pk'])

class AccountsAdminViewSet(viewsets.ModelViewSet):
    serializer_class = AccountSerializer
    permission_classes = [IsAdmin]
    queryset = Account.objects.all()

class TeamUserListView(ListAPIView):
    serializer_class = UserAdminSerializer
    permission_classes = [IsAdmin]

    def get_queryset(self):
        return User.objects.filter(team=self.kwargs['pk'])