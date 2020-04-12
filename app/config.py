import os, sys
from enum import Enum
from motor.motor_asyncio import AsyncIOMotorClient

METRIC = {
    "MSN_NAV": {
        "CRAWL_NAME": "MSN China navigation monitor",
        "INDEX_URL": 'https://www.msn.cn/zh-cn',

    },
    "NEW_Edge_MSN": {
        "CRAWL_NAME": "New Msn Edege Monitor",
        "INDEX_URL": os.environ.get('EDGE_URL', 'https://www.msn.cn/spartan/ntp?locale=zh-cn'),
        'monitor_type': 1

    },
    "NEW_Ie_MSN": {
        "CRAWL_NAME": "New Msn Ie Monitor",
        "INDEX_URL": os.environ.get('IE_URL', 'https://www.msn.cn/spartan/ientp?locale=zh-cn'),
        'monitor_type': 2

    },
    "NEW_Ext_MSN": {
        "CRAWL_NAME": "New Msn Ext Monitor",
        "INDEX_URL": os.environ.get('EXT_URL', 'https://www.msn.cn/spartan/dhp?locale=zh-cn'),
        'monitor_type': 3

    },
    "NEW_Chrome_MSN": {
        "CRAWL_NAME": "New Msn Chrome Monitor",
        "INDEX_URL": 'https://www.msn.cn/spartan/extntp?locale=zh-cn',

    },

}


class MongoConfig:
    MongoHost = str(os.environ.get('MONGO_HOST', '127.0.0.1'))
    MongoPort = int(os.environ.get('MONGO_PORT', 27017))
    MongoDB = str(os.environ.get('MONGO_DATABASE', "monitor_msn"))
    MONGODB_POOL_SIZE = int(os.environ.get('MAXPOOLSIZE', 100))
    MongoClient = AsyncIOMotorClient(MongoHost, MongoPort)
    CrawlLog = 'crawl_log'
    MonitorLog = 'monitor_log'
    IpStatistic = 'IpStatistic'

class IssueType(Enum):
    Timeout = 0
    RedirectToHomepage = 1
    ErrorPage = 2
    NotFoundPage = 404


class CodeStatus(Enum):
    SuccessCode = 200
    # if 很抱歉！您访问页面被外星人劫持了 in response,use 208
    LogoWordsError = 208
    Unauthorized = 401
    NotFoundError = 404
    RequestError = 400
    UnknownError = 500
    TimeoutError = 504
    NoDataError = 152
    CmsApiError = 153
    CmsUndoPublishError = 156
    PermissionDenied = 104
    FormatError = 105
    ParametersMissError = 106
    ParametersTypeError = 107
    InvalidDataError = 108
    DataDuplicateError = 109
    SqlError = 110
    SendMailError = 111
    JobRunError = 112
    CmsApiFormatError = 157


class BaseConfig:
    pass


class Local(BaseConfig):
    name = sys._getframe().f_code.co_name

    @property
    async def config(self):
        res = await MongoConfig.MongoClient[MongoConfig.MongoDB].DynamicConfig.find_one({"env": self.name},{"_id": 0})
        return res


class Pro(BaseConfig):
    name = sys._getframe().f_code.co_name

    @property
    async def config(self):
        res = await MongoConfig.MongoClient[MongoConfig.MongoDB].DynamicConfig.find_one({"env": self.name},{"_id": 0})
        return res


class Dev(BaseConfig):
    name = sys._getframe().f_code.co_name

    @property
    async def config(self):
        res = await MongoConfig.MongoClient[MongoConfig.MongoDB].DynamicConfig.find_one({"env": self.name}, {"_id": 0})
        return res
