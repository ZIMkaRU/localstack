import sys
from datetime import datetime
from typing import List, Optional

if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict

from localstack.aws.api import RequestContext, ServiceException, ServiceRequest, handler

Boolean = bool
MaxResults = int
NextToken = str
OperatorValue = str
SelectorField = str
SelectorName = str
String = str


class EventCategory(str):
    insight = "insight"


class InsightType(str):
    ApiCallRateInsight = "ApiCallRateInsight"
    ApiErrorRateInsight = "ApiErrorRateInsight"


class LookupAttributeKey(str):
    EventId = "EventId"
    EventName = "EventName"
    ReadOnly = "ReadOnly"
    Username = "Username"
    ResourceType = "ResourceType"
    ResourceName = "ResourceName"
    EventSource = "EventSource"
    AccessKeyId = "AccessKeyId"


class ReadWriteType(str):
    ReadOnly = "ReadOnly"
    WriteOnly = "WriteOnly"
    All = "All"


class CloudTrailARNInvalidException(ServiceException):
    pass


class CloudTrailAccessNotEnabledException(ServiceException):
    pass


class CloudTrailInvalidClientTokenIdException(ServiceException):
    pass


class CloudWatchLogsDeliveryUnavailableException(ServiceException):
    pass


class ConflictException(ServiceException):
    pass


class InsightNotEnabledException(ServiceException):
    pass


class InsufficientDependencyServiceAccessPermissionException(ServiceException):
    pass


class InsufficientEncryptionPolicyException(ServiceException):
    pass


class InsufficientS3BucketPolicyException(ServiceException):
    pass


class InsufficientSnsTopicPolicyException(ServiceException):
    pass


class InvalidCloudWatchLogsLogGroupArnException(ServiceException):
    pass


class InvalidCloudWatchLogsRoleArnException(ServiceException):
    pass


class InvalidEventCategoryException(ServiceException):
    pass


class InvalidEventSelectorsException(ServiceException):
    pass


class InvalidHomeRegionException(ServiceException):
    pass


class InvalidInsightSelectorsException(ServiceException):
    pass


class InvalidKmsKeyIdException(ServiceException):
    pass


class InvalidLookupAttributesException(ServiceException):
    pass


class InvalidMaxResultsException(ServiceException):
    pass


class InvalidNextTokenException(ServiceException):
    pass


class InvalidParameterCombinationException(ServiceException):
    pass


class InvalidS3BucketNameException(ServiceException):
    pass


class InvalidS3PrefixException(ServiceException):
    pass


class InvalidSnsTopicNameException(ServiceException):
    pass


class InvalidTagParameterException(ServiceException):
    pass


class InvalidTimeRangeException(ServiceException):
    pass


class InvalidTokenException(ServiceException):
    pass


class InvalidTrailNameException(ServiceException):
    pass


class KmsException(ServiceException):
    pass


class KmsKeyDisabledException(ServiceException):
    pass


class KmsKeyNotFoundException(ServiceException):
    pass


class MaximumNumberOfTrailsExceededException(ServiceException):
    pass


class NotOrganizationMasterAccountException(ServiceException):
    pass


class OperationNotPermittedException(ServiceException):
    pass


class OrganizationNotInAllFeaturesModeException(ServiceException):
    pass


class OrganizationsNotInUseException(ServiceException):
    pass


class ResourceNotFoundException(ServiceException):
    pass


class ResourceTypeNotSupportedException(ServiceException):
    pass


class S3BucketDoesNotExistException(ServiceException):
    pass


class TagsLimitExceededException(ServiceException):
    pass


class TrailAlreadyExistsException(ServiceException):
    pass


class TrailNotFoundException(ServiceException):
    pass


class TrailNotProvidedException(ServiceException):
    pass


class UnsupportedOperationException(ServiceException):
    pass


class Tag(TypedDict, total=False):
    Key: String
    Value: Optional[String]


