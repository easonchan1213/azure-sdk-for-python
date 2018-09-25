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


class TaskFailureInformation(Model):
    """Information about a task failure.

    All required parameters must be populated in order to send to Azure.

    :param category: Required. The category of the task error. Possible values
     include: 'userError', 'serverError'
    :type category: str or ~azure.batch.models.ErrorCategory
    :param code: An identifier for the task error. Codes are invariant and are
     intended to be consumed programmatically.
    :type code: str
    :param message: A message describing the task error, intended to be
     suitable for display in a user interface.
    :type message: str
    :param details: A list of additional details related to the error.
    :type details: list[~azure.batch.models.NameValuePair]
    """

    _validation = {
        'category': {'required': True},
    }

    _attribute_map = {
        'category': {'key': 'category', 'type': 'ErrorCategory'},
        'code': {'key': 'code', 'type': 'str'},
        'message': {'key': 'message', 'type': 'str'},
        'details': {'key': 'details', 'type': '[NameValuePair]'},
    }

    def __init__(self, **kwargs):
        super(TaskFailureInformation, self).__init__(**kwargs)
        self.category = kwargs.get('category', None)
        self.code = kwargs.get('code', None)
        self.message = kwargs.get('message', None)
        self.details = kwargs.get('details', None)
