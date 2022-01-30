import sys
from datetime import datetime
from typing import Dict, List, Optional

if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict

from localstack.aws.api import RequestContext, ServiceException, ServiceRequest, handler

Arn = str
Id = str
IntegerWithLengthBetween0And3600 = int
IntegerWithLengthBetween50And30000 = int
IntegerWithLengthBetweenMinus1And86400 = int
NextToken = str
SelectionExpression = str
SelectionKey = str
StringWithLengthBetween0And1024 = str
StringWithLengthBetween0And2048 = str
StringWithLengthBetween0And32K = str
StringWithLengthBetween1And1024 = str
StringWithLengthBetween1And128 = str
StringWithLengthBetween1And1600 = str
StringWithLengthBetween1And256 = str
StringWithLengthBetween1And512 = str
StringWithLengthBetween1And64 = str
UriWithLengthBetween1And2048 = str
__boolean = bool
__double = float
__integer = int
__string = str


class AuthorizationType(str):
    NONE = "NONE"
    AWS_IAM = "AWS_IAM"
    CUSTOM = "CUSTOM"
    JWT = "JWT"


class AuthorizerType(str):
    REQUEST = "REQUEST"
    JWT = "JWT"


class ConnectionType(str):
    INTERNET = "INTERNET"
    VPC_LINK = "VPC_LINK"


class ContentHandlingStrategy(str):
    CONVERT_TO_BINARY = "CONVERT_TO_BINARY"
    CONVERT_TO_TEXT = "CONVERT_TO_TEXT"


class DeploymentStatus(str):
    PENDING = "PENDING"
    FAILED = "FAILED"
    DEPLOYED = "DEPLOYED"


class DomainNameStatus(str):
    AVAILABLE = "AVAILABLE"
    UPDATING = "UPDATING"
    PENDING_CERTIFICATE_REIMPORT = "PENDING_CERTIFICATE_REIMPORT"
    PENDING_OWNERSHIP_VERIFICATION = "PENDING_OWNERSHIP_VERIFICATION"


class EndpointType(str):
    REGIONAL = "REGIONAL"
    EDGE = "EDGE"


class IntegrationType(str):
    AWS = "AWS"
    HTTP = "HTTP"
    MOCK = "MOCK"
    HTTP_PROXY = "HTTP_PROXY"
    AWS_PROXY = "AWS_PROXY"


class LoggingLevel(str):
    ERROR = "ERROR"
    INFO = "INFO"
    OFF = "OFF"


class PassthroughBehavior(str):
    WHEN_NO_MATCH = "WHEN_NO_MATCH"
    NEVER = "NEVER"
    WHEN_NO_TEMPLATES = "WHEN_NO_TEMPLATES"


class ProtocolType(str):
    WEBSOCKET = "WEBSOCKET"
    HTTP = "HTTP"


class SecurityPolicy(str):
    TLS_1_0 = "TLS_1_0"
    TLS_1_2 = "TLS_1_2"


class VpcLinkStatus(str):
    PENDING = "PENDING"
    AVAILABLE = "AVAILABLE"
    DELETING = "DELETING"
    FAILED = "FAILED"
    INACTIVE = "INACTIVE"


class VpcLinkVersion(str):
    V2 = "V2"


class AccessDeniedException(ServiceException):
    Message: Optional[__string]


class BadRequestException(ServiceException):
    Message: Optional[__string]


class ConflictException(ServiceException):
    Message: Optional[__string]


class NotFoundException(ServiceException):
    Message: Optional[__string]
    ResourceType: Optional[__string]


class TooManyRequestsException(ServiceException):
    LimitType: Optional[__string]
    Message: Optional[__string]


class AccessLogSettings(TypedDict, total=False):
    DestinationArn: Optional[Arn]
    Format: Optional[StringWithLengthBetween1And1024]


__listOf__string = List[__string]
Tags = Dict[__string, StringWithLengthBetween1And1600]
__timestampIso8601 = datetime
CorsHeaderList = List[__string]
CorsOriginList = List[__string]
CorsMethodList = List[StringWithLengthBetween1And64]


class Cors(TypedDict, total=False):
    AllowCredentials: Optional[__boolean]
    AllowHeaders: Optional[CorsHeaderList]
    AllowMethods: Optional[CorsMethodList]
    AllowOrigins: Optional[CorsOriginList]
    ExposeHeaders: Optional[CorsHeaderList]
    MaxAge: Optional[IntegerWithLengthBetweenMinus1And86400]


class Api(TypedDict, total=False):
    ApiEndpoint: Optional[__string]
    ApiGatewayManaged: Optional[__boolean]
    ApiId: Optional[Id]
    ApiKeySelectionExpression: Optional[SelectionExpression]
    CorsConfiguration: Optional[Cors]
    CreatedDate: Optional[__timestampIso8601]
    Description: Optional[StringWithLengthBetween0And1024]
    DisableSchemaValidation: Optional[__boolean]
    DisableExecuteApiEndpoint: Optional[__boolean]
    ImportInfo: Optional[__listOf__string]
    Name: StringWithLengthBetween1And128
    ProtocolType: ProtocolType
    RouteSelectionExpression: SelectionExpression
    Tags: Optional[Tags]
    Version: Optional[StringWithLengthBetween1And64]
    Warnings: Optional[__listOf__string]


class ApiMapping(TypedDict, total=False):
    ApiId: Id
    ApiMappingId: Optional[Id]
    ApiMappingKey: Optional[SelectionKey]
    Stage: StringWithLengthBetween1And128


__listOfApiMapping = List[ApiMapping]


class ApiMappings(TypedDict, total=False):
    Items: Optional[__listOfApiMapping]
    NextToken: Optional[NextToken]


__listOfApi = List[Api]


class Apis(TypedDict, total=False):
    Items: Optional[__listOfApi]
    NextToken: Optional[NextToken]


AuthorizationScopes = List[StringWithLengthBetween1And64]


class JWTConfiguration(TypedDict, total=False):
    Audience: Optional[__listOf__string]
    Issuer: Optional[UriWithLengthBetween1And2048]


IdentitySourceList = List[__string]


class Authorizer(TypedDict, total=False):
    AuthorizerCredentialsArn: Optional[Arn]
    AuthorizerId: Optional[Id]
    AuthorizerPayloadFormatVersion: Optional[StringWithLengthBetween1And64]
    AuthorizerResultTtlInSeconds: Optional[IntegerWithLengthBetween0And3600]
    AuthorizerType: Optional[AuthorizerType]
    AuthorizerUri: Optional[UriWithLengthBetween1And2048]
    EnableSimpleResponses: Optional[__boolean]
    IdentitySource: Optional[IdentitySourceList]
    IdentityValidationExpression: Optional[StringWithLengthBetween0And1024]
    JwtConfiguration: Optional[JWTConfiguration]
    Name: StringWithLengthBetween1And128


__listOfAuthorizer = List[Authorizer]


class Authorizers(TypedDict, total=False):
    Items: Optional[__listOfAuthorizer]
    NextToken: Optional[NextToken]


class CreateApiInput(TypedDict, total=False):
    ApiKeySelectionExpression: Optional[SelectionExpression]
    CorsConfiguration: Optional[Cors]
    CredentialsArn: Optional[Arn]
    Description: Optional[StringWithLengthBetween0And1024]
    DisableSchemaValidation: Optional[__boolean]
    DisableExecuteApiEndpoint: Optional[__boolean]
    Name: StringWithLengthBetween1And128
    ProtocolType: ProtocolType
    RouteKey: Optional[SelectionKey]
    RouteSelectionExpression: Optional[SelectionExpression]
    Tags: Optional[Tags]
    Target: Optional[UriWithLengthBetween1And2048]
    Version: Optional[StringWithLengthBetween1And64]


class CreateApiMappingInput(TypedDict, total=False):
    ApiId: Id
    ApiMappingKey: Optional[SelectionKey]
    Stage: StringWithLengthBetween1And128


class CreateApiMappingRequest(ServiceRequest):
    ApiId: Id
    ApiMappingKey: Optional[SelectionKey]
    DomainName: __string
    Stage: StringWithLengthBetween1And128


class CreateApiMappingResponse(TypedDict, total=False):
    ApiId: Optional[Id]
    ApiMappingId: Optional[Id]
    ApiMappingKey: Optional[SelectionKey]
    Stage: Optional[StringWithLengthBetween1And128]


class CreateApiRequest(ServiceRequest):
    ApiKeySelectionExpression: Optional[SelectionExpression]
    CorsConfiguration: Optional[Cors]
    CredentialsArn: Optional[Arn]
    Description: Optional[StringWithLengthBetween0And1024]
    DisableSchemaValidation: Optional[__boolean]
    DisableExecuteApiEndpoint: Optional[__boolean]
    Name: StringWithLengthBetween1And128
    ProtocolType: ProtocolType
    RouteKey: Optional[SelectionKey]
    RouteSelectionExpression: Optional[SelectionExpression]
    Tags: Optional[Tags]
    Target: Optional[UriWithLengthBetween1And2048]
    Version: Optional[StringWithLengthBetween1And64]


class CreateApiResponse(TypedDict, total=False):
    ApiEndpoint: Optional[__string]
    ApiGatewayManaged: Optional[__boolean]
    ApiId: Optional[Id]
    ApiKeySelectionExpression: Optional[SelectionExpression]
    CorsConfiguration: Optional[Cors]
    CreatedDate: Optional[__timestampIso8601]
    Description: Optional[StringWithLengthBetween0And1024]
    DisableSchemaValidation: Optional[__boolean]
    DisableExecuteApiEndpoint: Optional[__boolean]
    ImportInfo: Optional[__listOf__string]
    Name: Optional[StringWithLengthBetween1And128]
    ProtocolType: Optional[ProtocolType]
    RouteSelectionExpression: Optional[SelectionExpression]
    Tags: Optional[Tags]
    Version: Optional[StringWithLengthBetween1And64]
    Warnings: Optional[__listOf__string]


class CreateAuthorizerInput(TypedDict, total=False):
    AuthorizerCredentialsArn: Optional[Arn]
    AuthorizerPayloadFormatVersion: Optional[StringWithLengthBetween1And64]
    AuthorizerResultTtlInSeconds: Optional[IntegerWithLengthBetween0And3600]
    AuthorizerType: AuthorizerType
    AuthorizerUri: Optional[UriWithLengthBetween1And2048]
    EnableSimpleResponses: Optional[__boolean]
    IdentitySource: IdentitySourceList
    IdentityValidationExpression: Optional[StringWithLengthBetween0And1024]
    JwtConfiguration: Optional[JWTConfiguration]
    Name: StringWithLengthBetween1And128


class CreateAuthorizerRequest(ServiceRequest):
    ApiId: __string
    AuthorizerCredentialsArn: Optional[Arn]
    AuthorizerPayloadFormatVersion: Optional[StringWithLengthBetween1And64]
    AuthorizerResultTtlInSeconds: Optional[IntegerWithLengthBetween0And3600]
    AuthorizerType: AuthorizerType
    AuthorizerUri: Optional[UriWithLengthBetween1And2048]
    EnableSimpleResponses: Optional[__boolean]
    IdentitySource: IdentitySourceList
    IdentityValidationExpression: Optional[StringWithLengthBetween0And1024]
    JwtConfiguration: Optional[JWTConfiguration]
    Name: StringWithLengthBetween1And128


