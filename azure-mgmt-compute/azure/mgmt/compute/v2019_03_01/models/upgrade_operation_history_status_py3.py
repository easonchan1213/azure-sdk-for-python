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


class UpgradeOperationHistoryStatus(Model):
    """Information about the current running state of the overall upgrade.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :ivar code: Code indicating the current status of the upgrade. Possible
     values include: 'RollingForward', 'Cancelled', 'Completed', 'Faulted'
    :vartype code: str or ~azure.mgmt.compute.v2019_03_01.models.UpgradeState
    :ivar start_time: Start time of the upgrade.
    :vartype start_time: datetime
    :ivar end_time: End time of the upgrade.
    :vartype end_time: datetime
    """

    _validation = {
        'code': {'readonly': True},
        'start_time': {'readonly': True},
        'end_time': {'readonly': True},
    }

    _attribute_map = {
        'code': {'key': 'code', 'type': 'UpgradeState'},
        'start_time': {'key': 'startTime', 'type': 'iso-8601'},
        'end_time': {'key': 'endTime', 'type': 'iso-8601'},
    }

    def __init__(self, **kwargs) -> None:
        super(UpgradeOperationHistoryStatus, self).__init__(**kwargs)
        self.code = None
        self.start_time = None
        self.end_time = None
