from aiohttp import web
from decimal import Decimal, InvalidOperation
from multidict._multidict import MultiDictProxy

import simplejson


async def update_dict(query: MultiDictProxy) -> dict:
    data = {}
    total_dict = {'total_int': 0, 'total_decimal': Decimal('0')}
    for i, (key, val) in enumerate(query.items(), 1):
        if i % 2 != 0:
            try:
                data[key] = Decimal(val)
                total_dict['total_int'] += Decimal(val)
            except InvalidOperation:
                data[key] = val[::-1]
        elif i % 2 == 0:
            try:
                data[key] = int(val)
                total_dict['total_decimal'] += int(val)
            except ValueError:
                data[key] = val

    data.update(total_dict)
    return data


class DictUpdateView(web.View):
    async def put(self):
        updated_dict = await update_dict(self.request.query)
        data = simplejson.dumps(updated_dict)  # to normally serialize type Decimal into JSON
        return web.json_response(data)
