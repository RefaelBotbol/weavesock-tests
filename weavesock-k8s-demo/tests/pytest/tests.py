from up9lib import *
from authentication import authenticate

# logging.basicConfig(level=logging.DEBUG)


@data_driven_tests
class Tests_carts_sock_shop(unittest.TestCase):

    @json_dataset('data/dataset_139.json')
    @clear_session({'spanId': 139})
    def test_139_delete_carts_customerId(self, data_row):
        address, card, customer, items = data_row

        # POST http://orders.sock-shop/orders (endp 10)
        orders_sock_shop = get_http_client('http://orders.sock-shop', authenticate)
        with open('data/payload_for_endp_10.json', 'r') as json_payload_file:
            json_payload = json.load(json_payload_file)
        apply_into_json(json_payload, '$.address', address)
        apply_into_json(json_payload, '$.card', card)
        apply_into_json(json_payload, '$.customer', customer)
        apply_into_json(json_payload, '$.items', items)
        resp = orders_sock_shop.post('/orders', json=json_payload, headers=dict([('accept', 'application/json')]))
        resp.assert_status_code(201)
        resp.assert_jsonpath('$.address.city', expected_value='Glasgow')
        customerId = jsonpath('$.customerId', resp)

        # DELETE http://carts.sock-shop/carts/{customerId} (endp 139)
        carts_sock_shop = get_http_client('http://carts.sock-shop', authenticate)
        resp = carts_sock_shop.delete(f'/carts/{customerId}')
        resp.assert_status_code(202)

    @json_dataset('data/dataset_8.json')
    @clear_session({'spanId': 8})
    def test_008_post_carts_customerId_items(self, data_row):
        address, card, customer, items = data_row

        # POST http://orders.sock-shop/orders (endp 10)
        orders_sock_shop = get_http_client('http://orders.sock-shop', authenticate)
        with open('data/payload_for_endp_10.json', 'r') as json_payload_file:
            json_payload = json.load(json_payload_file)
        apply_into_json(json_payload, '$.address', address)
        apply_into_json(json_payload, '$.card', card)
        apply_into_json(json_payload, '$.customer', customer)
        apply_into_json(json_payload, '$.items', items)
        resp = orders_sock_shop.post('/orders', json=json_payload, headers=dict([('accept', 'application/json')]))
        resp.assert_status_code(201)
        resp.assert_jsonpath('$.address.city', expected_value='Glasgow')
        itemId = jsonpath('$.items[*].itemId', resp)
        unitPrice = jsonpath('$.items[*].unitPrice', resp)
        customerId = jsonpath('$.customerId', resp)

        # POST http://carts.sock-shop/carts/{customerId}/items (endp 8)
        carts_sock_shop = get_http_client('http://carts.sock-shop', authenticate)
        with open('data/payload_for_endp_8.json', 'r') as json_payload_file:
            json_payload = json.load(json_payload_file)
        apply_into_json(json_payload, '$.itemId', itemId)
        apply_into_json(json_payload, '$.unitPrice', unitPrice)
        resp = carts_sock_shop.post(f'/carts/{customerId}/items', json=json_payload, headers=dict([('accept', 'application/json')]))
        resp.assert_status_code(201)

    @json_dataset('data/dataset_26.json')
    @clear_session({'spanId': 26})
    def test_026_get_carts_customerId_items(self, data_row):
        address, card, customer, items = data_row

        # POST http://orders.sock-shop/orders (endp 10)
        orders_sock_shop = get_http_client('http://orders.sock-shop', authenticate)
        with open('data/payload_for_endp_10.json', 'r') as json_payload_file:
            json_payload = json.load(json_payload_file)
        apply_into_json(json_payload, '$.address', address)
        apply_into_json(json_payload, '$.card', card)
        apply_into_json(json_payload, '$.customer', customer)
        apply_into_json(json_payload, '$.items', items)
        resp = orders_sock_shop.post('/orders', json=json_payload, headers=dict([('accept', 'application/json')]))
        resp.assert_status_code(201)
        resp.assert_jsonpath('$.address.city', expected_value='Glasgow')
        customerId = jsonpath('$.customerId', resp)

        # GET http://carts.sock-shop/carts/{customerId}/items (endp 26)
        carts_sock_shop = get_http_client('http://carts.sock-shop', authenticate)
        resp = carts_sock_shop.get(f'/carts/{customerId}/items', headers=dict([('accept', 'application/json')]))
        resp.assert_status_code(200)

    @json_dataset('data/dataset_140.json')
    @clear_session({'spanId': 140})
    def test_140_post_carts_customerId_items(self, data_row):
        address, card, customer, items = data_row

        # POST http://orders.sock-shop/orders (endp 10)
        orders_sock_shop = get_http_client('http://orders.sock-shop', authenticate)
        with open('data/payload_for_endp_10.json', 'r') as json_payload_file:
            json_payload = json.load(json_payload_file)
        apply_into_json(json_payload, '$.address', address)
        apply_into_json(json_payload, '$.card', card)
        apply_into_json(json_payload, '$.customer', customer)
        apply_into_json(json_payload, '$.items', items)
        resp = orders_sock_shop.post('/orders', json=json_payload, headers=dict([('accept', 'application/json')]))
        resp.assert_status_code(201)
        resp.assert_jsonpath('$.address.city', expected_value='Glasgow')
        customerId = jsonpath('$.customerId', resp)

        # GET http://carts.sock-shop/carts/{customerId}/items (endp 142)
        carts_sock_shop = get_http_client('http://carts.sock-shop', authenticate)
        resp = carts_sock_shop.get(f'/carts/{customerId}/items', headers=dict([('accept', 'application/json')]))
        resp.assert_status_code(200)
        itemId = jsonpath('$[*].itemId', resp)
        unitPrice = jsonpath('$[*].unitPrice', resp)

        # POST http://carts.sock-shop/carts/{customerId}/items (endp 140)
        with open('data/payload_for_endp_140.json', 'r') as json_payload_file:
            json_payload = json.load(json_payload_file)
        apply_into_json(json_payload, '$.itemId', itemId)
        apply_into_json(json_payload, '$.unitPrice', unitPrice)
        resp = carts_sock_shop.post(f'/carts/{customerId}/items', json=json_payload, headers=dict([('accept', 'application/json')]))
        resp.assert_status_code(201)

    @json_dataset('data/dataset_9.json')
    @clear_session({'spanId': 9})
    def test_009_get_carts_customerId_merge(self, data_row):
        address, card, customer, items, sessionId = data_row

        # POST http://orders.sock-shop/orders (endp 10)
        orders_sock_shop = get_http_client('http://orders.sock-shop', authenticate)
        with open('data/payload_for_endp_10.json', 'r') as json_payload_file:
            json_payload = json.load(json_payload_file)
        apply_into_json(json_payload, '$.address', address)
        apply_into_json(json_payload, '$.card', card)
        apply_into_json(json_payload, '$.customer', customer)
        apply_into_json(json_payload, '$.items', items)
        resp = orders_sock_shop.post('/orders', json=json_payload, headers=dict([('accept', 'application/json')]))
        resp.assert_status_code(201)
        resp.assert_jsonpath('$.address.city', expected_value='Glasgow')
        customerId = jsonpath('$.customerId', resp)

        # GET http://carts.sock-shop/carts/{customerId}/merge (endp 9)
        carts_sock_shop = get_http_client('http://carts.sock-shop', authenticate)
        qstr = '?' + urlencode([('sessionId', sessionId)])
        resp = carts_sock_shop.get(f'/carts/{customerId}/merge' + qstr)
        resp.assert_status_code(202)

    @json_dataset('data/dataset_141.json')
    @clear_session({'spanId': 141})
    def test_141_get_carts_customerId_merge(self, data_row):
        address, card, customer, items, sessionId = data_row

        # POST http://orders.sock-shop/orders (endp 10)
        orders_sock_shop = get_http_client('http://orders.sock-shop', authenticate)
        with open('data/payload_for_endp_10.json', 'r') as json_payload_file:
            json_payload = json.load(json_payload_file)
        apply_into_json(json_payload, '$.address', address)
        apply_into_json(json_payload, '$.card', card)
        apply_into_json(json_payload, '$.customer', customer)
        apply_into_json(json_payload, '$.items', items)
        resp = orders_sock_shop.post('/orders', json=json_payload, headers=dict([('accept', 'application/json')]))
        resp.assert_status_code(201)
        resp.assert_jsonpath('$.address.city', expected_value='Glasgow')
        customerId = jsonpath('$.customerId', resp)

        # GET http://carts.sock-shop/carts/{customerId}/merge (endp 141)
        carts_sock_shop = get_http_client('http://carts.sock-shop', authenticate)
        qstr = '?' + urlencode([('sessionId', sessionId)])
        resp = carts_sock_shop.get(f'/carts/{customerId}/merge' + qstr)
        resp.assert_status_code(202)


