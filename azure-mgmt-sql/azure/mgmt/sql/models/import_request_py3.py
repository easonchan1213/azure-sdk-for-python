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

from .export_request_py3 import ExportRequest


class ImportRequest(ExportRequest):
    """Import database parameters.

    All required parameters must be populated in order to send to Azure.

    :param storage_key_type: Required. The type of the storage key to use.
     Possible values include: 'StorageAccessKey', 'SharedAccessKey'
    :type storage_key_type: str or ~azure.mgmt.sql.models.StorageKeyType
    :param storage_key: Required. The storage key to use.  If storage key type
     is SharedAccessKey, it must be preceded with a "?."
    :type storage_key: str
    :param storage_uri: Required. The storage uri to use.
    :type storage_uri: str
    :param administrator_login: Required. The name of the SQL administrator.
    :type administrator_login: str
    :param administrator_login_password: Required. The password of the SQL
     administrator.
    :type administrator_login_password: str
    :param authentication_type: The authentication type. Possible values
     include: 'SQL', 'ADPassword'. Default value: "SQL" .
    :type authentication_type: str or
     ~azure.mgmt.sql.models.AuthenticationType
    :param database_name: Required. The name of the database to import.
    :type database_name: str
    :param edition: Required. The edition for the database being created.
     To determine the editions that are available to your subscription in an
     Azure location, use the `Capabilities_ListByLocation` REST API or one of
     the following commands:
     ```azurecli
     az sql db list-editions -l <location> -o table
     ````
     ```powershell
     Get-AzSqlServerServiceObjective -Location <location>
     ````. Possible values include: 'Web', 'Business', 'Basic', 'Standard',
     'Premium', 'PremiumRS', 'Free', 'Stretch', 'DataWarehouse', 'System',
     'System2', 'GeneralPurpose', 'BusinessCritical', 'Hyperscale'
    :type edition: str or ~azure.mgmt.sql.models.DatabaseEdition
    :param service_objective_name: Required. The name of the service objective
     to assign to the database. Possible values include: 'System', 'System0',
     'System1', 'System2', 'System3', 'System4', 'System2L', 'System3L',
     'System4L', 'Free', 'Basic', 'S0', 'S1', 'S2', 'S3', 'S4', 'S6', 'S7',
     'S9', 'S12', 'P1', 'P2', 'P3', 'P4', 'P6', 'P11', 'P15', 'PRS1', 'PRS2',
     'PRS4', 'PRS6', 'DW100', 'DW200', 'DW300', 'DW400', 'DW500', 'DW600',
     'DW1000', 'DW1200', 'DW1000c', 'DW1500', 'DW1500c', 'DW2000', 'DW2000c',
     'DW3000', 'DW2500c', 'DW3000c', 'DW6000', 'DW5000c', 'DW6000c', 'DW7500c',
     'DW10000c', 'DW15000c', 'DW30000c', 'DS100', 'DS200', 'DS300', 'DS400',
     'DS500', 'DS600', 'DS1000', 'DS1200', 'DS1500', 'DS2000', 'ElasticPool'
    :type service_objective_name: str or
     ~azure.mgmt.sql.models.ServiceObjectiveName
    :param max_size_bytes: Required. The maximum size for the newly imported
     database.
    :type max_size_bytes: str
    """

    _validation = {
        'storage_key_type': {'required': True},
        'storage_key': {'required': True},
        'storage_uri': {'required': True},
        'administrator_login': {'required': True},
        'administrator_login_password': {'required': True},
        'database_name': {'required': True},
        'edition': {'required': True},
        'service_objective_name': {'required': True},
        'max_size_bytes': {'required': True},
    }

    _attribute_map = {
        'storage_key_type': {'key': 'storageKeyType', 'type': 'StorageKeyType'},
        'storage_key': {'key': 'storageKey', 'type': 'str'},
        'storage_uri': {'key': 'storageUri', 'type': 'str'},
        'administrator_login': {'key': 'administratorLogin', 'type': 'str'},
        'administrator_login_password': {'key': 'administratorLoginPassword', 'type': 'str'},
        'authentication_type': {'key': 'authenticationType', 'type': 'AuthenticationType'},
        'database_name': {'key': 'databaseName', 'type': 'str'},
        'edition': {'key': 'edition', 'type': 'str'},
        'service_objective_name': {'key': 'serviceObjectiveName', 'type': 'str'},
        'max_size_bytes': {'key': 'maxSizeBytes', 'type': 'str'},
    }

    def __init__(self, *, storage_key_type, storage_key: str, storage_uri: str, administrator_login: str, administrator_login_password: str, database_name: str, edition, service_objective_name, max_size_bytes: str, authentication_type="SQL", **kwargs) -> None:
        super(ImportRequest, self).__init__(storage_key_type=storage_key_type, storage_key=storage_key, storage_uri=storage_uri, administrator_login=administrator_login, administrator_login_password=administrator_login_password, authentication_type=authentication_type, **kwargs)
        self.database_name = database_name
        self.edition = edition
        self.service_objective_name = service_objective_name
        self.max_size_bytes = max_size_bytes