class CreateAuthorizerResponse(TypedDict, total=False):
    AuthorizerCredentialsArn: Optional[Arn]
    AuthorizerId: Optional[Id]
    AuthorizerPayloadFormatVersion: Optional[StringWithLengthBetween1And64]
    AuthorizerResultTtlInSeconds: Optional[IntegerWithLengthBetween0And3600]
    AuthorizerType: Optional[AuthorizerType]
    AuthorizerUri: Optional[UriWithLengthBetween1And2048]
    EnableSimpleResponses: Optional[__boolean]
    IdentitySource: Optional[IdentitySourceList]
    IdentityValidationExpression: Optional[StringWithLengthBetween0And1024]
    JwtConfiguration: Optional[JWTConfiguration]
    Name: Optional[StringWithLengthBetween1And128]


class CreateDeploymentInput(TypedDict, total=False):
    Description: Optional[StringWithLengthBetween0And1024]
    StageName: Optional[StringWithLengthBetween1And128]


class CreateDeploymentRequest(ServiceRequest):
    ApiId: __string
    Description: Optional[StringWithLengthBetween0And1024]
    StageName: Optional[StringWithLengthBetween1And128]


class CreateDeploymentResponse(TypedDict, total=False):
    AutoDeployed: Optional[__boolean]
    CreatedDate: Optional[__timestampIso8601]
    DeploymentId: Optional[Id]
    DeploymentStatus: Optional[DeploymentStatus]
    DeploymentStatusMessage: Optional[__string]
    Description: Optional[StringWithLengthBetween0And1024]


class MutualTlsAuthenticationInput(TypedDict, total=False):
    TruststoreUri: Optional[UriWithLengthBetween1And2048]
    TruststoreVersion: Optional[StringWithLengthBetween1And64]


class DomainNameConfiguration(TypedDict, total=False):
    ApiGatewayDomainName: Optional[__string]
    CertificateArn: Optional[Arn]
    CertificateName: Optional[StringWithLengthBetween1And128]
    CertificateUploadDate: Optional[__timestampIso8601]
    DomainNameStatus: Optional[DomainNameStatus]
    DomainNameStatusMessage: Optional[__string]
    EndpointType: Optional[EndpointType]
    HostedZoneId: Optional[__string]
    SecurityPolicy: Optional[SecurityPolicy]
    OwnershipVerificationCertificateArn: Optional[Arn]


DomainNameConfigurations = List[DomainNameConfiguration]


class CreateDomainNameInput(TypedDict, total=False):
    DomainName: StringWithLengthBetween1And512
    DomainNameConfigurations: Optional[DomainNameConfigurations]
    MutualTlsAuthentication: Optional[MutualTlsAuthenticationInput]
    Tags: Optional[Tags]


class CreateDomainNameRequest(ServiceRequest):
    DomainName: StringWithLengthBetween1And512
    DomainNameConfigurations: Optional[DomainNameConfigurations]
    MutualTlsAuthentication: Optional[MutualTlsAuthenticationInput]
    Tags: Optional[Tags]


class MutualTlsAuthentication(TypedDict, total=False):
    TruststoreUri: Optional[UriWithLengthBetween1And2048]
    TruststoreVersion: Optional[StringWithLengthBetween1And64]
    TruststoreWarnings: Optional[__listOf__string]


class CreateDomainNameResponse(TypedDict, total=False):
    ApiMappingSelectionExpression: Optional[SelectionExpression]
    DomainName: Optional[StringWithLengthBetween1And512]
    DomainNameConfigurations: Optional[DomainNameConfigurations]
    MutualTlsAuthentication: Optional[MutualTlsAuthentication]
    Tags: Optional[Tags]


class TlsConfigInput(TypedDict, total=False):
    ServerNameToVerify: Optional[StringWithLengthBetween1And512]


IntegrationParameters = Dict[__string, StringWithLengthBetween1And512]
ResponseParameters = Dict[__string, IntegrationParameters]
TemplateMap = Dict[__string, StringWithLengthBetween0And32K]


class CreateIntegrationInput(TypedDict, total=False):
    ConnectionId: Optional[StringWithLengthBetween1And1024]
    ConnectionType: Optional[ConnectionType]
    ContentHandlingStrategy: Optional[ContentHandlingStrategy]
    CredentialsArn: Optional[Arn]
    Description: Optional[StringWithLengthBetween0And1024]
    IntegrationMethod: Optional[StringWithLengthBetween1And64]
    IntegrationSubtype: Optional[StringWithLengthBetween1And128]
    IntegrationType: IntegrationType
    IntegrationUri: Optional[UriWithLengthBetween1And2048]
    PassthroughBehavior: Optional[PassthroughBehavior]
    PayloadFormatVersion: Optional[StringWithLengthBetween1And64]
    RequestParameters: Optional[IntegrationParameters]
    RequestTemplates: Optional[TemplateMap]
    ResponseParameters: Optional[ResponseParameters]
    TemplateSelectionExpression: Optional[SelectionExpression]
    TimeoutInMillis: Optional[IntegerWithLengthBetween50And30000]
    TlsConfig: Optional[TlsConfigInput]


class CreateIntegrationRequest(ServiceRequest):
    ApiId: __string
    ConnectionId: Optional[StringWithLengthBetween1And1024]
    ConnectionType: Optional[ConnectionType]
    ContentHandlingStrategy: Optional[ContentHandlingStrategy]
    CredentialsArn: Optional[Arn]
    Description: Optional[StringWithLengthBetween0And1024]
    IntegrationMethod: Optional[StringWithLengthBetween1And64]
    IntegrationSubtype: Optional[StringWithLengthBetween1And128]
    IntegrationType: IntegrationType
    IntegrationUri: Optional[UriWithLengthBetween1And2048]
    PassthroughBehavior: Optional[PassthroughBehavior]
    PayloadFormatVersion: Optional[StringWithLengthBetween1And64]
    RequestParameters: Optional[IntegrationParameters]
    RequestTemplates: Optional[TemplateMap]
    ResponseParameters: Optional[ResponseParameters]
    TemplateSelectionExpression: Optional[SelectionExpression]
    TimeoutInMillis: Optional[IntegerWithLengthBetween50And30000]
    TlsConfig: Optional[TlsConfigInput]


class TlsConfig(TypedDict, total=False):
    ServerNameToVerify: Optional[StringWithLengthBetween1And512]


class CreateIntegrationResult(TypedDict, total=False):
    ApiGatewayManaged: Optional[__boolean]
    ConnectionId: Optional[StringWithLengthBetween1And1024]
    ConnectionType: Optional[ConnectionType]
    ContentHandlingStrategy: Optional[ContentHandlingStrategy]
    CredentialsArn: Optional[Arn]
    Description: Optional[StringWithLengthBetween0And1024]
    IntegrationId: Optional[Id]
    IntegrationMethod: Optional[StringWithLengthBetween1And64]
    IntegrationResponseSelectionExpression: Optional[SelectionExpression]
    IntegrationSubtype: Optional[StringWithLengthBetween1And128]
    IntegrationType: Optional[IntegrationType]
    IntegrationUri: Optional[UriWithLengthBetween1And2048]
    PassthroughBehavior: Optional[PassthroughBehavior]
    PayloadFormatVersion: Optional[StringWithLengthBetween1And64]
    RequestParameters: Optional[IntegrationParameters]
    RequestTemplates: Optional[TemplateMap]
    ResponseParameters: Optional[ResponseParameters]
    TemplateSelectionExpression: Optional[SelectionExpression]
    TimeoutInMillis: Optional[IntegerWithLengthBetween50And30000]
    TlsConfig: Optional[TlsConfig]


class CreateIntegrationResponseInput(TypedDict, total=False):
    ContentHandlingStrategy: Optional[ContentHandlingStrategy]
    IntegrationResponseKey: SelectionKey
    ResponseParameters: Optional[IntegrationParameters]
    ResponseTemplates: Optional[TemplateMap]
    TemplateSelectionExpression: Optional[SelectionExpression]


class CreateIntegrationResponseRequest(ServiceRequest):
    ApiId: __string
    ContentHandlingStrategy: Optional[ContentHandlingStrategy]
    IntegrationId: __string
    IntegrationResponseKey: SelectionKey
    ResponseParameters: Optional[IntegrationParameters]
    ResponseTemplates: Optional[TemplateMap]
    TemplateSelectionExpression: Optional[SelectionExpression]


class CreateIntegrationResponseResponse(TypedDict, total=False):
    ContentHandlingStrategy: Optional[ContentHandlingStrategy]
    IntegrationResponseId: Optional[Id]
    IntegrationResponseKey: Optional[SelectionKey]
    ResponseParameters: Optional[IntegrationParameters]
    ResponseTemplates: Optional[TemplateMap]
    TemplateSelectionExpression: Optional[SelectionExpression]


class CreateModelInput(TypedDict, total=False):
    ContentType: Optional[StringWithLengthBetween1And256]
    Description: Optional[StringWithLengthBetween0And1024]
    Name: StringWithLengthBetween1And128
    Schema: StringWithLengthBetween0And32K


class CreateModelRequest(ServiceRequest):
    ApiId: __string
    ContentType: Optional[StringWithLengthBetween1And256]
    Description: Optional[StringWithLengthBetween0And1024]
    Name: StringWithLengthBetween1And128
    Schema: StringWithLengthBetween0And32K


class CreateModelResponse(TypedDict, total=False):
    ContentType: Optional[StringWithLengthBetween1And256]
    Description: Optional[StringWithLengthBetween0And1024]
    ModelId: Optional[Id]
    Name: Optional[StringWithLengthBetween1And128]
    Schema: Optional[StringWithLengthBetween0And32K]


class ParameterConstraints(TypedDict, total=False):
    Required: Optional[__boolean]


RouteParameters = Dict[__string, ParameterConstraints]
RouteModels = Dict[__string, StringWithLengthBetween1And128]


class CreateRouteInput(TypedDict, total=False):
    ApiKeyRequired: Optional[__boolean]
    AuthorizationScopes: Optional[AuthorizationScopes]
    AuthorizationType: Optional[AuthorizationType]
    AuthorizerId: Optional[Id]
    ModelSelectionExpression: Optional[SelectionExpression]
    OperationName: Optional[StringWithLengthBetween1And64]
    RequestModels: Optional[RouteModels]
    RequestParameters: Optional[RouteParameters]
    RouteKey: SelectionKey
    RouteResponseSelectionExpression: Optional[SelectionExpression]
    Target: Optional[StringWithLengthBetween1And128]


class CreateRouteRequest(ServiceRequest):
    ApiId: __string
    ApiKeyRequired: Optional[__boolean]
    AuthorizationScopes: Optional[AuthorizationScopes]
    AuthorizationType: Optional[AuthorizationType]
    AuthorizerId: Optional[Id]
    ModelSelectionExpression: Optional[SelectionExpression]
    OperationName: Optional[StringWithLengthBetween1And64]
    RequestModels: Optional[RouteModels]
    RequestParameters: Optional[RouteParameters]
    RouteKey: SelectionKey
    RouteResponseSelectionExpression: Optional[SelectionExpression]
    Target: Optional[StringWithLengthBetween1And128]


class CreateRouteResult(TypedDict, total=False):
    ApiGatewayManaged: Optional[__boolean]
    ApiKeyRequired: Optional[__boolean]
    AuthorizationScopes: Optional[AuthorizationScopes]
    AuthorizationType: Optional[AuthorizationType]
    AuthorizerId: Optional[Id]
    ModelSelectionExpression: Optional[SelectionExpression]
    OperationName: Optional[StringWithLengthBetween1And64]
    RequestModels: Optional[RouteModels]
    RequestParameters: Optional[RouteParameters]
    RouteId: Optional[Id]
    RouteKey: Optional[SelectionKey]
    RouteResponseSelectionExpression: Optional[SelectionExpression]
    Target: Optional[StringWithLengthBetween1And128]


