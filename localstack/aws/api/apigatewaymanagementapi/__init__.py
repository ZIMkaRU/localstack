import sys
from datetime import datetime
from typing import Optional

if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict

from localstack.aws.api import RequestContext, ServiceException, ServiceRequest, handler

__string = str


class ForbiddenException(ServiceException):
    pass


class GoneException(ServiceException):
    pass


class PayloadTooLargeException(ServiceException):
    Message: Optional[__string]


class LimitExceededException(ServiceException):
    pass


Data = bytes


class DeleteConnectionRequest(ServiceRequest):
    ConnectionId: __string


class GetConnectionRequest(ServiceRequest):
    ConnectionId: __string


__timestampIso8601 = datetime


class Identity(TypedDict, total=False):
    SourceIp: __string
    UserAgent: __string


class GetConnectionResponse(TypedDict, total=False):
    ConnectedAt: Optional[__timestampIso8601]
    Identity: Optional[Identity]
    LastActiveAt: Optional[__timestampIso8601]


class PostToConnectionRequest(ServiceRequest):
    Data: Data
    ConnectionId: __string


class ApigatewaymanagementapiApi:

    service = "apigatewaymanagementapi"
    version = "2018-11-29"

    @handler("DeleteConnection")
    def delete_connection(self, context: RequestContext, connection_id: __string) -> None:
        raise NotImplementedError

    @handler("GetConnection")
    def get_connection(
        self, context: RequestContext, connection_id: __string
    ) -> GetConnectionResponse:
        raise NotImplementedError

    @handler("PostToConnection")
    def post_to_connection(
        self, context: RequestContext, connection_id: __string, data: Data
    ) -> None:
        raise NotImplementedError
