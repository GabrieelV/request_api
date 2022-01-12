from fastapi import APIRouter, Request as RequestFastAPI

starships_routes = APIRouter()

@starships_routes.get("/api/starships/list")
def get_starships_in_pagination(request: RequestFastAPI):
    " get_starships_in_pagination "
    print(request.query_params['page'])
    print(request.query_params['ola'])

    return { "Ola": "mundo!" }