class CreateRouteResponseInput(TypedDict, total=False):
    ModelSelectionExpression: Optional[SelectionExpression]
    ResponseModels: Optional[RouteModels]
    ResponseParameters: Optional[RouteParameters]
    RouteResponseKey: SelectionKey


class CreateRouteResponseRequest(ServiceRequest):
    ApiId: __string
    ModelSelectionExpression: Optional[SelectionExpression]
    ResponseModels: Optional[RouteModels]
    ResponseParameters: Optional[RouteParameters]
    RouteId: __string
    RouteResponseKey: SelectionKey


class CreateRouteResponseResponse(TypedDict, total=False):
    ModelSelectionExpression: Optional[SelectionExpression]
    ResponseModels: Optional[RouteModels]
    ResponseParameters: Optional[RouteParameters]
    RouteResponseId: Optional[Id]
    RouteResponseKey: Optional[SelectionKey]


StageVariablesMap = Dict[__string, StringWithLengthBetween0And2048]


class RouteSettings(TypedDict, total=False):
    DataTraceEnabled: Optional[__boolean]
    DetailedMetricsEnabled: Optional[__boolean]
    LoggingLevel: Optional[LoggingLevel]
    ThrottlingBurstLimit: Optional[__integer]
    ThrottlingRateLimit: Optional[__double]


RouteSettingsMap = Dict[__string, RouteSettings]


class CreateStageInput(TypedDict, total=False):
    AccessLogSettings: Optional[AccessLogSettings]
    AutoDeploy: Optional[__boolean]
    ClientCertificateId: Optional[Id]
    DefaultRouteSettings: Optional[RouteSettings]
    DeploymentId: Optional[Id]
    Description: Optional[StringWithLengthBetween0And1024]
    RouteSettings: Optional[RouteSettingsMap]
    StageName: StringWithLengthBetween1And128
    StageVariables: Optional[StageVariablesMap]
    Tags: Optional[Tags]


class CreateStageRequest(ServiceRequest):
    AccessLogSettings: Optional[AccessLogSettings]
    ApiId: __string
    AutoDeploy: Optional[__boolean]
    ClientCertificateId: Optional[Id]
    DefaultRouteSettings: Optional[RouteSettings]
    DeploymentId: Optional[Id]
    Description: Optional[StringWithLengthBetween0And1024]
    RouteSettings: Optional[RouteSettingsMap]
    StageName: StringWithLengthBetween1And128
    StageVariables: Optional[StageVariablesMap]
    Tags: Optional[Tags]


class CreateStageResponse(TypedDict, total=False):
    AccessLogSettings: Optional[AccessLogSettings]
    ApiGatewayManaged: Optional[__boolean]
    AutoDeploy: Optional[__boolean]
    ClientCertificateId: Optional[Id]
    CreatedDate: Optional[__timestampIso8601]
    DefaultRouteSettings: Optional[RouteSettings]
    DeploymentId: Optional[Id]
    Description: Optional[StringWithLengthBetween0And1024]
    LastDeploymentStatusMessage: Optional[__string]
    LastUpdatedDate: Optional[__timestampIso8601]
    RouteSettings: Optional[RouteSettingsMap]
    StageName: Optional[StringWithLengthBetween1And128]
    StageVariables: Optional[StageVariablesMap]
    Tags: Optional[Tags]


SubnetIdList = List[__string]
SecurityGroupIdList = List[__string]


class CreateVpcLinkInput(TypedDict, total=False):
    Name: StringWithLengthBetween1And128
    SecurityGroupIds: Optional[SecurityGroupIdList]
    SubnetIds: SubnetIdList
    Tags: Optional[Tags]


class CreateVpcLinkRequest(ServiceRequest):
    Name: StringWithLengthBetween1And128
    SecurityGroupIds: Optional[SecurityGroupIdList]
    SubnetIds: SubnetIdList
    Tags: Optional[Tags]


class CreateVpcLinkResponse(TypedDict, total=False):
    CreatedDate: Optional[__timestampIso8601]
    Name: Optional[StringWithLengthBetween1And128]
    SecurityGroupIds: Optional[SecurityGroupIdList]
    SubnetIds: Optional[SubnetIdList]
    Tags: Optional[Tags]
    VpcLinkId: Optional[Id]
    VpcLinkStatus: Optional[VpcLinkStatus]
    VpcLinkStatusMessage: Optional[StringWithLengthBetween0And1024]
    VpcLinkVersion: Optional[VpcLinkVersion]


class DeleteAccessLogSettingsRequest(ServiceRequest):
    ApiId: __string
    StageName: __string


class DeleteApiMappingRequest(ServiceRequest):
    ApiMappingId: __string
    DomainName: __string


class DeleteApiRequest(ServiceRequest):
    ApiId: __string


class DeleteAuthorizerRequest(ServiceRequest):
    ApiId: __string
    AuthorizerId: __string


class DeleteCorsConfigurationRequest(ServiceRequest):
    ApiId: __string


class DeleteDeploymentRequest(ServiceRequest):
    ApiId: __string
    DeploymentId: __string


class DeleteDomainNameRequest(ServiceRequest):
    DomainName: __string


class DeleteIntegrationRequest(ServiceRequest):
    ApiId: __string
    IntegrationId: __string


class DeleteIntegrationResponseRequest(ServiceRequest):
    ApiId: __string
    IntegrationId: __string
    IntegrationResponseId: __string


class DeleteModelRequest(ServiceRequest):
    ApiId: __string
    ModelId: __string


class DeleteRouteRequest(ServiceRequest):
    ApiId: __string
    RouteId: __string


class DeleteRouteRequestParameterRequest(ServiceRequest):
    ApiId: __string
    RequestParameterKey: __string
    RouteId: __string


class DeleteRouteResponseRequest(ServiceRequest):
    ApiId: __string
    RouteId: __string
    RouteResponseId: __string


class DeleteRouteSettingsRequest(ServiceRequest):
    ApiId: __string
    RouteKey: __string
    StageName: __string


class DeleteStageRequest(ServiceRequest):
    ApiId: __string
    StageName: __string


class DeleteVpcLinkRequest(ServiceRequest):
    VpcLinkId: __string


class DeleteVpcLinkResponse(TypedDict, total=False):
    pass


class Deployment(TypedDict, total=False):
    AutoDeployed: Optional[__boolean]
    CreatedDate: Optional[__timestampIso8601]
    DeploymentId: Optional[Id]
    DeploymentStatus: Optional[DeploymentStatus]
    DeploymentStatusMessage: Optional[__string]
    Description: Optional[StringWithLengthBetween0And1024]


__listOfDeployment = List[Deployment]


class Deployments(TypedDict, total=False):
    Items: Optional[__listOfDeployment]
    NextToken: Optional[NextToken]


class DomainName(TypedDict, total=False):
    ApiMappingSelectionExpression: Optional[SelectionExpression]
    DomainName: StringWithLengthBetween1And512
    DomainNameConfigurations: Optional[DomainNameConfigurations]
    MutualTlsAuthentication: Optional[MutualTlsAuthentication]
    Tags: Optional[Tags]


__listOfDomainName = List[DomainName]


class DomainNames(TypedDict, total=False):
    Items: Optional[__listOfDomainName]
    NextToken: Optional[NextToken]


class ExportApiRequest(ServiceRequest):
    ApiId: __string
    ExportVersion: Optional[__string]
    IncludeExtensions: Optional[__boolean]
    OutputType: __string
    Specification: __string
    StageName: Optional[__string]


ExportedApi = bytes


class ExportApiResponse(TypedDict, total=False):
    body: Optional[ExportedApi]


class ResetAuthorizersCacheRequest(ServiceRequest):
    ApiId: __string
    StageName: __string


class GetApiMappingRequest(ServiceRequest):
    ApiMappingId: __string
    DomainName: __string


class GetApiMappingResponse(TypedDict, total=False):
    ApiId: Optional[Id]
    ApiMappingId: Optional[Id]
    ApiMappingKey: Optional[SelectionKey]
    Stage: Optional[StringWithLengthBetween1And128]


class GetApiMappingsRequest(ServiceRequest):
    DomainName: __string
    MaxResults: Optional[__string]
    NextToken: Optional[__string]


class GetApiMappingsResponse(TypedDict, total=False):
    Items: Optional[__listOfApiMapping]
    NextToken: Optional[NextToken]


class GetApiRequest(ServiceRequest):
    ApiId: __string


class GetApiResponse(TypedDict, total=False):
    ApiEndpoint: Optional[__string]
    ApiGatewayManaged: Optional[__boolean]
    ApiId: Optional[Id]
    ApiKeySelectionExpression: Optional[SelectionExpression]
    CorsConfiguration: Optional[Cors]
    CreatedDate: Optional[__timestampIso8601]
    Description: Optional[StringWithLengthBetween0And1024]
    DisableSchemaValidation: Optional[__boolean]
    DisableExecuteApiEndpoint: Optional[__boolean]
    ImportInfo: Optional[__listOf__string]
    Name: Optional[StringWithLengthBetween1And128]
    ProtocolType: Optional[ProtocolType]
    RouteSelectionExpression: Optional[SelectionExpression]
    Tags: Optional[Tags]
    Version: Optional[StringWithLengthBetween1And64]
    Warnings: Optional[__listOf__string]


class GetApisRequest(ServiceRequest):
    MaxResults: Optional[__string]
    NextToken: Optional[__string]


class GetApisResponse(TypedDict, total=False):
    Items: Optional[__listOfApi]
    NextToken: Optional[NextToken]


class GetAuthorizerRequest(ServiceRequest):
    ApiId: __string
    AuthorizerId: __string


class GetAuthorizerResponse(TypedDict, total=False):
    AuthorizerCredentialsArn: Optional[Arn]
    AuthorizerId: Optional[Id]
    AuthorizerPayloadFormatVersion: Optional[StringWithLengthBetween1And64]
    AuthorizerResultTtlInSeconds: Optional[IntegerWithLengthBetween0And3600]
    AuthorizerType: Optional[AuthorizerType]
    AuthorizerUri: Optional[UriWithLengthBetween1And2048]
    EnableSimpleResponses: Optional[__boolean]
    IdentitySource: Optional[IdentitySourceList]
    IdentityValidationExpression: Optional[StringWithLengthBetween0And1024]
    JwtConfiguration: Optional[JWTConfiguration]
    Name: Optional[StringWithLengthBetween1And128]


class GetAuthorizersRequest(ServiceRequest):
    ApiId: __string
    MaxResults: Optional[__string]
    NextToken: Optional[__string]


class GetAuthorizersResponse(TypedDict, total=False):
    Items: Optional[__listOfAuthorizer]
    NextToken: Optional[NextToken]


class GetDeploymentRequest(ServiceRequest):
    ApiId: __string
    DeploymentId: __string


class GetDeploymentResponse(TypedDict, total=False):
    AutoDeployed: Optional[__boolean]
    CreatedDate: Optional[__timestampIso8601]
    DeploymentId: Optional[Id]
    DeploymentStatus: Optional[DeploymentStatus]
    DeploymentStatusMessage: Optional[__string]
    Description: Optional[StringWithLengthBetween0And1024]


class GetDeploymentsRequest(ServiceRequest):
    ApiId: __string
    MaxResults: Optional[__string]
    NextToken: Optional[__string]


