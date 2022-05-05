from django.contrib.auth.models import User

from rest_framework.serializers import ModelSerializer, SerializerMethodField

from gpa.models import Account, Transaction


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class AccountSerializer(ModelSerializer):
    account_number = SerializerMethodField()

    class Meta:
        model = Account
        fields = '__all__'

    def get_account_number(self, instance):
        return instance.account_number()


class TransactionSerializer(ModelSerializer):
    class Meta:
        model = Transaction
        fields = '__all__'
