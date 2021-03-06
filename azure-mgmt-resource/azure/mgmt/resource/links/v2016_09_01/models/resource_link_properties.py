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


class ResourceLinkProperties(Model):
    """The resource link properties.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :ivar source_id: The fully qualified ID of the source resource in the
     link.
    :vartype source_id: str
    :param target_id: The fully qualified ID of the target resource in the
     link.
    :type target_id: str
    :param notes: Notes about the resource link.
    :type notes: str
    """

    _validation = {
        'source_id': {'readonly': True},
        'target_id': {'required': True},
    }

    _attribute_map = {
        'source_id': {'key': 'sourceId', 'type': 'str'},
        'target_id': {'key': 'targetId', 'type': 'str'},
        'notes': {'key': 'notes', 'type': 'str'},
    }

    def __init__(self, target_id, notes=None):
        self.source_id = None
        self.target_id = target_id
        self.notes = notes
