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

from .proxy_resource import ProxyResource


class StreamingLocator(ProxyResource):
    """A Streaming Locator resource.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    All required parameters must be populated in order to send to Azure.

    :ivar id: Fully qualified resource ID for the resource.
    :vartype id: str
    :ivar name: The name of the resource.
    :vartype name: str
    :ivar type: The type of the resource.
    :vartype type: str
    :param asset_name: Required. Asset Name
    :type asset_name: str
    :ivar created: The creation time of the Streaming Locator.
    :vartype created: datetime
    :param start_time: The start time of the Streaming Locator.
    :type start_time: datetime
    :param end_time: The end time of the Streaming Locator.
    :type end_time: datetime
    :param streaming_locator_id: The StreamingLocatorId of the Streaming
     Locator.
    :type streaming_locator_id: str
    :param streaming_policy_name: Required. Name of the Streaming Policy used
     by this Streaming Locator. Either specify the name of Streaming Policy you
     created or use one of the predefined Streaming Policies. The predefined
     Streaming Policies available are: 'Predefined_DownloadOnly',
     'Predefined_ClearStreamingOnly', 'Predefined_DownloadAndClearStreaming',
     'Predefined_ClearKey', 'Predefined_MultiDrmCencStreaming' and
     'Predefined_MultiDrmStreaming'
    :type streaming_policy_name: str
    :param default_content_key_policy_name: Name of the default
     ContentKeyPolicy used by this Streaming Locator.
    :type default_content_key_policy_name: str
    :param content_keys: The ContentKeys used by this Streaming Locator.
    :type content_keys:
     list[~azure.mgmt.media.models.StreamingLocatorContentKey]
    :param alternative_media_id: Alternative Media ID of this Streaming
     Locator
    :type alternative_media_id: str
    :param filters: A list of asset or account filters which apply to this
     streaming locator
    :type filters: list[str]
    """

    _validation = {
        'id': {'readonly': True},
        'name': {'readonly': True},
        'type': {'readonly': True},
        'asset_name': {'required': True},
        'created': {'readonly': True},
        'streaming_policy_name': {'required': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'asset_name': {'key': 'properties.assetName', 'type': 'str'},
        'created': {'key': 'properties.created', 'type': 'iso-8601'},
        'start_time': {'key': 'properties.startTime', 'type': 'iso-8601'},
        'end_time': {'key': 'properties.endTime', 'type': 'iso-8601'},
        'streaming_locator_id': {'key': 'properties.streamingLocatorId', 'type': 'str'},
        'streaming_policy_name': {'key': 'properties.streamingPolicyName', 'type': 'str'},
        'default_content_key_policy_name': {'key': 'properties.defaultContentKeyPolicyName', 'type': 'str'},
        'content_keys': {'key': 'properties.contentKeys', 'type': '[StreamingLocatorContentKey]'},
        'alternative_media_id': {'key': 'properties.alternativeMediaId', 'type': 'str'},
        'filters': {'key': 'properties.filters', 'type': '[str]'},
    }

    def __init__(self, **kwargs):
        super(StreamingLocator, self).__init__(**kwargs)
        self.asset_name = kwargs.get('asset_name', None)
        self.created = None
        self.start_time = kwargs.get('start_time', None)
        self.end_time = kwargs.get('end_time', None)
        self.streaming_locator_id = kwargs.get('streaming_locator_id', None)
        self.streaming_policy_name = kwargs.get('streaming_policy_name', None)
        self.default_content_key_policy_name = kwargs.get('default_content_key_policy_name', None)
        self.content_keys = kwargs.get('content_keys', None)
        self.alternative_media_id = kwargs.get('alternative_media_id', None)
        self.filters = kwargs.get('filters', None)
