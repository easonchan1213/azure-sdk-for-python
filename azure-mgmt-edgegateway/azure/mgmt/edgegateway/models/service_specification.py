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


class ServiceSpecification(Model):
    """Service specification.

    :param metric_specifications: Metric specification as defined by shoebox.
    :type metric_specifications:
     list[~azure.mgmt.edgegateway.models.MetricSpecificationV1]
    """

    _attribute_map = {
        'metric_specifications': {'key': 'metricSpecifications', 'type': '[MetricSpecificationV1]'},
    }

    def __init__(self, **kwargs):
        super(ServiceSpecification, self).__init__(**kwargs)
        self.metric_specifications = kwargs.get('metric_specifications', None)
