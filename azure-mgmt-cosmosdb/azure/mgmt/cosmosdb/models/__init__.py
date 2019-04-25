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

try:
    from .consistency_policy_py3 import ConsistencyPolicy
    from .capability_py3 import Capability
    from .location_py3 import Location
    from .failover_policy_py3 import FailoverPolicy
    from .virtual_network_rule_py3 import VirtualNetworkRule
    from .database_account_py3 import DatabaseAccount
    from .sql_database_py3 import SqlDatabase
    from .indexes_py3 import Indexes
    from .included_path_py3 import IncludedPath
    from .excluded_path_py3 import ExcludedPath
    from .indexing_policy_py3 import IndexingPolicy
    from .container_partition_key_py3 import ContainerPartitionKey
    from .unique_key_py3 import UniqueKey
    from .unique_key_policy_py3 import UniqueKeyPolicy
    from .conflict_resolution_policy_py3 import ConflictResolutionPolicy
    from .sql_container_py3 import SqlContainer
    from .mongodb_database_py3 import MongodbDatabase
    from .mongodb_collection_py3 import MongodbCollection
    from .table_py3 import Table
    from .cassandra_keyspace_py3 import CassandraKeyspace
    from .cassandra_table_py3 import CassandraTable
    from .gremlin_database_py3 import GremlinDatabase
    from .gremlin_graph_py3 import GremlinGraph
    from .error_response_py3 import ErrorResponse, ErrorResponseException
    from .failover_policies_py3 import FailoverPolicies
    from .region_for_online_offline_py3 import RegionForOnlineOffline
    from .resource_py3 import Resource
    from .extended_resource_properties_py3 import ExtendedResourceProperties
    from .database_account_create_update_parameters_py3 import DatabaseAccountCreateUpdateParameters
    from .database_account_patch_parameters_py3 import DatabaseAccountPatchParameters
    from .database_account_list_read_only_keys_result_py3 import DatabaseAccountListReadOnlyKeysResult
    from .database_account_list_keys_result_py3 import DatabaseAccountListKeysResult
    from .database_account_connection_string_py3 import DatabaseAccountConnectionString
    from .database_account_list_connection_strings_result_py3 import DatabaseAccountListConnectionStringsResult
    from .database_account_regenerate_key_parameters_py3 import DatabaseAccountRegenerateKeyParameters
    from .sql_database_resource_py3 import SqlDatabaseResource
    from .sql_database_create_update_parameters_py3 import SqlDatabaseCreateUpdateParameters
    from .sql_container_resource_py3 import SqlContainerResource
    from .sql_container_create_update_parameters_py3 import SqlContainerCreateUpdateParameters
    from .mongodb_database_resource_py3 import MongodbDatabaseResource
    from .mongodb_database_create_update_parameters_py3 import MongodbDatabaseCreateUpdateParameters
    from .mongo_index_keys_py3 import MongoIndexKeys
    from .mongo_index_options_py3 import MongoIndexOptions
    from .mongo_index_py3 import MongoIndex
    from .mongodb_collection_resource_py3 import MongodbCollectionResource
    from .mongodb_collection_create_update_parameters_py3 import MongodbCollectionCreateUpdateParameters
    from .table_resource_py3 import TableResource
    from .table_create_update_parameters_py3 import TableCreateUpdateParameters
    from .cassandra_keyspace_resource_py3 import CassandraKeyspaceResource
    from .cassandra_keyspace_create_update_parameters_py3 import CassandraKeyspaceCreateUpdateParameters
    from .column_py3 import Column
    from .cassandra_partition_key_py3 import CassandraPartitionKey
    from .cluster_key_py3 import ClusterKey
    from .cassandra_schema_py3 import CassandraSchema
    from .cassandra_table_resource_py3 import CassandraTableResource
    from .cassandra_table_create_update_parameters_py3 import CassandraTableCreateUpdateParameters
    from .gremlin_database_resource_py3 import GremlinDatabaseResource
    from .gremlin_database_create_update_parameters_py3 import GremlinDatabaseCreateUpdateParameters
    from .gremlin_graph_resource_py3 import GremlinGraphResource
    from .gremlin_graph_create_update_parameters_py3 import GremlinGraphCreateUpdateParameters
    from .operation_display_py3 import OperationDisplay
    from .operation_py3 import Operation
    from .metric_name_py3 import MetricName
    from .usage_py3 import Usage
    from .partition_usage_py3 import PartitionUsage
    from .metric_availability_py3 import MetricAvailability
    from .metric_definition_py3 import MetricDefinition
    from .metric_value_py3 import MetricValue
    from .metric_py3 import Metric
    from .percentile_metric_value_py3 import PercentileMetricValue
    from .percentile_metric_py3 import PercentileMetric
    from .partition_metric_py3 import PartitionMetric
