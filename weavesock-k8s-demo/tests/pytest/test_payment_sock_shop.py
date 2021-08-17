from up9lib import *
from authentication import authenticate

# logging.basicConfig(level=logging.DEBUG)


@data_driven_tests
class Tests_payment_sock_shop(unittest.TestCase):

    @json_dataset('data/27/dataset_27.json')
    @clear_session({'spanId': 27})
    def test_027_post_paymentAuth(self, data_row):
        address, amount, card, city, customer, id_, items, lastName, longNum, number, username = data_row

        # POST http://orders.sock-shop/orders (endp 10)
        orders_sock_shop = get_http_client('http://orders.sock-shop', authenticate)
        with open('data/27/payload_for_endp_10.json', 'r') as json_payload_file:
            json_payload = json.load(json_payload_file)
        apply_into_json(json_payload, '$.address', address)
        apply_into_json(json_payload, '$.card', card)
        apply_into_json(json_payload, '$.customer', customer)
        apply_into_json(json_payload, '$.items', items)
        resp = orders_sock_shop.post('/orders', json=json_payload, headers={'accept': 'application/json'})
        resp.assert_status_code(201)
        resp.assert_jsonpath('$.address.city', expected_value='Glasgow')
        customerId = jsonpath('$.customerId', resp)

        # GET http://user.sock-shop/cards/{id} (endp 24)
        user_sock_shop = get_http_client('http://user.sock-shop', authenticate)
        resp = user_sock_shop.get(f'/cards/{id_}', headers={'accept': 'application/hal+json'})
        resp.assert_status_code(200)
        resp.assert_jsonpath('$.city', expected_value='Glasgow')
        ccv = jsonpath('$.ccv', resp)
        expires = jsonpath('$.expires', resp)
        id1 = jsonpath('$.id', resp)

        # GET http://user.sock-shop/customers/{customerId} (endp 3)
        resp = user_sock_shop.get(f'/customers/{customerId}', headers={'accept': 'application/hal+json'})
        resp.assert_status_code(200)
        resp.assert_jsonpath('$.city', expected_value='Glasgow')
        firstName = jsonpath('$.firstName', resp)

        # GET http://user.sock-shop/addresses/{id} (endp 23)
        resp = user_sock_shop.get(f'/addresses/{id1}', headers={'accept': 'application/hal+json'})
        resp.assert_status_code(200)
        resp.assert_jsonpath('$.country', expected_value='United Kingdom')
        country = jsonpath('$.country', resp)
        postcode = jsonpath('$.postcode', resp)
        street = jsonpath('$.street', resp)

        # POST http://payment.sock-shop/paymentAuth (endp 27)
        payment_sock_shop = get_http_client('http://payment.sock-shop', authenticate)
        with open('data/27/payload_for_endp_27.json', 'r') as json_payload_file:
            json_payload = json.load(json_payload_file)
        apply_into_json(json_payload, '$.address.city', city)
        apply_into_json(json_payload, '$.address.country', country)
        apply_into_json(json_payload, '$.address.number', number)
        apply_into_json(json_payload, '$.address.postcode', postcode)
        apply_into_json(json_payload, '$.address.street', street)
        apply_into_json(json_payload, '$.amount', amount)
        apply_into_json(json_payload, '$.card.ccv', ccv)
        apply_into_json(json_payload, '$.card.expires', expires)
        apply_into_json(json_payload, '$.card.longNum', longNum)
        apply_into_json(json_payload, '$.customer.firstName', firstName)
        apply_into_json(json_payload, '$.customer.lastName', lastName)
        apply_into_json(json_payload, '$.customer.username', username)
        resp = payment_sock_shop.post('/paymentAuth', json=json_payload, headers={'accept': 'application/json'})
        resp.assert_status_code(200)

    @json_dataset('data/143/dataset_143.json')
    @clear_session({'spanId': 143})
    def test_143_post_paymentAuth(self, data_row):
        address, amount, card, city, customer, id_, items, lastName, longNum, number, username = data_row

        # POST http://orders.sock-shop/orders (endp 10)
        orders_sock_shop = get_http_client('http://orders.sock-shop', authenticate)
        with open('data/143/payload_for_endp_10.json', 'r') as json_payload_file:
            json_payload = json.load(json_payload_file)
        apply_into_json(json_payload, '$.address', address)
        apply_into_json(json_payload, '$.card', card)
        apply_into_json(json_payload, '$.customer', customer)
        apply_into_json(json_payload, '$.items', items)
        resp = orders_sock_shop.post('/orders', json=json_payload, headers={'accept': 'application/json'})
        resp.assert_status_code(201)
        resp.assert_jsonpath('$.address.city', expected_value='Glasgow')
        customerId = jsonpath('$.customerId', resp)

        # GET http://user.sock-shop/cards/{id} (endp 24)
        user_sock_shop = get_http_client('http://user.sock-shop', authenticate)
        resp = user_sock_shop.get(f'/cards/{id_}', headers={'accept': 'application/hal+json'})
        resp.assert_status_code(200)
        resp.assert_jsonpath('$.city', expected_value='Glasgow')
        id1 = jsonpath('$.id', resp)

        # GET http://user.sock-shop/customers/{customerId} (endp 127)
        resp = user_sock_shop.get(f'/customers/{customerId}', headers={'accept': 'application/hal+json'})
        resp.assert_status_code(200)
        resp.assert_jsonpath('$._links.self.href')
        firstName = jsonpath('$.firstName', resp)

        # GET http://user.sock-shop/addresses/{id} (endp 131)
        resp = user_sock_shop.get(f'/addresses/{id1}', headers={'accept': 'application/hal+json'})
        resp.assert_status_code(200)
        resp.assert_jsonpath('$._links.self.href')
        country = jsonpath('$.country', resp)
        postcode = jsonpath('$.postcode', resp)
        street = jsonpath('$.street', resp)

        # GET http://user.sock-shop/cards/{id} (endp 132)
        resp = user_sock_shop.get(f'/cards/{id_}', headers={'accept': 'application/hal+json'})
        resp.assert_status_code(200)
        resp.assert_jsonpath('$._links.card.href')
        ccv = jsonpath('$.ccv', resp)
        expires = jsonpath('$.expires', resp)

        # POST http://payment.sock-shop/paymentAuth (endp 143)
        payment_sock_shop = get_http_client('http://payment.sock-shop', authenticate)
        with open('data/143/payload_for_endp_143.json', 'r') as json_payload_file:
            json_payload = json.load(json_payload_file)
        apply_into_json(json_payload, '$.address.city', city)
        apply_into_json(json_payload, '$.address.country', country)
        apply_into_json(json_payload, '$.address.number', number)
        apply_into_json(json_payload, '$.address.postcode', postcode)
        apply_into_json(json_payload, '$.address.street', street)
        apply_into_json(json_payload, '$.amount', amount)
        apply_into_json(json_payload, '$.card.ccv', ccv)
        apply_into_json(json_payload, '$.card.expires', expires)
        apply_into_json(json_payload, '$.card.longNum', longNum)
        apply_into_json(json_payload, '$.customer.firstName', firstName)
        apply_into_json(json_payload, '$.customer.lastName', lastName)
        apply_into_json(json_payload, '$.customer.username', username)
        resp = payment_sock_shop.post('/paymentAuth', json=json_payload, headers={'accept': 'application/json'})
        resp.assert_status_code(200)
        resp.assert_jsonpath('$.message')
