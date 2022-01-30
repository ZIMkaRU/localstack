import sys
from typing import List, Optional

if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict

from localstack.aws.api import RequestContext, ServiceException, ServiceRequest, handler

MaxItems = int
__boolean = bool
__double = float
__integer = int
__string = str


class Capability(str):
    CAPABILITY_IAM = "CAPABILITY_IAM"
    CAPABILITY_NAMED_IAM = "CAPABILITY_NAMED_IAM"
    CAPABILITY_AUTO_EXPAND = "CAPABILITY_AUTO_EXPAND"
    CAPABILITY_RESOURCE_POLICY = "CAPABILITY_RESOURCE_POLICY"


class Status(str):
    PREPARING = "PREPARING"
    ACTIVE = "ACTIVE"
    EXPIRED = "EXPIRED"


class BadRequestException(ServiceException):
    ErrorCode: Optional[__string]
    Message: Optional[__string]


class ConflictException(ServiceException):
    ErrorCode: Optional[__string]
    Message: Optional[__string]


class ForbiddenException(ServiceException):
    ErrorCode: Optional[__string]
    Message: Optional[__string]


class InternalServerErrorException(ServiceException):
    ErrorCode: Optional[__string]
    Message: Optional[__string]


class NotFoundException(ServiceException):
    ErrorCode: Optional[__string]
    Message: Optional[__string]


class TooManyRequestsException(ServiceException):
    ErrorCode: Optional[__string]
    Message: Optional[__string]


__listOfCapability = List[Capability]
__listOf__string = List[__string]


class ParameterDefinition(TypedDict, total=False):
    AllowedPattern: Optional[__string]
    AllowedValues: Optional[__listOf__string]
    ConstraintDescription: Optional[__string]
    DefaultValue: Optional[__string]
    Description: Optional[__string]
    MaxLength: Optional[__integer]
    MaxValue: Optional[__integer]
    MinLength: Optional[__integer]
    MinValue: Optional[__integer]
    Name: __string
    NoEcho: Optional[__boolean]
    ReferencedByResources: __listOf__string
    Type: Optional[__string]


__listOfParameterDefinition = List[ParameterDefinition]


class Version(TypedDict, total=False):
    ApplicationId: __string
    CreationTime: __string
    ParameterDefinitions: __listOfParameterDefinition
    RequiredCapabilities: __listOfCapability
    ResourcesSupported: __boolean
    SemanticVersion: __string
    SourceCodeArchiveUrl: Optional[__string]
    SourceCodeUrl: Optional[__string]
    TemplateUrl: __string


class Application(TypedDict, total=False):
    ApplicationId: __string
    Author: __string
    CreationTime: Optional[__string]
    Description: __string
    HomePageUrl: Optional[__string]
    IsVerifiedAuthor: Optional[__boolean]
    Labels: Optional[__listOf__string]
    LicenseUrl: Optional[__string]
    Name: __string
    ReadmeUrl: Optional[__string]
    SpdxLicenseId: Optional[__string]
    VerifiedAuthorUrl: Optional[__string]
    Version: Optional[Version]


class ApplicationDependencySummary(TypedDict, total=False):
    ApplicationId: __string
    SemanticVersion: __string


__listOfApplicationDependencySummary = List[ApplicationDependencySummary]


class ApplicationDependencyPage(TypedDict, total=False):
    Dependencies: __listOfApplicationDependencySummary
    NextToken: Optional[__string]


class ApplicationSummary(TypedDict, total=False):
    ApplicationId: __string
    Author: __string
    CreationTime: Optional[__string]
    Description: __string
    HomePageUrl: Optional[__string]
    Labels: Optional[__listOf__string]
    Name: __string
    SpdxLicenseId: Optional[__string]


__listOfApplicationSummary = List[ApplicationSummary]


class ApplicationPage(TypedDict, total=False):
    Applications: __listOfApplicationSummary
    NextToken: Optional[__string]


class ApplicationPolicyStatement(TypedDict, total=False):
    Actions: __listOf__string
    PrincipalOrgIDs: Optional[__listOf__string]
    Principals: __listOf__string
    StatementId: Optional[__string]


__listOfApplicationPolicyStatement = List[ApplicationPolicyStatement]


class ApplicationPolicy(TypedDict, total=False):
    Statements: __listOfApplicationPolicyStatement


class VersionSummary(TypedDict, total=False):
    ApplicationId: __string
    CreationTime: __string
    SemanticVersion: __string
    SourceCodeUrl: Optional[__string]


__listOfVersionSummary = List[VersionSummary]


class ApplicationVersionPage(TypedDict, total=False):
    NextToken: Optional[__string]
    Versions: __listOfVersionSummary