@data_driven_tests
class Tests_catalogue_sock_shop(unittest.TestCase):

    @json_dataset('data/dataset_137.json')
    @clear_session({'spanId': 137})
    def test_137_get_catalogue(self, data_row):
        page, size, tags = data_row

        # GET http://catalogue.sock-shop/catalogue (endp 137)
        catalogue_sock_shop = get_http_client('http://catalogue.sock-shop', authenticate)
        qstr = '?' + urlencode([('page', page), ('size', size), ('sort', 'id'), ('tags', tags)])
        resp = catalogue_sock_shop.get('/catalogue' + qstr)
        resp.assert_status_code(200)

    @json_dataset('data/dataset_2.json')
    @clear_session({'spanId': 2})
    def test_002_get_catalogue_id(self, data_row):
        size, tags = data_row

        # GET http://catalogue.sock-shop/catalogue (endp 1)
        catalogue_sock_shop = get_http_client('http://catalogue.sock-shop', authenticate)
        qstr = '?' + urlencode([('page', '1'), ('size', size), ('sort', 'id'), ('tags', tags)])
        resp = catalogue_sock_shop.get('/catalogue' + qstr)
        resp.assert_status_code(200)
        id_ = jsonpath('$[*].id', resp)

        # GET http://catalogue.sock-shop/catalogue/{id} (endp 2)
        resp = catalogue_sock_shop.get(f'/catalogue/{id_}')
        resp.assert_status_code(200)

    @json_dataset('data/dataset_135.json')
    @clear_session({'spanId': 135})
    def test_135_get_catalogue_id(self, data_row):
        size, tags = data_row

        # GET http://catalogue.sock-shop/catalogue (endp 1)
        catalogue_sock_shop = get_http_client('http://catalogue.sock-shop', authenticate)
        qstr = '?' + urlencode([('page', '1'), ('size', size), ('sort', 'id'), ('tags', tags)])
        resp = catalogue_sock_shop.get('/catalogue' + qstr)
        resp.assert_status_code(200)
        id_ = jsonpath('$[*].id', resp)

        # GET http://catalogue.sock-shop/catalogue/{id} (endp 135)
        resp = catalogue_sock_shop.get(f'/catalogue/{id_}')
        resp.assert_status_code(200)

    @clear_session({'spanId': 85})
    def test_085_get_catalogue_size(self):
        # GET http://catalogue.sock-shop/tags (endp 87)
        catalogue_sock_shop = get_http_client('http://catalogue.sock-shop', authenticate)
        resp = catalogue_sock_shop.get('/tags')
        resp.assert_status_code(200)
        tags = jsonpath('$.tags[*]', resp)

        # GET http://catalogue.sock-shop/catalogue/size (endp 85)
        qstr = '?' + urlencode([('tags', tags)])
        resp = catalogue_sock_shop.get('/catalogue/size' + qstr)
        resp.assert_status_code(200)

    @clear_session({'spanId': 136})
    def test_136_get_catalogue_size(self):
        # GET http://catalogue.sock-shop/tags (endp 138)
        catalogue_sock_shop = get_http_client('http://catalogue.sock-shop', authenticate)
        resp = catalogue_sock_shop.get('/tags')
        resp.assert_status_code(200)
        tags = jsonpath('$.tags[*]', resp)

        # GET http://catalogue.sock-shop/catalogue/size (endp 136)
        qstr = '?' + urlencode([('tags', tags)])
        resp = catalogue_sock_shop.get('/catalogue/size' + qstr)
        resp.assert_status_code(200)


