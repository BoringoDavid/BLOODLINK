# bload_donor_app/tokens.py
from django.contrib.auth.tokens import PasswordResetTokenGenerator

class DonorPasswordResetTokenGenerator(PasswordResetTokenGenerator):
    def _make_hash_value(self, donor, timestamp):
        return str(donor.pk) + str(timestamp) + str(donor.password)

donor_password_reset_token = DonorPasswordResetTokenGenerator()


# for collector reset password 
# bload_donor_app/tokens.py

from django.contrib.auth.tokens import PasswordResetTokenGenerator

class CollectorPasswordResetTokenGenerator(PasswordResetTokenGenerator):
    def _make_hash_value(self, collector, timestamp):
        # Include pk, timestamp, and password hash in hash
        return str(collector.pk) + str(timestamp) + str(collector.password)

collector_password_reset_token = CollectorPasswordResetTokenGenerator()
