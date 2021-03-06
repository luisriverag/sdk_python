from tests.bunq_test import BunqSdkTestCase


class TestUserContext(BunqSdkTestCase):
    """
    Tests:
        UserContext
    """

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls._API_CONTEXT = cls._get_api_context()

    def test_build_user_context(self):
        from bunq.sdk.context.user_context import UserContext
        user_context = UserContext(
            self._API_CONTEXT.session_context.user_id,
            self._API_CONTEXT.session_context.get_user_reference()
        )
        user_context.refresh_user_context()

        self.assertIsNotNone(user_context.user_id)
        self.assertIsNotNone(user_context.primary_monetary_account.id_)