@data_driven_tests
class Tests_front_end_sock_shop(unittest.TestCase):

    @json_dataset('data/dataset_11.json')
    @clear_session({'spanId': 11})
    def test_011_get_(self, data_row):
        _meta_http_equiv, _script_document_cookie, class_classLoader_URLs_0_, content, expression = data_row

        # GET http://front-end.sock-shop/ (endp 11)
        front_end_sock_shop = get_http_client('http://front-end.sock-shop', authenticate)
        qstr = '?' + urlencode([('"</script>', ''), ('"><script>alert(\'struts_sa_surl_xss.nasl-1603621900\')</script>', ''), ('"><script>alert(\'struts_sa_surl_xss.nasl-1605657683\')</script>', ''), ('"><script>alert(\'struts_sa_surl_xss.nasl-1605658393\')</script>', ''), ("('\\u0023_memberAccess[\\'allowStaticMethodAccess\\']')(meh)", 'true'), ('(aaa)((\'\\u0023context[\\\'xwork.MethodAccessor.denyMethodExecution\\\']\\u003d\\u0023foo\')(\\u0023foo\\u003dnew java.lang.Boolean("false")))', ''), ("(asdf)(('\\u0023thread.sleep(5000)')(\\u0023thread\\u003d@java.lang.Thread@currentThread()))", '1'), ('<meta http-equiv', _meta_http_equiv), ('<script>document.cookie', _script_document_cookie), ('XDEBUG_SESSION_START', 'phpstorm'), ('a', 'fetch'), ('class.classLoader.URLs[0]', class_classLoader_URLs_0_), ('content', content), ('debug', 'command'), ('expression', expression), ('ho {COMPLETE_VERSION}', '')])
        resp = front_end_sock_shop.get('/' + qstr)
        resp.assert_status_code(200)
        resp.assert_cssselect('div#basket div.box form h1', expected_value='Shopping cart')

    @clear_session({'spanId': 28})
    def test_028_get_(self):
        # GET http://front-end.sock-shop/ (endp 28)
        front_end_sock_shop = get_http_client('http://front-end.sock-shop', authenticate)
        resp = front_end_sock_shop.get('/')
        resp.assert_status_code(200)

    @clear_session({'spanId': 67})
    def test_067_head_(self):
        # HEAD http://front-end.sock-shop/ (endp 67)
        front_end_sock_shop = get_http_client('http://front-end.sock-shop', authenticate)
        resp = front_end_sock_shop.head('/')
        resp.assert_status_code(200)

    @json_dataset('data/dataset_133.json')
    @clear_session({'spanId': 133})
    def test_133_get_(self, data_row):
        content, s, vars_0_ = data_row

        # GET http://front-end.sock-shop/ (endp 133)
        front_end_sock_shop = get_http_client('http://front-end.sock-shop', authenticate)
        qstr = '?' + urlencode([('XDEBUG_SESSION_START', 'phpstorm'), ('a', 'fetch'), ('content', content), ('data', '1'), ('filter', 'phpinfo'), ('function', 'call_user_func_array'), ('s', s), ('vars[0]', vars_0_)])
        resp = front_end_sock_shop.get('/' + qstr)
        resp.assert_status_code(200)
        resp.assert_cssselect('div#hot div.box div.container div h2', expected_value='Hot this week')

    @clear_session({'spanId': 134})
    def test_134_head_(self):
        # HEAD http://front-end.sock-shop/ (endp 134)
        front_end_sock_shop = get_http_client('http://front-end.sock-shop', authenticate)
        resp = front_end_sock_shop.head('/')
        resp.assert_status_code(200)

    @json_dataset('data/dataset_154.json')
    @clear_session({'spanId': 154})
    def test_154_get_(self, data_row):
        content, = data_row

        # GET http://front-end.sock-shop/ (endp 154)
        front_end_sock_shop = get_http_client('http://front-end.sock-shop', authenticate)
        qstr = '?' + urlencode([('a', 'fetch'), ('content', content)])
        resp = front_end_sock_shop.get('/' + qstr)
        resp.assert_status_code(200)
        resp.assert_cssselect('div#hot div.box div.container div h2', expected_value='Hot this week')

    @clear_session({'spanId': 159})
    def test_159_get_(self):
        # GET http://front-end.sock-shop/ (endp 159)
        front_end_sock_shop = get_http_client('http://front-end.sock-shop', authenticate)
        resp = front_end_sock_shop.get('/')
        resp.assert_status_code(200)
        resp.assert_cssselect('div#hot div.box div.container div h2', expected_value='Hot this week')

    @clear_session({'spanId': 201})
    def test_201_get_(self):
        # GET http://front-end.sock-shop/ (endp 201)
        front_end_sock_shop = get_http_client('http://front-end.sock-shop', authenticate)
        resp = front_end_sock_shop.get('/')
        resp.assert_status_code(200)
        resp.assert_cssselect('div#hot div.box div.container div h2', expected_value='Hot this week')

    @clear_session({'spanId': 203})
    def test_203_get_(self):
        # GET http://front-end.sock-shop/ (endp 203)
        front_end_sock_shop = get_http_client('http://front-end.sock-shop', authenticate)
        resp = front_end_sock_shop.get('/')
        resp.assert_status_code(200)
        resp.assert_cssselect('div#hot div.box div.container div h2', expected_value='Hot this week')

    @clear_session({'spanId': 204})
    def test_204_get_(self):
        # GET http://front-end.sock-shop/ (endp 204)
        front_end_sock_shop = get_http_client('http://front-end.sock-shop', authenticate)
        resp = front_end_sock_shop.get('/')
        resp.assert_status_code(200)
        resp.assert_cssselect('div#hot div.box div.container div h2', expected_value='Hot this week')

    @clear_session({'spanId': 205})
    def test_205_get_(self):
        # GET http://front-end.sock-shop/ (endp 205)
        front_end_sock_shop = get_http_client('http://front-end.sock-shop', authenticate)
        resp = front_end_sock_shop.get('/')
        resp.assert_status_code(200)
        resp.assert_cssselect('div#hot div.box div.container div h2', expected_value='Hot this week')

    @clear_session({'spanId': 206})
    def test_206_get_(self):
        # GET http://front-end.sock-shop/ (endp 206)
        front_end_sock_shop = get_http_client('http://front-end.sock-shop', authenticate)
        resp = front_end_sock_shop.get('/')
        resp.assert_status_code(200)
        resp.assert_cssselect('div#hot div.box div.container div h2', expected_value='Hot this week')

    @clear_session({'spanId': 213})
    def test_213_get_(self):
        # GET http://front-end.sock-shop/ (endp 213)
        front_end_sock_shop = get_http_client('http://front-end.sock-shop', authenticate)
        resp = front_end_sock_shop.get('/')
        resp.assert_status_code(200)
        resp.assert_cssselect('div#hot div.box div.container div h2', expected_value='Hot this week')

    @json_dataset('data/dataset_55.json')
    @clear_session({'spanId': 55})
    def test_055_get_param(self, data_row):
        param, = data_row

        # GET http://front-end.sock-shop/{param} (endp 55)
        front_end_sock_shop = get_http_client('http://front-end.sock-shop', authenticate)
        resp = front_end_sock_shop.get(f'/{param}', headers=dict([('x-requested-with', 'XMLHttpRequest')]))
        resp.assert_status_code(200)
        resp.assert_cssselect('div#top div.container div.offer a.btn.btn-success.btn-sm', expected_value='Offer of the day')

    @json_dataset('data/dataset_151.json')
    @clear_session({'spanId': 151})
    def test_151_get_param(self, data_row):
        param, = data_row

        # GET http://front-end.sock-shop/{param} (endp 151)
        front_end_sock_shop = get_http_client('http://front-end.sock-shop', authenticate)
        resp = front_end_sock_shop.get(f'/{param}', headers=dict([('x-requested-with', 'XMLHttpRequest')]))
        resp.assert_status_code(200)

    @json_dataset('data/dataset_208.json')
    @clear_session({'spanId': 208})
    def test_208_get_param____index_html(self, data_row):
        param, = data_row

        # GET http://front-end.sock-shop/{param}/../index.html (endp 208)
        front_end_sock_shop = get_http_client('http://front-end.sock-shop', authenticate)
        resp = front_end_sock_shop.get(f'/{param}/../index.html')
        resp.assert_status_code(200)
        resp.assert_cssselect('div#hot div.box div.container div h2', expected_value='Hot this week')

    @json_dataset('data/dataset_126.json')
    @clear_session({'spanId': 126})
    def test_126_post_Licenses_licenseId(self, data_row):
        licenseId, = data_row

        # POST http://front-end.sock-shop/Licenses/{licenseId} (endp 126)
        front_end_sock_shop = get_http_client('http://front-end.sock-shop', authenticate)
        resp = front_end_sock_shop.post(f'/Licenses/{licenseId}', data=[('chk', 'Test')])
        resp.assert_status_code(100)

    @clear_session({'spanId': 123})
    def test_123_get_SiteScope_(self):
        # GET http://front-end.sock-shop/SiteScope/ (endp 123)
        front_end_sock_shop = get_http_client('http://front-end.sock-shop', authenticate)
        resp = front_end_sock_shop.get('/SiteScope/')
        resp.assert_status_code(200)
        resp.assert_cssselect('div#hot div.box div.container div h2', expected_value='Hot this week')

    @clear_session({'spanId': 68})
    def test_068_get_address(self):
        # GET http://front-end.sock-shop/address (endp 68)
        front_end_sock_shop = get_http_client('http://front-end.sock-shop', authenticate)
        resp = front_end_sock_shop.get('/address', headers=dict([('x-requested-with', 'XMLHttpRequest')]))
        resp.assert_status_code(200)
        resp.assert_jsonpath('$.city', expected_value='Glasgow')

    @clear_session({'spanId': 168})
    def test_168_get_address(self):
        # GET http://front-end.sock-shop/address (endp 168)
        front_end_sock_shop = get_http_client('http://front-end.sock-shop', authenticate)
        resp = front_end_sock_shop.get('/address', headers=dict([('x-requested-with', 'XMLHttpRequest')]))
        resp.assert_status_code(200)

    @json_dataset('data/dataset_169.json')
    @clear_session({'spanId': 169})
    def test_169_post_addresses(self, data_row):
        number, postcode = data_row

        # POST http://front-end.sock-shop/addresses (endp 169)
        front_end_sock_shop = get_http_client('http://front-end.sock-shop', authenticate)
        with open('data/payload_for_endp_169.json', 'r') as json_payload_file:
            json_payload = json.load(json_payload_file)
        apply_into_json(json_payload, '$.number', number)
        apply_into_json(json_payload, '$.postcode', postcode)
        resp = front_end_sock_shop.post('/addresses', json=json_payload, headers=dict([('x-requested-with', 'XMLHttpRequest')]))
        resp.assert_status_code(200)

    @clear_session({'spanId': 13})
    def test_013_get_basket_html(self):
        # GET http://front-end.sock-shop/basket.html (endp 13)
        front_end_sock_shop = get_http_client('http://front-end.sock-shop', authenticate)
        resp = front_end_sock_shop.get('/basket.html')
        resp.assert_status_code(201)

    @clear_session({'spanId': 14})
    def test_014_get_basket_html(self):
        # GET http://front-end.sock-shop/basket.html (endp 14)
        front_end_sock_shop = get_http_client('http://front-end.sock-shop', authenticate)
        resp = front_end_sock_shop.get('/basket.html')
        resp.assert_status_code(200)
        resp.assert_cssselect('div#basket div.box form h1', expected_value='Shopping cart')

    @clear_session({'spanId': 170})
    def test_170_get_basket_html(self):
        # GET http://front-end.sock-shop/basket.html (endp 170)
        front_end_sock_shop = get_http_client('http://front-end.sock-shop', authenticate)
        resp = front_end_sock_shop.get('/basket.html')
        resp.assert_status_code(200)
        resp.assert_cssselect('div#basket div.box form h1', expected_value='Shopping cart')

    @clear_session({'spanId': 103})
    def test_103_get_c(self):
        # GET http://front-end.sock-shop/c (endp 103)
        front_end_sock_shop = get_http_client('http://front-end.sock-shop', authenticate)
        resp = front_end_sock_shop.get('/c')
        resp.assert_status_code(200)
        resp.assert_cssselect('div#hot div.box div.container div h2', expected_value='Hot this week')

    @clear_session({'spanId': 70})
    def test_070_get_card(self):
        # GET http://front-end.sock-shop/card (endp 70)
        front_end_sock_shop = get_http_client('http://front-end.sock-shop', authenticate)
        resp = front_end_sock_shop.get('/card', headers=dict([('x-requested-with', 'XMLHttpRequest')]))
        resp.assert_status_code(200)

    @clear_session({'spanId': 171})
    def test_171_get_card(self):
        # GET http://front-end.sock-shop/card (endp 171)
        front_end_sock_shop = get_http_client('http://front-end.sock-shop', authenticate)
        resp = front_end_sock_shop.get('/card', headers=dict([('x-requested-with', 'XMLHttpRequest')]))
        resp.assert_status_code(200)

    @json_dataset('data/dataset_172.json')
    @clear_session({'spanId': 172})
    def test_172_post_cards(self, data_row):
        ccv, expires, longNum = data_row

        # POST http://front-end.sock-shop/cards (endp 172)
        front_end_sock_shop = get_http_client('http://front-end.sock-shop', authenticate)
        with open('data/payload_for_endp_172.json', 'r') as json_payload_file:
            json_payload = json.load(json_payload_file)
        apply_into_json(json_payload, '$.ccv', ccv)
        apply_into_json(json_payload, '$.expires', expires)
        apply_into_json(json_payload, '$.longNum', longNum)
        resp = front_end_sock_shop.post('/cards', json=json_payload, headers=dict([('x-requested-with', 'XMLHttpRequest')]))
        resp.assert_status_code(200)

    @clear_session({'spanId': 16})
    def test_016_post_cart(self):
        # POST http://front-end.sock-shop/orders (endp 21)
        front_end_sock_shop = get_http_client('http://front-end.sock-shop', authenticate)
        resp = front_end_sock_shop.post('/orders', headers=dict([('x-requested-with', 'XMLHttpRequest')]))
        resp.assert_status_code(201)
        resp.assert_jsonpath('$.address.city', expected_value='Glasgow')
        id_ = jsonpath('$.items[*].itemId', resp)

        # POST http://front-end.sock-shop/cart (endp 16)
        with open('data/payload_for_endp_16.json', 'r') as json_payload_file:
            json_payload = json.load(json_payload_file)
        apply_into_json(json_payload, '$.id', id_)
        resp = front_end_sock_shop.post('/cart', json=json_payload, headers=dict([('x-requested-with', 'XMLHttpRequest')]))
        resp.assert_status_code(201)

    @json_dataset('data/dataset_33.json')
    @clear_session({'spanId': 33})
    def test_033_post_cart(self, data_row):
        size, tags = data_row

        # GET http://front-end.sock-shop/catalogue (endp 17)
        front_end_sock_shop = get_http_client('http://front-end.sock-shop', authenticate)
        qstr = '?' + urlencode([('page', '1'), ('size', size), ('sort', 'id'), ('tags', tags)])
        resp = front_end_sock_shop.get('/catalogue' + qstr, headers=dict([('x-requested-with', 'XMLHttpRequest')]))
        resp.assert_status_code(200)
        id_ = jsonpath('$[*].id', resp)

        # POST http://front-end.sock-shop/cart (endp 33)
        with open('data/payload_for_endp_33.json', 'r') as json_payload_file:
            json_payload = json.load(json_payload_file)
        apply_into_json(json_payload, '$.id', id_)
        resp = front_end_sock_shop.post('/cart', json=json_payload)
        resp.assert_status_code(202)

    @clear_session({'spanId': 39})
    def test_039_delete_cart(self):
        # DELETE http://front-end.sock-shop/cart (endp 39)
        front_end_sock_shop = get_http_client('http://front-end.sock-shop', authenticate)
        resp = front_end_sock_shop.delete('/cart')
        resp.assert_status_code(200)
        resp.assert_cssselect('div#content div.container div div.row.same-height-row div div.box.same-height h3', expected_value='You may also like these products')

    @clear_session({'spanId': 47})
    def test_047_get_cart(self):
        # GET http://front-end.sock-shop/cart (endp 47)
        front_end_sock_shop = get_http_client('http://front-end.sock-shop', authenticate)
        resp = front_end_sock_shop.get('/cart', headers=dict([('x-requested-with', 'XMLHttpRequest')]))
        resp.assert_status_code(200)

    @clear_session({'spanId': 63})
    def test_063_get_cart(self):
        # GET http://front-end.sock-shop/cart (endp 63)
        front_end_sock_shop = get_http_client('http://front-end.sock-shop', authenticate)
        resp = front_end_sock_shop.get('/cart', headers=dict([('x-requested-with', 'XMLHttpRequest')]))
        resp.assert_status_code(200)
        resp.assert_cssselect('div#copyright div.container div p.pull-left a', expected_value='Weaveworks')

    @clear_session({'spanId': 174})
    def test_174_post_cart(self):
        # GET http://front-end.sock-shop/cart (endp 146)
        front_end_sock_shop = get_http_client('http://front-end.sock-shop', authenticate)
        resp = front_end_sock_shop.get('/cart', headers=dict([('x-requested-with', 'XMLHttpRequest')]))
        resp.assert_status_code(200)
        id_ = jsonpath('$[*].itemId', resp)

        # POST http://front-end.sock-shop/cart (endp 174)
        with open('data/payload_for_endp_174.json', 'r') as json_payload_file:
            json_payload = json.load(json_payload_file)
        apply_into_json(json_payload, '$.id', id_)
        resp = front_end_sock_shop.post('/cart', json=json_payload, headers=dict([('x-requested-with', 'XMLHttpRequest')]))
        resp.assert_status_code(201)

    @clear_session({'spanId': 175})
    def test_175_delete_cart(self):
        # DELETE http://front-end.sock-shop/cart (endp 175)
        front_end_sock_shop = get_http_client('http://front-end.sock-shop', authenticate)
        resp = front_end_sock_shop.delete('/cart', headers=dict([('x-requested-with', 'XMLHttpRequest')]))
        resp.assert_status_code(202)

    @clear_session({'spanId': 286})
    def test_286_delete_cart(self):
        # DELETE http://front-end.sock-shop/cart (endp 286)
        front_end_sock_shop = get_http_client('http://front-end.sock-shop', authenticate)
        resp = front_end_sock_shop.delete('/cart', headers=dict([('x-requested-with', 'XMLHttpRequest')]))
        resp.assert_status_code(202)

    @clear_session({'spanId': 46})
    def test_046_get_catalogue(self):
        # GET http://front-end.sock-shop/catalogue (endp 46)
        front_end_sock_shop = get_http_client('http://front-end.sock-shop', authenticate)
        resp = front_end_sock_shop.get('/catalogue')
        resp.assert_status_code(201)
        resp.assert_jsonpath('$.address.city', expected_value='Glasgow')

    @json_dataset('data/dataset_65.json')
    @clear_session({'spanId': 65})
    def test_065_get_catalogue(self, data_row):
        size, = data_row

        # GET http://front-end.sock-shop/catalogue (endp 65)
        front_end_sock_shop = get_http_client('http://front-end.sock-shop', authenticate)
        qstr = '?' + urlencode([('size', size)])
        resp = front_end_sock_shop.get('/catalogue' + qstr, headers=dict([('x-requested-with', 'XMLHttpRequest')]))
        resp.assert_status_code(200)

    @json_dataset('data/dataset_121.json')
    @clear_session({'spanId': 121})
    def test_121_get_catalogue(self, data_row):
        size, = data_row

        # GET http://front-end.sock-shop/catalogue (endp 121)
        front_end_sock_shop = get_http_client('http://front-end.sock-shop', authenticate)
        qstr = '?' + urlencode([('page', '1'), ('size', size), ('tags', 'large')])
        resp = front_end_sock_shop.get('/catalogue' + qstr, headers=dict([('x-requested-with', 'XMLHttpRequest')]))
        resp.assert_status_code(200)

    @json_dataset('data/dataset_48.json')
    @clear_session({'spanId': 48})
    def test_048_get_catalogue_id(self, data_row):
        page, size, tags = data_row

        # GET http://front-end.sock-shop/catalogue (endp 147)
        front_end_sock_shop = get_http_client('http://front-end.sock-shop', authenticate)
        qstr = '?' + urlencode([('page', page), ('size', size), ('sort', 'id'), ('tags', tags)])
        resp = front_end_sock_shop.get('/catalogue' + qstr, headers=dict([('x-requested-with', 'XMLHttpRequest')]))
        resp.assert_status_code(200)
        id_ = jsonpath('$[*].id', resp)

        # GET http://front-end.sock-shop/catalogue/{id} (endp 48)
        resp = front_end_sock_shop.get(f'/catalogue/{id_}', headers=dict([('x-requested-with', 'XMLHttpRequest')]))
        resp.assert_status_code(200)

    @json_dataset('data/dataset_166.json')
    @clear_session({'spanId': 166})
    def test_166_get_catalogue_id(self, data_row):
        page, size, tags = data_row

        # GET http://front-end.sock-shop/catalogue (endp 147)
        front_end_sock_shop = get_http_client('http://front-end.sock-shop', authenticate)
        qstr = '?' + urlencode([('page', page), ('size', size), ('sort', 'id'), ('tags', tags)])
        resp = front_end_sock_shop.get('/catalogue' + qstr, headers=dict([('x-requested-with', 'XMLHttpRequest')]))
        resp.assert_status_code(200)
        id_ = jsonpath('$[*].id', resp)

        # GET http://front-end.sock-shop/catalogue/{id} (endp 166)
        resp = front_end_sock_shop.get(f'/catalogue/{id_}', headers=dict([('x-requested-with', 'XMLHttpRequest')]))
        resp.assert_status_code(200)

    @clear_session({'spanId': 75})
    def test_075_get_catalogue_size(self):
        # GET http://front-end.sock-shop/tags (endp 83)
        front_end_sock_shop = get_http_client('http://front-end.sock-shop', authenticate)
        resp = front_end_sock_shop.get('/tags', headers=dict([('x-requested-with', 'XMLHttpRequest')]))
        resp.assert_status_code(200)
        tags = jsonpath('$.tags[*]', resp)

        # GET http://front-end.sock-shop/catalogue/size (endp 75)
        qstr = '?' + urlencode([('tags', tags)])
        resp = front_end_sock_shop.get('/catalogue/size' + qstr, headers=dict([('x-requested-with', 'XMLHttpRequest')]))
        resp.assert_status_code(200)

    @clear_session({'spanId': 177})
    def test_177_get_catalogue_size(self):
        # GET http://front-end.sock-shop/catalogue/size (endp 177)
        front_end_sock_shop = get_http_client('http://front-end.sock-shop', authenticate)
        qstr = '?' + urlencode([('tags', '')])
        resp = front_end_sock_shop.get('/catalogue/size' + qstr, headers=dict([('x-requested-with', 'XMLHttpRequest')]))
        resp.assert_status_code(200)

    @json_dataset('data/dataset_18.json')
    @clear_session({'spanId': 18})
    def test_018_get_category_html(self, data_row):
        tags, = data_row

        # GET http://front-end.sock-shop/category.html (endp 18)
        front_end_sock_shop = get_http_client('http://front-end.sock-shop', authenticate)
        qstr = '?' + urlencode([('tags', tags)])
        resp = front_end_sock_shop.get('/category.html' + qstr)
        resp.assert_status_code(200)
        resp.assert_cssselect('div#content div.container div div.row.same-height-row div div.box.same-height h3', expected_value='You may also like these products')

    @clear_session({'spanId': 179})
    def test_179_get_category_html(self):
        # GET http://front-end.sock-shop/category.html (endp 179)
        front_end_sock_shop = get_http_client('http://front-end.sock-shop', authenticate)
        qstr = '?' + urlencode([('page', '2')])
        resp = front_end_sock_shop.get('/category.html' + qstr)
        resp.assert_status_code(200)
        resp.assert_cssselect('div#content div.container div div.panel.panel-default.sidebar-menu div.panel-heading h3.panel-title', expected_value='Filters ')

    @json_dataset('data/dataset_77.json')
    @clear_session({'spanId': 77})
    def test_077_get_customer_order_html(self, data_row):
        order, = data_row

        # GET http://front-end.sock-shop/customer-order.html (endp 77)
        front_end_sock_shop = get_http_client('http://front-end.sock-shop', authenticate)
        qstr = '?' + urlencode([('order', order)])
        resp = front_end_sock_shop.get('/customer-order.html' + qstr)
        resp.assert_status_code(200)
        resp.assert_cssselect('div#customer-order div.box h2', expected_value='Order #')

    @json_dataset('data/dataset_180.json')
    @clear_session({'spanId': 180})
    def test_180_get_customer_order_html(self, data_row):
        order, = data_row

        # GET http://front-end.sock-shop/customer-order.html (endp 180)
        front_end_sock_shop = get_http_client('http://front-end.sock-shop', authenticate)
        qstr = '?' + urlencode([('order', order)])
        resp = front_end_sock_shop.get('/customer-order.html' + qstr)
        resp.assert_status_code(200)
        resp.assert_cssselect('div#customer-order div.box h2', expected_value='Order #')

    @clear_session({'spanId': 78})
    def test_078_get_customer_orders_html(self):
        # GET http://front-end.sock-shop/customer-orders.html (endp 78)
        front_end_sock_shop = get_http_client('http://front-end.sock-shop', authenticate)
        resp = front_end_sock_shop.get('/customer-orders.html')
        resp.assert_status_code(200)
        resp.assert_cssselect('div#customer-orders div.box h1', expected_value='My orders')

    @clear_session({'spanId': 181})
    def test_181_get_customer_orders_html(self):
        # GET http://front-end.sock-shop/customer-orders.html (endp 181)
        front_end_sock_shop = get_http_client('http://front-end.sock-shop', authenticate)
        resp = front_end_sock_shop.get('/customer-orders.html')
        resp.assert_status_code(200)
        resp.assert_cssselect('div#customer-orders div.box h1', expected_value='My orders')

    @clear_session({'spanId': 50})
    def test_050_get_customers_customerId(self):
        # GET http://front-end.sock-shop/customers/{customerId} (endp 50)
        front_end_sock_shop = get_http_client('http://front-end.sock-shop', authenticate)
        resp = front_end_sock_shop.get(f"/customers/{str(get_data_from_cookie('logged_in'))}", headers=dict([('x-requested-with', 'XMLHttpRequest')]))
        resp.assert_status_code(200)

    @clear_session({'spanId': 148})
    def test_148_get_customers_customerId(self):
        # GET http://front-end.sock-shop/customers/{customerId} (endp 148)
        front_end_sock_shop = get_http_client('http://front-end.sock-shop', authenticate)
        resp = front_end_sock_shop.get(f"/customers/{str(get_data_from_cookie('logged_in'))}", headers=dict([('x-requested-with', 'XMLHttpRequest')]))
        resp.assert_status_code(200)

    @clear_session({'spanId': 163})
    def test_163_get_customers_wcbVLjJnpzpezACrWupvwuuQUEpXSBhZ(self):
        # GET http://front-end.sock-shop/customers/wcbVLjJnpzpezACrWupvwuuQUEpXSBhZ (endp 163)
        front_end_sock_shop = get_http_client('http://front-end.sock-shop', authenticate)
        resp = front_end_sock_shop.get('/customers/wcbVLjJnpzpezACrWupvwuuQUEpXSBhZ', headers=dict([('x-requested-with', 'XMLHttpRequest')]))
        resp.assert_status_code(200)
        resp.assert_jsonpath('$.lastName', expected_value='Name')

    @clear_session({'spanId': 19})
    def test_019_get_detail_html(self):
        # POST http://front-end.sock-shop/orders (endp 21)
        front_end_sock_shop = get_http_client('http://front-end.sock-shop', authenticate)
        resp = front_end_sock_shop.post('/orders', headers=dict([('x-requested-with', 'XMLHttpRequest')]))
        resp.assert_status_code(201)
        resp.assert_jsonpath('$.address.city', expected_value='Glasgow')
        id_ = jsonpath('$.items[*].itemId', resp)

        # GET http://front-end.sock-shop/detail.html (endp 19)
        qstr = '?' + urlencode([('id', id_)])
        resp = front_end_sock_shop.get('/detail.html' + qstr)
        resp.assert_status_code(200)
        resp.assert_cssselect('div#content div.container div div.row.same-height-row div div.box.same-height h3', expected_value='You may also like these products')

    @json_dataset('data/dataset_183.json')
    @clear_session({'spanId': 183})
    def test_183_get_detail_html(self, data_row):
        page, size, tags = data_row

        # GET http://front-end.sock-shop/catalogue (endp 147)
        front_end_sock_shop = get_http_client('http://front-end.sock-shop', authenticate)
        qstr = '?' + urlencode([('page', page), ('size', size), ('sort', 'id'), ('tags', tags)])
        resp = front_end_sock_shop.get('/catalogue' + qstr, headers=dict([('x-requested-with', 'XMLHttpRequest')]))
        resp.assert_status_code(200)
        id_ = jsonpath('$[*].id', resp)

        # GET http://front-end.sock-shop/detail.html (endp 183)
        qstr = '?' + urlencode([('id', id_)])
        resp = front_end_sock_shop.get('/detail.html' + qstr)
        resp.assert_status_code(200)
        resp.assert_cssselect('div#content div.container div div.row.same-height-row div div.box.same-height h3', expected_value='You may also like these products')

    @clear_session({'spanId': 54})
    def test_054_get_footer_html(self):
        # GET http://front-end.sock-shop/footer.html (endp 54)
        front_end_sock_shop = get_http_client('http://front-end.sock-shop', authenticate)
        resp = front_end_sock_shop.get('/footer.html', headers=dict([('x-requested-with', 'XMLHttpRequest')]))
        resp.assert_status_code(200)
        resp.assert_cssselect('div#copyright div.container div p.pull-left a', expected_value='Weaveworks')

    @clear_session({'spanId': 101})
    def test_101_get_footer_html(self):
        # GET http://front-end.sock-shop/footer.html (endp 101)
        front_end_sock_shop = get_http_client('http://front-end.sock-shop', authenticate)
        resp = front_end_sock_shop.get('/footer.html', headers=dict([('x-requested-with', 'XMLHttpRequest')]))
        resp.assert_status_code(200)

    @clear_session({'spanId': 149})
    def test_149_get_footer_html(self):
        # GET http://front-end.sock-shop/footer.html (endp 149)
        front_end_sock_shop = get_http_client('http://front-end.sock-shop', authenticate)
        resp = front_end_sock_shop.get('/footer.html', headers=dict([('x-requested-with', 'XMLHttpRequest')]))
        resp.assert_status_code(200)
        resp.assert_cssselect('div#copyright div.container div p.pull-left a', expected_value='Weaveworks')

    @json_dataset('data/dataset_61.json')
    @clear_session({'spanId': 61})
    def test_061_get_index_html(self, data_row):
        urlmaskfilter, = data_row

        # GET http://front-end.sock-shop/index.html (endp 61)
        front_end_sock_shop = get_http_client('http://front-end.sock-shop', authenticate)
        qstr = '?' + urlencode([('urlmaskfilter', urlmaskfilter)])
        resp = front_end_sock_shop.get('/index.html' + qstr)
        resp.assert_status_code(200)
        resp.assert_cssselect('div#hot div.box div.container div h2', expected_value='Hot this week')

    @json_dataset('data/dataset_184.json')
    @clear_session({'spanId': 184})
    def test_184_get_index_html(self, data_row):
        findcli, = data_row

        # GET http://front-end.sock-shop/index.html (endp 184)
        front_end_sock_shop = get_http_client('http://front-end.sock-shop', authenticate)
        qstr = '?' + urlencode([('findcli', findcli), ('test', '')])
        resp = front_end_sock_shop.get('/index.html' + qstr)
        resp.assert_status_code(200)
        resp.assert_cssselect('div#hot div.box div.container div h2', expected_value='Hot this week')

    @clear_session({'spanId': 210})
    def test_210_head_index_html(self):
        # HEAD http://front-end.sock-shop/index.html (endp 210)
        front_end_sock_shop = get_http_client('http://front-end.sock-shop', authenticate)
        resp = front_end_sock_shop.head('/index.html')
        resp.assert_status_code(200)

    @json_dataset('data/dataset_95.json')
    @clear_session({'spanId': 95})
    def test_095_post_lib_phpunit_phpunit_src_Util_PHP_eval_stdin_php(self, data_row):
        __, = data_row

        # POST http://front-end.sock-shop/lib/phpunit/phpunit/src/Util/PHP/eval-stdin.php (endp 95)
        front_end_sock_shop = get_http_client('http://front-end.sock-shop', authenticate)
        resp = front_end_sock_shop.post('/lib/phpunit/phpunit/src/Util/PHP/eval-stdin.php', data=[('<?', __), ('?>', '')])
        resp.assert_status_code(200)
        resp.assert_cssselect('div#hot div.box div.container div h2', expected_value='Hot this week')

    # authentication-related test
    @clear_session({'spanId': 20})
    def test_020_get_login(self):
        # GET http://front-end.sock-shop/login (endp 20)
        front_end_sock_shop = get_http_client('http://front-end.sock-shop', dummy_auth)
        resp = front_end_sock_shop.get('/login', headers=dict([('x-requested-with', 'XMLHttpRequest')]))
        resp.assert_status_code(200)
        resp.assert_cssselect('div#hot div.box div.container div h2', expected_value='Hot this week')

    # authentication-related test
    @clear_session({'spanId': 150})
    def test_150_get_login(self):
        # GET http://front-end.sock-shop/login (endp 150)
        front_end_sock_shop = get_http_client('http://front-end.sock-shop', dummy_auth)
        resp = front_end_sock_shop.get('/login', headers=dict([('x-requested-with', 'XMLHttpRequest')]))
        resp.assert_status_code(200)
        resp.assert_cssselect('p', expected_value='Cookie is set')

    @clear_session({'spanId': 215})
    def test_215_get_metrics(self):
        # GET http://front-end.sock-shop/metrics (endp 215)
        front_end_sock_shop = get_http_client('http://front-end.sock-shop', authenticate)
        resp = front_end_sock_shop.get('/metrics')
        resp.assert_status_code(200)

    @clear_session({'spanId': 22})
    def test_022_post_orders(self):
        # POST http://front-end.sock-shop/orders (endp 22)
        front_end_sock_shop = get_http_client('http://front-end.sock-shop', authenticate)
        resp = front_end_sock_shop.post('/orders')
        resp.assert_status_code(200)
        resp.assert_cssselect('div#hot div.box div.container div h2', expected_value='Hot this week')

    @clear_session({'spanId': 186})
    def test_186_get_orders(self):
        # GET http://front-end.sock-shop/orders (endp 186)
        front_end_sock_shop = get_http_client('http://front-end.sock-shop', authenticate)
        resp = front_end_sock_shop.get('/orders', headers=dict([('x-requested-with', 'XMLHttpRequest')]))
        resp.assert_status_code(201)
        resp.assert_jsonpath('$[*].address.city', expected_value='elsewhere')

    @clear_session({'spanId': 187})
    def test_187_post_orders(self):
        # POST http://front-end.sock-shop/orders (endp 187)
        front_end_sock_shop = get_http_client('http://front-end.sock-shop', authenticate)
        resp = front_end_sock_shop.post('/orders', headers=dict([('x-requested-with', 'XMLHttpRequest')]))
        resp.assert_status_code(201)
        resp.assert_jsonpath('$.address.city', expected_value='elsewhere')

    @clear_session({'spanId': 82})
    def test_082_get_orders_id(self):
        # GET http://front-end.sock-shop/orders (endp 80)
        front_end_sock_shop = get_http_client('http://front-end.sock-shop', authenticate)
        resp = front_end_sock_shop.get('/orders', headers=dict([('x-requested-with', 'XMLHttpRequest')]))
        resp.assert_status_code(201)
        resp.assert_jsonpath('$.[*].address.city', expected_value='Glasgow')
        id_ = url_part('/2', jsonpath('$[*]._links.self.href', resp))

        # GET http://front-end.sock-shop/orders/{id} (endp 82)
        resp = front_end_sock_shop.get(f'/orders/{id_}', headers=dict([('x-requested-with', 'XMLHttpRequest')]))
        resp.assert_status_code(200)
        resp.assert_jsonpath('$.address.city', expected_value='Glasgow')

    @clear_session({'spanId': 188})
    def test_188_get_orders_id(self):
        # GET http://front-end.sock-shop/orders (endp 80)
        front_end_sock_shop = get_http_client('http://front-end.sock-shop', authenticate)
        resp = front_end_sock_shop.get('/orders', headers=dict([('x-requested-with', 'XMLHttpRequest')]))
        resp.assert_status_code(201)
        resp.assert_jsonpath('$.[*].address.city', expected_value='Glasgow')
        id_ = url_part('/2', jsonpath('$[*]._links.self.href', resp))

        # GET http://front-end.sock-shop/orders/{id} (endp 188)
        resp = front_end_sock_shop.get(f'/orders/{id_}', headers=dict([('x-requested-with', 'XMLHttpRequest')]))
        resp.assert_status_code(200)
        resp.assert_jsonpath('$.address.city', expected_value='elsewhere')

    @json_dataset('data/dataset_102.json')
    @clear_session({'spanId': 102})
    def test_102_post_plus_qiang_php(self, data_row):
        blbl, = data_row

        # POST http://front-end.sock-shop/plus/qiang.php (endp 102)
        front_end_sock_shop = get_http_client('http://front-end.sock-shop', authenticate)
        resp = front_end_sock_shop.post('/plus/qiang.php', data=[('blbl', blbl)])
        resp.assert_status_code(200)
        resp.assert_cssselect('div#hot div.box div.container div h2', expected_value='Hot this week')

    # authentication-related test
    @clear_session({'spanId': 66})
    def test_066_get_por_login_psw_csp(self):
        # GET http://front-end.sock-shop/por/login_psw.csp (endp 66)
        front_end_sock_shop = get_http_client('http://front-end.sock-shop', dummy_auth)
        resp = front_end_sock_shop.get('/por/login_psw.csp')
        resp.assert_status_code(200)
        resp.assert_cssselect('div#hot div.box div.container div h2', expected_value='Hot this week')

    # authentication-related test
    @json_dataset('data/dataset_189.json')
    @clear_session({'spanId': 189})
    def test_189_post_register(self, data_row):
        email_, firstName, lastName, password, username = data_row

        # POST http://front-end.sock-shop/register (endp 189)
        front_end_sock_shop = get_http_client('http://front-end.sock-shop', dummy_auth)
        with open('data/payload_for_endp_189.json', 'r') as json_payload_file:
            json_payload = json.load(json_payload_file)
        apply_into_json(json_payload, '$.email', email_)
        apply_into_json(json_payload, '$.firstName', firstName)
        apply_into_json(json_payload, '$.lastName', lastName)
        apply_into_json(json_payload, '$.password', password)
        apply_into_json(json_payload, '$.username', username)
        resp = front_end_sock_shop.post('/register', json=json_payload, headers=dict([('x-requested-with', 'XMLHttpRequest')]))
        resp.assert_status_code(200)

    @clear_session({'spanId': 190})
    def test_190_get_tags(self):
        # GET http://front-end.sock-shop/tags (endp 190)
        front_end_sock_shop = get_http_client('http://front-end.sock-shop', authenticate)
        resp = front_end_sock_shop.get('/tags', headers=dict([('x-requested-with', 'XMLHttpRequest')]))
        resp.assert_status_code(200)

    @clear_session({'spanId': 56})
    def test_056_get_topbar_html(self):
        # GET http://front-end.sock-shop/topbar.html (endp 56)
        front_end_sock_shop = get_http_client('http://front-end.sock-shop', authenticate)
        resp = front_end_sock_shop.get('/topbar.html', headers=dict([('x-requested-with', 'XMLHttpRequest')]))
        resp.assert_status_code(200)
        resp.assert_cssselect('div#hot div.box div.container div h2', expected_value='Hot this week')

    @clear_session({'spanId': 152})
    def test_152_get_topbar_html(self):
        # GET http://front-end.sock-shop/topbar.html (endp 152)
        front_end_sock_shop = get_http_client('http://front-end.sock-shop', authenticate)
        resp = front_end_sock_shop.get('/topbar.html', headers=dict([('x-requested-with', 'XMLHttpRequest')]))
        resp.assert_status_code(200)
        resp.assert_cssselect('div#top div.container div.offer a.btn.btn-success.btn-sm', expected_value='Offer of the day')