TagsList = List[Tag]


class AddTagsRequest(ServiceRequest):
    ResourceId: String
    TagsList: Optional[TagsList]


class AddTagsResponse(TypedDict, total=False):
    pass


Operator = List[OperatorValue]


class AdvancedFieldSelector(TypedDict, total=False):
    Field: SelectorField
    Equals: Optional[Operator]
    StartsWith: Optional[Operator]
    EndsWith: Optional[Operator]
    NotEquals: Optional[Operator]
    NotStartsWith: Optional[Operator]
    NotEndsWith: Optional[Operator]


AdvancedFieldSelectors = List[AdvancedFieldSelector]


class AdvancedEventSelector(TypedDict, total=False):
    Name: Optional[SelectorName]
    FieldSelectors: AdvancedFieldSelectors


AdvancedEventSelectors = List[AdvancedEventSelector]
ByteBuffer = bytes


class CreateTrailRequest(ServiceRequest):
    Name: String
    S3BucketName: String
    S3KeyPrefix: Optional[String]
    SnsTopicName: Optional[String]
    IncludeGlobalServiceEvents: Optional[Boolean]
    IsMultiRegionTrail: Optional[Boolean]
    EnableLogFileValidation: Optional[Boolean]
    CloudWatchLogsLogGroupArn: Optional[String]
    CloudWatchLogsRoleArn: Optional[String]
    KmsKeyId: Optional[String]
    IsOrganizationTrail: Optional[Boolean]
    TagsList: Optional[TagsList]


class CreateTrailResponse(TypedDict, total=False):
    Name: Optional[String]
    S3BucketName: Optional[String]
    S3KeyPrefix: Optional[String]
    SnsTopicName: Optional[String]
    SnsTopicARN: Optional[String]
    IncludeGlobalServiceEvents: Optional[Boolean]
    IsMultiRegionTrail: Optional[Boolean]
    TrailARN: Optional[String]
    LogFileValidationEnabled: Optional[Boolean]
    CloudWatchLogsLogGroupArn: Optional[String]
    CloudWatchLogsRoleArn: Optional[String]
    KmsKeyId: Optional[String]
    IsOrganizationTrail: Optional[Boolean]


DataResourceValues = List[String]


class DataResource(TypedDict, total=False):
    Type: Optional[String]
    Values: Optional[DataResourceValues]


DataResources = List[DataResource]
Date = datetime


class DeleteTrailRequest(ServiceRequest):
    Name: String


class DeleteTrailResponse(TypedDict, total=False):
    pass


TrailNameList = List[String]


class DescribeTrailsRequest(ServiceRequest):
    trailNameList: Optional[TrailNameList]
    includeShadowTrails: Optional[Boolean]


class Trail(TypedDict, total=False):
    Name: Optional[String]
    S3BucketName: Optional[String]
    S3KeyPrefix: Optional[String]
    SnsTopicName: Optional[String]
    SnsTopicARN: Optional[String]
    IncludeGlobalServiceEvents: Optional[Boolean]
    IsMultiRegionTrail: Optional[Boolean]
    HomeRegion: Optional[String]
    TrailARN: Optional[String]
    LogFileValidationEnabled: Optional[Boolean]
    CloudWatchLogsLogGroupArn: Optional[String]
    CloudWatchLogsRoleArn: Optional[String]
    KmsKeyId: Optional[String]
    HasCustomEventSelectors: Optional[Boolean]
    HasInsightSelectors: Optional[Boolean]
    IsOrganizationTrail: Optional[Boolean]


TrailList = List[Trail]


class DescribeTrailsResponse(TypedDict, total=False):
    trailList: Optional[TrailList]


class Resource(TypedDict, total=False):
    ResourceType: Optional[String]
    ResourceName: Optional[String]


ResourceList = List[Resource]


