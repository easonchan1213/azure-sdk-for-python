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


class NetworkConfigurationDiagnosticParameters(Model):
    """Parameters to get network configuration diagnostic.

    All required parameters must be populated in order to send to Azure.

    :param target_resource_id: Required. The ID of the target resource to
     perform network configuration diagnostic. Valid options are VM,
     NetworkInterface, VMSS/NetworkInterface and Application Gateway.
    :type target_resource_id: str
    :param verbosity_level: Verbosity level. Accepted values are 'Normal',
     'Minimum', 'Full'. Possible values include: 'Normal', 'Minimum', 'Full'
    :type verbosity_level: str or
     ~azure.mgmt.network.v2018_08_01.models.VerbosityLevel
    :param profiles: Required. List of network configuration diagnostic
     profiles.
    :type profiles:
     list[~azure.mgmt.network.v2018_08_01.models.NetworkConfigurationDiagnosticProfile]
    """

    _validation = {
        'target_resource_id': {'required': True},
        'profiles': {'required': True},
    }

    _attribute_map = {
        'target_resource_id': {'key': 'targetResourceId', 'type': 'str'},
        'verbosity_level': {'key': 'verbosityLevel', 'type': 'str'},
        'profiles': {'key': 'profiles', 'type': '[NetworkConfigurationDiagnosticProfile]'},
    }

    def __init__(self, **kwargs):
        super(NetworkConfigurationDiagnosticParameters, self).__init__(**kwargs)
        self.target_resource_id = kwargs.get('target_resource_id', None)
        self.verbosity_level = kwargs.get('verbosity_level', None)
        self.profiles = kwargs.get('profiles', None)
