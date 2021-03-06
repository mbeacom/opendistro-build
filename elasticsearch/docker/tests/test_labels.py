# Copyright 2019 Amazon.com, Inc. or its affiliates. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License").
# You may not use this file except in compliance with the License.
# A copy of the License is located at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# or in the "license" file accompanying this file. This file is distributed
# on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either
# express or implied. See the License for the specific language governing
# permissions and limitations under the License.

# Description:
# Test if the labels are correct

from .fixtures import elasticsearch


def test_labels(elasticsearch):
    labels = elasticsearch.docker_metadata['Config']['Labels']
    assert labels['org.label-schema.name'] == 'opendistroforelasticsearch'
    assert labels['org.label-schema.schema-version'] == '1.0'
    assert labels['org.label-schema.url'] == 'https://opendistro.github.io'
    assert labels['org.label-schema.vcs-url'] == 'https://github.com/opendistro-for-elasticsearch/opendistro-build'
    assert labels['org.label-schema.version'] == '0.9.0'
    assert labels['org.label-schema.license'] == 'Apache-2.0'
