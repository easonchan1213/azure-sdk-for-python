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


class RunCommandResult(Model):
    """RunCommandResult.

    :param value: Run command operation response.
    :type value:
     list[~azure.mgmt.compute.v2018_06_01.models.InstanceViewStatus]
    """

    _attribute_map = {
        'value': {'key': 'value', 'type': '[InstanceViewStatus]'},
    }

    def __init__(self, *, value=None, **kwargs) -> None:
        super(RunCommandResult, self).__init__(**kwargs)
        self.value = value
