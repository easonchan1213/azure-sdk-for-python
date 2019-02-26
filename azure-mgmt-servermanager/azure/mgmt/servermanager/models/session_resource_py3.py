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

from .resource_py3 import Resource


class SessionResource(Resource):
    """The session object.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :ivar id: Resource Manager Resource ID.
    :vartype id: str
    :ivar type: Resource Manager Resource Type.
    :vartype type: str
    :ivar name: Resource Manager Resource Name.
    :vartype name: str
    :ivar location: Resource Manager Resource Location.
    :vartype location: str
    :param tags: Resource Manager Resource Tags.
    :type tags: dict[str, str]
    :param etag:
    :type etag: str
    :param user_name: The username connecting to the session.
    :type user_name: str
    :param created: UTC date and time when node was first added to management
     service.
    :type created: datetime
    :param updated: UTC date and time when node was last updated.
    :type updated: datetime
    """

    _validation = {
        'id': {'readonly': True},
        'type': {'readonly': True},
        'name': {'readonly': True},
        'location': {'readonly': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'location': {'key': 'location', 'type': 'str'},
        'tags': {'key': 'tags', 'type': '{str}'},
        'etag': {'key': 'etag', 'type': 'str'},
        'user_name': {'key': 'properties.userName', 'type': 'str'},
        'created': {'key': 'properties.created', 'type': 'iso-8601'},
        'updated': {'key': 'properties.updated', 'type': 'iso-8601'},
    }

    def __init__(self, *, tags=None, etag: str=None, user_name: str=None, created=None, updated=None, **kwargs) -> None:
        super(SessionResource, self).__init__(tags=tags, etag=etag, **kwargs)
        self.user_name = user_name
        self.created = created
        self.updated = updated
