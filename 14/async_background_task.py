from time import time
import asyncio
from all.sites import sites
from aiohttp import web, request
from aiohttp.web_middlewares import middleware
from aiohttp.web_request import Request
from aiohttp.web_response import json_response


user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36 (KHTML, like Gecko) ' \
             'Chrome/81.0.4044.138 Safari/537.36'


site_check_results = {}


async def background_task():
    while True:
        pending = [asyncio.create_task(send_request(site)) for site in sites]

        while pending:
            done, pending = await asyncio.wait(pending, return_when=asyncio.FIRST_COMPLETED)
            task_result = done.pop().result()
            url, status = task_result

            site_check_results[url] = {
                'status': status,
                'time': time(),
            }

        print(time(), 'Background task interation done')
        await asyncio.sleep(10)


async def start_background_tasks(app):
    app['background_task'] = asyncio.create_task(background_task())


async def stop_background_tasks(app):
    app['background_task'].cancel()
    await app['background_task']


async def send_request(url):                                                            # выполняет http запрос и возращает статус
    async with request('GET', url, headers={'User-Agent': user_agent}) as response:
        return url, response.status


async def ping(request: Request):
    return site_check_results


async def health(request: Request):
    print(asyncio.all_tasks())
    return {'message': 'ok'}


@middleware
async def json_middleware(request, handler):
    resp = await handler(request)
    return json_response(resp)


app = web.Application(middlewares=[json_middleware])
app.router.add_route('GET', "/ping", ping)                                              # какой http метод, адрес, и сам header (функция)
app.router.add_route('GET', "/health", health)
app.on_startup.append(start_background_tasks)
app.on_cleanup.append(stop_background_tasks)


if __name__ == '__main__':
    web.run_app(app, host="127.0.0.1")