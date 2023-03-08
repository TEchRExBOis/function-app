

import logging

import azure.functions as func

import os
import uvicorn
from pymongo import MongoClient
from fastapi import FastAPI


def main(req: func.HttpRequest) -> func.HttpResponse:
    headers = {
    'Access-Control-Allow-Origin': '*',
    'Access-Control-Allow-Methods': 'GET, POST, PUT, DELETE',
    'Access-Control-Allow-Headers': 'Content-Type'
}
    logging.info('Python HTTP trigger function processed a request.')
    cosmos_client = MongoClient("mongodb://tfex-cosmos-db-75497:cUI5RlR3rvMhQJ75dONdGMtPq4F3VFwCT9d1abrNDC2PB9XB7bRLfh7BENTStz1iVTTOekSto4hmACDbYjOCPw==@tfex-cosmos-db-75497.mongo.cosmos.azure.com:10255/?ssl=true&retrywrites=false&replicaSet=globaldb&maxIdleTimeMS=120000&appName=@tfex-cosmos-db-75497@")
    database_name = "website_visits"
    collection_name = "visits"

    collection = cosmos_client[database_name][collection_name]
    document = collection.find_one()

    # Get the visits field from the document
    count = int(document["visits"])

    print(count)
    # Increment visit count and save to Cosmos DB
    new_count = count + 1
    collection.replace_one({}, {"visits": new_count}, upsert=True)

    #return {"message": f"Welcome to my website! You are visitor number {new_count}."}
    # return func.HttpResponse(f"Welcome! You are visitor number {new_count}.")
#    name = req.params.get('name')
    #if not name:
    #    try:
    #        req_body = req.get_json()
    #    except ValueError:
    #        pass
    #    else:
    #        name = req_body.get('name')

    #if name:
        #return func.HttpResponse(f"Hello, {name}. This HTTP triggered function executed successfully.")
    return func.HttpResponse(f"{new_count}", headers=headers)
    
    #else:
    #    return func.HttpResponse(
    #         "This HTTP triggered function executed successfully. Pass a name in the query string or in the request body for a personalized response.",
    #         status_code=200




             
   #     )

   #change file name
   #change another file name
