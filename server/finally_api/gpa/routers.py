from rest_framework.routers import SimpleRouter

from gpa import viewsets

router = SimpleRouter()
router.register(r'accounts', viewsets.AccountViewSet, basename="accounts")
router.register(r'transactions', viewsets.TransactionViewSet, basename="transactions")
router.register(r'users', viewsets.UserViewSet, basename="users")