class Event(TypedDict, total=False):
    EventId: Optional[String]
    EventName: Optional[String]
    ReadOnly: Optional[String]
    AccessKeyId: Optional[String]
    EventTime: Optional[Date]
    EventSource: Optional[String]
    Username: Optional[String]
    Resources: Optional[ResourceList]
    CloudTrailEvent: Optional[String]


ExcludeManagementEventSources = List[String]


class EventSelector(TypedDict, total=False):
    ReadWriteType: Optional[ReadWriteType]
    IncludeManagementEvents: Optional[Boolean]
    DataResources: Optional[DataResources]
    ExcludeManagementEventSources: Optional[ExcludeManagementEventSources]


EventSelectors = List[EventSelector]
EventsList = List[Event]


class GetEventSelectorsRequest(ServiceRequest):
    TrailName: String


class GetEventSelectorsResponse(TypedDict, total=False):
    TrailARN: Optional[String]
    EventSelectors: Optional[EventSelectors]
    AdvancedEventSelectors: Optional[AdvancedEventSelectors]


class GetInsightSelectorsRequest(ServiceRequest):
    TrailName: String


class InsightSelector(TypedDict, total=False):
    InsightType: Optional[InsightType]


InsightSelectors = List[InsightSelector]


class GetInsightSelectorsResponse(TypedDict, total=False):
    TrailARN: Optional[String]
    InsightSelectors: Optional[InsightSelectors]


class GetTrailRequest(ServiceRequest):
    Name: String


class GetTrailResponse(TypedDict, total=False):
    Trail: Optional[Trail]


class GetTrailStatusRequest(ServiceRequest):
    Name: String


class GetTrailStatusResponse(TypedDict, total=False):
    IsLogging: Optional[Boolean]
    LatestDeliveryError: Optional[String]
    LatestNotificationError: Optional[String]
    LatestDeliveryTime: Optional[Date]
    LatestNotificationTime: Optional[Date]
    StartLoggingTime: Optional[Date]
    StopLoggingTime: Optional[Date]
    LatestCloudWatchLogsDeliveryError: Optional[String]
    LatestCloudWatchLogsDeliveryTime: Optional[Date]
    LatestDigestDeliveryTime: Optional[Date]
    LatestDigestDeliveryError: Optional[String]
    LatestDeliveryAttemptTime: Optional[String]
    LatestNotificationAttemptTime: Optional[String]
    LatestNotificationAttemptSucceeded: Optional[String]
    LatestDeliveryAttemptSucceeded: Optional[String]
    TimeLoggingStarted: Optional[String]
    TimeLoggingStopped: Optional[String]


class ListPublicKeysRequest(ServiceRequest):
    StartTime: Optional[Date]
    EndTime: Optional[Date]
    NextToken: Optional[String]


class PublicKey(TypedDict, total=False):
    Value: Optional[ByteBuffer]
    ValidityStartTime: Optional[Date]
    ValidityEndTime: Optional[Date]
    Fingerprint: Optional[String]


PublicKeyList = List[PublicKey]


class ListPublicKeysResponse(TypedDict, total=False):
    PublicKeyList: Optional[PublicKeyList]
    NextToken: Optional[String]


ResourceIdList = List[String]


class ListTagsRequest(ServiceRequest):
    ResourceIdList: ResourceIdList
    NextToken: Optional[String]


class ResourceTag(TypedDict, total=False):
    ResourceId: Optional[String]
    TagsList: Optional[TagsList]


ResourceTagList = List[ResourceTag]


class ListTagsResponse(TypedDict, total=False):
    ResourceTagList: Optional[ResourceTagList]
    NextToken: Optional[String]


class ListTrailsRequest(ServiceRequest):
    NextToken: Optional[String]


class TrailInfo(TypedDict, total=False):
    TrailARN: Optional[String]
    Name: Optional[String]
    HomeRegion: Optional[String]


Trails = List[TrailInfo]