class GetDeploymentsResponse(TypedDict, total=False):
    Items: Optional[__listOfDeployment]
    NextToken: Optional[NextToken]


class GetDomainNameRequest(ServiceRequest):
    DomainName: __string


class GetDomainNameResponse(TypedDict, total=False):
    ApiMappingSelectionExpression: Optional[SelectionExpression]
    DomainName: Optional[StringWithLengthBetween1And512]
    DomainNameConfigurations: Optional[DomainNameConfigurations]
    MutualTlsAuthentication: Optional[MutualTlsAuthentication]
    Tags: Optional[Tags]


class GetDomainNamesRequest(ServiceRequest):
    MaxResults: Optional[__string]
    NextToken: Optional[__string]


class GetDomainNamesResponse(TypedDict, total=False):
    Items: Optional[__listOfDomainName]
    NextToken: Optional[NextToken]


class GetIntegrationRequest(ServiceRequest):
    ApiId: __string
    IntegrationId: __string


class GetIntegrationResult(TypedDict, total=False):
    ApiGatewayManaged: Optional[__boolean]
    ConnectionId: Optional[StringWithLengthBetween1And1024]
    ConnectionType: Optional[ConnectionType]
    ContentHandlingStrategy: Optional[ContentHandlingStrategy]
    CredentialsArn: Optional[Arn]
    Description: Optional[StringWithLengthBetween0And1024]
    IntegrationId: Optional[Id]
    IntegrationMethod: Optional[StringWithLengthBetween1And64]
    IntegrationResponseSelectionExpression: Optional[SelectionExpression]
    IntegrationSubtype: Optional[StringWithLengthBetween1And128]
    IntegrationType: Optional[IntegrationType]
    IntegrationUri: Optional[UriWithLengthBetween1And2048]
    PassthroughBehavior: Optional[PassthroughBehavior]
    PayloadFormatVersion: Optional[StringWithLengthBetween1And64]
    RequestParameters: Optional[IntegrationParameters]
    RequestTemplates: Optional[TemplateMap]
    ResponseParameters: Optional[ResponseParameters]
    TemplateSelectionExpression: Optional[SelectionExpression]
    TimeoutInMillis: Optional[IntegerWithLengthBetween50And30000]
    TlsConfig: Optional[TlsConfig]


class GetIntegrationResponseRequest(ServiceRequest):
    ApiId: __string
    IntegrationId: __string
    IntegrationResponseId: __string


class GetIntegrationResponseResponse(TypedDict, total=False):
    ContentHandlingStrategy: Optional[ContentHandlingStrategy]
    IntegrationResponseId: Optional[Id]
    IntegrationResponseKey: Optional[SelectionKey]
    ResponseParameters: Optional[IntegrationParameters]
    ResponseTemplates: Optional[TemplateMap]
    TemplateSelectionExpression: Optional[SelectionExpression]


class GetIntegrationResponsesRequest(ServiceRequest):
    ApiId: __string
    IntegrationId: __string
    MaxResults: Optional[__string]
    NextToken: Optional[__string]


class IntegrationResponse(TypedDict, total=False):
    ContentHandlingStrategy: Optional[ContentHandlingStrategy]
    IntegrationResponseId: Optional[Id]
    IntegrationResponseKey: SelectionKey
    ResponseParameters: Optional[IntegrationParameters]
    ResponseTemplates: Optional[TemplateMap]
    TemplateSelectionExpression: Optional[SelectionExpression]


__listOfIntegrationResponse = List[IntegrationResponse]


class GetIntegrationResponsesResponse(TypedDict, total=False):
    Items: Optional[__listOfIntegrationResponse]
    NextToken: Optional[NextToken]


class GetIntegrationsRequest(ServiceRequest):
    ApiId: __string
    MaxResults: Optional[__string]
    NextToken: Optional[__string]


class Integration(TypedDict, total=False):
    ApiGatewayManaged: Optional[__boolean]
    ConnectionId: Optional[StringWithLengthBetween1And1024]
    ConnectionType: Optional[ConnectionType]
    ContentHandlingStrategy: Optional[ContentHandlingStrategy]
    CredentialsArn: Optional[Arn]
    Description: Optional[StringWithLengthBetween0And1024]
    IntegrationId: Optional[Id]
    IntegrationMethod: Optional[StringWithLengthBetween1And64]
    IntegrationResponseSelectionExpression: Optional[SelectionExpression]
    IntegrationSubtype: Optional[StringWithLengthBetween1And128]
    IntegrationType: Optional[IntegrationType]
    IntegrationUri: Optional[UriWithLengthBetween1And2048]
    PassthroughBehavior: Optional[PassthroughBehavior]
    PayloadFormatVersion: Optional[StringWithLengthBetween1And64]
    RequestParameters: Optional[IntegrationParameters]
    RequestTemplates: Optional[TemplateMap]
    ResponseParameters: Optional[ResponseParameters]
    TemplateSelectionExpression: Optional[SelectionExpression]
    TimeoutInMillis: Optional[IntegerWithLengthBetween50And30000]
    TlsConfig: Optional[TlsConfig]


__listOfIntegration = List[Integration]


class GetIntegrationsResponse(TypedDict, total=False):
    Items: Optional[__listOfIntegration]
    NextToken: Optional[NextToken]


class GetModelRequest(ServiceRequest):
    ApiId: __string
    ModelId: __string


class GetModelResponse(TypedDict, total=False):
    ContentType: Optional[StringWithLengthBetween1And256]
    Description: Optional[StringWithLengthBetween0And1024]
    ModelId: Optional[Id]
    Name: Optional[StringWithLengthBetween1And128]
    Schema: Optional[StringWithLengthBetween0And32K]


class GetModelTemplateRequest(ServiceRequest):
    ApiId: __string
    ModelId: __string


class GetModelTemplateResponse(TypedDict, total=False):
    Value: Optional[__string]


class GetModelsRequest(ServiceRequest):
    ApiId: __string
    MaxResults: Optional[__string]
    NextToken: Optional[__string]


class Model(TypedDict, total=False):
    ContentType: Optional[StringWithLengthBetween1And256]
    Description: Optional[StringWithLengthBetween0And1024]
    ModelId: Optional[Id]
    Name: StringWithLengthBetween1And128
    Schema: Optional[StringWithLengthBetween0And32K]


__listOfModel = List[Model]


class GetModelsResponse(TypedDict, total=False):
    Items: Optional[__listOfModel]
    NextToken: Optional[NextToken]


class GetRouteRequest(ServiceRequest):
    ApiId: __string
    RouteId: __string


class GetRouteResult(TypedDict, total=False):
    ApiGatewayManaged: Optional[__boolean]
    ApiKeyRequired: Optional[__boolean]
    AuthorizationScopes: Optional[AuthorizationScopes]
    AuthorizationType: Optional[AuthorizationType]
    AuthorizerId: Optional[Id]
    ModelSelectionExpression: Optional[SelectionExpression]
    OperationName: Optional[StringWithLengthBetween1And64]
    RequestModels: Optional[RouteModels]
    RequestParameters: Optional[RouteParameters]
    RouteId: Optional[Id]
    RouteKey: Optional[SelectionKey]
    RouteResponseSelectionExpression: Optional[SelectionExpression]
    Target: Optional[StringWithLengthBetween1And128]


class GetRouteResponseRequest(ServiceRequest):
    ApiId: __string
    RouteId: __string
    RouteResponseId: __string


class GetRouteResponseResponse(TypedDict, total=False):
    ModelSelectionExpression: Optional[SelectionExpression]
    ResponseModels: Optional[RouteModels]
    ResponseParameters: Optional[RouteParameters]
    RouteResponseId: Optional[Id]
    RouteResponseKey: Optional[SelectionKey]


class GetRouteResponsesRequest(ServiceRequest):
    ApiId: __string
    MaxResults: Optional[__string]
    NextToken: Optional[__string]
    RouteId: __string


class RouteResponse(TypedDict, total=False):
    ModelSelectionExpression: Optional[SelectionExpression]
    ResponseModels: Optional[RouteModels]
    ResponseParameters: Optional[RouteParameters]
    RouteResponseId: Optional[Id]
    RouteResponseKey: SelectionKey


__listOfRouteResponse = List[RouteResponse]


class GetRouteResponsesResponse(TypedDict, total=False):
    Items: Optional[__listOfRouteResponse]
    NextToken: Optional[NextToken]


class GetRoutesRequest(ServiceRequest):
    ApiId: __string
    MaxResults: Optional[__string]
    NextToken: Optional[__string]


class Route(TypedDict, total=False):
    ApiGatewayManaged: Optional[__boolean]
    ApiKeyRequired: Optional[__boolean]
    AuthorizationScopes: Optional[AuthorizationScopes]
    AuthorizationType: Optional[AuthorizationType]
    AuthorizerId: Optional[Id]
    ModelSelectionExpression: Optional[SelectionExpression]
    OperationName: Optional[StringWithLengthBetween1And64]
    RequestModels: Optional[RouteModels]
    RequestParameters: Optional[RouteParameters]
    RouteId: Optional[Id]
    RouteKey: SelectionKey
    RouteResponseSelectionExpression: Optional[SelectionExpression]
    Target: Optional[StringWithLengthBetween1And128]


__listOfRoute = List[Route]


class GetRoutesResponse(TypedDict, total=False):
    Items: Optional[__listOfRoute]
    NextToken: Optional[NextToken]


class GetStageRequest(ServiceRequest):
    ApiId: __string
    StageName: __string


class GetStageResponse(TypedDict, total=False):
    AccessLogSettings: Optional[AccessLogSettings]
    ApiGatewayManaged: Optional[__boolean]
    AutoDeploy: Optional[__boolean]
    ClientCertificateId: Optional[Id]
    CreatedDate: Optional[__timestampIso8601]
    DefaultRouteSettings: Optional[RouteSettings]
    DeploymentId: Optional[Id]
    Description: Optional[StringWithLengthBetween0And1024]
    LastDeploymentStatusMessage: Optional[__string]
    LastUpdatedDate: Optional[__timestampIso8601]
    RouteSettings: Optional[RouteSettingsMap]
    StageName: Optional[StringWithLengthBetween1And128]
    StageVariables: Optional[StageVariablesMap]
    Tags: Optional[Tags]


class GetStagesRequest(ServiceRequest):
    ApiId: __string
    MaxResults: Optional[__string]
    NextToken: Optional[__string]


class Stage(TypedDict, total=False):
    AccessLogSettings: Optional[AccessLogSettings]
    ApiGatewayManaged: Optional[__boolean]
    AutoDeploy: Optional[__boolean]
    ClientCertificateId: Optional[Id]
    CreatedDate: Optional[__timestampIso8601]
    DefaultRouteSettings: Optional[RouteSettings]
    DeploymentId: Optional[Id]
    Description: Optional[StringWithLengthBetween0And1024]
    LastDeploymentStatusMessage: Optional[__string]
    LastUpdatedDate: Optional[__timestampIso8601]
    RouteSettings: Optional[RouteSettingsMap]
    StageName: StringWithLengthBetween1And128
    StageVariables: Optional[StageVariablesMap]
    Tags: Optional[Tags]


__listOfStage = List[Stage]


class GetStagesResponse(TypedDict, total=False):
    Items: Optional[__listOfStage]
    NextToken: Optional[NextToken]


class GetTagsRequest(ServiceRequest):
    ResourceArn: __string


class GetTagsResponse(TypedDict, total=False):
    Tags: Optional[Tags]


