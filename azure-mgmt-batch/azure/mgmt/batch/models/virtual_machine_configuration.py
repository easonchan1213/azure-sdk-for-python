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


class VirtualMachineConfiguration(Model):
    """The configuration for compute nodes in a pool based on the Azure Virtual
    Machines infrastructure.

    :param image_reference: A reference to the Azure Virtual Machines
     Marketplace Image or the custom Virtual Machine Image to use.
    :type image_reference: ~azure.mgmt.batch.models.ImageReference
    :param os_disk: Settings for the operating system disk of the Virtual
     Machine.
    :type os_disk: ~azure.mgmt.batch.models.OSDisk
    :param node_agent_sku_id: The SKU of the Batch node agent to be
     provisioned on compute nodes in the pool. The Batch node agent is a
     program that runs on each node in the pool, and provides the
     command-and-control interface between the node and the Batch service.
     There are different implementations of the node agent, known as SKUs, for
     different operating systems. You must specify a node agent SKU which
     matches the selected image reference. To get the list of supported node
     agent SKUs along with their list of verified image references, see the
     'List supported node agent SKUs' operation.
    :type node_agent_sku_id: str
    :param windows_configuration: Windows operating system settings on the
     virtual machine. This property must not be specified if the imageReference
     specifies a Linux OS image.
    :type windows_configuration: ~azure.mgmt.batch.models.WindowsConfiguration
    :param data_disks: The configuration for data disks attached to the
     comptue nodes in the pool. This property must be specified if the compute
     nodes in the pool need to have empty data disks attached to them.
    :type data_disks: list[~azure.mgmt.batch.models.DataDisk]
    :param license_type: The type of on-premises license to be used when
     deploying the operating system. This only applies to images that contain
     the Windows operating system, and should only be used when you hold valid
     on-premises licenses for the nodes which will be deployed. If omitted, no
     on-premises licensing discount is applied. Values are:
     Windows_Server - The on-premises license is for Windows Server.
     Windows_Client - The on-premises license is for Windows Client.
    :type license_type: str
    """

    _validation = {
        'image_reference': {'required': True},
        'node_agent_sku_id': {'required': True},
    }

    _attribute_map = {
        'image_reference': {'key': 'imageReference', 'type': 'ImageReference'},
        'os_disk': {'key': 'osDisk', 'type': 'OSDisk'},
        'node_agent_sku_id': {'key': 'nodeAgentSkuId', 'type': 'str'},
        'windows_configuration': {'key': 'windowsConfiguration', 'type': 'WindowsConfiguration'},
        'data_disks': {'key': 'dataDisks', 'type': '[DataDisk]'},
        'license_type': {'key': 'licenseType', 'type': 'str'},
    }

    def __init__(self, image_reference, node_agent_sku_id, os_disk=None, windows_configuration=None, data_disks=None, license_type=None):
        super(VirtualMachineConfiguration, self).__init__()
        self.image_reference = image_reference
        self.os_disk = os_disk
        self.node_agent_sku_id = node_agent_sku_id
        self.windows_configuration = windows_configuration
        self.data_disks = data_disks
        self.license_type = license_type