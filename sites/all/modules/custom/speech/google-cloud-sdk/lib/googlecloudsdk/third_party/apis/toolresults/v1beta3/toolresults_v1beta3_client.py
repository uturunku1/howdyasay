"""Generated client library for toolresults version v1beta3."""
# NOTE: This file is autogenerated and should not be edited by hand.
from apitools.base.py import base_api
from googlecloudsdk.third_party.apis.toolresults.v1beta3 import toolresults_v1beta3_messages as messages


class ToolresultsV1beta3(base_api.BaseApiClient):
  """Generated client library for service toolresults version v1beta3."""

  MESSAGES_MODULE = messages
  BASE_URL = u'https://www.googleapis.com/toolresults/v1beta3/'

  _PACKAGE = u'toolresults'
  _SCOPES = [u'https://www.googleapis.com/auth/cloud-platform']
  _VERSION = u'v1beta3'
  _CLIENT_ID = '1042881264118.apps.googleusercontent.com'
  _CLIENT_SECRET = 'x_Tw5K8nnjoRAqULM9PFAC2b'
  _USER_AGENT = 'x_Tw5K8nnjoRAqULM9PFAC2b'
  _CLIENT_CLASS_NAME = u'ToolresultsV1beta3'
  _URL_VERSION = u'v1beta3'
  _API_KEY = None

  def __init__(self, url='', credentials=None,
               get_credentials=True, http=None, model=None,
               log_request=False, log_response=False,
               credentials_args=None, default_global_params=None,
               additional_http_headers=None):
    """Create a new toolresults handle."""
    url = url or self.BASE_URL
    super(ToolresultsV1beta3, self).__init__(
        url, credentials=credentials,
        get_credentials=get_credentials, http=http, model=model,
        log_request=log_request, log_response=log_response,
        credentials_args=credentials_args,
        default_global_params=default_global_params,
        additional_http_headers=additional_http_headers)
    self.projects_histories_executions_steps_perfMetricsSummary = self.ProjectsHistoriesExecutionsStepsPerfMetricsSummaryService(self)
    self.projects_histories_executions_steps_perfSampleSeries_samples = self.ProjectsHistoriesExecutionsStepsPerfSampleSeriesSamplesService(self)
    self.projects_histories_executions_steps_perfSampleSeries = self.ProjectsHistoriesExecutionsStepsPerfSampleSeriesService(self)
    self.projects_histories_executions_steps_thumbnails = self.ProjectsHistoriesExecutionsStepsThumbnailsService(self)
    self.projects_histories_executions_steps = self.ProjectsHistoriesExecutionsStepsService(self)
    self.projects_histories_executions = self.ProjectsHistoriesExecutionsService(self)
    self.projects_histories = self.ProjectsHistoriesService(self)
    self.projects = self.ProjectsService(self)

  class ProjectsHistoriesExecutionsStepsPerfMetricsSummaryService(base_api.BaseApiService):
    """Service class for the projects_histories_executions_steps_perfMetricsSummary resource."""

    _NAME = u'projects_histories_executions_steps_perfMetricsSummary'

    def __init__(self, client):
      super(ToolresultsV1beta3.ProjectsHistoriesExecutionsStepsPerfMetricsSummaryService, self).__init__(client)
      self._upload_configs = {
          }

    def Create(self, request, global_params=None):
      """Creates a PerfMetricsSummary resource.

May return any of the following error code(s): - ALREADY_EXISTS - A PerfMetricSummary already exists for the given Step - NOT_FOUND - The containing Step does not exist

      Args:
        request: (PerfMetricsSummary) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (PerfMetricsSummary) The response message.
      """
      config = self.GetMethodConfig('Create')
      return self._RunMethod(
          config, request, global_params=global_params)

    Create.method_config = lambda: base_api.ApiMethodInfo(
        http_method=u'POST',
        method_id=u'toolresults.projects.histories.executions.steps.perfMetricsSummary.create',
        ordered_params=[u'projectId', u'historyId', u'executionId', u'stepId'],
        path_params=[u'executionId', u'historyId', u'projectId', u'stepId'],
        query_params=[],
        relative_path=u'projects/{projectId}/histories/{historyId}/executions/{executionId}/steps/{stepId}/perfMetricsSummary',
        request_field='<request>',
        request_type_name=u'PerfMetricsSummary',
        response_type_name=u'PerfMetricsSummary',
        supports_download=False,
    )

  class ProjectsHistoriesExecutionsStepsPerfSampleSeriesSamplesService(base_api.BaseApiService):
    """Service class for the projects_histories_executions_steps_perfSampleSeries_samples resource."""

    _NAME = u'projects_histories_executions_steps_perfSampleSeries_samples'

    def __init__(self, client):
      super(ToolresultsV1beta3.ProjectsHistoriesExecutionsStepsPerfSampleSeriesSamplesService, self).__init__(client)
      self._upload_configs = {
          }

    def BatchCreate(self, request, global_params=None):
      """Creates a batch of PerfSamples - a client can submit multiple batches of Perf Samples through repeated calls to this method in order to split up a large request payload - duplicates and existing timestamp entries will be ignored. - the batch operation may partially succeed - the set of elements successfully inserted is returned in the response (omits items which already existed in the database).

May return any of the following canonical error codes: - NOT_FOUND - The containing PerfSampleSeries does not exist

      Args:
        request: (ToolresultsProjectsHistoriesExecutionsStepsPerfSampleSeriesSamplesBatchCreateRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (BatchCreatePerfSamplesResponse) The response message.
      """
      config = self.GetMethodConfig('BatchCreate')
      return self._RunMethod(
          config, request, global_params=global_params)

    BatchCreate.method_config = lambda: base_api.ApiMethodInfo(
        http_method=u'POST',
        method_id=u'toolresults.projects.histories.executions.steps.perfSampleSeries.samples.batchCreate',
        ordered_params=[u'projectId', u'historyId', u'executionId', u'stepId', u'sampleSeriesId'],
        path_params=[u'executionId', u'historyId', u'projectId', u'sampleSeriesId', u'stepId'],
        query_params=[],
        relative_path=u'projects/{projectId}/histories/{historyId}/executions/{executionId}/steps/{stepId}/perfSampleSeries/{sampleSeriesId}/samples:batchCreate',
        request_field=u'batchCreatePerfSamplesRequest',
        request_type_name=u'ToolresultsProjectsHistoriesExecutionsStepsPerfSampleSeriesSamplesBatchCreateRequest',
        response_type_name=u'BatchCreatePerfSamplesResponse',
        supports_download=False,
    )

    def List(self, request, global_params=None):
      """Lists the Performance Samples of a given Sample Series - The list results are sorted by timestamps ascending - The default page size is 500 samples; and maximum size allowed 5000 - The response token indicates the last returned PerfSample timestamp - When the results size exceeds the page size, submit a subsequent request including the page token to return the rest of the samples up to the page limit.

May return any of the following canonical error codes: - OUT_OF_RANGE - The specified request page_token is out of valid range - NOT_FOUND - The containing PerfSampleSeries does not exist

      Args:
        request: (ToolresultsProjectsHistoriesExecutionsStepsPerfSampleSeriesSamplesListRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (ListPerfSamplesResponse) The response message.
      """
      config = self.GetMethodConfig('List')
      return self._RunMethod(
          config, request, global_params=global_params)

    List.method_config = lambda: base_api.ApiMethodInfo(
        http_method=u'GET',
        method_id=u'toolresults.projects.histories.executions.steps.perfSampleSeries.samples.list',
        ordered_params=[u'projectId', u'historyId', u'executionId', u'stepId', u'sampleSeriesId'],
        path_params=[u'executionId', u'historyId', u'projectId', u'sampleSeriesId', u'stepId'],
        query_params=[u'pageSize', u'pageToken'],
        relative_path=u'projects/{projectId}/histories/{historyId}/executions/{executionId}/steps/{stepId}/perfSampleSeries/{sampleSeriesId}/samples',
        request_field='',
        request_type_name=u'ToolresultsProjectsHistoriesExecutionsStepsPerfSampleSeriesSamplesListRequest',
        response_type_name=u'ListPerfSamplesResponse',
        supports_download=False,
    )

  class ProjectsHistoriesExecutionsStepsPerfSampleSeriesService(base_api.BaseApiService):
    """Service class for the projects_histories_executions_steps_perfSampleSeries resource."""

    _NAME = u'projects_histories_executions_steps_perfSampleSeries'

    def __init__(self, client):
      super(ToolresultsV1beta3.ProjectsHistoriesExecutionsStepsPerfSampleSeriesService, self).__init__(client)
      self._upload_configs = {
          }

    def Create(self, request, global_params=None):
      """Creates a PerfSampleSeries.

May return any of the following error code(s): - ALREADY_EXISTS - PerfMetricSummary already exists for the given Step - NOT_FOUND - The containing Step does not exist

      Args:
        request: (PerfSampleSeries) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (PerfSampleSeries) The response message.
      """
      config = self.GetMethodConfig('Create')
      return self._RunMethod(
          config, request, global_params=global_params)

    Create.method_config = lambda: base_api.ApiMethodInfo(
        http_method=u'POST',
        method_id=u'toolresults.projects.histories.executions.steps.perfSampleSeries.create',
        ordered_params=[u'projectId', u'historyId', u'executionId', u'stepId'],
        path_params=[u'executionId', u'historyId', u'projectId', u'stepId'],
        query_params=[],
        relative_path=u'projects/{projectId}/histories/{historyId}/executions/{executionId}/steps/{stepId}/perfSampleSeries',
        request_field='<request>',
        request_type_name=u'PerfSampleSeries',
        response_type_name=u'PerfSampleSeries',
        supports_download=False,
    )

    def Get(self, request, global_params=None):
      """Gets a PerfSampleSeries.

May return any of the following error code(s): - NOT_FOUND - The specified PerfSampleSeries does not exist

      Args:
        request: (ToolresultsProjectsHistoriesExecutionsStepsPerfSampleSeriesGetRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (PerfSampleSeries) The response message.
      """
      config = self.GetMethodConfig('Get')
      return self._RunMethod(
          config, request, global_params=global_params)

    Get.method_config = lambda: base_api.ApiMethodInfo(
        http_method=u'GET',
        method_id=u'toolresults.projects.histories.executions.steps.perfSampleSeries.get',
        ordered_params=[u'projectId', u'historyId', u'executionId', u'stepId', u'sampleSeriesId'],
        path_params=[u'executionId', u'historyId', u'projectId', u'sampleSeriesId', u'stepId'],
        query_params=[],
        relative_path=u'projects/{projectId}/histories/{historyId}/executions/{executionId}/steps/{stepId}/perfSampleSeries/{sampleSeriesId}',
        request_field='',
        request_type_name=u'ToolresultsProjectsHistoriesExecutionsStepsPerfSampleSeriesGetRequest',
        response_type_name=u'PerfSampleSeries',
        supports_download=False,
    )

    def List(self, request, global_params=None):
      """Lists PerfSampleSeries for a given Step.

The request provides an optional filter which specifies one or more PerfMetricsType to include in the result; if none returns all. The resulting PerfSampleSeries are sorted by ids.

May return any of the following canonical error codes: - NOT_FOUND - The containing Step does not exist

      Args:
        request: (ToolresultsProjectsHistoriesExecutionsStepsPerfSampleSeriesListRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (ListPerfSampleSeriesResponse) The response message.
      """
      config = self.GetMethodConfig('List')
      return self._RunMethod(
          config, request, global_params=global_params)

    List.method_config = lambda: base_api.ApiMethodInfo(
        http_method=u'GET',
        method_id=u'toolresults.projects.histories.executions.steps.perfSampleSeries.list',
        ordered_params=[u'projectId', u'historyId', u'executionId', u'stepId'],
        path_params=[u'executionId', u'historyId', u'projectId', u'stepId'],
        query_params=[u'filter'],
        relative_path=u'projects/{projectId}/histories/{historyId}/executions/{executionId}/steps/{stepId}/perfSampleSeries',
        request_field='',
        request_type_name=u'ToolresultsProjectsHistoriesExecutionsStepsPerfSampleSeriesListRequest',
        response_type_name=u'ListPerfSampleSeriesResponse',
        supports_download=False,
    )

  class ProjectsHistoriesExecutionsStepsThumbnailsService(base_api.BaseApiService):
    """Service class for the projects_histories_executions_steps_thumbnails resource."""

    _NAME = u'projects_histories_executions_steps_thumbnails'

    def __init__(self, client):
      super(ToolresultsV1beta3.ProjectsHistoriesExecutionsStepsThumbnailsService, self).__init__(client)
      self._upload_configs = {
          }

    def List(self, request, global_params=None):
      """Lists thumbnails of images attached to a step.

May return any of the following canonical error codes: - PERMISSION_DENIED - if the user is not authorized to read from the project, or from any of the images - INVALID_ARGUMENT - if the request is malformed - NOT_FOUND - if the step does not exist, or if any of the images do not exist

      Args:
        request: (ToolresultsProjectsHistoriesExecutionsStepsThumbnailsListRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (ListStepThumbnailsResponse) The response message.
      """
      config = self.GetMethodConfig('List')
      return self._RunMethod(
          config, request, global_params=global_params)

    List.method_config = lambda: base_api.ApiMethodInfo(
        http_method=u'GET',
        method_id=u'toolresults.projects.histories.executions.steps.thumbnails.list',
        ordered_params=[u'projectId', u'historyId', u'executionId', u'stepId'],
        path_params=[u'executionId', u'historyId', u'projectId', u'stepId'],
        query_params=[u'pageSize', u'pageToken'],
        relative_path=u'projects/{projectId}/histories/{historyId}/executions/{executionId}/steps/{stepId}/thumbnails',
        request_field='',
        request_type_name=u'ToolresultsProjectsHistoriesExecutionsStepsThumbnailsListRequest',
        response_type_name=u'ListStepThumbnailsResponse',
        supports_download=False,
    )

  class ProjectsHistoriesExecutionsStepsService(base_api.BaseApiService):
    """Service class for the projects_histories_executions_steps resource."""

    _NAME = u'projects_histories_executions_steps'

    def __init__(self, client):
      super(ToolresultsV1beta3.ProjectsHistoriesExecutionsStepsService, self).__init__(client)
      self._upload_configs = {
          }

    def Create(self, request, global_params=None):
      """Creates a Step.

The returned Step will have the id set.

May return any of the following canonical error codes:

- PERMISSION_DENIED - if the user is not authorized to write to project - INVALID_ARGUMENT - if the request is malformed - FAILED_PRECONDITION - if the step is too large (more than 10Mib) - NOT_FOUND - if the containing Execution does not exist

      Args:
        request: (ToolresultsProjectsHistoriesExecutionsStepsCreateRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Step) The response message.
      """
      config = self.GetMethodConfig('Create')
      return self._RunMethod(
          config, request, global_params=global_params)

    Create.method_config = lambda: base_api.ApiMethodInfo(
        http_method=u'POST',
        method_id=u'toolresults.projects.histories.executions.steps.create',
        ordered_params=[u'projectId', u'historyId', u'executionId'],
        path_params=[u'executionId', u'historyId', u'projectId'],
        query_params=[u'requestId'],
        relative_path=u'projects/{projectId}/histories/{historyId}/executions/{executionId}/steps',
        request_field=u'step',
        request_type_name=u'ToolresultsProjectsHistoriesExecutionsStepsCreateRequest',
        response_type_name=u'Step',
        supports_download=False,
    )

    def Get(self, request, global_params=None):
      """Gets a Step.

May return any of the following canonical error codes:

- PERMISSION_DENIED - if the user is not authorized to read project - INVALID_ARGUMENT - if the request is malformed - NOT_FOUND - if the Step does not exist

      Args:
        request: (ToolresultsProjectsHistoriesExecutionsStepsGetRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Step) The response message.
      """
      config = self.GetMethodConfig('Get')
      return self._RunMethod(
          config, request, global_params=global_params)

    Get.method_config = lambda: base_api.ApiMethodInfo(
        http_method=u'GET',
        method_id=u'toolresults.projects.histories.executions.steps.get',
        ordered_params=[u'projectId', u'historyId', u'executionId', u'stepId'],
        path_params=[u'executionId', u'historyId', u'projectId', u'stepId'],
        query_params=[],
        relative_path=u'projects/{projectId}/histories/{historyId}/executions/{executionId}/steps/{stepId}',
        request_field='',
        request_type_name=u'ToolresultsProjectsHistoriesExecutionsStepsGetRequest',
        response_type_name=u'Step',
        supports_download=False,
    )

    def GetPerfMetricsSummary(self, request, global_params=None):
      """Retrieves a PerfMetricsSummary.

May return any of the following error code(s): - NOT_FOUND - The specified PerfMetricsSummary does not exist

      Args:
        request: (ToolresultsProjectsHistoriesExecutionsStepsGetPerfMetricsSummaryRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (PerfMetricsSummary) The response message.
      """
      config = self.GetMethodConfig('GetPerfMetricsSummary')
      return self._RunMethod(
          config, request, global_params=global_params)

    GetPerfMetricsSummary.method_config = lambda: base_api.ApiMethodInfo(
        http_method=u'GET',
        method_id=u'toolresults.projects.histories.executions.steps.getPerfMetricsSummary',
        ordered_params=[u'projectId', u'historyId', u'executionId', u'stepId'],
        path_params=[u'executionId', u'historyId', u'projectId', u'stepId'],
        query_params=[],
        relative_path=u'projects/{projectId}/histories/{historyId}/executions/{executionId}/steps/{stepId}/perfMetricsSummary',
        request_field='',
        request_type_name=u'ToolresultsProjectsHistoriesExecutionsStepsGetPerfMetricsSummaryRequest',
        response_type_name=u'PerfMetricsSummary',
        supports_download=False,
    )

    def List(self, request, global_params=None):
      """Lists Steps for a given Execution.

The steps are sorted by creation_time in descending order. The step_id key will be used to order the steps with the same creation_time.

May return any of the following canonical error codes:

- PERMISSION_DENIED - if the user is not authorized to read project - INVALID_ARGUMENT - if the request is malformed - FAILED_PRECONDITION - if an argument in the request happens to be invalid; e.g. if an attempt is made to list the children of a nonexistent Step - NOT_FOUND - if the containing Execution does not exist

      Args:
        request: (ToolresultsProjectsHistoriesExecutionsStepsListRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (ListStepsResponse) The response message.
      """
      config = self.GetMethodConfig('List')
      return self._RunMethod(
          config, request, global_params=global_params)

    List.method_config = lambda: base_api.ApiMethodInfo(
        http_method=u'GET',
        method_id=u'toolresults.projects.histories.executions.steps.list',
        ordered_params=[u'projectId', u'historyId', u'executionId'],
        path_params=[u'executionId', u'historyId', u'projectId'],
        query_params=[u'pageSize', u'pageToken'],
        relative_path=u'projects/{projectId}/histories/{historyId}/executions/{executionId}/steps',
        request_field='',
        request_type_name=u'ToolresultsProjectsHistoriesExecutionsStepsListRequest',
        response_type_name=u'ListStepsResponse',
        supports_download=False,
    )

    def Patch(self, request, global_params=None):
      """Updates an existing Step with the supplied partial entity.

May return any of the following canonical error codes:

- PERMISSION_DENIED - if the user is not authorized to write project - INVALID_ARGUMENT - if the request is malformed - FAILED_PRECONDITION - if the requested state transition is illegal (e.g try to upload a duplicate xml file), if the updated step is too large (more than 10Mib) - NOT_FOUND - if the containing Execution does not exist

      Args:
        request: (ToolresultsProjectsHistoriesExecutionsStepsPatchRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Step) The response message.
      """
      config = self.GetMethodConfig('Patch')
      return self._RunMethod(
          config, request, global_params=global_params)

    Patch.method_config = lambda: base_api.ApiMethodInfo(
        http_method=u'PATCH',
        method_id=u'toolresults.projects.histories.executions.steps.patch',
        ordered_params=[u'projectId', u'historyId', u'executionId', u'stepId'],
        path_params=[u'executionId', u'historyId', u'projectId', u'stepId'],
        query_params=[u'requestId'],
        relative_path=u'projects/{projectId}/histories/{historyId}/executions/{executionId}/steps/{stepId}',
        request_field=u'step',
        request_type_name=u'ToolresultsProjectsHistoriesExecutionsStepsPatchRequest',
        response_type_name=u'Step',
        supports_download=False,
    )

    def PublishXunitXmlFiles(self, request, global_params=None):
      """Publish xml files to an existing Step.

May return any of the following canonical error codes:

- PERMISSION_DENIED - if the user is not authorized to write project - INVALID_ARGUMENT - if the request is malformed - FAILED_PRECONDITION - if the requested state transition is illegal, e.g try to upload a duplicate xml file or a file too large. - NOT_FOUND - if the containing Execution does not exist

      Args:
        request: (ToolresultsProjectsHistoriesExecutionsStepsPublishXunitXmlFilesRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Step) The response message.
      """
      config = self.GetMethodConfig('PublishXunitXmlFiles')
      return self._RunMethod(
          config, request, global_params=global_params)

    PublishXunitXmlFiles.method_config = lambda: base_api.ApiMethodInfo(
        http_method=u'POST',
        method_id=u'toolresults.projects.histories.executions.steps.publishXunitXmlFiles',
        ordered_params=[u'projectId', u'historyId', u'executionId', u'stepId'],
        path_params=[u'executionId', u'historyId', u'projectId', u'stepId'],
        query_params=[],
        relative_path=u'projects/{projectId}/histories/{historyId}/executions/{executionId}/steps/{stepId}:publishXunitXmlFiles',
        request_field=u'publishXunitXmlFilesRequest',
        request_type_name=u'ToolresultsProjectsHistoriesExecutionsStepsPublishXunitXmlFilesRequest',
        response_type_name=u'Step',
        supports_download=False,
    )

  class ProjectsHistoriesExecutionsService(base_api.BaseApiService):
    """Service class for the projects_histories_executions resource."""

    _NAME = u'projects_histories_executions'

    def __init__(self, client):
      super(ToolresultsV1beta3.ProjectsHistoriesExecutionsService, self).__init__(client)
      self._upload_configs = {
          }

    def Create(self, request, global_params=None):
      """Creates an Execution.

The returned Execution will have the id set.

May return any of the following canonical error codes:

- PERMISSION_DENIED - if the user is not authorized to write to project - INVALID_ARGUMENT - if the request is malformed - NOT_FOUND - if the containing History does not exist

      Args:
        request: (ToolresultsProjectsHistoriesExecutionsCreateRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Execution) The response message.
      """
      config = self.GetMethodConfig('Create')
      return self._RunMethod(
          config, request, global_params=global_params)

    Create.method_config = lambda: base_api.ApiMethodInfo(
        http_method=u'POST',
        method_id=u'toolresults.projects.histories.executions.create',
        ordered_params=[u'projectId', u'historyId'],
        path_params=[u'historyId', u'projectId'],
        query_params=[u'requestId'],
        relative_path=u'projects/{projectId}/histories/{historyId}/executions',
        request_field=u'execution',
        request_type_name=u'ToolresultsProjectsHistoriesExecutionsCreateRequest',
        response_type_name=u'Execution',
        supports_download=False,
    )

    def Get(self, request, global_params=None):
      """Gets an Execution.

May return any of the following canonical error codes:

- PERMISSION_DENIED - if the user is not authorized to write to project - INVALID_ARGUMENT - if the request is malformed - NOT_FOUND - if the Execution does not exist

      Args:
        request: (ToolresultsProjectsHistoriesExecutionsGetRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Execution) The response message.
      """
      config = self.GetMethodConfig('Get')
      return self._RunMethod(
          config, request, global_params=global_params)

    Get.method_config = lambda: base_api.ApiMethodInfo(
        http_method=u'GET',
        method_id=u'toolresults.projects.histories.executions.get',
        ordered_params=[u'projectId', u'historyId', u'executionId'],
        path_params=[u'executionId', u'historyId', u'projectId'],
        query_params=[],
        relative_path=u'projects/{projectId}/histories/{historyId}/executions/{executionId}',
        request_field='',
        request_type_name=u'ToolresultsProjectsHistoriesExecutionsGetRequest',
        response_type_name=u'Execution',
        supports_download=False,
    )

    def List(self, request, global_params=None):
      """Lists Histories for a given Project.

The executions are sorted by creation_time in descending order. The execution_id key will be used to order the executions with the same creation_time.

May return any of the following canonical error codes:

- PERMISSION_DENIED - if the user is not authorized to read project - INVALID_ARGUMENT - if the request is malformed - NOT_FOUND - if the containing History does not exist

      Args:
        request: (ToolresultsProjectsHistoriesExecutionsListRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (ListExecutionsResponse) The response message.
      """
      config = self.GetMethodConfig('List')
      return self._RunMethod(
          config, request, global_params=global_params)

    List.method_config = lambda: base_api.ApiMethodInfo(
        http_method=u'GET',
        method_id=u'toolresults.projects.histories.executions.list',
        ordered_params=[u'projectId', u'historyId'],
        path_params=[u'historyId', u'projectId'],
        query_params=[u'pageSize', u'pageToken'],
        relative_path=u'projects/{projectId}/histories/{historyId}/executions',
        request_field='',
        request_type_name=u'ToolresultsProjectsHistoriesExecutionsListRequest',
        response_type_name=u'ListExecutionsResponse',
        supports_download=False,
    )

    def Patch(self, request, global_params=None):
      """Updates an existing Execution with the supplied partial entity.

May return any of the following canonical error codes:

- PERMISSION_DENIED - if the user is not authorized to write to project - INVALID_ARGUMENT - if the request is malformed - FAILED_PRECONDITION - if the requested state transition is illegal - NOT_FOUND - if the containing History does not exist

      Args:
        request: (ToolresultsProjectsHistoriesExecutionsPatchRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (Execution) The response message.
      """
      config = self.GetMethodConfig('Patch')
      return self._RunMethod(
          config, request, global_params=global_params)

    Patch.method_config = lambda: base_api.ApiMethodInfo(
        http_method=u'PATCH',
        method_id=u'toolresults.projects.histories.executions.patch',
        ordered_params=[u'projectId', u'historyId', u'executionId'],
        path_params=[u'executionId', u'historyId', u'projectId'],
        query_params=[u'requestId'],
        relative_path=u'projects/{projectId}/histories/{historyId}/executions/{executionId}',
        request_field=u'execution',
        request_type_name=u'ToolresultsProjectsHistoriesExecutionsPatchRequest',
        response_type_name=u'Execution',
        supports_download=False,
    )

  class ProjectsHistoriesService(base_api.BaseApiService):
    """Service class for the projects_histories resource."""

    _NAME = u'projects_histories'

    def __init__(self, client):
      super(ToolresultsV1beta3.ProjectsHistoriesService, self).__init__(client)
      self._upload_configs = {
          }

    def Create(self, request, global_params=None):
      """Creates a History.

The returned History will have the id set.

May return any of the following canonical error codes:

- PERMISSION_DENIED - if the user is not authorized to write to project - INVALID_ARGUMENT - if the request is malformed - NOT_FOUND - if the containing project does not exist

      Args:
        request: (ToolresultsProjectsHistoriesCreateRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (History) The response message.
      """
      config = self.GetMethodConfig('Create')
      return self._RunMethod(
          config, request, global_params=global_params)

    Create.method_config = lambda: base_api.ApiMethodInfo(
        http_method=u'POST',
        method_id=u'toolresults.projects.histories.create',
        ordered_params=[u'projectId'],
        path_params=[u'projectId'],
        query_params=[u'requestId'],
        relative_path=u'projects/{projectId}/histories',
        request_field=u'history',
        request_type_name=u'ToolresultsProjectsHistoriesCreateRequest',
        response_type_name=u'History',
        supports_download=False,
    )

    def Get(self, request, global_params=None):
      """Gets a History.

May return any of the following canonical error codes:

- PERMISSION_DENIED - if the user is not authorized to read project - INVALID_ARGUMENT - if the request is malformed - NOT_FOUND - if the History does not exist

      Args:
        request: (ToolresultsProjectsHistoriesGetRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (History) The response message.
      """
      config = self.GetMethodConfig('Get')
      return self._RunMethod(
          config, request, global_params=global_params)

    Get.method_config = lambda: base_api.ApiMethodInfo(
        http_method=u'GET',
        method_id=u'toolresults.projects.histories.get',
        ordered_params=[u'projectId', u'historyId'],
        path_params=[u'historyId', u'projectId'],
        query_params=[],
        relative_path=u'projects/{projectId}/histories/{historyId}',
        request_field='',
        request_type_name=u'ToolresultsProjectsHistoriesGetRequest',
        response_type_name=u'History',
        supports_download=False,
    )

    def List(self, request, global_params=None):
      """Lists Histories for a given Project.

The histories are sorted by modification time in descending order. The history_id key will be used to order the history with the same modification time.

May return any of the following canonical error codes:

- PERMISSION_DENIED - if the user is not authorized to read project - INVALID_ARGUMENT - if the request is malformed - NOT_FOUND - if the History does not exist

      Args:
        request: (ToolresultsProjectsHistoriesListRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (ListHistoriesResponse) The response message.
      """
      config = self.GetMethodConfig('List')
      return self._RunMethod(
          config, request, global_params=global_params)

    List.method_config = lambda: base_api.ApiMethodInfo(
        http_method=u'GET',
        method_id=u'toolresults.projects.histories.list',
        ordered_params=[u'projectId'],
        path_params=[u'projectId'],
        query_params=[u'filterByName', u'pageSize', u'pageToken'],
        relative_path=u'projects/{projectId}/histories',
        request_field='',
        request_type_name=u'ToolresultsProjectsHistoriesListRequest',
        response_type_name=u'ListHistoriesResponse',
        supports_download=False,
    )

  class ProjectsService(base_api.BaseApiService):
    """Service class for the projects resource."""

    _NAME = u'projects'

    def __init__(self, client):
      super(ToolresultsV1beta3.ProjectsService, self).__init__(client)
      self._upload_configs = {
          }

    def GetSettings(self, request, global_params=None):
      """Gets the Tool Results settings for a project.

May return any of the following canonical error codes:

- PERMISSION_DENIED - if the user is not authorized to read from project

      Args:
        request: (ToolresultsProjectsGetSettingsRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (ProjectSettings) The response message.
      """
      config = self.GetMethodConfig('GetSettings')
      return self._RunMethod(
          config, request, global_params=global_params)

    GetSettings.method_config = lambda: base_api.ApiMethodInfo(
        http_method=u'GET',
        method_id=u'toolresults.projects.getSettings',
        ordered_params=[u'projectId'],
        path_params=[u'projectId'],
        query_params=[],
        relative_path=u'projects/{projectId}/settings',
        request_field='',
        request_type_name=u'ToolresultsProjectsGetSettingsRequest',
        response_type_name=u'ProjectSettings',
        supports_download=False,
    )

    def InitializeSettings(self, request, global_params=None):
      """Creates resources for settings which have not yet been set.

Currently, this creates a single resource: a Google Cloud Storage bucket, to be used as the default bucket for this project. The bucket is created in the name of the user calling. Except in rare cases, calling this method in parallel from multiple clients will only create a single bucket. In order to avoid unnecessary storage charges, the bucket is configured to automatically delete objects older than 90 days.

The bucket is created with the project-private ACL: All project team members are given permissions to the bucket and objects created within it according to their roles. Project owners have owners rights, and so on. The default ACL on objects created in the bucket is project-private as well. See Google Cloud Storage documentation for more details.

If there is already a default bucket set and the project can access the bucket, this call does nothing. However, if the project doesn't have the permission to access the bucket or the bucket is deteleted, a new bucket will be created.

May return any canonical error codes, including the following:

- PERMISSION_DENIED - if the user is not authorized to write to project - Any error code raised by Google Cloud Storage

      Args:
        request: (ToolresultsProjectsInitializeSettingsRequest) input message
        global_params: (StandardQueryParameters, default: None) global arguments
      Returns:
        (ProjectSettings) The response message.
      """
      config = self.GetMethodConfig('InitializeSettings')
      return self._RunMethod(
          config, request, global_params=global_params)

    InitializeSettings.method_config = lambda: base_api.ApiMethodInfo(
        http_method=u'POST',
        method_id=u'toolresults.projects.initializeSettings',
        ordered_params=[u'projectId'],
        path_params=[u'projectId'],
        query_params=[],
        relative_path=u'projects/{projectId}:initializeSettings',
        request_field='',
        request_type_name=u'ToolresultsProjectsInitializeSettingsRequest',
        response_type_name=u'ProjectSettings',
        supports_download=False,
    )