class GetVpcLinkRequest(ServiceRequest):
    VpcLinkId: __string


class GetVpcLinkResponse(TypedDict, total=False):
    CreatedDate: Optional[__timestampIso8601]
    Name: Optional[StringWithLengthBetween1And128]
    SecurityGroupIds: Optional[SecurityGroupIdList]
    SubnetIds: Optional[SubnetIdList]
    Tags: Optional[Tags]
    VpcLinkId: Optional[Id]
    VpcLinkStatus: Optional[VpcLinkStatus]
    VpcLinkStatusMessage: Optional[StringWithLengthBetween0And1024]
    VpcLinkVersion: Optional[VpcLinkVersion]


class GetVpcLinksRequest(ServiceRequest):
    MaxResults: Optional[__string]
    NextToken: Optional[__string]


class VpcLink(TypedDict, total=False):
    CreatedDate: Optional[__timestampIso8601]
    Name: StringWithLengthBetween1And128
    SecurityGroupIds: SecurityGroupIdList
    SubnetIds: SubnetIdList
    Tags: Optional[Tags]
    VpcLinkId: Id
    VpcLinkStatus: Optional[VpcLinkStatus]
    VpcLinkStatusMessage: Optional[StringWithLengthBetween0And1024]
    VpcLinkVersion: Optional[VpcLinkVersion]


__listOfVpcLink = List[VpcLink]


class GetVpcLinksResponse(TypedDict, total=False):
    Items: Optional[__listOfVpcLink]
    NextToken: Optional[NextToken]


class ImportApiInput(TypedDict, total=False):
    Body: __string


class ImportApiRequest(ServiceRequest):
    Basepath: Optional[__string]
    Body: __string
    FailOnWarnings: Optional[__boolean]


class ImportApiResponse(TypedDict, total=False):
    ApiEndpoint: Optional[__string]
    ApiGatewayManaged: Optional[__boolean]
    ApiId: Optional[Id]
    ApiKeySelectionExpression: Optional[SelectionExpression]
    CorsConfiguration: Optional[Cors]
    CreatedDate: Optional[__timestampIso8601]
    Description: Optional[StringWithLengthBetween0And1024]
    DisableSchemaValidation: Optional[__boolean]
    DisableExecuteApiEndpoint: Optional[__boolean]
    ImportInfo: Optional[__listOf__string]
    Name: Optional[StringWithLengthBetween1And128]
    ProtocolType: Optional[ProtocolType]
    RouteSelectionExpression: Optional[SelectionExpression]
    Tags: Optional[Tags]
    Version: Optional[StringWithLengthBetween1And64]
    Warnings: Optional[__listOf__string]


class IntegrationResponses(TypedDict, total=False):
    Items: Optional[__listOfIntegrationResponse]
    NextToken: Optional[NextToken]


class Integrations(TypedDict, total=False):
    Items: Optional[__listOfIntegration]
    NextToken: Optional[NextToken]


class LimitExceededException(TypedDict, total=False):
    LimitType: Optional[__string]
    Message: Optional[__string]


class Models(TypedDict, total=False):
    Items: Optional[__listOfModel]
    NextToken: Optional[NextToken]


class ReimportApiInput(TypedDict, total=False):
    Body: __string


class ReimportApiRequest(ServiceRequest):
    ApiId: __string
    Basepath: Optional[__string]
    Body: __string
    FailOnWarnings: Optional[__boolean]


class ReimportApiResponse(TypedDict, total=False):
    ApiEndpoint: Optional[__string]
    ApiGatewayManaged: Optional[__boolean]
    ApiId: Optional[Id]
    ApiKeySelectionExpression: Optional[SelectionExpression]
    CorsConfiguration: Optional[Cors]
    CreatedDate: Optional[__timestampIso8601]
    Description: Optional[StringWithLengthBetween0And1024]
    DisableSchemaValidation: Optional[__boolean]
    DisableExecuteApiEndpoint: Optional[__boolean]
    ImportInfo: Optional[__listOf__string]
    Name: Optional[StringWithLengthBetween1And128]
    ProtocolType: Optional[ProtocolType]
    RouteSelectionExpression: Optional[SelectionExpression]
    Tags: Optional[Tags]
    Version: Optional[StringWithLengthBetween1And64]
    Warnings: Optional[__listOf__string]


class RouteResponses(TypedDict, total=False):
    Items: Optional[__listOfRouteResponse]
    NextToken: Optional[NextToken]


class Routes(TypedDict, total=False):
    Items: Optional[__listOfRoute]
    NextToken: Optional[NextToken]


class Stages(TypedDict, total=False):
    Items: Optional[__listOfStage]
    NextToken: Optional[NextToken]


class TagResourceInput(TypedDict, total=False):
    Tags: Optional[Tags]


class TagResourceRequest(ServiceRequest):
    ResourceArn: __string
    Tags: Optional[Tags]


class TagResourceResponse(TypedDict, total=False):
    pass


class Template(TypedDict, total=False):
    Value: Optional[__string]


class UntagResourceRequest(ServiceRequest):
    ResourceArn: __string
    TagKeys: __listOf__string


class UpdateApiInput(TypedDict, total=False):
    ApiKeySelectionExpression: Optional[SelectionExpression]
    CorsConfiguration: Optional[Cors]
    CredentialsArn: Optional[Arn]
    Description: Optional[StringWithLengthBetween0And1024]
    DisableExecuteApiEndpoint: Optional[__boolean]
    DisableSchemaValidation: Optional[__boolean]
    Name: Optional[StringWithLengthBetween1And128]
    RouteKey: Optional[SelectionKey]
    RouteSelectionExpression: Optional[SelectionExpression]
    Target: Optional[UriWithLengthBetween1And2048]
    Version: Optional[StringWithLengthBetween1And64]


class UpdateApiMappingInput(TypedDict, total=False):
    ApiId: Optional[Id]
    ApiMappingKey: Optional[SelectionKey]
    Stage: Optional[StringWithLengthBetween1And128]


class UpdateApiMappingRequest(ServiceRequest):
    ApiId: Id
    ApiMappingId: __string
    ApiMappingKey: Optional[SelectionKey]
    DomainName: __string
    Stage: Optional[StringWithLengthBetween1And128]


class UpdateApiMappingResponse(TypedDict, total=False):
    ApiId: Optional[Id]
    ApiMappingId: Optional[Id]
    ApiMappingKey: Optional[SelectionKey]
    Stage: Optional[StringWithLengthBetween1And128]


class UpdateApiRequest(ServiceRequest):
    ApiId: __string
    ApiKeySelectionExpression: Optional[SelectionExpression]
    CorsConfiguration: Optional[Cors]
    CredentialsArn: Optional[Arn]
    Description: Optional[StringWithLengthBetween0And1024]
    DisableSchemaValidation: Optional[__boolean]
    DisableExecuteApiEndpoint: Optional[__boolean]
    Name: Optional[StringWithLengthBetween1And128]
    RouteKey: Optional[SelectionKey]
    RouteSelectionExpression: Optional[SelectionExpression]
    Target: Optional[UriWithLengthBetween1And2048]
    Version: Optional[StringWithLengthBetween1And64]


class UpdateApiResponse(TypedDict, total=False):
    ApiEndpoint: Optional[__string]
    ApiGatewayManaged: Optional[__boolean]
    ApiId: Optional[Id]
    ApiKeySelectionExpression: Optional[SelectionExpression]
    CorsConfiguration: Optional[Cors]
    CreatedDate: Optional[__timestampIso8601]
    Description: Optional[StringWithLengthBetween0And1024]
    DisableSchemaValidation: Optional[__boolean]
    DisableExecuteApiEndpoint: Optional[__boolean]
    ImportInfo: Optional[__listOf__string]
    Name: Optional[StringWithLengthBetween1And128]
    ProtocolType: Optional[ProtocolType]
    RouteSelectionExpression: Optional[SelectionExpression]
    Tags: Optional[Tags]
    Version: Optional[StringWithLengthBetween1And64]
    Warnings: Optional[__listOf__string]


class UpdateAuthorizerInput(TypedDict, total=False):
    AuthorizerCredentialsArn: Optional[Arn]
    AuthorizerPayloadFormatVersion: Optional[StringWithLengthBetween1And64]
    AuthorizerResultTtlInSeconds: Optional[IntegerWithLengthBetween0And3600]
    AuthorizerType: Optional[AuthorizerType]
    AuthorizerUri: Optional[UriWithLengthBetween1And2048]
    EnableSimpleResponses: Optional[__boolean]
    IdentitySource: Optional[IdentitySourceList]
    IdentityValidationExpression: Optional[StringWithLengthBetween0And1024]
    JwtConfiguration: Optional[JWTConfiguration]
    Name: Optional[StringWithLengthBetween1And128]


class UpdateAuthorizerRequest(ServiceRequest):
    ApiId: __string
    AuthorizerCredentialsArn: Optional[Arn]
    AuthorizerId: __string
    AuthorizerPayloadFormatVersion: Optional[StringWithLengthBetween1And64]
    AuthorizerResultTtlInSeconds: Optional[IntegerWithLengthBetween0And3600]
    AuthorizerType: Optional[AuthorizerType]
    AuthorizerUri: Optional[UriWithLengthBetween1And2048]
    EnableSimpleResponses: Optional[__boolean]
    IdentitySource: Optional[IdentitySourceList]
    IdentityValidationExpression: Optional[StringWithLengthBetween0And1024]
    JwtConfiguration: Optional[JWTConfiguration]
    Name: Optional[StringWithLengthBetween1And128]


class UpdateAuthorizerResponse(TypedDict, total=False):
    AuthorizerCredentialsArn: Optional[Arn]
    AuthorizerId: Optional[Id]
    AuthorizerPayloadFormatVersion: Optional[StringWithLengthBetween1And64]
    AuthorizerResultTtlInSeconds: Optional[IntegerWithLengthBetween0And3600]
    AuthorizerType: Optional[AuthorizerType]
    AuthorizerUri: Optional[UriWithLengthBetween1And2048]
    EnableSimpleResponses: Optional[__boolean]
    IdentitySource: Optional[IdentitySourceList]
    IdentityValidationExpression: Optional[StringWithLengthBetween0And1024]
    JwtConfiguration: Optional[JWTConfiguration]
    Name: Optional[StringWithLengthBetween1And128]


class UpdateDeploymentInput(TypedDict, total=False):
    Description: Optional[StringWithLengthBetween0And1024]


class UpdateDeploymentRequest(ServiceRequest):
    ApiId: __string
    DeploymentId: __string
    Description: Optional[StringWithLengthBetween0And1024]


class UpdateDeploymentResponse(TypedDict, total=False):
    AutoDeployed: Optional[__boolean]
    CreatedDate: Optional[__timestampIso8601]
    DeploymentId: Optional[Id]
    DeploymentStatus: Optional[DeploymentStatus]
    DeploymentStatusMessage: Optional[__string]
    Description: Optional[StringWithLengthBetween0And1024]


class UpdateDomainNameInput(TypedDict, total=False):
    DomainNameConfigurations: Optional[DomainNameConfigurations]
    MutualTlsAuthentication: Optional[MutualTlsAuthenticationInput]


class UpdateDomainNameRequest(ServiceRequest):
    DomainName: __string
    DomainNameConfigurations: Optional[DomainNameConfigurations]
    MutualTlsAuthentication: Optional[MutualTlsAuthenticationInput]


