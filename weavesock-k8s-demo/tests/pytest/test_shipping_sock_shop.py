from up9lib import *
from authentication import authenticate

# logging.basicConfig(level=logging.DEBUG)


@data_driven_tests
class Tests_shipping_sock_shop(unittest.TestCase):

    @json_dataset('data/25/dataset_25.json')
    @clear_session({'spanId': 25})
    def test_025_post_shipping(self, data_row):
        id_, = data_row

        # GET http://user.sock-shop/cards/{id} (endp 24)
        user_sock_shop = get_http_client('http://user.sock-shop', authenticate)
        resp = user_sock_shop.get(f'/cards/{id_}', headers={'accept': 'application/hal+json'})
        resp.assert_status_code(200)
        resp.assert_jsonpath('$.city', expected_value='Glasgow')
        name = jsonpath('$.id', resp)

        # POST http://shipping.sock-shop/shipping (endp 25)
        shipping_sock_shop = get_http_client('http://shipping.sock-shop', authenticate)
        with open('data/25/payload_for_endp_25.json', 'r') as json_payload_file:
            json_payload = json.load(json_payload_file)
        apply_into_json(json_payload, '$.id', str(uuid.uuid4()))
        apply_into_json(json_payload, '$.name', name)
        resp = shipping_sock_shop.post('/shipping', json=json_payload, headers={'accept': 'application/json'})
        resp.assert_status_code(201)

    @json_dataset('data/144/dataset_144.json')
    @clear_session({'spanId': 144})
    def test_144_post_shipping(self, data_row):
        name, = data_row

        # POST http://shipping.sock-shop/shipping (endp 144)
        shipping_sock_shop = get_http_client('http://shipping.sock-shop', authenticate)
        with open('data/144/payload_for_endp_144.json', 'r') as json_payload_file:
            json_payload = json.load(json_payload_file)
        apply_into_json(json_payload, '$.id', str(uuid.uuid4()))
        apply_into_json(json_payload, '$.name', name)
        resp = shipping_sock_shop.post('/shipping', json=json_payload, headers={'accept': 'application/json'})
        resp.assert_status_code(201)
        resp.assert_jsonpath('$.id')