except (SyntaxError, ImportError):
    from .consistency_policy import ConsistencyPolicy
    from .capability import Capability
    from .location import Location
    from .failover_policy import FailoverPolicy
    from .virtual_network_rule import VirtualNetworkRule
    from .database_account import DatabaseAccount
    from .sql_database import SqlDatabase
    from .indexes import Indexes
    from .included_path import IncludedPath
    from .excluded_path import ExcludedPath
    from .indexing_policy import IndexingPolicy
    from .container_partition_key import ContainerPartitionKey
    from .unique_key import UniqueKey
    from .unique_key_policy import UniqueKeyPolicy
    from .conflict_resolution_policy import ConflictResolutionPolicy
    from .sql_container import SqlContainer
    from .mongodb_database import MongodbDatabase
    from .mongodb_collection import MongodbCollection
    from .table import Table
    from .cassandra_keyspace import CassandraKeyspace
    from .cassandra_table import CassandraTable
    from .gremlin_database import GremlinDatabase
    from .gremlin_graph import GremlinGraph
    from .error_response import ErrorResponse, ErrorResponseException
    from .failover_policies import FailoverPolicies
    from .region_for_online_offline import RegionForOnlineOffline
    from .resource import Resource
    from .extended_resource_properties import ExtendedResourceProperties
    from .database_account_create_update_parameters import DatabaseAccountCreateUpdateParameters
    from .database_account_patch_parameters import DatabaseAccountPatchParameters
    from .database_account_list_read_only_keys_result import DatabaseAccountListReadOnlyKeysResult
    from .database_account_list_keys_result import DatabaseAccountListKeysResult
    from .database_account_connection_string import DatabaseAccountConnectionString
    from .database_account_list_connection_strings_result import DatabaseAccountListConnectionStringsResult
    from .database_account_regenerate_key_parameters import DatabaseAccountRegenerateKeyParameters
    from .sql_database_resource import SqlDatabaseResource
    from .sql_database_create_update_parameters import SqlDatabaseCreateUpdateParameters
    from .sql_container_resource import SqlContainerResource
    from .sql_container_create_update_parameters import SqlContainerCreateUpdateParameters
    from .mongodb_database_resource import MongodbDatabaseResource
    from .mongodb_database_create_update_parameters import MongodbDatabaseCreateUpdateParameters
    from .mongo_index_keys import MongoIndexKeys
    from .mongo_index_options import MongoIndexOptions
    from .mongo_index import MongoIndex
    from .mongodb_collection_resource import MongodbCollectionResource
    from .mongodb_collection_create_update_parameters import MongodbCollectionCreateUpdateParameters
    from .table_resource import TableResource
    from .table_create_update_parameters import TableCreateUpdateParameters
    from .cassandra_keyspace_resource import CassandraKeyspaceResource
    from .cassandra_keyspace_create_update_parameters import CassandraKeyspaceCreateUpdateParameters
    from .column import Column
    from .cassandra_partition_key import CassandraPartitionKey
    from .cluster_key import ClusterKey
    from .cassandra_schema import CassandraSchema
    from .cassandra_table_resource import CassandraTableResource
    from .cassandra_table_create_update_parameters import CassandraTableCreateUpdateParameters
    from .gremlin_database_resource import GremlinDatabaseResource
    from .gremlin_database_create_update_parameters import GremlinDatabaseCreateUpdateParameters
    from .gremlin_graph_resource import GremlinGraphResource
    from .gremlin_graph_create_update_parameters import GremlinGraphCreateUpdateParameters
    from .operation_display import OperationDisplay
    from .operation import Operation
    from .metric_name import MetricName
    from .usage import Usage
    from .partition_usage import PartitionUsage
    from .metric_availability import MetricAvailability
    from .metric_definition import MetricDefinition
    from .metric_value import MetricValue
    from .metric import Metric
    from .percentile_metric_value import PercentileMetricValue
    from .percentile_metric import PercentileMetric
    from .partition_metric import PartitionMetric