class ListTrailsResponse(TypedDict, total=False):
    Trails: Optional[Trails]
    NextToken: Optional[String]


class LookupAttribute(TypedDict, total=False):
    AttributeKey: LookupAttributeKey
    AttributeValue: String


LookupAttributesList = List[LookupAttribute]


class LookupEventsRequest(ServiceRequest):
    LookupAttributes: Optional[LookupAttributesList]
    StartTime: Optional[Date]
    EndTime: Optional[Date]
    EventCategory: Optional[EventCategory]
    MaxResults: Optional[MaxResults]
    NextToken: Optional[NextToken]


class LookupEventsResponse(TypedDict, total=False):
    Events: Optional[EventsList]
    NextToken: Optional[NextToken]


class PutEventSelectorsRequest(ServiceRequest):
    TrailName: String
    EventSelectors: Optional[EventSelectors]
    AdvancedEventSelectors: Optional[AdvancedEventSelectors]


class PutEventSelectorsResponse(TypedDict, total=False):
    TrailARN: Optional[String]
    EventSelectors: Optional[EventSelectors]
    AdvancedEventSelectors: Optional[AdvancedEventSelectors]


class PutInsightSelectorsRequest(ServiceRequest):
    TrailName: String
    InsightSelectors: InsightSelectors


class PutInsightSelectorsResponse(TypedDict, total=False):
    TrailARN: Optional[String]
    InsightSelectors: Optional[InsightSelectors]


class RemoveTagsRequest(ServiceRequest):
    ResourceId: String
    TagsList: Optional[TagsList]


class RemoveTagsResponse(TypedDict, total=False):
    pass


class StartLoggingRequest(ServiceRequest):
    Name: String


class StartLoggingResponse(TypedDict, total=False):
    pass


class StopLoggingRequest(ServiceRequest):
    Name: String


class StopLoggingResponse(TypedDict, total=False):
    pass


class UpdateTrailRequest(ServiceRequest):
    Name: String
    S3BucketName: Optional[String]
    S3KeyPrefix: Optional[String]
    SnsTopicName: Optional[String]
    IncludeGlobalServiceEvents: Optional[Boolean]
    IsMultiRegionTrail: Optional[Boolean]
    EnableLogFileValidation: Optional[Boolean]
    CloudWatchLogsLogGroupArn: Optional[String]
    CloudWatchLogsRoleArn: Optional[String]
    KmsKeyId: Optional[String]
    IsOrganizationTrail: Optional[Boolean]


class UpdateTrailResponse(TypedDict, total=False):
    Name: Optional[String]
    S3BucketName: Optional[String]
    S3KeyPrefix: Optional[String]
    SnsTopicName: Optional[String]
    SnsTopicARN: Optional[String]
    IncludeGlobalServiceEvents: Optional[Boolean]
    IsMultiRegionTrail: Optional[Boolean]
    TrailARN: Optional[String]
    LogFileValidationEnabled: Optional[Boolean]
    CloudWatchLogsLogGroupArn: Optional[String]
    CloudWatchLogsRoleArn: Optional[String]
    KmsKeyId: Optional[String]
    IsOrganizationTrail: Optional[Boolean]