@data_driven_tests
class Tests_orders_sock_shop(unittest.TestCase):

    @json_dataset('data/dataset_92.json')
    @clear_session({'spanId': 92})
    def test_092_get_orders_id(self, data_row):
        address, card, customer, items = data_row

        # POST http://orders.sock-shop/orders (endp 10)
        orders_sock_shop = get_http_client('http://orders.sock-shop', authenticate)
        with open('data/payload_for_endp_10.json', 'r') as json_payload_file:
            json_payload = json.load(json_payload_file)
        apply_into_json(json_payload, '$.address', address)
        apply_into_json(json_payload, '$.card', card)
        apply_into_json(json_payload, '$.customer', customer)
        apply_into_json(json_payload, '$.items', items)
        resp = orders_sock_shop.post('/orders', json=json_payload, headers=dict([('accept', 'application/json')]))
        resp.assert_status_code(201)
        resp.assert_jsonpath('$.address.city', expected_value='Glasgow')
        custId = jsonpath('$.customerId', resp)

        # GET http://orders.sock-shop/orders/search/customerId (endp 94)
        qstr = '?' + urlencode([('custId', custId), ('sort', 'date')])
        resp = orders_sock_shop.get('/orders/search/customerId' + qstr)
        resp.assert_status_code(200)
        resp.assert_jsonpath('$._embedded.customerOrders.[*].address.country', expected_value='United Kingdom')
        id_ = url_part('/2', jsonpath('$._embedded.customerOrders[*]._links.self.href', resp))

        # GET http://orders.sock-shop/orders/{id} (endp 92)
        resp = orders_sock_shop.get(f'/orders/{id_}')
        resp.assert_status_code(200)
        resp.assert_jsonpath('$.address.city', expected_value='Glasgow')

    @json_dataset('data/dataset_199.json')
    @clear_session({'spanId': 199})
    def test_199_get_orders_id(self, data_row):
        address, card, customer, items = data_row

        # POST http://orders.sock-shop/orders (endp 10)
        orders_sock_shop = get_http_client('http://orders.sock-shop', authenticate)
        with open('data/payload_for_endp_10.json', 'r') as json_payload_file:
            json_payload = json.load(json_payload_file)
        apply_into_json(json_payload, '$.address', address)
        apply_into_json(json_payload, '$.card', card)
        apply_into_json(json_payload, '$.customer', customer)
        apply_into_json(json_payload, '$.items', items)
        resp = orders_sock_shop.post('/orders', json=json_payload, headers=dict([('accept', 'application/json')]))
        resp.assert_status_code(201)
        resp.assert_jsonpath('$.address.city', expected_value='Glasgow')
        custId = jsonpath('$.customerId', resp)

        # GET http://orders.sock-shop/orders/search/customerId (endp 94)
        qstr = '?' + urlencode([('custId', custId), ('sort', 'date')])
        resp = orders_sock_shop.get('/orders/search/customerId' + qstr)
        resp.assert_status_code(200)
        resp.assert_jsonpath('$._embedded.customerOrders.[*].address.country', expected_value='United Kingdom')
        id_ = url_part('/2', jsonpath('$._embedded.customerOrders[*]._links.self.href', resp))

        # GET http://orders.sock-shop/orders/{id} (endp 199)
        resp = orders_sock_shop.get(f'/orders/{id_}')
        resp.assert_status_code(200)
        resp.assert_jsonpath('$.address.city', expected_value='elsewhere')

    @json_dataset('data/dataset_93.json')
    @clear_session({'spanId': 93})
    def test_093_get_orders_search_customerId(self, data_row):
        address, card, customer, items = data_row

        # POST http://orders.sock-shop/orders (endp 10)
        orders_sock_shop = get_http_client('http://orders.sock-shop', authenticate)
        with open('data/payload_for_endp_10.json', 'r') as json_payload_file:
            json_payload = json.load(json_payload_file)
        apply_into_json(json_payload, '$.address', address)
        apply_into_json(json_payload, '$.card', card)
        apply_into_json(json_payload, '$.customer', customer)
        apply_into_json(json_payload, '$.items', items)
        resp = orders_sock_shop.post('/orders', json=json_payload, headers=dict([('accept', 'application/json')]))
        resp.assert_status_code(201)
        resp.assert_jsonpath('$.address.city', expected_value='Glasgow')
        custId = jsonpath('$.customerId', resp)

        # GET http://orders.sock-shop/orders/search/customerId (endp 93)
        qstr = '?' + urlencode([('custId', custId), ('sort', 'date')])
        resp = orders_sock_shop.get('/orders/search/customerId' + qstr)
        resp.assert_status_code(200)

    @json_dataset('data/dataset_156.json')
    @clear_session({'spanId': 156})
    def test_156_get_orders_search_customerId(self, data_row):
        address, card, customer, items, items1 = data_row

        # POST http://orders.sock-shop/orders (endp 10)
        orders_sock_shop = get_http_client('http://orders.sock-shop', authenticate)
        with open('data/payload_for_endp_10.json', 'r') as json_payload_file:
            json_payload = json.load(json_payload_file)
        apply_into_json(json_payload, '$.address', address)
        apply_into_json(json_payload, '$.card', card)
        apply_into_json(json_payload, '$.customer', customer)
        apply_into_json(json_payload, '$.items', items)
        resp = orders_sock_shop.post('/orders', json=json_payload, headers=dict([('accept', 'application/json')]))
        resp.assert_status_code(201)
        resp.assert_jsonpath('$.address.city', expected_value='Glasgow')
        customerId = jsonpath('$.customerId', resp)

        # GET http://user.sock-shop/customers/{customerId} (endp 127)
        user_sock_shop = get_http_client('http://user.sock-shop', authenticate)
        resp = user_sock_shop.get(f'/customers/{customerId}', headers=dict([('accept', 'application/hal+json')]))
        resp.assert_status_code(200)
        customer1 = jsonpath('$._links.self.href', resp)

        # GET http://user.sock-shop/customers/{customerId}/addresses (endp 128)
        resp = user_sock_shop.get(f'/customers/{customerId}/addresses')
        resp.assert_status_code(200)
        address1 = jsonpath('$._embedded.address[*]._links.address.href', resp)

        # GET http://user.sock-shop/customers/{customerId}/cards (endp 129)
        resp = user_sock_shop.get(f'/customers/{customerId}/cards')
        resp.assert_status_code(200)
        card1 = jsonpath('$._embedded.card[*]._links.card.href', resp)

        # POST http://orders.sock-shop/orders (endp 155)
        with open('data/payload_for_endp_155.json', 'r') as json_payload_file:
            json_payload = json.load(json_payload_file)
        apply_into_json(json_payload, '$.address', address1)
        apply_into_json(json_payload, '$.card', card1)
        apply_into_json(json_payload, '$.customer', customer1)
        apply_into_json(json_payload, '$.items', items1)
        resp = orders_sock_shop.post('/orders', json=json_payload, headers=dict([('accept', 'application/json')]))
        resp.assert_status_code(201)
        custId = jsonpath('$.customerId', resp)

        # GET http://orders.sock-shop/orders/search/customerId (endp 156)
        qstr = '?' + urlencode([('custId', custId), ('sort', 'date')])
        resp = orders_sock_shop.get('/orders/search/customerId' + qstr)
        resp.assert_status_code(200)


