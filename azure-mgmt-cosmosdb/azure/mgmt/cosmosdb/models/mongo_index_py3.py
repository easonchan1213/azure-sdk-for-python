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


class MongoIndex(Model):
    """Cosmos DB Mongodb collection index key.

    :param key: Cosmos DB Mongodb collection index keys
    :type key: ~azure.mgmt.cosmosdb.models.MongoIndexKeys
    :param options: Cosmos DB Mongodb collection index key options
    :type options: ~azure.mgmt.cosmosdb.models.MongoIndexOptions
    """

    _attribute_map = {
        'key': {'key': 'key', 'type': 'MongoIndexKeys'},
        'options': {'key': 'options', 'type': 'MongoIndexOptions'},
    }

    def __init__(self, *, key=None, options=None, **kwargs) -> None:
        super(MongoIndex, self).__init__(**kwargs)
        self.key = key
        self.options = options
