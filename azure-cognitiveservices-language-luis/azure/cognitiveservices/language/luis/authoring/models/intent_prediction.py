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


class IntentPrediction(Model):
    """A suggested intent.

    :param name: The intent's name
    :type name: str
    :param score: The intent's score, based on the prediction model.
    :type score: float
    """

    _attribute_map = {
        'name': {'key': 'name', 'type': 'str'},
        'score': {'key': 'score', 'type': 'float'},
    }

    def __init__(self, **kwargs):
        super(IntentPrediction, self).__init__(**kwargs)
        self.name = kwargs.get('name', None)
        self.score = kwargs.get('score', None)
