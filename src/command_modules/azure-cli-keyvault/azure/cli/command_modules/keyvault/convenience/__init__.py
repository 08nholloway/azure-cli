#---------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
#---------------------------------------------------------------------------------------------

from azure.cli.command_modules.keyvault.convenience import \
    http_bearer_challenge_cache as HttpBearerChallengeCache
from .http_bearer_challenge import HttpBearerChallenge
from .key_vault_client import KeyVaultClient
from .key_vault_authentication import KeyVaultAuthentication
from .version import VERSION

__all__ = ['HttpBearerChallengeCache', 'HttpBearerChallenge', 'KeyVaultClient',
           'KeyVaultAuthentication']

__version__ = VERSION
