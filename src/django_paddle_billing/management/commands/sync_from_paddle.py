from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = "Sync data from Paddle"

    def add_arguments(self, parser):
        parser.add_argument('-a', '--all', action='store_true', help='sync all models')
        parser.add_argument('-ad', '--address', action='store_true', help='sync address')
        parser.add_argument('-b', '--business', action='store_true', help='sync business')
        parser.add_argument('-po', '--product', action='store_true', help='sync product')
        parser.add_argument('-pi', '--price', action='store_true', help='sync price')
        parser.add_argument('-s', '--subscription', action='store_true', help='sync subscriptions')
        parser.add_argument('-c', '--customer', action='store_true', help='sync customer')
        parser.add_argument('-t', '--transaction', action='store_true', help='sync transaction')

    def handle(self, *args, **options):
        _all = options['all']
        address = options['address']
        business = options['business']
        product = options['product']
        price = options['price']
        subscription = options['subscription']
        customer = options['customer']
        transaction = options['transaction']

        try:
            # ----------------
            # Address
            from django_paddle_billing.models import Address

            if _all or address:
                Address.sync_from_paddle()

            # ----------------
            # Business
            from django_paddle_billing.models import Business

            if _all or business:
                Business.sync_from_paddle()

            # ----------------
            # Products
            from django_paddle_billing.models import Product

            if _all or product:
                Product.sync_from_paddle()
            # products = Product.objects.all()

            # ----------------
            # Prices
            from django_paddle_billing.models import Price

            if _all or price:
                Price.sync_from_paddle()

            # ----------------
            # Customers
            from django_paddle_billing.models import Customer

            if _all or customer:
                Customer.sync_from_paddle()

            # ----------------
            # Subscriptions
            from django_paddle_billing.models import Subscription

            if _all or subscription:
                Subscription.sync_from_paddle()

            # ----------------
            # Transactions
            from django_paddle_billing.models import Transaction
            
            if _all or transaction:
                Transaction.sync_from_paddle()

            self.stdout.write(self.style.SUCCESS("Successfully synced data from Paddle"))

        except Exception as e:
            self.stdout.write(self.style.ERROR("Failed to sync data from Paddle"))
            self.stdout.write(self.style.ERROR(e))