class UpdateDomainNameResponse(TypedDict, total=False):
    ApiMappingSelectionExpression: Optional[SelectionExpression]
    DomainName: Optional[StringWithLengthBetween1And512]
    DomainNameConfigurations: Optional[DomainNameConfigurations]
    MutualTlsAuthentication: Optional[MutualTlsAuthentication]
    Tags: Optional[Tags]


class UpdateIntegrationInput(TypedDict, total=False):
    ConnectionId: Optional[StringWithLengthBetween1And1024]
    ConnectionType: Optional[ConnectionType]
    ContentHandlingStrategy: Optional[ContentHandlingStrategy]
    CredentialsArn: Optional[Arn]
    Description: Optional[StringWithLengthBetween0And1024]
    IntegrationMethod: Optional[StringWithLengthBetween1And64]
    IntegrationSubtype: Optional[StringWithLengthBetween1And128]
    IntegrationType: Optional[IntegrationType]
    IntegrationUri: Optional[UriWithLengthBetween1And2048]
    PassthroughBehavior: Optional[PassthroughBehavior]
    PayloadFormatVersion: Optional[StringWithLengthBetween1And64]
    RequestParameters: Optional[IntegrationParameters]
    RequestTemplates: Optional[TemplateMap]
    ResponseParameters: Optional[ResponseParameters]
    TemplateSelectionExpression: Optional[SelectionExpression]
    TimeoutInMillis: Optional[IntegerWithLengthBetween50And30000]
    TlsConfig: Optional[TlsConfigInput]


class UpdateIntegrationRequest(ServiceRequest):
    ApiId: __string
    ConnectionId: Optional[StringWithLengthBetween1And1024]
    ConnectionType: Optional[ConnectionType]
    ContentHandlingStrategy: Optional[ContentHandlingStrategy]
    CredentialsArn: Optional[Arn]
    Description: Optional[StringWithLengthBetween0And1024]
    IntegrationId: __string
    IntegrationMethod: Optional[StringWithLengthBetween1And64]
    IntegrationSubtype: Optional[StringWithLengthBetween1And128]
    IntegrationType: Optional[IntegrationType]
    IntegrationUri: Optional[UriWithLengthBetween1And2048]
    PassthroughBehavior: Optional[PassthroughBehavior]
    PayloadFormatVersion: Optional[StringWithLengthBetween1And64]
    RequestParameters: Optional[IntegrationParameters]
    RequestTemplates: Optional[TemplateMap]
    ResponseParameters: Optional[ResponseParameters]
    TemplateSelectionExpression: Optional[SelectionExpression]
    TimeoutInMillis: Optional[IntegerWithLengthBetween50And30000]
    TlsConfig: Optional[TlsConfigInput]


class UpdateIntegrationResult(TypedDict, total=False):
    ApiGatewayManaged: Optional[__boolean]
    ConnectionId: Optional[StringWithLengthBetween1And1024]
    ConnectionType: Optional[ConnectionType]
    ContentHandlingStrategy: Optional[ContentHandlingStrategy]
    CredentialsArn: Optional[Arn]
    Description: Optional[StringWithLengthBetween0And1024]
    IntegrationId: Optional[Id]
    IntegrationMethod: Optional[StringWithLengthBetween1And64]
    IntegrationResponseSelectionExpression: Optional[SelectionExpression]
    IntegrationSubtype: Optional[StringWithLengthBetween1And128]
    IntegrationType: Optional[IntegrationType]
    IntegrationUri: Optional[UriWithLengthBetween1And2048]
    PassthroughBehavior: Optional[PassthroughBehavior]
    PayloadFormatVersion: Optional[StringWithLengthBetween1And64]
    RequestParameters: Optional[IntegrationParameters]
    RequestTemplates: Optional[TemplateMap]
    ResponseParameters: Optional[ResponseParameters]
    TemplateSelectionExpression: Optional[SelectionExpression]
    TimeoutInMillis: Optional[IntegerWithLengthBetween50And30000]
    TlsConfig: Optional[TlsConfig]


class UpdateIntegrationResponseInput(TypedDict, total=False):
    ContentHandlingStrategy: Optional[ContentHandlingStrategy]
    IntegrationResponseKey: Optional[SelectionKey]
    ResponseParameters: Optional[IntegrationParameters]
    ResponseTemplates: Optional[TemplateMap]
    TemplateSelectionExpression: Optional[SelectionExpression]


class UpdateIntegrationResponseRequest(ServiceRequest):
    ApiId: __string
    ContentHandlingStrategy: Optional[ContentHandlingStrategy]
    IntegrationId: __string
    IntegrationResponseId: __string
    IntegrationResponseKey: Optional[SelectionKey]
    ResponseParameters: Optional[IntegrationParameters]
    ResponseTemplates: Optional[TemplateMap]
    TemplateSelectionExpression: Optional[SelectionExpression]


class UpdateIntegrationResponseResponse(TypedDict, total=False):
    ContentHandlingStrategy: Optional[ContentHandlingStrategy]
    IntegrationResponseId: Optional[Id]
    IntegrationResponseKey: Optional[SelectionKey]
    ResponseParameters: Optional[IntegrationParameters]
    ResponseTemplates: Optional[TemplateMap]
    TemplateSelectionExpression: Optional[SelectionExpression]


class UpdateModelInput(TypedDict, total=False):
    ContentType: Optional[StringWithLengthBetween1And256]
    Description: Optional[StringWithLengthBetween0And1024]
    Name: Optional[StringWithLengthBetween1And128]
    Schema: Optional[StringWithLengthBetween0And32K]


class UpdateModelRequest(ServiceRequest):
    ApiId: __string
    ContentType: Optional[StringWithLengthBetween1And256]
    Description: Optional[StringWithLengthBetween0And1024]
    ModelId: __string
    Name: Optional[StringWithLengthBetween1And128]
    Schema: Optional[StringWithLengthBetween0And32K]


class UpdateModelResponse(TypedDict, total=False):
    ContentType: Optional[StringWithLengthBetween1And256]
    Description: Optional[StringWithLengthBetween0And1024]
    ModelId: Optional[Id]
    Name: Optional[StringWithLengthBetween1And128]
    Schema: Optional[StringWithLengthBetween0And32K]


class UpdateRouteInput(TypedDict, total=False):
    ApiKeyRequired: Optional[__boolean]
    AuthorizationScopes: Optional[AuthorizationScopes]
    AuthorizationType: Optional[AuthorizationType]
    AuthorizerId: Optional[Id]
    ModelSelectionExpression: Optional[SelectionExpression]
    OperationName: Optional[StringWithLengthBetween1And64]
    RequestModels: Optional[RouteModels]
    RequestParameters: Optional[RouteParameters]
    RouteKey: Optional[SelectionKey]
    RouteResponseSelectionExpression: Optional[SelectionExpression]
    Target: Optional[StringWithLengthBetween1And128]


class UpdateRouteRequest(ServiceRequest):
    ApiId: __string
    ApiKeyRequired: Optional[__boolean]
    AuthorizationScopes: Optional[AuthorizationScopes]
    AuthorizationType: Optional[AuthorizationType]
    AuthorizerId: Optional[Id]
    ModelSelectionExpression: Optional[SelectionExpression]
    OperationName: Optional[StringWithLengthBetween1And64]
    RequestModels: Optional[RouteModels]
    RequestParameters: Optional[RouteParameters]
    RouteId: __string
    RouteKey: Optional[SelectionKey]
    RouteResponseSelectionExpression: Optional[SelectionExpression]
    Target: Optional[StringWithLengthBetween1And128]


class UpdateRouteResult(TypedDict, total=False):
    ApiGatewayManaged: Optional[__boolean]
    ApiKeyRequired: Optional[__boolean]
    AuthorizationScopes: Optional[AuthorizationScopes]
    AuthorizationType: Optional[AuthorizationType]
    AuthorizerId: Optional[Id]
    ModelSelectionExpression: Optional[SelectionExpression]
    OperationName: Optional[StringWithLengthBetween1And64]
    RequestModels: Optional[RouteModels]
    RequestParameters: Optional[RouteParameters]
    RouteId: Optional[Id]
    RouteKey: Optional[SelectionKey]
    RouteResponseSelectionExpression: Optional[SelectionExpression]
    Target: Optional[StringWithLengthBetween1And128]


class UpdateRouteResponseInput(TypedDict, total=False):
    ModelSelectionExpression: Optional[SelectionExpression]
    ResponseModels: Optional[RouteModels]
    ResponseParameters: Optional[RouteParameters]
    RouteResponseKey: Optional[SelectionKey]


class UpdateRouteResponseRequest(ServiceRequest):
    ApiId: __string
    ModelSelectionExpression: Optional[SelectionExpression]
    ResponseModels: Optional[RouteModels]
    ResponseParameters: Optional[RouteParameters]
    RouteId: __string
    RouteResponseId: __string
    RouteResponseKey: Optional[SelectionKey]


class UpdateRouteResponseResponse(TypedDict, total=False):
    ModelSelectionExpression: Optional[SelectionExpression]
    ResponseModels: Optional[RouteModels]
    ResponseParameters: Optional[RouteParameters]
    RouteResponseId: Optional[Id]
    RouteResponseKey: Optional[SelectionKey]


class UpdateStageInput(TypedDict, total=False):
    AccessLogSettings: Optional[AccessLogSettings]
    AutoDeploy: Optional[__boolean]
    ClientCertificateId: Optional[Id]
    DefaultRouteSettings: Optional[RouteSettings]
    DeploymentId: Optional[Id]
    Description: Optional[StringWithLengthBetween0And1024]
    RouteSettings: Optional[RouteSettingsMap]
    StageVariables: Optional[StageVariablesMap]


class UpdateStageRequest(ServiceRequest):
    AccessLogSettings: Optional[AccessLogSettings]
    ApiId: __string
    AutoDeploy: Optional[__boolean]
    ClientCertificateId: Optional[Id]
    DefaultRouteSettings: Optional[RouteSettings]
    DeploymentId: Optional[Id]
    Description: Optional[StringWithLengthBetween0And1024]
    RouteSettings: Optional[RouteSettingsMap]
    StageName: __string
    StageVariables: Optional[StageVariablesMap]


class UpdateStageResponse(TypedDict, total=False):
    AccessLogSettings: Optional[AccessLogSettings]
    ApiGatewayManaged: Optional[__boolean]
    AutoDeploy: Optional[__boolean]
    ClientCertificateId: Optional[Id]
    CreatedDate: Optional[__timestampIso8601]
    DefaultRouteSettings: Optional[RouteSettings]
    DeploymentId: Optional[Id]
    Description: Optional[StringWithLengthBetween0And1024]
    LastDeploymentStatusMessage: Optional[__string]
    LastUpdatedDate: Optional[__timestampIso8601]
    RouteSettings: Optional[RouteSettingsMap]
    StageName: Optional[StringWithLengthBetween1And128]
    StageVariables: Optional[StageVariablesMap]
    Tags: Optional[Tags]


class UpdateVpcLinkInput(TypedDict, total=False):
    Name: Optional[StringWithLengthBetween1And128]


class UpdateVpcLinkRequest(ServiceRequest):
    Name: Optional[StringWithLengthBetween1And128]
    VpcLinkId: __string


class UpdateVpcLinkResponse(TypedDict, total=False):
    CreatedDate: Optional[__timestampIso8601]
    Name: Optional[StringWithLengthBetween1And128]
    SecurityGroupIds: Optional[SecurityGroupIdList]
    SubnetIds: Optional[SubnetIdList]
    Tags: Optional[Tags]
    VpcLinkId: Optional[Id]
    VpcLinkStatus: Optional[VpcLinkStatus]
    VpcLinkStatusMessage: Optional[StringWithLengthBetween0And1024]
    VpcLinkVersion: Optional[VpcLinkVersion]


