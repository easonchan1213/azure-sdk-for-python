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


class SSISExecutionParameter(Model):
    """SSIS execution parameter.

    All required parameters must be populated in order to send to Azure.

    :param value: Required. SSIS package execution parameter value. Type:
     string (or Expression with resultType string).
    :type value: object
    """

    _validation = {
        'value': {'required': True},
    }

    _attribute_map = {
        'value': {'key': 'value', 'type': 'object'},
    }

    def __init__(self, *, value, **kwargs) -> None:
        super(SSISExecutionParameter, self).__init__(**kwargs)
        self.value = value
