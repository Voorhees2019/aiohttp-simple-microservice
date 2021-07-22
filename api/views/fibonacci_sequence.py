from aiohttp import web
from aiohttp_apispec import docs, response_schema, request_schema
from api import schema


async def get_fibonacci_numbers_till(n: int) -> list:
    a, b = 0, 1
    fibonacci_list = []
    while a < n:
        fibonacci_list.append(a)
        a, b = b, a + b
    return fibonacci_list


class FibonacciSequenceView(web.View):
    @docs(
        tags=["Fibonacci sequence"],
        summary="Display Fibonacci sequence",
        description="Get as a response Fibonacci sequence till the given 'N' parameter in request body. "
                    "'N' must be in range [0, 1 000 000]",
    )
    @request_schema(schema=schema.FibonacciRequestSchema())
    @response_schema(
        schema=schema.FibonacciSuccessSchema(),
        code=200,
        description="Return success response with dict",
    )
    @response_schema(
        schema=schema.BadRequestSchema(),
        code=400,
        description="Return success response with dict",
    )
    async def post(self):
        if not self.request.body_exists:
            raise web.HTTPBadRequest(text='[ERROR] Provide N parameter')

        body = await self.request.json()
        n = body.get('n')
        try:
            n = int(n)
        except ValueError:
            raise web.HTTPBadRequest(text='[ERROR] N must be an integer')

        if n < 0 or n > 1_000_000:
            raise web.HTTPBadRequest(text='[ERROR] N must be an integer from 0 to 1 000 000')

        fibonacci_seq = await get_fibonacci_numbers_till(n)
        return web.json_response({f'fibonacci_sequence': fibonacci_seq})
