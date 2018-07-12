# -*- coding: utf-8 -*-
# Copyright 2018, CS Systemes d'Information, http://www.c-s.fr
#
# This file is part of EODAG project
#     https://www.github.com/CS-SI/EODAG
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
from __future__ import unicode_literals

# All tests files should import mock from this place
try:
    from unittest import mock  # PY3
except ImportError:
    import mock  # PY2


def no_blanks(string):
    """Removes all the blanks in string

    :param string: A string to remove blanks from
    :type string: str | unicode (PY2 only)

    :returns the same string with all blank characters removed
    """
    return string.replace('\n', '').replace('\t', '').replace(' ', '')
