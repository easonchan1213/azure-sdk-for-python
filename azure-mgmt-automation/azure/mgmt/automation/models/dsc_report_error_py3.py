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


class DscReportError(Model):
    """Definition of the dsc node report error type.

    :param error_source: Gets or sets the source of the error.
    :type error_source: str
    :param resource_id: Gets or sets the resource ID which generated the
     error.
    :type resource_id: str
    :param error_code: Gets or sets the error code.
    :type error_code: str
    :param error_message: Gets or sets the error message.
    :type error_message: str
    :param locale: Gets or sets the locale of the error.
    :type locale: str
    :param error_details: Gets or sets the error details.
    :type error_details: str
    """

    _attribute_map = {
        'error_source': {'key': 'errorSource', 'type': 'str'},
        'resource_id': {'key': 'resourceId', 'type': 'str'},
        'error_code': {'key': 'errorCode', 'type': 'str'},
        'error_message': {'key': 'errorMessage', 'type': 'str'},
        'locale': {'key': 'locale', 'type': 'str'},
        'error_details': {'key': 'errorDetails', 'type': 'str'},
    }

    def __init__(self, *, error_source: str=None, resource_id: str=None, error_code: str=None, error_message: str=None, locale: str=None, error_details: str=None, **kwargs) -> None:
        super(DscReportError, self).__init__(**kwargs)
        self.error_source = error_source
        self.resource_id = resource_id
        self.error_code = error_code
        self.error_message = error_message
        self.locale = locale
        self.error_details = error_details
