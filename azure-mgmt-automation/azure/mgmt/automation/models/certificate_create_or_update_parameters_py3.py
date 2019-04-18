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


class CertificateCreateOrUpdateParameters(Model):
    """The parameters supplied to the create or update or replace certificate
    operation.

    All required parameters must be populated in order to send to Azure.

    :param name: Required. Gets or sets the name of the certificate.
    :type name: str
    :param base64_value: Required. Gets or sets the base64 encoded value of
     the certificate.
    :type base64_value: str
    :param description: Gets or sets the description of the certificate.
    :type description: str
    :param thumbprint: Gets or sets the thumbprint of the certificate.
    :type thumbprint: str
    :param is_exportable: Gets or sets the is exportable flag of the
     certificate.
    :type is_exportable: bool
    """

    _validation = {
        'name': {'required': True},
        'base64_value': {'required': True},
    }

    _attribute_map = {
        'name': {'key': 'name', 'type': 'str'},
        'base64_value': {'key': 'properties.base64Value', 'type': 'str'},
        'description': {'key': 'properties.description', 'type': 'str'},
        'thumbprint': {'key': 'properties.thumbprint', 'type': 'str'},
        'is_exportable': {'key': 'properties.isExportable', 'type': 'bool'},
    }

    def __init__(self, *, name: str, base64_value: str, description: str=None, thumbprint: str=None, is_exportable: bool=None, **kwargs) -> None:
        super(CertificateCreateOrUpdateParameters, self).__init__(**kwargs)
        self.name = name
        self.base64_value = base64_value
        self.description = description
        self.thumbprint = thumbprint
        self.is_exportable = is_exportable