class CloudtrailApi:

    service = "cloudtrail"
    version = "2013-11-01"

    @handler("AddTags")
    def add_tags(
        self, context: RequestContext, resource_id: String, tags_list: TagsList = None
    ) -> AddTagsResponse:
        raise NotImplementedError

    @handler("CreateTrail")
    def create_trail(
        self,
        context: RequestContext,
        name: String,
        s3_bucket_name: String,
        s3_key_prefix: String = None,
        sns_topic_name: String = None,
        include_global_service_events: Boolean = None,
        is_multi_region_trail: Boolean = None,
        enable_log_file_validation: Boolean = None,
        cloud_watch_logs_log_group_arn: String = None,
        cloud_watch_logs_role_arn: String = None,
        kms_key_id: String = None,
        is_organization_trail: Boolean = None,
        tags_list: TagsList = None,
    ) -> CreateTrailResponse:
        raise NotImplementedError

    @handler("DeleteTrail")
    def delete_trail(self, context: RequestContext, name: String) -> DeleteTrailResponse:
        raise NotImplementedError

    @handler("DescribeTrails")
    def describe_trails(
        self,
        context: RequestContext,
        trail_name_list: TrailNameList = None,
        include_shadow_trails: Boolean = None,
    ) -> DescribeTrailsResponse:
        raise NotImplementedError

    @handler("GetEventSelectors")
    def get_event_selectors(
        self, context: RequestContext, trail_name: String
    ) -> GetEventSelectorsResponse:
        raise NotImplementedError

    @handler("GetInsightSelectors")
    def get_insight_selectors(
        self, context: RequestContext, trail_name: String
    ) -> GetInsightSelectorsResponse:
        raise NotImplementedError

    @handler("GetTrail")
    def get_trail(self, context: RequestContext, name: String) -> GetTrailResponse:
        raise NotImplementedError

    @handler("GetTrailStatus")
    def get_trail_status(self, context: RequestContext, name: String) -> GetTrailStatusResponse:
        raise NotImplementedError

    @handler("ListPublicKeys")
    def list_public_keys(
        self,
        context: RequestContext,
        start_time: Date = None,
        end_time: Date = None,
        next_token: String = None,
    ) -> ListPublicKeysResponse:
        raise NotImplementedError

    @handler("ListTags")
    def list_tags(
        self,
        context: RequestContext,
        resource_id_list: ResourceIdList,
        next_token: String = None,
    ) -> ListTagsResponse:
        raise NotImplementedError

    @handler("ListTrails")
    def list_trails(self, context: RequestContext, next_token: String = None) -> ListTrailsResponse:
        raise NotImplementedError

    @handler("LookupEvents")
    def lookup_events(
        self,
        context: RequestContext,
        lookup_attributes: LookupAttributesList = None,
        start_time: Date = None,
        end_time: Date = None,
        event_category: EventCategory = None,
        max_results: MaxResults = None,
        next_token: NextToken = None,
    ) -> LookupEventsResponse:
        raise NotImplementedError

    @handler("PutEventSelectors")
    def put_event_selectors(
        self,
        context: RequestContext,
        trail_name: String,
        event_selectors: EventSelectors = None,
        advanced_event_selectors: AdvancedEventSelectors = None,
    ) -> PutEventSelectorsResponse:
        raise NotImplementedError

    @handler("PutInsightSelectors")
    def put_insight_selectors(
        self,
        context: RequestContext,
        trail_name: String,
        insight_selectors: InsightSelectors,
    ) -> PutInsightSelectorsResponse:
        raise NotImplementedError

    @handler("RemoveTags")
    def remove_tags(
        self, context: RequestContext, resource_id: String, tags_list: TagsList = None
    ) -> RemoveTagsResponse:
        raise NotImplementedError

    @handler("StartLogging")
    def start_logging(self, context: RequestContext, name: String) -> StartLoggingResponse:
        raise NotImplementedError

    @handler("StopLogging")
    def stop_logging(self, context: RequestContext, name: String) -> StopLoggingResponse:
        raise NotImplementedError

    @handler("UpdateTrail")
    def update_trail(
        self,
        context: RequestContext,
        name: String,
        s3_bucket_name: String = None,
        s3_key_prefix: String = None,
        sns_topic_name: String = None,
        include_global_service_events: Boolean = None,
        is_multi_region_trail: Boolean = None,
        enable_log_file_validation: Boolean = None,
        cloud_watch_logs_log_group_arn: String = None,
        cloud_watch_logs_role_arn: String = None,
        kms_key_id: String = None,
        is_organization_trail: Boolean = None,
    ) -> UpdateTrailResponse:
        raise NotImplementedError