@data_driven_tests
class Tests_payment_sock_shop(unittest.TestCase):

    @json_dataset('data/dataset_27.json')
    @clear_session({'spanId': 27})
    def test_027_post_paymentAuth(self, data_row):
        address, amount, card, city, customer, id_, items, lastName, longNum, number, username = data_row

        # POST http://orders.sock-shop/orders (endp 10)
        orders_sock_shop = get_http_client('http://orders.sock-shop', authenticate)
        with open('data/payload_for_endp_10.json', 'r') as json_payload_file:
            json_payload = json.load(json_payload_file)
        apply_into_json(json_payload, '$.address', address)
        apply_into_json(json_payload, '$.card', card)
        apply_into_json(json_payload, '$.customer', customer)
        apply_into_json(json_payload, '$.items', items)
        resp = orders_sock_shop.post('/orders', json=json_payload, headers=dict([('accept', 'application/json')]))
        resp.assert_status_code(201)
        resp.assert_jsonpath('$.address.city', expected_value='Glasgow')
        customerId = jsonpath('$.customerId', resp)

        # GET http://user.sock-shop/cards/{id} (endp 24)
        user_sock_shop = get_http_client('http://user.sock-shop', authenticate)
        resp = user_sock_shop.get(f'/cards/{id_}', headers=dict([('accept', 'application/hal+json')]))
        resp.assert_status_code(200)
        resp.assert_jsonpath('$.city', expected_value='Glasgow')
        ccv = jsonpath('$.ccv', resp)
        expires = jsonpath('$.expires', resp)
        id1 = jsonpath('$.id', resp)

        # GET http://user.sock-shop/customers/{customerId} (endp 3)
        resp = user_sock_shop.get(f'/customers/{customerId}', headers=dict([('accept', 'application/hal+json')]))
        resp.assert_status_code(200)
        resp.assert_jsonpath('$.city', expected_value='Glasgow')
        firstName = jsonpath('$.firstName', resp)

        # GET http://user.sock-shop/addresses/{id} (endp 23)
        resp = user_sock_shop.get(f'/addresses/{id1}', headers=dict([('accept', 'application/hal+json')]))
        resp.assert_status_code(200)
        resp.assert_jsonpath('$.country', expected_value='United Kingdom')
        country = jsonpath('$.country', resp)
        postcode = jsonpath('$.postcode', resp)
        street = jsonpath('$.street', resp)

        # POST http://payment.sock-shop/paymentAuth (endp 27)
        payment_sock_shop = get_http_client('http://payment.sock-shop', authenticate)
        with open('data/payload_for_endp_27.json', 'r') as json_payload_file:
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
        resp = payment_sock_shop.post('/paymentAuth', json=json_payload, headers=dict([('accept', 'application/json')]))
        resp.assert_status_code(200)

    @json_dataset('data/dataset_143.json')
    @clear_session({'spanId': 143})
    def test_143_post_paymentAuth(self, data_row):
        address, amount, card, city, customer, id_, items, lastName, longNum, number, username = data_row

        # POST http://orders.sock-shop/orders (endp 10)
        orders_sock_shop = get_http_client('http://orders.sock-shop', authenticate)
        with open('data/payload_for_endp_10.json', 'r') as json_payload_file:
            json_payload = json.load(json_payload_file)
        apply_into_json(json_payload, '$.address', address)
        apply_into_json(json_payload, '$.card', card)
        apply_into_json(json_payload, '$.customer', customer)
        apply_into_json(json_payload, '$.items', items)
        resp = orders_sock_shop.post('/orders', json=json_payload, headers=dict([('accept', 'application/json')]))
        resp.assert_status_code(201)
        resp.assert_jsonpath('$.address.city', expected_value='Glasgow')
        customerId = jsonpath('$.customerId', resp)

        # GET http://user.sock-shop/cards/{id} (endp 24)
        user_sock_shop = get_http_client('http://user.sock-shop', authenticate)
        resp = user_sock_shop.get(f'/cards/{id_}', headers=dict([('accept', 'application/hal+json')]))
        resp.assert_status_code(200)
        resp.assert_jsonpath('$.city', expected_value='Glasgow')
        id1 = jsonpath('$.id', resp)

        # GET http://user.sock-shop/customers/{customerId} (endp 127)
        resp = user_sock_shop.get(f'/customers/{customerId}', headers=dict([('accept', 'application/hal+json')]))
        resp.assert_status_code(200)
        firstName = jsonpath('$.firstName', resp)

        # GET http://user.sock-shop/addresses/{id} (endp 131)
        resp = user_sock_shop.get(f'/addresses/{id1}', headers=dict([('accept', 'application/hal+json')]))
        resp.assert_status_code(200)
        country = jsonpath('$.country', resp)
        postcode = jsonpath('$.postcode', resp)
        street = jsonpath('$.street', resp)

        # GET http://user.sock-shop/cards/{id} (endp 132)
        resp = user_sock_shop.get(f'/cards/{id_}', headers=dict([('accept', 'application/hal+json')]))
        resp.assert_status_code(200)
        ccv = jsonpath('$.ccv', resp)
        expires = jsonpath('$.expires', resp)

        # POST http://payment.sock-shop/paymentAuth (endp 143)
        payment_sock_shop = get_http_client('http://payment.sock-shop', authenticate)
        with open('data/payload_for_endp_143.json', 'r') as json_payload_file:
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
        resp = payment_sock_shop.post('/paymentAuth', json=json_payload, headers=dict([('accept', 'application/json')]))
        resp.assert_status_code(200)


