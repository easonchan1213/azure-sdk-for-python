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


class MonitoringDetails(Model):
    """Details needed to monitor a Hana Instance.

    :param hana_vnet: ARM ID of an Azure Vnet with access to the HANA
     instance.
    :type hana_vnet: str
    :param hana_hostname: Hostname of the HANA Instance blade.
    :type hana_hostname: str
    :param hana_instance_num: A number between 00 and 99, stored as a string
     to maintain leading zero.
    :type hana_instance_num: str
    :param db_container: Either single or multiple depending on the use of
     MDC(Multiple Database Containers). Possible values include: 'single',
     'multiple'. Default value: "single" .
    :type db_container: str or
     ~azure.mgmt.hanaonazure.models.HanaDatabaseContainersEnum
    :param hana_database: Name of the database itself.  It only needs to be
     specified if using MDC
    :type hana_database: str
    :param hana_db_username: Username for the HANA database to login to for
     monitoring
    :type hana_db_username: str
    :param hana_db_password: Password for the HANA database to login for
     monitoring
    :type hana_db_password: str
    """

    _attribute_map = {
        'hana_vnet': {'key': 'hanaVnet', 'type': 'str'},
        'hana_hostname': {'key': 'hanaHostname', 'type': 'str'},
        'hana_instance_num': {'key': 'hanaInstanceNum', 'type': 'str'},
        'db_container': {'key': 'dbContainer', 'type': 'str'},
        'hana_database': {'key': 'hanaDatabase', 'type': 'str'},
        'hana_db_username': {'key': 'hanaDbUsername', 'type': 'str'},
        'hana_db_password': {'key': 'hanaDbPassword', 'type': 'str'},
    }

    def __init__(self, *, hana_vnet: str=None, hana_hostname: str=None, hana_instance_num: str=None, db_container="single", hana_database: str=None, hana_db_username: str=None, hana_db_password: str=None, **kwargs) -> None:
        super(MonitoringDetails, self).__init__(**kwargs)
        self.hana_vnet = hana_vnet
        self.hana_hostname = hana_hostname
        self.hana_instance_num = hana_instance_num
        self.db_container = db_container
        self.hana_database = hana_database
        self.hana_db_username = hana_db_username
        self.hana_db_password = hana_db_password
