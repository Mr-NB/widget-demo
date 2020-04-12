#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from app.config import MongoConfig
from app.util import Util
from app import app


class MONGO(object):

    def __init__(self, db=MongoConfig.MongoDB, collectionName=None):
        self.client = app.MongoClient
        self.db = self.client[db][collectionName]

    async def create_index(self, name=None, fields=None, expire=0):
        if fields:
            await self.drop_index(name)
            return await self.db.create_index(fields, expireAfterSeconds=expire, name=name)

    async def drop_index(self, index_name):
        try:
            await self.db.drop_index(index_name)
        except:
            pass

    async def show_index(self):
        return await self.db.index_information()

    async def update_one(self,filter = {}, operation={},upsert = True):
        update_res = await self.db.update_one(filter=filter,update=operation,upsert=upsert)
        return update_res.modified_count

    async def insert_one(self, data=None):
        await self.db.insert_one(data)

    async def insert_many(self, data=None, orderd=True):
        result = await self.db.insert_many(data, ordered=orderd)
        return result

    async def find(self, fiter_condition={}, show_parameters={"_id": 0}, length=100000,
                   sort=("_id", 1)):
        documents = self.db.find(fiter_condition, show_parameters).sort([sort])
        result_list = await documents.to_list(length=length)
        return result_list

    async def mongo_delete(self, filter_condition={}):
        await self.db.delete_one(filter_condition)

    async def mongo_group(self, name=None, filter=None, length=100000):

        '''

        :param collectionname:
        :param name:
        :param filter: [
                {
                    "$match":filter

                },
                 {
                "$group": {"_id": "$group_by_key", "count": {"$sum": 1},
                "XD_ids":{"$push":"$will show"}}
                 }
            ]  type|list
        :param length:
        :return: {'_id': 'lifestyle', 'count': 1}
        '''

        if filter:
            result = self.db.aggregate(filter)
        else:
            result = self.db.aggregate([{
                "$group": {"_id": "${}".format(name), "count": {"$sum": 1}}
            }])
        result_list = await result.to_list(length=length)
        return result_list
