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

from .proxy_resource_py3 import ProxyResource


class TrafficManagerGeographicHierarchy(ProxyResource):
    """Class representing the Geographic hierarchy used with the Geographic
    traffic routing method.

    :param id: Fully qualified resource Id for the resource. Ex -
     /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/trafficManagerProfiles/{resourceName}
    :type id: str
    :param name: The name of the resource
    :type name: str
    :param type: The type of the resource. Ex-
     Microsoft.Network/trafficManagerProfiles.
    :type type: str
    :param geographic_hierarchy: The region at the root of the hierarchy from
     all the regions in the hierarchy can be retrieved.
    :type geographic_hierarchy: ~azure.mgmt.trafficmanager.models.Region
    """

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'geographic_hierarchy': {'key': 'properties.geographicHierarchy', 'type': 'Region'},
    }

    def __init__(self, *, id: str=None, name: str=None, type: str=None, geographic_hierarchy=None, **kwargs) -> None:
        super(TrafficManagerGeographicHierarchy, self).__init__(id=id, name=name, type=type, **kwargs)
        self.geographic_hierarchy = geographic_hierarchy