class ChangeSetDetails(TypedDict, total=False):
    ApplicationId: __string
    ChangeSetId: __string
    SemanticVersion: __string
    StackId: __string


class CreateApplicationInput(TypedDict, total=False):
    Author: __string
    Description: __string
    HomePageUrl: Optional[__string]
    Labels: Optional[__listOf__string]
    LicenseBody: Optional[__string]
    LicenseUrl: Optional[__string]
    Name: __string
    ReadmeBody: Optional[__string]
    ReadmeUrl: Optional[__string]
    SemanticVersion: Optional[__string]
    SourceCodeArchiveUrl: Optional[__string]
    SourceCodeUrl: Optional[__string]
    SpdxLicenseId: Optional[__string]
    TemplateBody: Optional[__string]
    TemplateUrl: Optional[__string]


class CreateApplicationRequest(ServiceRequest):
    Author: __string
    Description: __string
    HomePageUrl: Optional[__string]
    Labels: Optional[__listOf__string]
    LicenseBody: Optional[__string]
    LicenseUrl: Optional[__string]
    Name: __string
    ReadmeBody: Optional[__string]
    ReadmeUrl: Optional[__string]
    SemanticVersion: Optional[__string]
    SourceCodeArchiveUrl: Optional[__string]
    SourceCodeUrl: Optional[__string]
    SpdxLicenseId: Optional[__string]
    TemplateBody: Optional[__string]
    TemplateUrl: Optional[__string]


class CreateApplicationResponse(TypedDict, total=False):
    ApplicationId: Optional[__string]
    Author: Optional[__string]
    CreationTime: Optional[__string]
    Description: Optional[__string]
    HomePageUrl: Optional[__string]
    IsVerifiedAuthor: Optional[__boolean]
    Labels: Optional[__listOf__string]
    LicenseUrl: Optional[__string]
    Name: Optional[__string]
    ReadmeUrl: Optional[__string]
    SpdxLicenseId: Optional[__string]
    VerifiedAuthorUrl: Optional[__string]
    Version: Optional[Version]


class CreateApplicationVersionInput(TypedDict, total=False):
    SourceCodeArchiveUrl: Optional[__string]
    SourceCodeUrl: Optional[__string]
    TemplateBody: Optional[__string]
    TemplateUrl: Optional[__string]


class CreateApplicationVersionRequest(ServiceRequest):
    ApplicationId: __string
    SemanticVersion: __string
    SourceCodeArchiveUrl: Optional[__string]
    SourceCodeUrl: Optional[__string]
    TemplateBody: Optional[__string]
    TemplateUrl: Optional[__string]


class CreateApplicationVersionResponse(TypedDict, total=False):
    ApplicationId: Optional[__string]
    CreationTime: Optional[__string]
    ParameterDefinitions: Optional[__listOfParameterDefinition]
    RequiredCapabilities: Optional[__listOfCapability]
    ResourcesSupported: Optional[__boolean]
    SemanticVersion: Optional[__string]
    SourceCodeArchiveUrl: Optional[__string]
    SourceCodeUrl: Optional[__string]
    TemplateUrl: Optional[__string]


class Tag(TypedDict, total=False):
    Key: __string
    Value: __string


__listOfTag = List[Tag]


class RollbackTrigger(TypedDict, total=False):
    Arn: __string
    Type: __string


__listOfRollbackTrigger = List[RollbackTrigger]


class RollbackConfiguration(TypedDict, total=False):
    MonitoringTimeInMinutes: Optional[__integer]
    RollbackTriggers: Optional[__listOfRollbackTrigger]


class ParameterValue(TypedDict, total=False):
    Name: __string
    Value: __string


__listOfParameterValue = List[ParameterValue]


class CreateCloudFormationChangeSetInput(TypedDict, total=False):
    Capabilities: Optional[__listOf__string]
    ChangeSetName: Optional[__string]
    ClientToken: Optional[__string]
    Description: Optional[__string]
    NotificationArns: Optional[__listOf__string]
    ParameterOverrides: Optional[__listOfParameterValue]
    ResourceTypes: Optional[__listOf__string]
    RollbackConfiguration: Optional[RollbackConfiguration]
    SemanticVersion: Optional[__string]
    StackName: __string
    Tags: Optional[__listOfTag]
    TemplateId: Optional[__string]


class CreateCloudFormationChangeSetRequest(ServiceRequest):
    ApplicationId: __string
    Capabilities: Optional[__listOf__string]
    ChangeSetName: Optional[__string]
    ClientToken: Optional[__string]
    Description: Optional[__string]
    NotificationArns: Optional[__listOf__string]
    ParameterOverrides: Optional[__listOfParameterValue]
    ResourceTypes: Optional[__listOf__string]
    RollbackConfiguration: Optional[RollbackConfiguration]
    SemanticVersion: Optional[__string]
    StackName: __string
    Tags: Optional[__listOfTag]
    TemplateId: Optional[__string]


