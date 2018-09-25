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


class NodeRebootParameter(Model):
    """Options for rebooting a compute node.

    :param node_reboot_option: When to reboot the compute node and what to do
     with currently running tasks. The default value is requeue. Possible
     values include: 'requeue', 'terminate', 'taskCompletion', 'retainedData'
    :type node_reboot_option: str or
     ~azure.batch.models.ComputeNodeRebootOption
    """

    _attribute_map = {
        'node_reboot_option': {'key': 'nodeRebootOption', 'type': 'ComputeNodeRebootOption'},
    }

    def __init__(self, *, node_reboot_option=None, **kwargs) -> None:
        super(NodeRebootParameter, self).__init__(**kwargs)
        self.node_reboot_option = node_reboot_option