@data_driven_tests
class Tests_shipping_sock_shop(unittest.TestCase):

    @json_dataset('data/dataset_25.json')
    @clear_session({'spanId': 25})
    def test_025_post_shipping(self, data_row):
        id_, = data_row

        # GET http://user.sock-shop/cards/{id} (endp 24)
        user_sock_shop = get_http_client('http://user.sock-shop', authenticate)
        resp = user_sock_shop.get(f'/cards/{id_}', headers=dict([('accept', 'application/hal+json')]))
        resp.assert_status_code(200)
        resp.assert_jsonpath('$.city', expected_value='Glasgow')
        name = jsonpath('$.id', resp)

        # POST http://shipping.sock-shop/shipping (endp 25)
        shipping_sock_shop = get_http_client('http://shipping.sock-shop', authenticate)
        with open('data/payload_for_endp_25.json', 'r') as json_payload_file:
            json_payload = json.load(json_payload_file)
        apply_into_json(json_payload, '$.id', str(uuid.uuid4()))
        apply_into_json(json_payload, '$.name', name)
        resp = shipping_sock_shop.post('/shipping', json=json_payload, headers=dict([('accept', 'application/json')]))
        resp.assert_status_code(201)

    @json_dataset('data/dataset_144.json')
    @clear_session({'spanId': 144})
    def test_144_post_shipping(self, data_row):
        name, = data_row

        # POST http://shipping.sock-shop/shipping (endp 144)
        shipping_sock_shop = get_http_client('http://shipping.sock-shop', authenticate)
        with open('data/payload_for_endp_144.json', 'r') as json_payload_file:
            json_payload = json.load(json_payload_file)
        apply_into_json(json_payload, '$.id', str(uuid.uuid4()))
        apply_into_json(json_payload, '$.name', name)
        resp = shipping_sock_shop.post('/shipping', json=json_payload, headers=dict([('accept', 'application/json')]))
        resp.assert_status_code(201)