class CreateCloudFormationChangeSetResponse(TypedDict, total=False):
    ApplicationId: Optional[__string]
    ChangeSetId: Optional[__string]
    SemanticVersion: Optional[__string]
    StackId: Optional[__string]


class CreateCloudFormationTemplateRequest(ServiceRequest):
    ApplicationId: __string
    SemanticVersion: Optional[__string]


class CreateCloudFormationTemplateResponse(TypedDict, total=False):
    ApplicationId: Optional[__string]
    CreationTime: Optional[__string]
    ExpirationTime: Optional[__string]
    SemanticVersion: Optional[__string]
    Status: Optional[Status]
    TemplateId: Optional[__string]
    TemplateUrl: Optional[__string]


class DeleteApplicationRequest(ServiceRequest):
    ApplicationId: __string


class GetApplicationPolicyRequest(ServiceRequest):
    ApplicationId: __string


class GetApplicationPolicyResponse(TypedDict, total=False):
    Statements: Optional[__listOfApplicationPolicyStatement]


class GetApplicationRequest(ServiceRequest):
    ApplicationId: __string
    SemanticVersion: Optional[__string]


class GetApplicationResponse(TypedDict, total=False):
    ApplicationId: Optional[__string]
    Author: Optional[__string]
    CreationTime: Optional[__string]
    Description: Optional[__string]
    HomePageUrl: Optional[__string]
    IsVerifiedAuthor: Optional[__boolean]
    Labels: Optional[__listOf__string]
    LicenseUrl: Optional[__string]
    Name: Optional[__string]
    ReadmeUrl: Optional[__string]
    SpdxLicenseId: Optional[__string]
    VerifiedAuthorUrl: Optional[__string]
    Version: Optional[Version]


class GetCloudFormationTemplateRequest(ServiceRequest):
    ApplicationId: __string
    TemplateId: __string


class GetCloudFormationTemplateResponse(TypedDict, total=False):
    ApplicationId: Optional[__string]
    CreationTime: Optional[__string]
    ExpirationTime: Optional[__string]
    SemanticVersion: Optional[__string]
    Status: Optional[Status]
    TemplateId: Optional[__string]
    TemplateUrl: Optional[__string]


class ListApplicationDependenciesRequest(ServiceRequest):
    ApplicationId: __string
    MaxItems: Optional[MaxItems]
    NextToken: Optional[__string]
    SemanticVersion: Optional[__string]


class ListApplicationDependenciesResponse(TypedDict, total=False):
    Dependencies: Optional[__listOfApplicationDependencySummary]
    NextToken: Optional[__string]


class ListApplicationVersionsRequest(ServiceRequest):
    ApplicationId: __string
    MaxItems: Optional[MaxItems]
    NextToken: Optional[__string]


class ListApplicationVersionsResponse(TypedDict, total=False):
    NextToken: Optional[__string]
    Versions: Optional[__listOfVersionSummary]


class ListApplicationsRequest(ServiceRequest):
    MaxItems: Optional[MaxItems]
    NextToken: Optional[__string]


class ListApplicationsResponse(TypedDict, total=False):
    Applications: Optional[__listOfApplicationSummary]
    NextToken: Optional[__string]


class PutApplicationPolicyRequest(ServiceRequest):
    ApplicationId: __string
    Statements: __listOfApplicationPolicyStatement


class PutApplicationPolicyResponse(TypedDict, total=False):
    Statements: Optional[__listOfApplicationPolicyStatement]


class TemplateDetails(TypedDict, total=False):
    ApplicationId: __string
    CreationTime: __string
    ExpirationTime: __string
    SemanticVersion: __string
    Status: Status
    TemplateId: __string
    TemplateUrl: __string


class UnshareApplicationInput(TypedDict, total=False):
    OrganizationId: __string


class UnshareApplicationRequest(ServiceRequest):
    ApplicationId: __string
    OrganizationId: __string


class UpdateApplicationInput(TypedDict, total=False):
    Author: Optional[__string]
    Description: Optional[__string]
    HomePageUrl: Optional[__string]
    Labels: Optional[__listOf__string]
    ReadmeBody: Optional[__string]
    ReadmeUrl: Optional[__string]


class UpdateApplicationRequest(ServiceRequest):
    ApplicationId: __string
    Author: Optional[__string]
    Description: Optional[__string]
    HomePageUrl: Optional[__string]
    Labels: Optional[__listOf__string]
    ReadmeBody: Optional[__string]
    ReadmeUrl: Optional[__string]


