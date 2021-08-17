from up9lib import *
from authentication import authenticate

# logging.basicConfig(level=logging.DEBUG)


@data_driven_tests
class Tests_orders_sock_shop(unittest.TestCase):

    @json_dataset('data/10/dataset_10.json')
    @clear_session({'spanId': 10})
    def test_010_post_orders(self, data_row):
        address, card, customer, items = data_row

        # POST http://orders.sock-shop/orders (endp 10)
        orders_sock_shop = get_http_client('http://orders.sock-shop', authenticate)
        with open('data/10/payload_for_endp_10.json', 'r') as json_payload_file:
            json_payload = json.load(json_payload_file)
        apply_into_json(json_payload, '$.address', address)
        apply_into_json(json_payload, '$.card', card)
        apply_into_json(json_payload, '$.customer', customer)
        apply_into_json(json_payload, '$.items', items)
        resp = orders_sock_shop.post('/orders', json=json_payload, headers={'accept': 'application/json'})
        resp.assert_status_code(201)
        resp.assert_jsonpath('$.address.city', expected_value='Glasgow')

    @json_dataset('data/155/dataset_155.json')
    @clear_session({'spanId': 155})
    def test_155_post_orders(self, data_row):
        address, card, card1, customer, items, items1 = data_row

        # POST http://orders.sock-shop/orders (endp 10)
        orders_sock_shop = get_http_client('http://orders.sock-shop', authenticate)
        with open('data/155/payload_for_endp_10.json', 'r') as json_payload_file:
            json_payload = json.load(json_payload_file)
        apply_into_json(json_payload, '$.address', address)
        apply_into_json(json_payload, '$.card', card)
        apply_into_json(json_payload, '$.customer', customer)
        apply_into_json(json_payload, '$.items', items)
        resp = orders_sock_shop.post('/orders', json=json_payload, headers={'accept': 'application/json'})
        resp.assert_status_code(201)
        resp.assert_jsonpath('$.address.city', expected_value='Glasgow')
        customerId = jsonpath('$.customerId', resp)

        # GET http://user.sock-shop/customers/{customerId} (endp 127)
        user_sock_shop = get_http_client('http://user.sock-shop', authenticate)
        resp = user_sock_shop.get(f'/customers/{customerId}', headers={'accept': 'application/hal+json'})
        resp.assert_status_code(200)
        resp.assert_jsonpath('$._links.self.href')
        customer1 = jsonpath('$._links.self.href', resp)

        # GET http://user.sock-shop/customers/{customerId}/addresses (endp 128)
        resp = user_sock_shop.get(f'/customers/{customerId}/addresses')
        resp.assert_status_code(200)
        resp.assert_jsonpath('$._embedded.address[*]._links.self.href')
        address1 = jsonpath('$._embedded.address[*]._links.address.href', resp)

        # POST http://orders.sock-shop/orders (endp 155)
        with open('data/155/payload_for_endp_155.json', 'r') as json_payload_file:
            json_payload = json.load(json_payload_file)
        apply_into_json(json_payload, '$.address', address1)
        apply_into_json(json_payload, '$.card', card1)
        apply_into_json(json_payload, '$.customer', customer1)
        apply_into_json(json_payload, '$.items', items1)
        resp = orders_sock_shop.post('/orders', json=json_payload, headers={'accept': 'application/json'})
        resp.assert_status_code(201)
        resp.assert_jsonpath('$.card.ccv')

    @json_dataset('data/92/dataset_92.json')
    @clear_session({'spanId': 92})
    def test_092_get_orders_id(self, data_row):
        address, card, customer, items = data_row

        # POST http://orders.sock-shop/orders (endp 10)
        orders_sock_shop = get_http_client('http://orders.sock-shop', authenticate)
        with open('data/92/payload_for_endp_10.json', 'r') as json_payload_file:
            json_payload = json.load(json_payload_file)
        apply_into_json(json_payload, '$.address', address)
        apply_into_json(json_payload, '$.card', card)
        apply_into_json(json_payload, '$.customer', customer)
        apply_into_json(json_payload, '$.items', items)
        resp = orders_sock_shop.post('/orders', json=json_payload, headers={'accept': 'application/json'})
        resp.assert_status_code(201)
        resp.assert_jsonpath('$.address.city', expected_value='Glasgow')
        custId = jsonpath('$.customerId', resp)

        # GET http://orders.sock-shop/orders/search/customerId (endp 94)
        qstr = '?' + urlencode({'custId': custId, 'sort': 'date'})
        resp = orders_sock_shop.get('/orders/search/customerId' + qstr)
        resp.assert_status_code(200)
        resp.assert_jsonpath('$._embedded.customerOrders.[*].address.country', expected_value='United Kingdom')
        id_ = url_part('/2', jsonpath('$._embedded.customerOrders[*]._links.self.href', resp))

        # GET http://orders.sock-shop/orders/{id} (endp 92)
        resp = orders_sock_shop.get(f'/orders/{id_}')
        resp.assert_status_code(200)
        resp.assert_jsonpath('$.address.city', expected_value='Glasgow')

    @json_dataset('data/199/dataset_199.json')
    @clear_session({'spanId': 199})
    def test_199_get_orders_id(self, data_row):
        address, card, customer, items = data_row

        # POST http://orders.sock-shop/orders (endp 10)
        orders_sock_shop = get_http_client('http://orders.sock-shop', authenticate)
        with open('data/199/payload_for_endp_10.json', 'r') as json_payload_file:
            json_payload = json.load(json_payload_file)
        apply_into_json(json_payload, '$.address', address)
        apply_into_json(json_payload, '$.card', card)
        apply_into_json(json_payload, '$.customer', customer)
        apply_into_json(json_payload, '$.items', items)
        resp = orders_sock_shop.post('/orders', json=json_payload, headers={'accept': 'application/json'})
        resp.assert_status_code(201)
        resp.assert_jsonpath('$.address.city', expected_value='Glasgow')
        custId = jsonpath('$.customerId', resp)

        # GET http://orders.sock-shop/orders/search/customerId (endp 94)
        qstr = '?' + urlencode({'custId': custId, 'sort': 'date'})
        resp = orders_sock_shop.get('/orders/search/customerId' + qstr)
        resp.assert_status_code(200)
        resp.assert_jsonpath('$._embedded.customerOrders.[*].address.country', expected_value='United Kingdom')
        id_ = url_part('/2', jsonpath('$._embedded.customerOrders[*]._links.self.href', resp))

        # GET http://orders.sock-shop/orders/{id} (endp 199)
        resp = orders_sock_shop.get(f'/orders/{id_}')
        resp.assert_status_code(200)
        resp.assert_jsonpath('$.address.city', expected_value='elsewhere')

    @json_dataset('data/93/dataset_93.json')
    @clear_session({'spanId': 93})
    def test_093_get_orders_search_customerId(self, data_row):
        address, card, customer, items = data_row

        # POST http://orders.sock-shop/orders (endp 10)
        orders_sock_shop = get_http_client('http://orders.sock-shop', authenticate)
        with open('data/93/payload_for_endp_10.json', 'r') as json_payload_file:
            json_payload = json.load(json_payload_file)
        apply_into_json(json_payload, '$.address', address)
        apply_into_json(json_payload, '$.card', card)
        apply_into_json(json_payload, '$.customer', customer)
        apply_into_json(json_payload, '$.items', items)
        resp = orders_sock_shop.post('/orders', json=json_payload, headers={'accept': 'application/json'})
        resp.assert_status_code(201)
        resp.assert_jsonpath('$.address.city', expected_value='Glasgow')
        custId = jsonpath('$.customerId', resp)

        # GET http://orders.sock-shop/orders/search/customerId (endp 93)
        qstr = '?' + urlencode({'custId': custId, 'sort': 'date'})
        resp = orders_sock_shop.get('/orders/search/customerId' + qstr)
        resp.assert_status_code(200)

    @json_dataset('data/94/dataset_94.json')
    @clear_session({'spanId': 94})
    def test_094_get_orders_search_customerId(self, data_row):
        address, card, customer, items = data_row

        # POST http://orders.sock-shop/orders (endp 10)
        orders_sock_shop = get_http_client('http://orders.sock-shop', authenticate)
        with open('data/94/payload_for_endp_10.json', 'r') as json_payload_file:
            json_payload = json.load(json_payload_file)
        apply_into_json(json_payload, '$.address', address)
        apply_into_json(json_payload, '$.card', card)
        apply_into_json(json_payload, '$.customer', customer)
        apply_into_json(json_payload, '$.items', items)
        resp = orders_sock_shop.post('/orders', json=json_payload, headers={'accept': 'application/json'})
        resp.assert_status_code(201)
        resp.assert_jsonpath('$.address.city', expected_value='Glasgow')
        custId = jsonpath('$.customerId', resp)

        # GET http://orders.sock-shop/orders/search/customerId (endp 94)
        qstr = '?' + urlencode({'custId': custId, 'sort': 'date'})
        resp = orders_sock_shop.get('/orders/search/customerId' + qstr)
        resp.assert_status_code(200)
        resp.assert_jsonpath('$._embedded.customerOrders.[*].address.country', expected_value='United Kingdom')

    @json_dataset('data/156/dataset_156.json')
    @clear_session({'spanId': 156})
    def test_156_get_orders_search_customerId(self, data_row):
        address, card, card1, customer, items, items1 = data_row

        # POST http://orders.sock-shop/orders (endp 10)
        orders_sock_shop = get_http_client('http://orders.sock-shop', authenticate)
        with open('data/156/payload_for_endp_10.json', 'r') as json_payload_file:
            json_payload = json.load(json_payload_file)
        apply_into_json(json_payload, '$.address', address)
        apply_into_json(json_payload, '$.card', card)
        apply_into_json(json_payload, '$.customer', customer)
        apply_into_json(json_payload, '$.items', items)
        resp = orders_sock_shop.post('/orders', json=json_payload, headers={'accept': 'application/json'})
        resp.assert_status_code(201)
        resp.assert_jsonpath('$.address.city', expected_value='Glasgow')
        customerId = jsonpath('$.customerId', resp)

        # GET http://user.sock-shop/customers/{customerId} (endp 127)
        user_sock_shop = get_http_client('http://user.sock-shop', authenticate)
        resp = user_sock_shop.get(f'/customers/{customerId}', headers={'accept': 'application/hal+json'})
        resp.assert_status_code(200)
        resp.assert_jsonpath('$._links.self.href')
        customer1 = jsonpath('$._links.self.href', resp)

        # GET http://user.sock-shop/customers/{customerId}/addresses (endp 128)
        resp = user_sock_shop.get(f'/customers/{customerId}/addresses')
        resp.assert_status_code(200)
        resp.assert_jsonpath('$._embedded.address[*]._links.self.href')
        address1 = jsonpath('$._embedded.address[*]._links.address.href', resp)

        # POST http://orders.sock-shop/orders (endp 155)
        with open('data/156/payload_for_endp_155.json', 'r') as json_payload_file:
            json_payload = json.load(json_payload_file)
        apply_into_json(json_payload, '$.address', address1)
        apply_into_json(json_payload, '$.card', card1)
        apply_into_json(json_payload, '$.customer', customer1)
        apply_into_json(json_payload, '$.items', items1)
        resp = orders_sock_shop.post('/orders', json=json_payload, headers={'accept': 'application/json'})
        resp.assert_status_code(201)
        resp.assert_jsonpath('$.card.ccv')
        custId = jsonpath('$.customerId', resp)

        # GET http://orders.sock-shop/orders/search/customerId (endp 156)
        qstr = '?' + urlencode({'custId': custId, 'sort': 'date'})
        resp = orders_sock_shop.get('/orders/search/customerId' + qstr)
        resp.assert_status_code(200)
