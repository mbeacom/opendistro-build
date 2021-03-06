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
# Test if the lables is correct in the dockerfile

from .fixtures import kibana


def test_labels(kibana):
    labels = kibana.docker_metadata['Config']['Labels']
    assert labels['org.label-schema.name'] == 'opendistroforelasticsearch-kibana'
    assert labels['org.label-schema.schema-version'] == '1.0'
    assert labels['org.label-schema.url'] == 'https://opendistro.github.io'
    assert labels['org.label-schema.vcs-url'] == 'https://github.com/opendistro-for-elasticsearch/opendistro-build'
    assert labels['org.label-schema.vendor'] == 'Amazon'
    assert labels['org.label-schema.version'] == '0.9.0'