@data_driven_tests
class Tests_user_sock_shop(unittest.TestCase):

    @json_dataset('data/dataset_191.json')
    @clear_session({'spanId': 191})
    def test_191_post_addresses(self, data_row):
        city, country, number, postcode, street, userID = data_row

        # POST http://user.sock-shop/addresses (endp 191)
        user_sock_shop = get_http_client('http://user.sock-shop', authenticate)
        with open('data/payload_for_endp_191.json', 'r') as json_payload_file:
            json_payload = json.load(json_payload_file)
        apply_into_json(json_payload, '$.city', city)
        apply_into_json(json_payload, '$.country', country)
        apply_into_json(json_payload, '$.number', number)
        apply_into_json(json_payload, '$.postcode', postcode)
        apply_into_json(json_payload, '$.street', street)
        apply_into_json(json_payload, '$.userID', userID)
        resp = user_sock_shop.post('/addresses', json=json_payload, headers=dict([('accept', 'application/json')]))
        resp.assert_status_code(200)

    @json_dataset('data/dataset_192.json')
    @clear_session({'spanId': 192})
    def test_192_post_cards(self, data_row):
        ccv, expires, longNum, userID = data_row

        # POST http://user.sock-shop/cards (endp 192)
        user_sock_shop = get_http_client('http://user.sock-shop', authenticate)
        with open('data/payload_for_endp_192.json', 'r') as json_payload_file:
            json_payload = json.load(json_payload_file)
        apply_into_json(json_payload, '$.ccv', ccv)
        apply_into_json(json_payload, '$.expires', expires)
        apply_into_json(json_payload, '$.longNum', longNum)
        apply_into_json(json_payload, '$.userID', userID)
        resp = user_sock_shop.post('/cards', json=json_payload, headers=dict([('accept', 'application/json')]))
        resp.assert_status_code(200)

    @json_dataset('data/dataset_4.json')
    @clear_session({'spanId': 4})
    def test_004_get_customers_customerId_addresses(self, data_row):
        address, card, customer, items = data_row

        # POST http://orders.sock-shop/orders (endp 10)
        orders_sock_shop = get_http_client('http://orders.sock-shop', authenticate)
        with open('data/payload_for_endp_10.json', 'r') as json_payload_file:
            json_payload = json.load(json_payload_file)
        apply_into_json(json_payload, '$.address', address)
        apply_into_json(json_payload, '$.card', card)
        apply_into_json(json_payload, '$.customer', customer)
        apply_into_json(json_payload, '$.items', items)
        resp = orders_sock_shop.post('/orders', json=json_payload, headers=dict([('accept', 'application/json')]))
        resp.assert_status_code(201)
        resp.assert_jsonpath('$.address.city', expected_value='Glasgow')
        customerId = jsonpath('$.customerId', resp)

        # GET http://user.sock-shop/customers/{customerId}/addresses (endp 4)
        user_sock_shop = get_http_client('http://user.sock-shop', authenticate)
        resp = user_sock_shop.get(f'/customers/{customerId}/addresses')
        resp.assert_status_code(200)
        resp.assert_jsonpath('$._embedded.address.[*].country', expected_value='United Kingdom')

    @json_dataset('data/dataset_5.json')
    @clear_session({'spanId': 5})
    def test_005_get_customers_customerId_cards(self, data_row):
        address, card, customer, items = data_row

        # POST http://orders.sock-shop/orders (endp 10)
        orders_sock_shop = get_http_client('http://orders.sock-shop', authenticate)
        with open('data/payload_for_endp_10.json', 'r') as json_payload_file:
            json_payload = json.load(json_payload_file)
        apply_into_json(json_payload, '$.address', address)
        apply_into_json(json_payload, '$.card', card)
        apply_into_json(json_payload, '$.customer', customer)
        apply_into_json(json_payload, '$.items', items)
        resp = orders_sock_shop.post('/orders', json=json_payload, headers=dict([('accept', 'application/json')]))
        resp.assert_status_code(201)
        resp.assert_jsonpath('$.address.city', expected_value='Glasgow')
        customerId = jsonpath('$.customerId', resp)

        # GET http://user.sock-shop/customers/{customerId}/cards (endp 5)
        user_sock_shop = get_http_client('http://user.sock-shop', authenticate)
        resp = user_sock_shop.get(f'/customers/{customerId}/cards')
        resp.assert_status_code(200)

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

    # authentication-related test
    @json_dataset('data/dataset_197.json')
    @clear_session({'spanId': 197})
    def test_197_post_register(self, data_row):
        email_, firstName, lastName, password, username = data_row

        # POST http://user.sock-shop/register (endp 197)
        user_sock_shop = get_http_client('http://user.sock-shop', dummy_auth)
        with open('data/payload_for_endp_197.json', 'r') as json_payload_file:
            json_payload = json.load(json_payload_file)
        apply_into_json(json_payload, '$.email', email_)
        apply_into_json(json_payload, '$.firstName', firstName)
        apply_into_json(json_payload, '$.lastName', lastName)
        apply_into_json(json_payload, '$.password', password)
        apply_into_json(json_payload, '$.username', username)
        resp = user_sock_shop.post('/register', json=json_payload, headers=dict([('accept', 'application/json')]))
        resp.assert_status_code(200)
