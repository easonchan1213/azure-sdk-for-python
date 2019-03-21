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


class PeeringPropertiesExchange(Model):
    """The properties that define an exchange peering.

    :param connections: The set of connections that constitute an exchange
     peering.
    :type connections: list[~azure.mgmt.peering.models.ExchangeConnection]
    :param peer_asn: The reference of the peer ASN.
    :type peer_asn: ~azure.mgmt.peering.models.SubResource
    """

    _attribute_map = {
        'connections': {'key': 'connections', 'type': '[ExchangeConnection]'},
        'peer_asn': {'key': 'peerAsn', 'type': 'SubResource'},
    }

    def __init__(self, **kwargs):
        super(PeeringPropertiesExchange, self).__init__(**kwargs)
        self.connections = kwargs.get('connections', None)
        self.peer_asn = kwargs.get('peer_asn', None)
