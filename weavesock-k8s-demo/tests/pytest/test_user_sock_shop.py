from up9lib import *
from authentication import authenticate

# logging.basicConfig(level=logging.DEBUG)


@data_driven_tests
class Tests_user_sock_shop(unittest.TestCase):

    @json_dataset('data/191/dataset_191.json')
    @clear_session({'spanId': 191})
    def test_191_post_addresses(self, data_row):
        city, country, number, postcode, street, userID = data_row

        # POST http://user.sock-shop/addresses (endp 191)
        user_sock_shop = get_http_client('http://user.sock-shop', authenticate)
        with open('data/191/payload_for_endp_191.json', 'r') as json_payload_file:
            json_payload = json.load(json_payload_file)
        apply_into_json(json_payload, '$.city', city)
        apply_into_json(json_payload, '$.country', country)
        apply_into_json(json_payload, '$.number', number)
        apply_into_json(json_payload, '$.postcode', postcode)
        apply_into_json(json_payload, '$.street', street)
        apply_into_json(json_payload, '$.userID', userID)
        resp = user_sock_shop.post('/addresses', json=json_payload, headers={'accept': 'application/json'})
        resp.assert_status_code(200)

    @json_dataset('data/23/dataset_23.json')
    @clear_session({'spanId': 23})
    def test_023_get_addresses_id(self, data_row):
        id_, = data_row

        # GET http://user.sock-shop/cards/{id} (endp 24)
        user_sock_shop = get_http_client('http://user.sock-shop', authenticate)
        resp = user_sock_shop.get(f'/cards/{id_}', headers={'accept': 'application/hal+json'})
        resp.assert_status_code(200)
        resp.assert_jsonpath('$.city', expected_value='Glasgow')
        id1 = jsonpath('$.id', resp)

        # GET http://user.sock-shop/addresses/{id} (endp 23)
        resp = user_sock_shop.get(f'/addresses/{id1}', headers={'accept': 'application/hal+json'})
        resp.assert_status_code(200)
        resp.assert_jsonpath('$.country', expected_value='United Kingdom')

    @json_dataset('data/131/dataset_131.json')
    @clear_session({'spanId': 131})
    def test_131_get_addresses_id(self, data_row):
        id_, = data_row

        # GET http://user.sock-shop/cards/{id} (endp 24)
        user_sock_shop = get_http_client('http://user.sock-shop', authenticate)
        resp = user_sock_shop.get(f'/cards/{id_}', headers={'accept': 'application/hal+json'})
        resp.assert_status_code(200)
        resp.assert_jsonpath('$.city', expected_value='Glasgow')
        id1 = jsonpath('$.id', resp)

        # GET http://user.sock-shop/addresses/{id} (endp 131)
        resp = user_sock_shop.get(f'/addresses/{id1}', headers={'accept': 'application/hal+json'})
        resp.assert_status_code(200)
        resp.assert_jsonpath('$._links.self.href')

    @json_dataset('data/192/dataset_192.json')
    @clear_session({'spanId': 192})
    def test_192_post_cards(self, data_row):
        ccv, expires, longNum, userID = data_row

        # POST http://user.sock-shop/cards (endp 192)
        user_sock_shop = get_http_client('http://user.sock-shop', authenticate)
        with open('data/192/payload_for_endp_192.json', 'r') as json_payload_file:
            json_payload = json.load(json_payload_file)
        apply_into_json(json_payload, '$.ccv', ccv)
        apply_into_json(json_payload, '$.expires', expires)
        apply_into_json(json_payload, '$.longNum', longNum)
        apply_into_json(json_payload, '$.userID', userID)
        resp = user_sock_shop.post('/cards', json=json_payload, headers={'accept': 'application/json'})
        resp.assert_status_code(200)

    @json_dataset('data/24/dataset_24.json')
    @clear_session({'spanId': 24})
    def test_024_get_cards_id(self, data_row):
        id_, = data_row

        # GET http://user.sock-shop/cards/{id} (endp 24)
        user_sock_shop = get_http_client('http://user.sock-shop', authenticate)
        resp = user_sock_shop.get(f'/cards/{id_}', headers={'accept': 'application/hal+json'})
        resp.assert_status_code(200)
        resp.assert_jsonpath('$.city', expected_value='Glasgow')

    @json_dataset('data/132/dataset_132.json')
    @clear_session({'spanId': 132})
    def test_132_get_cards_id(self, data_row):
        id_, = data_row

        # GET http://user.sock-shop/cards/{id} (endp 132)
        user_sock_shop = get_http_client('http://user.sock-shop', authenticate)
        resp = user_sock_shop.get(f'/cards/{id_}', headers={'accept': 'application/hal+json'})
        resp.assert_status_code(200)
        resp.assert_jsonpath('$._links.card.href')

    @json_dataset('data/3/dataset_3.json')
    @clear_session({'spanId': 3})
    def test_003_get_customers_customerId(self, data_row):
        address, card, customer, items = data_row

        # POST http://orders.sock-shop/orders (endp 10)
        orders_sock_shop = get_http_client('http://orders.sock-shop', authenticate)
        with open('data/3/payload_for_endp_10.json', 'r') as json_payload_file:
            json_payload = json.load(json_payload_file)
        apply_into_json(json_payload, '$.address', address)
        apply_into_json(json_payload, '$.card', card)
        apply_into_json(json_payload, '$.customer', customer)
        apply_into_json(json_payload, '$.items', items)
        resp = orders_sock_shop.post('/orders', json=json_payload, headers={'accept': 'application/json'})
        resp.assert_status_code(201)
        resp.assert_jsonpath('$.address.city', expected_value='Glasgow')
        customerId = jsonpath('$.customerId', resp)

        # GET http://user.sock-shop/customers/{customerId} (endp 3)
        user_sock_shop = get_http_client('http://user.sock-shop', authenticate)
        resp = user_sock_shop.get(f'/customers/{customerId}', headers={'accept': 'application/hal+json'})
        resp.assert_status_code(200)
        resp.assert_jsonpath('$.city', expected_value='Glasgow')

    @json_dataset('data/127/dataset_127.json')
    @clear_session({'spanId': 127})
    def test_127_get_customers_customerId(self, data_row):
        address, card, customer, items = data_row

        # POST http://orders.sock-shop/orders (endp 10)
        orders_sock_shop = get_http_client('http://orders.sock-shop', authenticate)
        with open('data/127/payload_for_endp_10.json', 'r') as json_payload_file:
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

    @json_dataset('data/4/dataset_4.json')
    @clear_session({'spanId': 4})
    def test_004_get_customers_customerId_addresses(self, data_row):
        address, card, customer, items = data_row

        # POST http://orders.sock-shop/orders (endp 10)
        orders_sock_shop = get_http_client('http://orders.sock-shop', authenticate)
        with open('data/4/payload_for_endp_10.json', 'r') as json_payload_file:
            json_payload = json.load(json_payload_file)
        apply_into_json(json_payload, '$.address', address)
        apply_into_json(json_payload, '$.card', card)
        apply_into_json(json_payload, '$.customer', customer)
        apply_into_json(json_payload, '$.items', items)
        resp = orders_sock_shop.post('/orders', json=json_payload, headers={'accept': 'application/json'})
        resp.assert_status_code(201)
        resp.assert_jsonpath('$.address.city', expected_value='Glasgow')
        customerId = jsonpath('$.customerId', resp)

        # GET http://user.sock-shop/customers/{customerId}/addresses (endp 4)
        user_sock_shop = get_http_client('http://user.sock-shop', authenticate)
        resp = user_sock_shop.get(f'/customers/{customerId}/addresses')
        resp.assert_status_code(200)
        resp.assert_jsonpath('$._embedded.address.[*].country', expected_value='United Kingdom')

    @json_dataset('data/128/dataset_128.json')
    @clear_session({'spanId': 128})
    def test_128_get_customers_customerId_addresses(self, data_row):
        address, card, customer, items = data_row

        # POST http://orders.sock-shop/orders (endp 10)
        orders_sock_shop = get_http_client('http://orders.sock-shop', authenticate)
        with open('data/128/payload_for_endp_10.json', 'r') as json_payload_file:
            json_payload = json.load(json_payload_file)
        apply_into_json(json_payload, '$.address', address)
        apply_into_json(json_payload, '$.card', card)
        apply_into_json(json_payload, '$.customer', customer)
        apply_into_json(json_payload, '$.items', items)
        resp = orders_sock_shop.post('/orders', json=json_payload, headers={'accept': 'application/json'})
        resp.assert_status_code(201)
        resp.assert_jsonpath('$.address.city', expected_value='Glasgow')
        customerId = jsonpath('$.customerId', resp)

        # GET http://user.sock-shop/customers/{customerId}/addresses (endp 128)
        user_sock_shop = get_http_client('http://user.sock-shop', authenticate)
        resp = user_sock_shop.get(f'/customers/{customerId}/addresses')
        resp.assert_status_code(200)
        resp.assert_jsonpath('$._embedded.address[*]._links.self.href')

    @json_dataset('data/5/dataset_5.json')
    @clear_session({'spanId': 5})
    def test_005_get_customers_customerId_cards(self, data_row):
        address, card, customer, items = data_row

        # POST http://orders.sock-shop/orders (endp 10)
        orders_sock_shop = get_http_client('http://orders.sock-shop', authenticate)
        with open('data/5/payload_for_endp_10.json', 'r') as json_payload_file:
            json_payload = json.load(json_payload_file)
        apply_into_json(json_payload, '$.address', address)
        apply_into_json(json_payload, '$.card', card)
        apply_into_json(json_payload, '$.customer', customer)
        apply_into_json(json_payload, '$.items', items)
        resp = orders_sock_shop.post('/orders', json=json_payload, headers={'accept': 'application/json'})
        resp.assert_status_code(201)
        resp.assert_jsonpath('$.address.city', expected_value='Glasgow')
        customerId = jsonpath('$.customerId', resp)

        # GET http://user.sock-shop/customers/{customerId}/cards (endp 5)
        user_sock_shop = get_http_client('http://user.sock-shop', authenticate)
        resp = user_sock_shop.get(f'/customers/{customerId}/cards')
        resp.assert_status_code(200)

    @json_dataset('data/129/dataset_129.json')
    @clear_session({'spanId': 129})
    def test_129_get_customers_customerId_cards(self, data_row):
        address, card, customer, items = data_row

        # POST http://orders.sock-shop/orders (endp 10)
        orders_sock_shop = get_http_client('http://orders.sock-shop', authenticate)
        with open('data/129/payload_for_endp_10.json', 'r') as json_payload_file:
            json_payload = json.load(json_payload_file)
        apply_into_json(json_payload, '$.address', address)
        apply_into_json(json_payload, '$.card', card)
        apply_into_json(json_payload, '$.customer', customer)
        apply_into_json(json_payload, '$.items', items)
        resp = orders_sock_shop.post('/orders', json=json_payload, headers={'accept': 'application/json'})
        resp.assert_status_code(201)
        resp.assert_jsonpath('$.address.city', expected_value='Glasgow')
        customerId = jsonpath('$.customerId', resp)

        # GET http://user.sock-shop/customers/{customerId}/cards (endp 129)
        user_sock_shop = get_http_client('http://user.sock-shop', authenticate)
        resp = user_sock_shop.get(f'/customers/{customerId}/cards')
        resp.assert_status_code(200)
        resp.assert_jsonpath('$._embedded.card[*]._links.card.href')

    # authentication-related test
    @clear_session({'spanId': 6})
    def test_006_get_login(self):
        # GET http://user.sock-shop/login (endp 6)
        user_sock_shop = get_http_client('http://user.sock-shop', dummy_auth)
        resp = user_sock_shop.get('/login')
        resp.assert_status_code(200)

    # authentication-related test
    @clear_session({'spanId': 130})
    def test_130_get_login(self):
        # GET http://user.sock-shop/login (endp 130)
        user_sock_shop = get_http_client('http://user.sock-shop', dummy_auth)
        resp = user_sock_shop.get('/login')
        resp.assert_status_code(200)
        resp.assert_jsonpath('$.user._links.self.href')

    # authentication-related test
    @json_dataset('data/197/dataset_197.json')
    @clear_session({'spanId': 197})
    def test_197_post_register(self, data_row):
        email_, firstName, lastName, password, username = data_row

        # POST http://user.sock-shop/register (endp 197)
        user_sock_shop = get_http_client('http://user.sock-shop', dummy_auth)
        with open('data/197/payload_for_endp_197.json', 'r') as json_payload_file:
            json_payload = json.load(json_payload_file)
        apply_into_json(json_payload, '$.email', email_)
        apply_into_json(json_payload, '$.firstName', firstName)
        apply_into_json(json_payload, '$.lastName', lastName)
        apply_into_json(json_payload, '$.password', password)
        apply_into_json(json_payload, '$.username', username)
        resp = user_sock_shop.post('/register', json=json_payload, headers={'accept': 'application/json'})
        resp.assert_status_code(200)
