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


class TranslateResultAllItem(Model):
    """TranslateResultAllItem.

    :param detected_language:
    :type detected_language:
     ~azure.cognitiveservices.translatortext.models.TranslateResultAllItemDetectedLanguage
    :param translations:
    :type translations:
     list[~azure.cognitiveservices.translatortext.models.TranslateResultAllItemTranslationsItem]
    """

    _attribute_map = {
        'detected_language': {'key': 'detectedLanguage', 'type': 'TranslateResultAllItemDetectedLanguage'},
        'translations': {'key': 'translations', 'type': '[TranslateResultAllItemTranslationsItem]'},
    }

    def __init__(self, **kwargs):
        super(TranslateResultAllItem, self).__init__(**kwargs)
        self.detected_language = kwargs.get('detected_language', None)
        self.translations = kwargs.get('translations', None)