from .database_account_paged import DatabaseAccountPaged
from .metric_paged import MetricPaged
from .usage_paged import UsagePaged
from .metric_definition_paged import MetricDefinitionPaged
from .sql_database_paged import SqlDatabasePaged
from .sql_container_paged import SqlContainerPaged
from .mongodb_database_paged import MongodbDatabasePaged
from .mongodb_collection_paged import MongodbCollectionPaged
from .table_paged import TablePaged
from .cassandra_keyspace_paged import CassandraKeyspacePaged
from .cassandra_table_paged import CassandraTablePaged
from .gremlin_database_paged import GremlinDatabasePaged
from .gremlin_graph_paged import GremlinGraphPaged
from .operation_paged import OperationPaged
from .percentile_metric_paged import PercentileMetricPaged
from .partition_metric_paged import PartitionMetricPaged
from .partition_usage_paged import PartitionUsagePaged
from .cosmos_db_enums import (
    DatabaseAccountKind,
    DatabaseAccountOfferType,
    DefaultConsistencyLevel,
    IndexingMode,
    DataType,
    IndexKind,
    PartitionKind,
    ConflictResolutionMode,
    KeyKind,
    UnitType,
    PrimaryAggregationType,
)

__all__ = [
    'ConsistencyPolicy',
    'Capability',
    'Location',
    'FailoverPolicy',
    'VirtualNetworkRule',
    'DatabaseAccount',
    'SqlDatabase',
    'Indexes',
    'IncludedPath',
    'ExcludedPath',
    'IndexingPolicy',
    'ContainerPartitionKey',
    'UniqueKey',
    'UniqueKeyPolicy',
    'ConflictResolutionPolicy',
    'SqlContainer',
    'MongodbDatabase',
    'MongodbCollection',
    'Table',
    'CassandraKeyspace',
    'CassandraTable',
    'GremlinDatabase',
    'GremlinGraph',
    'ErrorResponse', 'ErrorResponseException',
    'FailoverPolicies',
    'RegionForOnlineOffline',
    'Resource',
    'ExtendedResourceProperties',
    'DatabaseAccountCreateUpdateParameters',
    'DatabaseAccountPatchParameters',
    'DatabaseAccountListReadOnlyKeysResult',
    'DatabaseAccountListKeysResult',
    'DatabaseAccountConnectionString',
    'DatabaseAccountListConnectionStringsResult',
    'DatabaseAccountRegenerateKeyParameters',
    'SqlDatabaseResource',
    'SqlDatabaseCreateUpdateParameters',
    'SqlContainerResource',
    'SqlContainerCreateUpdateParameters',
    'MongodbDatabaseResource',
    'MongodbDatabaseCreateUpdateParameters',
    'MongoIndexKeys',
    'MongoIndexOptions',
    'MongoIndex',
    'MongodbCollectionResource',
    'MongodbCollectionCreateUpdateParameters',
    'TableResource',
    'TableCreateUpdateParameters',
    'CassandraKeyspaceResource',
    'CassandraKeyspaceCreateUpdateParameters',
    'Column',
    'CassandraPartitionKey',
    'ClusterKey',
    'CassandraSchema',
    'CassandraTableResource',
    'CassandraTableCreateUpdateParameters',
    'GremlinDatabaseResource',
    'GremlinDatabaseCreateUpdateParameters',
    'GremlinGraphResource',
    'GremlinGraphCreateUpdateParameters',
    'OperationDisplay',
    'Operation',
    'MetricName',
    'Usage',
    'PartitionUsage',
    'MetricAvailability',
    'MetricDefinition',
    'MetricValue',
    'Metric',
    'PercentileMetricValue',
    'PercentileMetric',
    'PartitionMetric',
    'DatabaseAccountPaged',
    'MetricPaged',
    'UsagePaged',
    'MetricDefinitionPaged',
    'SqlDatabasePaged',
    'SqlContainerPaged',
    'MongodbDatabasePaged',
    'MongodbCollectionPaged',
    'TablePaged',
    'CassandraKeyspacePaged',
    'CassandraTablePaged',
    'GremlinDatabasePaged',
    'GremlinGraphPaged',
    'OperationPaged',
    'PercentileMetricPaged',
    'PartitionMetricPaged',
    'PartitionUsagePaged',
    'DatabaseAccountKind',
    'DatabaseAccountOfferType',
    'DefaultConsistencyLevel',
    'IndexingMode',
    'DataType',
    'IndexKind',
    'PartitionKind',
    'ConflictResolutionMode',
    'KeyKind',
    'UnitType',
    'PrimaryAggregationType',
]
