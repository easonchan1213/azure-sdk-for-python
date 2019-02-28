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


class DictionaryLookupResultItemTranslationsItem(Model):
    """DictionaryLookupResultItemTranslationsItem.

    :param normalized_target:
    :type normalized_target: str
    :param display_target:
    :type display_target: str
    :param pos_tag:
    :type pos_tag: str
    :param confidence:
    :type confidence: float
    :param prefix_word:
    :type prefix_word: str
    :param back_translations:
    :type back_translations:
     list[~azure.cognitiveservices.translatortext.models.DictionaryLookupResultItemTranslationsItemBackTranslationsItem]
    """

    _attribute_map = {
        'normalized_target': {'key': 'normalizedTarget', 'type': 'str'},
        'display_target': {'key': 'displayTarget', 'type': 'str'},
        'pos_tag': {'key': 'posTag', 'type': 'str'},
        'confidence': {'key': 'confidence', 'type': 'float'},
        'prefix_word': {'key': 'prefixWord', 'type': 'str'},
        'back_translations': {'key': 'backTranslations', 'type': '[DictionaryLookupResultItemTranslationsItemBackTranslationsItem]'},
    }

    def __init__(self, *, normalized_target: str=None, display_target: str=None, pos_tag: str=None, confidence: float=None, prefix_word: str=None, back_translations=None, **kwargs) -> None:
        super(DictionaryLookupResultItemTranslationsItem, self).__init__(**kwargs)
        self.normalized_target = normalized_target
        self.display_target = display_target
        self.pos_tag = pos_tag
        self.confidence = confidence
        self.prefix_word = prefix_word
        self.back_translations = back_translations
