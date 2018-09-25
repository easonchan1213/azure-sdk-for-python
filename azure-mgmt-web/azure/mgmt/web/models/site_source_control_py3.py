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

from .proxy_only_resource_py3 import ProxyOnlyResource


class SiteSourceControl(ProxyOnlyResource):
    """Source control configuration for an app.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :ivar id: Resource Id.
    :vartype id: str
    :ivar name: Resource Name.
    :vartype name: str
    :param kind: Kind of resource.
    :type kind: str
    :ivar type: Resource type.
    :vartype type: str
    :param repo_url: Repository or source control URL.
    :type repo_url: str
    :param branch: Name of branch to use for deployment.
    :type branch: str
    :param is_manual_integration: <code>true</code> to limit to manual
     integration; <code>false</code> to enable continuous integration (which
     configures webhooks into online repos like GitHub).
    :type is_manual_integration: bool
    :param deployment_rollback_enabled: <code>true</code> to enable deployment
     rollback; otherwise, <code>false</code>.
    :type deployment_rollback_enabled: bool
    :param is_mercurial: <code>true</code> for a Mercurial repository;
     <code>false</code> for a Git repository.
    :type is_mercurial: bool
    """

    _validation = {
        'id': {'readonly': True},
        'name': {'readonly': True},
        'type': {'readonly': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'kind': {'key': 'kind', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'repo_url': {'key': 'properties.repoUrl', 'type': 'str'},
        'branch': {'key': 'properties.branch', 'type': 'str'},
        'is_manual_integration': {'key': 'properties.isManualIntegration', 'type': 'bool'},
        'deployment_rollback_enabled': {'key': 'properties.deploymentRollbackEnabled', 'type': 'bool'},
        'is_mercurial': {'key': 'properties.isMercurial', 'type': 'bool'},
    }

    def __init__(self, *, kind: str=None, repo_url: str=None, branch: str=None, is_manual_integration: bool=None, deployment_rollback_enabled: bool=None, is_mercurial: bool=None, **kwargs) -> None:
        super(SiteSourceControl, self).__init__(kind=kind, **kwargs)
        self.repo_url = repo_url
        self.branch = branch
        self.is_manual_integration = is_manual_integration
        self.deployment_rollback_enabled = deployment_rollback_enabled
        self.is_mercurial = is_mercurial
