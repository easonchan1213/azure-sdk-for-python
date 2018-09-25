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


class ClusterConfigurationUpgradeDescription(Model):
    """Describes the parameters for a standalone cluster configuration upgrade.

    All required parameters must be populated in order to send to Azure.

    :param cluster_config: Required. The cluster configuration.
    :type cluster_config: str
    :param health_check_retry_timeout: The length of time between attempts to
     perform a health checks if the application or cluster is not healthy.
     Default value: "PT0H0M0S" .
    :type health_check_retry_timeout: timedelta
    :param health_check_wait_duration_in_seconds: The length of time to wait
     after completing an upgrade domain before starting the health checks
     process. Default value: "PT0H0M0S" .
    :type health_check_wait_duration_in_seconds: timedelta
    :param health_check_stable_duration_in_seconds: The length of time that
     the application or cluster must remain healthy. Default value: "PT0H0M0S"
     .
    :type health_check_stable_duration_in_seconds: timedelta
    :param upgrade_domain_timeout_in_seconds: The timeout for the upgrade
     domain. Default value: "PT0H0M0S" .
    :type upgrade_domain_timeout_in_seconds: timedelta
    :param upgrade_timeout_in_seconds: The upgrade timeout. Default value:
     "PT0H0M0S" .
    :type upgrade_timeout_in_seconds: timedelta
    :param max_percent_unhealthy_applications: The maximum allowed percentage
     of unhealthy applications during the upgrade. Allowed values are integer
     values from zero to 100. Default value: 0 .
    :type max_percent_unhealthy_applications: int
    :param max_percent_unhealthy_nodes: The maximum allowed percentage of
     unhealthy nodes during the upgrade. Allowed values are integer values from
     zero to 100. Default value: 0 .
    :type max_percent_unhealthy_nodes: int
    :param max_percent_delta_unhealthy_nodes: The maximum allowed percentage
     of delta health degradation during the upgrade. Allowed values are integer
     values from zero to 100. Default value: 0 .
    :type max_percent_delta_unhealthy_nodes: int
    :param max_percent_upgrade_domain_delta_unhealthy_nodes: The maximum
     allowed percentage of upgrade domain delta health degradation during the
     upgrade. Allowed values are integer values from zero to 100. Default
     value: 0 .
    :type max_percent_upgrade_domain_delta_unhealthy_nodes: int
    :param application_health_policies: Defines the application health policy
     map used to evaluate the health of an application or one of its children
     entities.
    :type application_health_policies:
     ~azure.servicefabric.models.ApplicationHealthPolicies
    """

    _validation = {
        'cluster_config': {'required': True},
    }

    _attribute_map = {
        'cluster_config': {'key': 'ClusterConfig', 'type': 'str'},
        'health_check_retry_timeout': {'key': 'HealthCheckRetryTimeout', 'type': 'duration'},
        'health_check_wait_duration_in_seconds': {'key': 'HealthCheckWaitDurationInSeconds', 'type': 'duration'},
        'health_check_stable_duration_in_seconds': {'key': 'HealthCheckStableDurationInSeconds', 'type': 'duration'},
        'upgrade_domain_timeout_in_seconds': {'key': 'UpgradeDomainTimeoutInSeconds', 'type': 'duration'},
        'upgrade_timeout_in_seconds': {'key': 'UpgradeTimeoutInSeconds', 'type': 'duration'},
        'max_percent_unhealthy_applications': {'key': 'MaxPercentUnhealthyApplications', 'type': 'int'},
        'max_percent_unhealthy_nodes': {'key': 'MaxPercentUnhealthyNodes', 'type': 'int'},
        'max_percent_delta_unhealthy_nodes': {'key': 'MaxPercentDeltaUnhealthyNodes', 'type': 'int'},
        'max_percent_upgrade_domain_delta_unhealthy_nodes': {'key': 'MaxPercentUpgradeDomainDeltaUnhealthyNodes', 'type': 'int'},
        'application_health_policies': {'key': 'ApplicationHealthPolicies', 'type': 'ApplicationHealthPolicies'},
    }

    def __init__(self, *, cluster_config: str, health_check_retry_timeout="PT0H0M0S", health_check_wait_duration_in_seconds="PT0H0M0S", health_check_stable_duration_in_seconds="PT0H0M0S", upgrade_domain_timeout_in_seconds="PT0H0M0S", upgrade_timeout_in_seconds="PT0H0M0S", max_percent_unhealthy_applications: int=0, max_percent_unhealthy_nodes: int=0, max_percent_delta_unhealthy_nodes: int=0, max_percent_upgrade_domain_delta_unhealthy_nodes: int=0, application_health_policies=None, **kwargs) -> None:
        super(ClusterConfigurationUpgradeDescription, self).__init__(**kwargs)
        self.cluster_config = cluster_config
        self.health_check_retry_timeout = health_check_retry_timeout
        self.health_check_wait_duration_in_seconds = health_check_wait_duration_in_seconds
        self.health_check_stable_duration_in_seconds = health_check_stable_duration_in_seconds
        self.upgrade_domain_timeout_in_seconds = upgrade_domain_timeout_in_seconds
        self.upgrade_timeout_in_seconds = upgrade_timeout_in_seconds
        self.max_percent_unhealthy_applications = max_percent_unhealthy_applications
        self.max_percent_unhealthy_nodes = max_percent_unhealthy_nodes
        self.max_percent_delta_unhealthy_nodes = max_percent_delta_unhealthy_nodes
        self.max_percent_upgrade_domain_delta_unhealthy_nodes = max_percent_upgrade_domain_delta_unhealthy_nodes
        self.application_health_policies = application_health_policies
