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


class KeyImportParameters(Model):
    """The key import parameters.

    All required parameters must be populated in order to send to Azure.

    :param hsm: Whether to import as a hardware key (HSM) or software key.
    :type hsm: bool
    :param key: Required. The Json web key
    :type key: ~azure.keyvault.v7_0.models.JsonWebKey
    :param key_attributes: The key management attributes.
    :type key_attributes: ~azure.keyvault.v7_0.models.KeyAttributes
    :param tags: Application specific metadata in the form of key-value pairs.
    :type tags: dict[str, str]
    """

    _validation = {
        'key': {'required': True},
    }

    _attribute_map = {
        'hsm': {'key': 'Hsm', 'type': 'bool'},
        'key': {'key': 'key', 'type': 'JsonWebKey'},
        'key_attributes': {'key': 'attributes', 'type': 'KeyAttributes'},
        'tags': {'key': 'tags', 'type': '{str}'},
    }

    def __init__(self, *, key, hsm: bool=None, key_attributes=None, tags=None, **kwargs) -> None:
        super(KeyImportParameters, self).__init__(**kwargs)
        self.hsm = hsm
        self.key = key
        self.key_attributes = key_attributes
        self.tags = tags
