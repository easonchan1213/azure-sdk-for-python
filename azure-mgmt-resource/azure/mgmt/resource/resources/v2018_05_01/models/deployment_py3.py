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


class Deployment(Model):
    """Deployment operation parameters.

    All required parameters must be populated in order to send to Azure.

    :param location: The location to store the deployment data.
    :type location: str
    :param properties: Required. The deployment properties.
    :type properties:
     ~azure.mgmt.resource.resources.v2018_05_01.models.DeploymentProperties
    """

    _validation = {
        'properties': {'required': True},
    }

    _attribute_map = {
        'location': {'key': 'location', 'type': 'str'},
        'properties': {'key': 'properties', 'type': 'DeploymentProperties'},
    }

    def __init__(self, *, properties, location: str=None, **kwargs) -> None:
        super(Deployment, self).__init__(**kwargs)
        self.location = location
        self.properties = properties
