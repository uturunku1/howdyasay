# Copyright 2016 Google Inc. All Rights Reserved.
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
"""Utilities for ml-engine operations commands."""
from googlecloudsdk.core import properties
from googlecloudsdk.core import resources


def Cancel(operations_client, operation):
  operation_ref = resources.REGISTRY.Parse(
      operation,
      params={'projectsId': properties.VALUES.core.project.GetOrFail},
      collection='ml.projects.operations')
  return operations_client.Cancel(operation_ref)


def Delete(operations_client, operation):
  operation_ref = resources.REGISTRY.Parse(
      operation,
      params={'projectsId': properties.VALUES.core.project.GetOrFail},
      collection='ml.projects.operations')
  return operations_client.Delete(operation_ref)


def Describe(operations_client, operation):
  operation_ref = resources.REGISTRY.Parse(
      operation,
      params={'projectsId': properties.VALUES.core.project.GetOrFail},
      collection='ml.projects.operations')
  return operations_client.Get(operation_ref)


def List(operations_client):
  project_ref = resources.REGISTRY.Parse(
      properties.VALUES.core.project.GetOrFail(),
      collection='ml.projects')
  return operations_client.List(project_ref)


def Wait(operations_client, operation):
  operation_ref = resources.REGISTRY.Parse(
      operation,
      params={'projectsId': properties.VALUES.core.project.GetOrFail},
      collection='ml.projects.operations')
  operation = operations_client.Get(operation_ref)
  return operations_client.WaitForOperation(operation)
