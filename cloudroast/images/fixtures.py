"""
Copyright 2013 Rackspace

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
"""

from cafe.drivers.unittest.fixtures import BaseTestFixture
from cloudcafe.images.config import ImagesConfig
from cloudcafe.common.resources import ResourcePool


class ImagesFixture(BaseTestFixture):
    @classmethod
    def setUpClass(cls):
        super(ImagesFixture, cls).setUpClass()
        cls.config = ImagesConfig()
        cls.resources = ResourcePool()

    @classmethod
    def tearDownClass(cls):
        cls.resources.release()
        super(ImagesFixture, cls).tearDownClass()
