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


class Category(Model):
    """An object describing identified category.

    :param name: Name of the category.
    :type name: str
    :param score: Scoring of the category.
    :type score: float
    :param detail:
    :type detail:
     ~azure.cognitiveservices.vision.computervision.models.CategoryDetail
    """

    _attribute_map = {
        'name': {'key': 'name', 'type': 'str'},
        'score': {'key': 'score', 'type': 'float'},
        'detail': {'key': 'detail', 'type': 'CategoryDetail'},
    }

    def __init__(self, **kwargs):
        super(Category, self).__init__(**kwargs)
        self.name = kwargs.get('name', None)
        self.score = kwargs.get('score', None)
        self.detail = kwargs.get('detail', None)