class VpcLinks(TypedDict, total=False):
    Items: Optional[__listOfVpcLink]
    NextToken: Optional[NextToken]


__long = int
__timestampUnix = datetime


class Apigatewayv2Api:

    service = "apigatewayv2"
    version = "2018-11-29"

    @handler("CreateApi")
    def create_api(
        self,
        context: RequestContext,
        protocol_type: ProtocolType,
        name: StringWithLengthBetween1And128,
        api_key_selection_expression: SelectionExpression = None,
        cors_configuration: Cors = None,
        credentials_arn: Arn = None,
        description: StringWithLengthBetween0And1024 = None,
        disable_schema_validation: __boolean = None,
        disable_execute_api_endpoint: __boolean = None,
        route_key: SelectionKey = None,
        route_selection_expression: SelectionExpression = None,
        tags: Tags = None,
        target: UriWithLengthBetween1And2048 = None,
        version: StringWithLengthBetween1And64 = None,
    ) -> CreateApiResponse:
        raise NotImplementedError

    @handler("CreateApiMapping")
    def create_api_mapping(
        self,
        context: RequestContext,
        domain_name: __string,
        stage: StringWithLengthBetween1And128,
        api_id: Id,
        api_mapping_key: SelectionKey = None,
    ) -> CreateApiMappingResponse:
        raise NotImplementedError

    @handler("CreateAuthorizer")
    def create_authorizer(
        self,
        context: RequestContext,
        api_id: __string,
        authorizer_type: AuthorizerType,
        identity_source: IdentitySourceList,
        name: StringWithLengthBetween1And128,
        authorizer_credentials_arn: Arn = None,
        authorizer_payload_format_version: StringWithLengthBetween1And64 = None,
        authorizer_result_ttl_in_seconds: IntegerWithLengthBetween0And3600 = None,
        authorizer_uri: UriWithLengthBetween1And2048 = None,
        enable_simple_responses: __boolean = None,
        identity_validation_expression: StringWithLengthBetween0And1024 = None,
        jwt_configuration: JWTConfiguration = None,
    ) -> CreateAuthorizerResponse:
        raise NotImplementedError

    @handler("CreateDeployment")
    def create_deployment(
        self,
        context: RequestContext,
        api_id: __string,
        description: StringWithLengthBetween0And1024 = None,
        stage_name: StringWithLengthBetween1And128 = None,
    ) -> CreateDeploymentResponse:
        raise NotImplementedError

    @handler("CreateDomainName")
    def create_domain_name(
        self,
        context: RequestContext,
        domain_name: StringWithLengthBetween1And512,
        domain_name_configurations: DomainNameConfigurations = None,
        mutual_tls_authentication: MutualTlsAuthenticationInput = None,
        tags: Tags = None,
    ) -> CreateDomainNameResponse:
        raise NotImplementedError

    @handler("CreateIntegration")
    def create_integration(
        self,
        context: RequestContext,
        api_id: __string,
        integration_type: IntegrationType,
        connection_id: StringWithLengthBetween1And1024 = None,
        connection_type: ConnectionType = None,
        content_handling_strategy: ContentHandlingStrategy = None,
        credentials_arn: Arn = None,
        description: StringWithLengthBetween0And1024 = None,
        integration_method: StringWithLengthBetween1And64 = None,
        integration_subtype: StringWithLengthBetween1And128 = None,
        integration_uri: UriWithLengthBetween1And2048 = None,
        passthrough_behavior: PassthroughBehavior = None,
        payload_format_version: StringWithLengthBetween1And64 = None,
        request_parameters: IntegrationParameters = None,
        request_templates: TemplateMap = None,
        response_parameters: ResponseParameters = None,
        template_selection_expression: SelectionExpression = None,
        timeout_in_millis: IntegerWithLengthBetween50And30000 = None,
        tls_config: TlsConfigInput = None,
    ) -> CreateIntegrationResult:
        raise NotImplementedError

    @handler("CreateIntegrationResponse")
    def create_integration_response(
        self,
        context: RequestContext,
        api_id: __string,
        integration_id: __string,
        integration_response_key: SelectionKey,
        content_handling_strategy: ContentHandlingStrategy = None,
        response_parameters: IntegrationParameters = None,
        response_templates: TemplateMap = None,
        template_selection_expression: SelectionExpression = None,
    ) -> CreateIntegrationResponseResponse:
        raise NotImplementedError

    @handler("CreateModel")
    def create_model(
        self,
        context: RequestContext,
        api_id: __string,
        schema: StringWithLengthBetween0And32K,
        name: StringWithLengthBetween1And128,
        content_type: StringWithLengthBetween1And256 = None,
        description: StringWithLengthBetween0And1024 = None,
    ) -> CreateModelResponse:
        raise NotImplementedError

    @handler("CreateRoute")
    def create_route(
        self,
        context: RequestContext,
        api_id: __string,
        route_key: SelectionKey,
        api_key_required: __boolean = None,
        authorization_scopes: AuthorizationScopes = None,
        authorization_type: AuthorizationType = None,
        authorizer_id: Id = None,
        model_selection_expression: SelectionExpression = None,
        operation_name: StringWithLengthBetween1And64 = None,
        request_models: RouteModels = None,
        request_parameters: RouteParameters = None,
        route_response_selection_expression: SelectionExpression = None,
        target: StringWithLengthBetween1And128 = None,
    ) -> CreateRouteResult:
        raise NotImplementedError

    @handler("CreateRouteResponse")
    def create_route_response(
        self,
        context: RequestContext,
        api_id: __string,
        route_id: __string,
        route_response_key: SelectionKey,
        model_selection_expression: SelectionExpression = None,
        response_models: RouteModels = None,
        response_parameters: RouteParameters = None,
    ) -> CreateRouteResponseResponse:
        raise NotImplementedError

    @handler("CreateStage")
    def create_stage(
        self,
        context: RequestContext,
        api_id: __string,
        stage_name: StringWithLengthBetween1And128,
        access_log_settings: AccessLogSettings = None,
        auto_deploy: __boolean = None,
        client_certificate_id: Id = None,
        default_route_settings: RouteSettings = None,
        deployment_id: Id = None,
        description: StringWithLengthBetween0And1024 = None,
        route_settings: RouteSettingsMap = None,
        stage_variables: StageVariablesMap = None,
        tags: Tags = None,
    ) -> CreateStageResponse:
        raise NotImplementedError

    @handler("CreateVpcLink")
    def create_vpc_link(
        self,
        context: RequestContext,
        subnet_ids: SubnetIdList,
        name: StringWithLengthBetween1And128,
        security_group_ids: SecurityGroupIdList = None,
        tags: Tags = None,
    ) -> CreateVpcLinkResponse:
        raise NotImplementedError

    @handler("DeleteAccessLogSettings")
    def delete_access_log_settings(
        self, context: RequestContext, stage_name: __string, api_id: __string
    ) -> None:
        raise NotImplementedError

    @handler("DeleteApi")
    def delete_api(self, context: RequestContext, api_id: __string) -> None:
        raise NotImplementedError

    @handler("DeleteApiMapping")
    def delete_api_mapping(
        self, context: RequestContext, api_mapping_id: __string, domain_name: __string
    ) -> None:
        raise NotImplementedError

    @handler("DeleteAuthorizer")
    def delete_authorizer(
        self, context: RequestContext, authorizer_id: __string, api_id: __string
    ) -> None:
        raise NotImplementedError

    @handler("DeleteCorsConfiguration")
    def delete_cors_configuration(self, context: RequestContext, api_id: __string) -> None:
        raise NotImplementedError

    @handler("DeleteDeployment")
    def delete_deployment(
        self, context: RequestContext, api_id: __string, deployment_id: __string
    ) -> None:
        raise NotImplementedError

    @handler("DeleteDomainName")
    def delete_domain_name(self, context: RequestContext, domain_name: __string) -> None:
        raise NotImplementedError

    @handler("DeleteIntegration")
    def delete_integration(
        self, context: RequestContext, api_id: __string, integration_id: __string
    ) -> None:
        raise NotImplementedError

    @handler("DeleteIntegrationResponse")
    def delete_integration_response(
        self,
        context: RequestContext,
        api_id: __string,
        integration_response_id: __string,
        integration_id: __string,
    ) -> None:
        raise NotImplementedError

    @handler("DeleteModel")
    def delete_model(self, context: RequestContext, model_id: __string, api_id: __string) -> None:
        raise NotImplementedError

    @handler("DeleteRoute")
    def delete_route(self, context: RequestContext, api_id: __string, route_id: __string) -> None:
        raise NotImplementedError

    @handler("DeleteRouteRequestParameter")
    def delete_route_request_parameter(
        self,
        context: RequestContext,
        request_parameter_key: __string,
        api_id: __string,
        route_id: __string,
    ) -> None:
        raise NotImplementedError

    @handler("DeleteRouteResponse")
    def delete_route_response(
        self,
        context: RequestContext,
        route_response_id: __string,
        api_id: __string,
        route_id: __string,
    ) -> None:
        raise NotImplementedError

    @handler("DeleteRouteSettings")
    def delete_route_settings(
        self,
        context: RequestContext,
        stage_name: __string,
        route_key: __string,
        api_id: __string,
    ) -> None:
        raise NotImplementedError

    @handler("DeleteStage")
    def delete_stage(self, context: RequestContext, stage_name: __string, api_id: __string) -> None:
        raise NotImplementedError

    @handler("DeleteVpcLink")
    def delete_vpc_link(
        self, context: RequestContext, vpc_link_id: __string
    ) -> DeleteVpcLinkResponse:
        raise NotImplementedError

    @handler("ExportApi")
    def export_api(
        self,
        context: RequestContext,
        specification: __string,
        output_type: __string,
        api_id: __string,
        export_version: __string = None,
        include_extensions: __boolean = None,
        stage_name: __string = None,
    ) -> ExportApiResponse:
        raise NotImplementedError

    @handler("ResetAuthorizersCache")
    def reset_authorizers_cache(
        self, context: RequestContext, stage_name: __string, api_id: __string
    ) -> None:
        raise NotImplementedError

    @handler("GetApi")
    def get_api(self, context: RequestContext, api_id: __string) -> GetApiResponse:
        raise NotImplementedError

    @handler("GetApiMapping")
    def get_api_mapping(
        self, context: RequestContext, api_mapping_id: __string, domain_name: __string
    ) -> GetApiMappingResponse:
        raise NotImplementedError

    @handler("GetApiMappings")
    def get_api_mappings(
        self,
        context: RequestContext,
        domain_name: __string,
        max_results: __string = None,
        next_token: __string = None,
    ) -> GetApiMappingsResponse:
        raise NotImplementedError

    @handler("GetApis")
    def get_apis(
        self,
        context: RequestContext,
        max_results: __string = None,
        next_token: __string = None,
    ) -> GetApisResponse:
        raise NotImplementedError

    @handler("GetAuthorizer")
    def get_authorizer(
        self, context: RequestContext, authorizer_id: __string, api_id: __string
    ) -> GetAuthorizerResponse:
        raise NotImplementedError

    @handler("GetAuthorizers")
    def get_authorizers(
        self,
        context: RequestContext,
        api_id: __string,
        max_results: __string = None,
        next_token: __string = None,
    ) -> GetAuthorizersResponse:
        raise NotImplementedError

    @handler("GetDeployment")
    def get_deployment(
        self, context: RequestContext, api_id: __string, deployment_id: __string
    ) -> GetDeploymentResponse:
        raise NotImplementedError

    @handler("GetDeployments")
    def get_deployments(
        self,
        context: RequestContext,
        api_id: __string,
        max_results: __string = None,
        next_token: __string = None,
    ) -> GetDeploymentsResponse:
        raise NotImplementedError

    @handler("GetDomainName")
    def get_domain_name(
        self, context: RequestContext, domain_name: __string
    ) -> GetDomainNameResponse:
        raise NotImplementedError

    @handler("GetDomainNames")
    def get_domain_names(
        self,
        context: RequestContext,
        max_results: __string = None,
        next_token: __string = None,
    ) -> GetDomainNamesResponse:
        raise NotImplementedError

    @handler("GetIntegration")
    def get_integration(
        self, context: RequestContext, api_id: __string, integration_id: __string
    ) -> GetIntegrationResult:
        raise NotImplementedError

    @handler("GetIntegrationResponse")
    def get_integration_response(
        self,
        context: RequestContext,
        api_id: __string,
        integration_response_id: __string,
        integration_id: __string,
    ) -> GetIntegrationResponseResponse:
        raise NotImplementedError

    @handler("GetIntegrationResponses")
    def get_integration_responses(
        self,
        context: RequestContext,
        integration_id: __string,
        api_id: __string,
        max_results: __string = None,
        next_token: __string = None,
    ) -> GetIntegrationResponsesResponse:
        raise NotImplementedError

    @handler("GetIntegrations")
    def get_integrations(
        self,
        context: RequestContext,
        api_id: __string,
        max_results: __string = None,
        next_token: __string = None,
    ) -> GetIntegrationsResponse:
        raise NotImplementedError

    @handler("GetModel")
    def get_model(
        self, context: RequestContext, model_id: __string, api_id: __string
    ) -> GetModelResponse:
        raise NotImplementedError

    @handler("GetModelTemplate")
    def get_model_template(
        self, context: RequestContext, model_id: __string, api_id: __string
    ) -> GetModelTemplateResponse:
        raise NotImplementedError

    @handler("GetModels")
    def get_models(
        self,
        context: RequestContext,
        api_id: __string,
        max_results: __string = None,
        next_token: __string = None,
    ) -> GetModelsResponse:
        raise NotImplementedError

    @handler("GetRoute")
    def get_route(
        self, context: RequestContext, api_id: __string, route_id: __string
    ) -> GetRouteResult:
        raise NotImplementedError

    @handler("GetRouteResponse")
    def get_route_response(
        self,
        context: RequestContext,
        route_response_id: __string,
        api_id: __string,
        route_id: __string,
    ) -> GetRouteResponseResponse:
        raise NotImplementedError

    @handler("GetRouteResponses")
    def get_route_responses(
        self,
        context: RequestContext,
        route_id: __string,
        api_id: __string,
        max_results: __string = None,
        next_token: __string = None,
    ) -> GetRouteResponsesResponse:
        raise NotImplementedError

    @handler("GetRoutes")
    def get_routes(
        self,
        context: RequestContext,
        api_id: __string,
        max_results: __string = None,
        next_token: __string = None,
    ) -> GetRoutesResponse:
        raise NotImplementedError

    @handler("GetStage")
    def get_stage(
        self, context: RequestContext, stage_name: __string, api_id: __string
    ) -> GetStageResponse:
        raise NotImplementedError

    @handler("GetStages")
    def get_stages(
        self,
        context: RequestContext,
        api_id: __string,
        max_results: __string = None,
        next_token: __string = None,
    ) -> GetStagesResponse:
        raise NotImplementedError

    @handler("GetTags")
    def get_tags(self, context: RequestContext, resource_arn: __string) -> GetTagsResponse:
        raise NotImplementedError

    @handler("GetVpcLink")
    def get_vpc_link(self, context: RequestContext, vpc_link_id: __string) -> GetVpcLinkResponse:
        raise NotImplementedError

    @handler("GetVpcLinks")
    def get_vpc_links(
        self,
        context: RequestContext,
        max_results: __string = None,
        next_token: __string = None,
    ) -> GetVpcLinksResponse:
        raise NotImplementedError

    @handler("ImportApi")
    def import_api(
        self,
        context: RequestContext,
        body: __string,
        basepath: __string = None,
        fail_on_warnings: __boolean = None,
    ) -> ImportApiResponse:
        raise NotImplementedError

    @handler("ReimportApi")
    def reimport_api(
        self,
        context: RequestContext,
        api_id: __string,
        body: __string,
        basepath: __string = None,
        fail_on_warnings: __boolean = None,
    ) -> ReimportApiResponse:
        raise NotImplementedError

    @handler("TagResource")
    def tag_resource(
        self, context: RequestContext, resource_arn: __string, tags: Tags = None
    ) -> TagResourceResponse:
        raise NotImplementedError

    @handler("UntagResource")
    def untag_resource(
        self,
        context: RequestContext,
        resource_arn: __string,
        tag_keys: __listOf__string,
    ) -> None:
        raise NotImplementedError

    @handler("UpdateApi")
    def update_api(
        self,
        context: RequestContext,
        api_id: __string,
        api_key_selection_expression: SelectionExpression = None,
        cors_configuration: Cors = None,
        credentials_arn: Arn = None,
        description: StringWithLengthBetween0And1024 = None,
        disable_schema_validation: __boolean = None,
        disable_execute_api_endpoint: __boolean = None,
        name: StringWithLengthBetween1And128 = None,
        route_key: SelectionKey = None,
        route_selection_expression: SelectionExpression = None,
        target: UriWithLengthBetween1And2048 = None,
        version: StringWithLengthBetween1And64 = None,
    ) -> UpdateApiResponse:
        raise NotImplementedError

    @handler("UpdateApiMapping")
    def update_api_mapping(
        self,
        context: RequestContext,
        api_mapping_id: __string,
        api_id: Id,
        domain_name: __string,
        api_mapping_key: SelectionKey = None,
        stage: StringWithLengthBetween1And128 = None,
    ) -> UpdateApiMappingResponse:
        raise NotImplementedError

    @handler("UpdateAuthorizer")
    def update_authorizer(
        self,
        context: RequestContext,
        authorizer_id: __string,
        api_id: __string,
        authorizer_credentials_arn: Arn = None,
        authorizer_payload_format_version: StringWithLengthBetween1And64 = None,
        authorizer_result_ttl_in_seconds: IntegerWithLengthBetween0And3600 = None,
        authorizer_type: AuthorizerType = None,
        authorizer_uri: UriWithLengthBetween1And2048 = None,
        enable_simple_responses: __boolean = None,
        identity_source: IdentitySourceList = None,
        identity_validation_expression: StringWithLengthBetween0And1024 = None,
        jwt_configuration: JWTConfiguration = None,
        name: StringWithLengthBetween1And128 = None,
    ) -> UpdateAuthorizerResponse:
        raise NotImplementedError

    @handler("UpdateDeployment")
    def update_deployment(
        self,
        context: RequestContext,
        api_id: __string,
        deployment_id: __string,
        description: StringWithLengthBetween0And1024 = None,
    ) -> UpdateDeploymentResponse:
        raise NotImplementedError

    @handler("UpdateDomainName")
    def update_domain_name(
        self,
        context: RequestContext,
        domain_name: __string,
        domain_name_configurations: DomainNameConfigurations = None,
        mutual_tls_authentication: MutualTlsAuthenticationInput = None,
    ) -> UpdateDomainNameResponse:
        raise NotImplementedError

    @handler("UpdateIntegration")
    def update_integration(
        self,
        context: RequestContext,
        api_id: __string,
        integration_id: __string,
        connection_id: StringWithLengthBetween1And1024 = None,
        connection_type: ConnectionType = None,
        content_handling_strategy: ContentHandlingStrategy = None,
        credentials_arn: Arn = None,
        description: StringWithLengthBetween0And1024 = None,
        integration_method: StringWithLengthBetween1And64 = None,
        integration_subtype: StringWithLengthBetween1And128 = None,
        integration_type: IntegrationType = None,
        integration_uri: UriWithLengthBetween1And2048 = None,
        passthrough_behavior: PassthroughBehavior = None,
        payload_format_version: StringWithLengthBetween1And64 = None,
        request_parameters: IntegrationParameters = None,
        request_templates: TemplateMap = None,
        response_parameters: ResponseParameters = None,
        template_selection_expression: SelectionExpression = None,
        timeout_in_millis: IntegerWithLengthBetween50And30000 = None,
        tls_config: TlsConfigInput = None,
    ) -> UpdateIntegrationResult:
        raise NotImplementedError

    @handler("UpdateIntegrationResponse")
    def update_integration_response(
        self,
        context: RequestContext,
        api_id: __string,
        integration_response_id: __string,
        integration_id: __string,
        content_handling_strategy: ContentHandlingStrategy = None,
        integration_response_key: SelectionKey = None,
        response_parameters: IntegrationParameters = None,
        response_templates: TemplateMap = None,
        template_selection_expression: SelectionExpression = None,
    ) -> UpdateIntegrationResponseResponse:
        raise NotImplementedError

    @handler("UpdateModel")
    def update_model(
        self,
        context: RequestContext,
        model_id: __string,
        api_id: __string,
        content_type: StringWithLengthBetween1And256 = None,
        description: StringWithLengthBetween0And1024 = None,
        name: StringWithLengthBetween1And128 = None,
        schema: StringWithLengthBetween0And32K = None,
    ) -> UpdateModelResponse:
        raise NotImplementedError

    @handler("UpdateRoute")
    def update_route(
        self,
        context: RequestContext,
        api_id: __string,
        route_id: __string,
        api_key_required: __boolean = None,
        authorization_scopes: AuthorizationScopes = None,
        authorization_type: AuthorizationType = None,
        authorizer_id: Id = None,
        model_selection_expression: SelectionExpression = None,
        operation_name: StringWithLengthBetween1And64 = None,
        request_models: RouteModels = None,
        request_parameters: RouteParameters = None,
        route_key: SelectionKey = None,
        route_response_selection_expression: SelectionExpression = None,
        target: StringWithLengthBetween1And128 = None,
    ) -> UpdateRouteResult:
        raise NotImplementedError

    @handler("UpdateRouteResponse")
    def update_route_response(
        self,
        context: RequestContext,
        route_response_id: __string,
        api_id: __string,
        route_id: __string,
        model_selection_expression: SelectionExpression = None,
        response_models: RouteModels = None,
        response_parameters: RouteParameters = None,
        route_response_key: SelectionKey = None,
    ) -> UpdateRouteResponseResponse:
        raise NotImplementedError

    @handler("UpdateStage")
    def update_stage(
        self,
        context: RequestContext,
        stage_name: __string,
        api_id: __string,
        access_log_settings: AccessLogSettings = None,
        auto_deploy: __boolean = None,
        client_certificate_id: Id = None,
        default_route_settings: RouteSettings = None,
        deployment_id: Id = None,
        description: StringWithLengthBetween0And1024 = None,
        route_settings: RouteSettingsMap = None,
        stage_variables: StageVariablesMap = None,
    ) -> UpdateStageResponse:
        raise NotImplementedError

    @handler("UpdateVpcLink")
    def update_vpc_link(
        self,
        context: RequestContext,
        vpc_link_id: __string,
        name: StringWithLengthBetween1And128 = None,
    ) -> UpdateVpcLinkResponse:
        raise NotImplementedError
