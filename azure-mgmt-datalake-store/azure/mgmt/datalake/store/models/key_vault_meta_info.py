# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class KeyVaultMetaInfo(Model):
    """Metadata information used by account encryption.

    All required parameters must be populated in order to send to Azure.

    :param key_vault_resource_id: Required. The resource identifier for the
     user managed Key Vault being used to encrypt.
    :type key_vault_resource_id: str
    :param encryption_key_name: Required. The name of the user managed
     encryption key.
    :type encryption_key_name: str
    :param encryption_key_version: Required. The version of the user managed
     encryption key.
    :type encryption_key_version: str
    """

    _validation = {
        'key_vault_resource_id': {'required': True},
        'encryption_key_name': {'required': True},
        'encryption_key_version': {'required': True},
    }

    _attribute_map = {
        'key_vault_resource_id': {'key': 'keyVaultResourceId', 'type': 'str'},
        'encryption_key_name': {'key': 'encryptionKeyName', 'type': 'str'},
        'encryption_key_version': {'key': 'encryptionKeyVersion', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(KeyVaultMetaInfo, self).__init__(**kwargs)
        self.key_vault_resource_id = kwargs.get('key_vault_resource_id', None)
        self.encryption_key_name = kwargs.get('encryption_key_name', None)
        self.encryption_key_version = kwargs.get('encryption_key_version', None)
