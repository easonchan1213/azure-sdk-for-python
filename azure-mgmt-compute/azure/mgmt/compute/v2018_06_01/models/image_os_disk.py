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


class ImageOSDisk(Model):
    """Describes an Operating System disk.

    All required parameters must be populated in order to send to Azure.

    :param os_type: Required. This property allows you to specify the type of
     the OS that is included in the disk if creating a VM from a custom image.
     <br><br> Possible values are: <br><br> **Windows** <br><br> **Linux**.
     Possible values include: 'Windows', 'Linux'
    :type os_type: str or
     ~azure.mgmt.compute.v2018_06_01.models.OperatingSystemTypes
    :param os_state: Required. The OS State. Possible values include:
     'Generalized', 'Specialized'
    :type os_state: str or
     ~azure.mgmt.compute.v2018_06_01.models.OperatingSystemStateTypes
    :param snapshot: The snapshot.
    :type snapshot: ~azure.mgmt.compute.v2018_06_01.models.SubResource
    :param managed_disk: The managedDisk.
    :type managed_disk: ~azure.mgmt.compute.v2018_06_01.models.SubResource
    :param blob_uri: The Virtual Hard Disk.
    :type blob_uri: str
    :param caching: Specifies the caching requirements. <br><br> Possible
     values are: <br><br> **None** <br><br> **ReadOnly** <br><br> **ReadWrite**
     <br><br> Default: **None for Standard storage. ReadOnly for Premium
     storage**. Possible values include: 'None', 'ReadOnly', 'ReadWrite'
    :type caching: str or ~azure.mgmt.compute.v2018_06_01.models.CachingTypes
    :param disk_size_gb: Specifies the size of empty data disks in gigabytes.
     This element can be used to overwrite the name of the disk in a virtual
     machine image. <br><br> This value cannot be larger than 1023 GB
    :type disk_size_gb: int
    :param storage_account_type: Specifies the storage account type for the
     managed disk. Possible values are: Standard_LRS, Premium_LRS, and
     StandardSSD_LRS. Possible values include: 'Standard_LRS', 'Premium_LRS',
     'StandardSSD_LRS', 'UltraSSD_LRS'
    :type storage_account_type: str or
     ~azure.mgmt.compute.v2018_06_01.models.StorageAccountTypes
    """

    _validation = {
        'os_type': {'required': True},
        'os_state': {'required': True},
    }

    _attribute_map = {
        'os_type': {'key': 'osType', 'type': 'OperatingSystemTypes'},
        'os_state': {'key': 'osState', 'type': 'OperatingSystemStateTypes'},
        'snapshot': {'key': 'snapshot', 'type': 'SubResource'},
        'managed_disk': {'key': 'managedDisk', 'type': 'SubResource'},
        'blob_uri': {'key': 'blobUri', 'type': 'str'},
        'caching': {'key': 'caching', 'type': 'CachingTypes'},
        'disk_size_gb': {'key': 'diskSizeGB', 'type': 'int'},
        'storage_account_type': {'key': 'storageAccountType', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(ImageOSDisk, self).__init__(**kwargs)
        self.os_type = kwargs.get('os_type', None)
        self.os_state = kwargs.get('os_state', None)
        self.snapshot = kwargs.get('snapshot', None)
        self.managed_disk = kwargs.get('managed_disk', None)
        self.blob_uri = kwargs.get('blob_uri', None)
        self.caching = kwargs.get('caching', None)
        self.disk_size_gb = kwargs.get('disk_size_gb', None)
        self.storage_account_type = kwargs.get('storage_account_type', None)