class UpdateApplicationResponse(TypedDict, total=False):
    ApplicationId: Optional[__string]
    Author: Optional[__string]
    CreationTime: Optional[__string]
    Description: Optional[__string]
    HomePageUrl: Optional[__string]
    IsVerifiedAuthor: Optional[__boolean]
    Labels: Optional[__listOf__string]
    LicenseUrl: Optional[__string]
    Name: Optional[__string]
    ReadmeUrl: Optional[__string]
    SpdxLicenseId: Optional[__string]
    VerifiedAuthorUrl: Optional[__string]
    Version: Optional[Version]


__long = int


class ServerlessrepoApi:

    service = "serverlessrepo"
    version = "2017-09-08"

    @handler("CreateApplication")
    def create_application(
        self,
        context: RequestContext,
        description: __string,
        name: __string,
        author: __string,
        home_page_url: __string = None,
        labels: __listOf__string = None,
        license_body: __string = None,
        license_url: __string = None,
        readme_body: __string = None,
        readme_url: __string = None,
        semantic_version: __string = None,
        source_code_archive_url: __string = None,
        source_code_url: __string = None,
        spdx_license_id: __string = None,
        template_body: __string = None,
        template_url: __string = None,
    ) -> CreateApplicationResponse:
        raise NotImplementedError

    @handler("CreateApplicationVersion")
    def create_application_version(
        self,
        context: RequestContext,
        application_id: __string,
        semantic_version: __string,
        source_code_archive_url: __string = None,
        source_code_url: __string = None,
        template_body: __string = None,
        template_url: __string = None,
    ) -> CreateApplicationVersionResponse:
        raise NotImplementedError

    @handler("CreateCloudFormationChangeSet")
    def create_cloud_formation_change_set(
        self,
        context: RequestContext,
        application_id: __string,
        stack_name: __string,
        capabilities: __listOf__string = None,
        change_set_name: __string = None,
        client_token: __string = None,
        description: __string = None,
        notification_arns: __listOf__string = None,
        parameter_overrides: __listOfParameterValue = None,
        resource_types: __listOf__string = None,
        rollback_configuration: RollbackConfiguration = None,
        semantic_version: __string = None,
        tags: __listOfTag = None,
        template_id: __string = None,
    ) -> CreateCloudFormationChangeSetResponse:
        raise NotImplementedError

    @handler("CreateCloudFormationTemplate")
    def create_cloud_formation_template(
        self,
        context: RequestContext,
        application_id: __string,
        semantic_version: __string = None,
    ) -> CreateCloudFormationTemplateResponse:
        raise NotImplementedError

    @handler("DeleteApplication")
    def delete_application(self, context: RequestContext, application_id: __string) -> None:
        raise NotImplementedError

    @handler("GetApplication")
    def get_application(
        self,
        context: RequestContext,
        application_id: __string,
        semantic_version: __string = None,
    ) -> GetApplicationResponse:
        raise NotImplementedError

    @handler("GetApplicationPolicy")
    def get_application_policy(
        self, context: RequestContext, application_id: __string
    ) -> GetApplicationPolicyResponse:
        raise NotImplementedError

    @handler("GetCloudFormationTemplate")
    def get_cloud_formation_template(
        self, context: RequestContext, application_id: __string, template_id: __string
    ) -> GetCloudFormationTemplateResponse:
        raise NotImplementedError

    @handler("ListApplicationDependencies")
    def list_application_dependencies(
        self,
        context: RequestContext,
        application_id: __string,
        max_items: MaxItems = None,
        next_token: __string = None,
        semantic_version: __string = None,
    ) -> ListApplicationDependenciesResponse:
        raise NotImplementedError

    @handler("ListApplicationVersions")
    def list_application_versions(
        self,
        context: RequestContext,
        application_id: __string,
        max_items: MaxItems = None,
        next_token: __string = None,
    ) -> ListApplicationVersionsResponse:
        raise NotImplementedError

    @handler("ListApplications")
    def list_applications(
        self,
        context: RequestContext,
        max_items: MaxItems = None,
        next_token: __string = None,
    ) -> ListApplicationsResponse:
        raise NotImplementedError

    @handler("PutApplicationPolicy")
    def put_application_policy(
        self,
        context: RequestContext,
        application_id: __string,
        statements: __listOfApplicationPolicyStatement,
    ) -> PutApplicationPolicyResponse:
        raise NotImplementedError

    @handler("UnshareApplication")
    def unshare_application(
        self,
        context: RequestContext,
        application_id: __string,
        organization_id: __string,
    ) -> None:
        raise NotImplementedError

    @handler("UpdateApplication")
    def update_application(
        self,
        context: RequestContext,
        application_id: __string,
        author: __string = None,
        description: __string = None,
        home_page_url: __string = None,
        labels: __listOf__string = None,
        readme_body: __string = None,
        readme_url: __string = None,
    ) -> UpdateApplicationResponse:
        raise NotImplementedError
