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


class QueryOptions(Model):
    """Additional parameters for a set of operations.

    :param top: Maximum number of records to return.
    :type top: int
    :param filter: OData filter expression.
    :type filter: str
    :param order_by: Ordering expression using OData notation. One or more
     comma-separated column names with an optional "desc" (the default) or
     "asc", e.g. "$orderby=PolicyAssignmentId, ResourceId asc".
    :type order_by: str
    :param select: Select expression using OData notation. Limits the columns
     on each record to just those requested, e.g. "$select=PolicyAssignmentId,
     ResourceId".
    :type select: str
    :param from_property: ISO 8601 formatted timestamp specifying the start
     time of the interval to query. When not specified, the service uses ($to -
     1-day).
    :type from_property: datetime
    :param to: ISO 8601 formatted timestamp specifying the end time of the
     interval to query. When not specified, the service uses request time.
    :type to: datetime
    :param apply: OData apply expression for aggregations.
    :type apply: str
    """

    _attribute_map = {
        'top': {'key': '', 'type': 'int'},
        'filter': {'key': '', 'type': 'str'},
        'order_by': {'key': '', 'type': 'str'},
        'select': {'key': '', 'type': 'str'},
        'from_property': {'key': '', 'type': 'iso-8601'},
        'to': {'key': '', 'type': 'iso-8601'},
        'apply': {'key': '', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(QueryOptions, self).__init__(**kwargs)
        self.top = kwargs.get('top', None)
        self.filter = kwargs.get('filter', None)
        self.order_by = kwargs.get('order_by', None)
        self.select = kwargs.get('select', None)
        self.from_property = kwargs.get('from_property', None)
        self.to = kwargs.get('to', None)
        self.apply = kwargs.get('apply', None)
