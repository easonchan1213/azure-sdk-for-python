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


class LanguagesResultDictionary(Model):
    """LanguagesResultDictionary.

    :param language_code:
    :type language_code:
     ~azure.cognitiveservices.translatortext.models.LanguagesResultDictionaryLanguageCode
    """

    _attribute_map = {
        'language_code': {'key': 'languageCode', 'type': 'LanguagesResultDictionaryLanguageCode'},
    }

    def __init__(self, *, language_code=None, **kwargs) -> None:
        super(LanguagesResultDictionary, self).__init__(**kwargs)
        self.language_code = language_code
