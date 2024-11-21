import os

from typing import Any
from infisical_client import (
    ClientSettings,
    InfisicalClient,
    ListSecretsOptions,
    AuthenticationOptions,
    UniversalAuthMethod,
)


class InfisicalManagedCredentials:
    def __init__(self) -> None:
        try:
            self.client = InfisicalClient(
                ClientSettings(
                    auth=AuthenticationOptions(
                        universal_auth=UniversalAuthMethod(
                            client_id=os.environ["INFISICAL_CLIENT_ID"],
                            client_secret=os.environ["INFISICAL_SECRET"],
                        ),
                    ),
                    cache_ttl=1,
                )
            )
        except Exception:
            raise Exception("Could not connect to Infisical")

    def __call__(self, *args: Any, **kwds: Any) -> bool:
        try:
            secrets = self.client.listSecrets(
                options=ListSecretsOptions(
                    environment="dev",
                    project_id=os.environ["INFISICAL_PROJECT_ID"],
                    attach_to_process_env=True,
                ),
            )
            return True
        except Exception:
            raise Exception("Could not connect to Infisical")
