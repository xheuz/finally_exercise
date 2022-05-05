from datetime import datetime

from django.contrib.auth.models import User
from django.db.models import Sum

from rest_framework import status
from rest_framework.decorators import action
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response

from gpa.models import Account, Transaction
from gpa.serializers import AccountSerializer, TransactionSerializer, UserSerializer


class AccountViewSet(ModelViewSet):
    serializer_class = AccountSerializer
    perimssion_classes = [IsAuthenticated]

    def get_queryset(self):
        if self.request.user.is_authenticated:
            return Account.objects.filter(user_id=self.request.user)

    def get_permmissions(self):
        if self.action in ["list", "retrieve"]:
            return [IsAuthenticated()]
        return [IsAdminUser()]

    @action(detail=True, url_path="date/(?P<date>[^/.]+)", methods=["GET"])
    def date(self, request, pk, date):
        if not request.user.is_authenticated:
            return Response(status=status.HTTP_401_UNAUTHORIZED)

        try:
            _date = datetime.strptime(date, "%Y%m%d")
            account = Account.objects.get(pk=pk)
            total_amount = account.transactions.filter(date__gte=_date).aggregate(Sum('amount'))['amount__sum']
            previous_balance = account.current_balance + total_amount

            res = AccountSerializer(account).data
            res['current_balance'] = previous_balance
            return Response(res)
        except Account.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        except Exception:
            return Response(status=status.HTTP_400_BAD_REQUEST)


class TransactionViewSet(ModelViewSet):
    serializer_class = TransactionSerializer
    perimssion_classes = [IsAuthenticated]

    def get_queryset(self):
        if self.request.user.is_authenticated:
            return Transaction.objects.filter(user_id=self.request.user)


class UserViewSet(ModelViewSet):
    serializer_class = UserSerializer
    permmission_classes = [IsAdminUser]
    queryset = User.objects.all()
