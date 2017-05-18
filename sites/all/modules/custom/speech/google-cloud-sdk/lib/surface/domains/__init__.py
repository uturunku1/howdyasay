# Copyright 2017 Google Inc. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""The gcloud domains group."""

from googlecloudsdk.calliope import base
from googlecloudsdk.core import exceptions
from googlecloudsdk.core import log
from googlecloudsdk.core import properties
from googlecloudsdk.core import resources
from googlecloudsdk.core.util import platforms


@base.ReleaseTracks(base.ReleaseTrack.BETA)
class Domains(base.Group):
  """Base class for gcloud domains command group."""

  detailed_help = {
      'brief': 'Manage domains for your Google Cloud projects.',
      'DESCRIPTION': """
          The gcloud domains command group lets you view and manage your
          custom domains for use across Google projects.
          """,
      'EXAMPLES': """\
          To verify a domain you own, run:

            $ {command} verify example.com

          To list your verified domains, run:

            $ {command} list-user-verified
          """
  }
