from rest_framework import viewsets
from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.filters import SearchFilter
from rest_framework.decorators import action
from rest_framework.response import Response
from user.models import User, Team, Profile, Account
from .serializers import UserAdminSerializer
from ...permission import IsAdmin
from ...common.serializers import TeamSerializer, UserDetailSerializer, UserDetailUpdateSerializer, ProfileSerializer, AccountSerializer, AccountUpdateSerializer
from user.constants import ROLE_TEAM_MANAGER, ROLE_DEVELOPER


class UserAdminViewSet(viewsets.ModelViewSet):
    # serializer_class = UserAdminSerializer
    permission_classes = [IsAdmin]
    queryset = User.objects.all()
    filter_backends = [SearchFilter]
    search_fields = ['@username', '^first_name', '@last_name']
    
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

    @action(detail=False, permission_classes=[IsAdmin], url_path='unassigned-users')
    def unassigned_users(self, request, *args, **kwargs):
        SerializerClass = UserAdminSerializer
        serializer = SerializerClass(
            User.objects.filter(role__in=[ROLE_DEVELOPER, ROLE_TEAM_MANAGER], team__isnull=True), 
            many=True
        )
        return Response(serializer.data)


class ProfileListAdminView(ListAPIView):
    serializer_class = ProfileSerializer
    permission_classes = [IsAdmin]
    
    def get_queryset(self):
        return Profile.objects.filter(user_id=self.kwargs['pk'])


class ProfilesAdminViewSet(viewsets.ModelViewSet):
    serializer_class = ProfileSerializer
    queryset = Profile.objects.all()
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        if user.is_admin:
            return Profile.objects.all()
        elif user.is_developer:
            return Profile.objects.filter(user=user)
        elif user.is_team_manager:
            return Profile.objects.filter(user__in=user.team_members)


class AccountListByProfileIdView(ListAPIView):
    serializer_class = AccountSerializer
    permission_classes = [IsAdmin]

    def get_queryset(self):
        return Account.objects.filter(profile_id=self.kwargs['pk'])


class AccountsAdminViewSet(viewsets.ModelViewSet):
    serializer_class = AccountSerializer
    queryset = Account.objects.all()
    permission_classes = [IsAuthenticated]

    def get_serializer_class(self):
        if self.request.method == 'PUT' or self.request.method == 'POST':
            return AccountUpdateSerializer
        else:
            return AccountSerializer
    
    def get_queryset(self):
        user = self.request.user
        if user.is_admin:
            return Account.objects.all()
        elif user.is_developer:
            return Account.objects.filter(profile__user=user)
        elif user.is_team_manager:
            return Account.objects.filter(profile__user__in=user.team_members)


class TeamUserListView(ListAPIView):
    serializer_class = UserAdminSerializer
    permission_classes = [IsAdmin]

    def get_queryset(self):
        return User.objects.filter(team=self.kwargs['pk'])
