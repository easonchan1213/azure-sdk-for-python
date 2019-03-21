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


class PeeringPropertiesDirect(Model):
    """The properties that define a direct peering.

    :param connections: The set of connections that constitute a direct
     peering.
    :type connections: list[~azure.mgmt.peering.models.DirectConnection]
    :param use_for_peering_service: The flag that indicates whether or not the
     peering is used for peering service.
    :type use_for_peering_service: bool
    :param peer_asn: The reference of the peer ASN.
    :type peer_asn: ~azure.mgmt.peering.models.SubResource
    """

    _attribute_map = {
        'connections': {'key': 'connections', 'type': '[DirectConnection]'},
        'use_for_peering_service': {'key': 'useForPeeringService', 'type': 'bool'},
        'peer_asn': {'key': 'peerAsn', 'type': 'SubResource'},
    }

    def __init__(self, *, connections=None, use_for_peering_service: bool=None, peer_asn=None, **kwargs) -> None:
        super(PeeringPropertiesDirect, self).__init__(**kwargs)
        self.connections = connections
        self.use_for_peering_service = use_for_peering_service
        self.peer_asn = peer_asn
