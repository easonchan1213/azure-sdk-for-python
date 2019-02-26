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


class RdpConnection(Model):
    """Represents a .rdp file.

    :param contents: The contents of the .rdp file
    :type contents: str
    """

    _attribute_map = {
        'contents': {'key': 'contents', 'type': 'str'},
    }

    def __init__(self, *, contents: str=None, **kwargs) -> None:
        super(RdpConnection, self).__init__(**kwargs)
        self.contents = contents
