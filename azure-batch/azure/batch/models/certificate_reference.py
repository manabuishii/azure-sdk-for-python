# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft and contributors.  All rights reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#
# See the License for the specific language governing permissions and
# limitations under the License.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class CertificateReference(Model):
    """
    A reference to a certificate to be installed on compute nodes in a pool.

    :param thumbprint: Gets or sets the thumbprint of the certificate.
    :type thumbprint: str
    :param thumbprint_algorithm: Gets or sets the algorithm with which the
     thumbprint is associated.  This must be sha1.
    :type thumbprint_algorithm: str
    :param store_location: Gets or sets the location of the certificate store
     on the compute node into which to install the certificate. The default
     value is CurrentUser. Possible values include: 'currentuser',
     'localmachine', 'unmapped'
    :type store_location: str
    :param store_name: Gets or sets the name of the certificate store on the
     compute node into which to install the certificate. The default value is
     My.
    :type store_name: str
    :param visibility: Gets or sets which user accounts on the compute node
     should have access to the private data of the certificate. This may be
     any subset of the values 'starttask', 'task' and 'remoteuser', separated
     by commas. The default is all accounts, corresponding to the string
     'starttask,task,remoteuser'.
    :type visibility: list of str
    """ 

    _validation = {
        'thumbprint': {'required': True},
        'thumbprint_algorithm': {'required': True},
    }

    _attribute_map = {
        'thumbprint': {'key': 'thumbprint', 'type': 'str'},
        'thumbprint_algorithm': {'key': 'thumbprintAlgorithm', 'type': 'str'},
        'store_location': {'key': 'storeLocation', 'type': 'CertificateStoreLocation'},
        'store_name': {'key': 'storeName', 'type': 'str'},
        'visibility': {'key': 'visibility', 'type': '[CertificateVisibility]'},
    }

    def __init__(self, thumbprint, thumbprint_algorithm, store_location=None, store_name=None, visibility=None):
        self.thumbprint = thumbprint
        self.thumbprint_algorithm = thumbprint_algorithm
        self.store_location = store_location
        self.store_name = store_name
        self.visibility = visibility