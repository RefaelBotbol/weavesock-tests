from up9lib import *
from authentication import authenticate

# logging.basicConfig(level=logging.DEBUG)


@data_driven_tests
class Tests_front_end_sock_shop(unittest.TestCase):

    @json_dataset('data/11/dataset_11.json')
    @clear_session({'spanId': 11})
    def test_011_get_(self, data_row):
        _meta_http_equiv, _script_document_cookie, class_classLoader_URLs_0_, content, expression = data_row

        # GET http://front-end.sock-shop/ (endp 11)
        front_end_sock_shop = get_http_client('http://front-end.sock-shop', authenticate)
        qstr = '?' + urlencode({'"</script>': '', '"><script>alert(\'struts_sa_surl_xss.nasl-1603621900\')</script>': '', '"><script>alert(\'struts_sa_surl_xss.nasl-1605657683\')</script>': '', '"><script>alert(\'struts_sa_surl_xss.nasl-1605658393\')</script>': '', "('\\u0023_memberAccess[\\'allowStaticMethodAccess\\']')(meh)": 'true', '(aaa)((\'\\u0023context[\\\'xwork.MethodAccessor.denyMethodExecution\\\']\\u003d\\u0023foo\')(\\u0023foo\\u003dnew java.lang.Boolean("false")))': '', "(asdf)(('\\u0023thread.sleep(5000)')(\\u0023thread\\u003d@java.lang.Thread@currentThread()))": '1', '<meta http-equiv': _meta_http_equiv, '<script>document.cookie': _script_document_cookie, 'XDEBUG_SESSION_START': 'phpstorm', 'a': 'fetch', 'class.classLoader.URLs[0]': class_classLoader_URLs_0_, 'content': content, 'debug': 'command', 'expression': expression, 'ho {COMPLETE_VERSION}': ''})
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

    @json_dataset('data/133/dataset_133.json')
    @clear_session({'spanId': 133})
    def test_133_get_(self, data_row):
        PHPSESSID, action, album, category, content, dispsize, feed, id_, invitaion_code, mod, mode, name, page, param, s, vars_0_, weekstartday = data_row

        # GET http://front-end.sock-shop/ (endp 133)
        front_end_sock_shop = get_http_client('http://front-end.sock-shop', authenticate)
        qstr = '?' + urlencode({'': param, '\x00': '', '"><script>alert(document.domain)</script>': '', "/'": '', '<script>alert(document.domain)</script>': '', 'OpenServer': '', 'PHPSESSID': PHPSESSID, 'XDEBUG_SESSION_START': 'phpstorm', 'a': 'fetch', 'action': action, 'album': album, 'category': category, 'cmd': 'show', 'content': content, 'cpmvc_do_action': 'mvparse', 'data': '1', 'debug': '1', 'dispsize': dispsize, 'f': 'edit', 'feed': feed, 'filter': 'phpinfo', 'function': 'call_user_func_array', 'id': id_, 'invitaion_code': invitaion_code, 'mod': mod, 'mode': mode, 'name': name, 'op': 'browse', 'page': page, 'parent': '0', 'q[]': 'x', 's': s, 'show_dash_widget': '1', 'start': '0', 'user': '', 'vars[0]': vars_0_, 'weekstartday': weekstartday})
        resp = front_end_sock_shop.get('/' + qstr)
        resp.assert_status_code(200)
        resp.assert_cssselect('div#hot div.box div.container div h2', expected_value='Hot this week')

    @clear_session({'spanId': 134})
    def test_134_head_(self):
        # HEAD http://front-end.sock-shop/ (endp 134)
        front_end_sock_shop = get_http_client('http://front-end.sock-shop', authenticate)
        resp = front_end_sock_shop.head('/')
        resp.assert_status_code(200)

    @json_dataset('data/154/dataset_154.json')
    @clear_session({'spanId': 154})
    def test_154_get_(self, data_row):
        content, = data_row

        # GET http://front-end.sock-shop/ (endp 154)
        front_end_sock_shop = get_http_client('http://front-end.sock-shop', authenticate)
        qstr = '?' + urlencode({'a': 'fetch', 'content': content})
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

    @clear_session({'spanId': 303})
    def test_303_get_(self):
        # GET http://front-end.sock-shop/ (endp 303)
        front_end_sock_shop = get_http_client('http://front-end.sock-shop', authenticate)
        resp = front_end_sock_shop.get('/')
        resp.assert_status_code(200)
        resp.assert_cssselect('div#hot div.box div.container div h2', expected_value='Hot this week')

    @clear_session({'spanId': 304})
    def test_304_get_(self):
        # GET http://front-end.sock-shop/ (endp 304)
        front_end_sock_shop = get_http_client('http://front-end.sock-shop', authenticate)
        resp = front_end_sock_shop.get('/')
        resp.assert_status_code(200)
        resp.assert_cssselect('div#hot div.box div.container div h2', expected_value='Hot this week')

    @clear_session({'spanId': 305})
    def test_305_get_(self):
        # GET http://front-end.sock-shop/ (endp 305)
        front_end_sock_shop = get_http_client('http://front-end.sock-shop', authenticate)
        resp = front_end_sock_shop.get('/')
        resp.assert_status_code(200)
        resp.assert_cssselect('div#hot div.box div.container div h2', expected_value='Hot this week')

    @clear_session({'spanId': 306})
    def test_306_get_(self):
        # GET http://front-end.sock-shop/ (endp 306)
        front_end_sock_shop = get_http_client('http://front-end.sock-shop', authenticate)
        resp = front_end_sock_shop.get('/')
        resp.assert_status_code(200)
        resp.assert_cssselect('div#hot div.box div.container div h2', expected_value='Hot this week')

    @clear_session({'spanId': 307})
    def test_307_get_(self):
        # GET http://front-end.sock-shop/ (endp 307)
        front_end_sock_shop = get_http_client('http://front-end.sock-shop', authenticate)
        resp = front_end_sock_shop.get('/')
        resp.assert_status_code(200)
        resp.assert_cssselect('div#hot div.box div.container div h2', expected_value='Hot this week')

    @clear_session({'spanId': 308})
    def test_308_get_(self):
        # GET http://front-end.sock-shop/ (endp 308)
        front_end_sock_shop = get_http_client('http://front-end.sock-shop', authenticate)
        resp = front_end_sock_shop.get('/')
        resp.assert_status_code(200)
        resp.assert_cssselect('div#hot div.box div.container div h2', expected_value='Hot this week')

    @clear_session({'spanId': 309})
    def test_309_get_(self):
        # GET http://front-end.sock-shop/ (endp 309)
        front_end_sock_shop = get_http_client('http://front-end.sock-shop', authenticate)
        resp = front_end_sock_shop.get('/')
        resp.assert_status_code(200)
        resp.assert_cssselect('div#hot div.box div.container div h2', expected_value='Hot this week')

    @clear_session({'spanId': 310})
    def test_310_get_(self):
        # GET http://front-end.sock-shop/ (endp 310)
        front_end_sock_shop = get_http_client('http://front-end.sock-shop', authenticate)
        resp = front_end_sock_shop.get('/')
        resp.assert_status_code(200)
        resp.assert_cssselect('div#hot div.box div.container div h2', expected_value='Hot this week')

    @clear_session({'spanId': 311})
    def test_311_get_(self):
        # GET http://front-end.sock-shop/ (endp 311)
        front_end_sock_shop = get_http_client('http://front-end.sock-shop', authenticate)
        resp = front_end_sock_shop.get('/')
        resp.assert_status_code(200)
        resp.assert_cssselect('div#hot div.box div.container div h2', expected_value='Hot this week')

    @clear_session({'spanId': 312})
    def test_312_get_(self):
        # GET http://front-end.sock-shop/ (endp 312)
        front_end_sock_shop = get_http_client('http://front-end.sock-shop', authenticate)
        resp = front_end_sock_shop.get('/')
        resp.assert_status_code(200)
        resp.assert_cssselect('div#hot div.box div.container div h2', expected_value='Hot this week')

    @clear_session({'spanId': 313})
    def test_313_get_(self):
        # GET http://front-end.sock-shop/ (endp 313)
        front_end_sock_shop = get_http_client('http://front-end.sock-shop', authenticate)
        resp = front_end_sock_shop.get('/')
        resp.assert_status_code(200)
        resp.assert_cssselect('div#hot div.box div.container div h2', expected_value='Hot this week')

    @clear_session({'spanId': 314})
    def test_314_get_(self):
        # GET http://front-end.sock-shop/ (endp 314)
        front_end_sock_shop = get_http_client('http://front-end.sock-shop', authenticate)
        resp = front_end_sock_shop.get('/')
        resp.assert_status_code(200)
        resp.assert_cssselect('div#hot div.box div.container div h2', expected_value='Hot this week')

    @clear_session({'spanId': 316})
    def test_316_get_(self):
        # GET http://front-end.sock-shop/ (endp 316)
        front_end_sock_shop = get_http_client('http://front-end.sock-shop', authenticate)
        resp = front_end_sock_shop.get('/')
        resp.assert_status_code(200)
        resp.assert_cssselect('div#hot div.box div.container div h2', expected_value='Hot this week')

    @clear_session({'spanId': 317})
    def test_317_get_(self):
        # GET http://front-end.sock-shop/ (endp 317)
        front_end_sock_shop = get_http_client('http://front-end.sock-shop', authenticate)
        resp = front_end_sock_shop.get('/')
        resp.assert_status_code(200)
        resp.assert_cssselect('div#hot div.box div.container div h2', expected_value='Hot this week')

    @clear_session({'spanId': 319})
    def test_319_get_(self):
        # GET http://front-end.sock-shop/ (endp 319)
        front_end_sock_shop = get_http_client('http://front-end.sock-shop', authenticate)
        resp = front_end_sock_shop.get('/')
        resp.assert_status_code(200)
        resp.assert_cssselect('div#hot div.box div.container div h2', expected_value='Hot this week')

    @json_dataset('data/55/dataset_55.json')
    @clear_session({'spanId': 55})
    def test_055_get_param(self, data_row):
        param, = data_row

        # GET http://front-end.sock-shop/{param} (endp 55)
        front_end_sock_shop = get_http_client('http://front-end.sock-shop', authenticate)
        resp = front_end_sock_shop.get(f'/{param}', headers={'x-requested-with': 'XMLHttpRequest'})
        resp.assert_status_code(200)
        resp.assert_cssselect('div#top div.container div.offer a.btn.btn-success.btn-sm', expected_value='Offer of the day')

    @json_dataset('data/151/dataset_151.json')
    @clear_session({'spanId': 151})
    def test_151_get_param(self, data_row):
        param, = data_row

        # GET http://front-end.sock-shop/{param} (endp 151)
        front_end_sock_shop = get_http_client('http://front-end.sock-shop', authenticate)
        resp = front_end_sock_shop.get(f'/{param}', headers={'x-requested-with': 'XMLHttpRequest'})
        resp.assert_status_code(200)
        resp.assert_cssselect('div#hot div.box div.container div h2', expected_value='Hot this week')

    @json_dataset('data/208/dataset_208.json')
    @clear_session({'spanId': 208})
    def test_208_get_param1_param2_index_html(self, data_row):
        param, param1 = data_row

        # GET http://front-end.sock-shop/{param1}/{param2}/index.html (endp 208)
        front_end_sock_shop = get_http_client('http://front-end.sock-shop', authenticate)
        resp = front_end_sock_shop.get(f'/{param}/{param1}/index.html')
        resp.assert_status_code(200)
        resp.assert_cssselect('div#hot div.box div.container div h2', expected_value='Hot this week')

    @json_dataset('data/126/dataset_126.json')
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
        resp = front_end_sock_shop.get('/address', headers={'x-requested-with': 'XMLHttpRequest'})
        resp.assert_status_code(200)
        resp.assert_jsonpath('$.city', expected_value='Glasgow')

    @clear_session({'spanId': 168})
    def test_168_get_address(self):
        # GET http://front-end.sock-shop/address (endp 168)
        front_end_sock_shop = get_http_client('http://front-end.sock-shop', authenticate)
        resp = front_end_sock_shop.get('/address', headers={'x-requested-with': 'XMLHttpRequest'})
        resp.assert_status_code(200)

    @json_dataset('data/169/dataset_169.json')
    @clear_session({'spanId': 169})
    def test_169_post_addresses(self, data_row):
        number, postcode = data_row

        # POST http://front-end.sock-shop/addresses (endp 169)
        front_end_sock_shop = get_http_client('http://front-end.sock-shop', authenticate)
        with open('data/169/payload_for_endp_169.json', 'r') as json_payload_file:
            json_payload = json.load(json_payload_file)
        apply_into_json(json_payload, '$.number', number)
        apply_into_json(json_payload, '$.postcode', postcode)
        resp = front_end_sock_shop.post('/addresses', json=json_payload, headers={'x-requested-with': 'XMLHttpRequest'})
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
        resp = front_end_sock_shop.get('/card', headers={'x-requested-with': 'XMLHttpRequest'})
        resp.assert_status_code(200)

    @clear_session({'spanId': 171})
    def test_171_get_card(self):
        # GET http://front-end.sock-shop/card (endp 171)
        front_end_sock_shop = get_http_client('http://front-end.sock-shop', authenticate)
        resp = front_end_sock_shop.get('/card', headers={'x-requested-with': 'XMLHttpRequest'})
        resp.assert_status_code(200)

    @json_dataset('data/172/dataset_172.json')
    @clear_session({'spanId': 172})
    def test_172_post_cards(self, data_row):
        ccv, expires, longNum = data_row

        # POST http://front-end.sock-shop/cards (endp 172)
        front_end_sock_shop = get_http_client('http://front-end.sock-shop', authenticate)
        with open('data/172/payload_for_endp_172.json', 'r') as json_payload_file:
            json_payload = json.load(json_payload_file)
        apply_into_json(json_payload, '$.ccv', ccv)
        apply_into_json(json_payload, '$.expires', expires)
        apply_into_json(json_payload, '$.longNum', longNum)
        resp = front_end_sock_shop.post('/cards', json=json_payload, headers={'x-requested-with': 'XMLHttpRequest'})
        resp.assert_status_code(200)

    @clear_session({'spanId': 16})
    def test_016_post_cart(self):
        # POST http://front-end.sock-shop/orders (endp 21)
        front_end_sock_shop = get_http_client('http://front-end.sock-shop', authenticate)
        resp = front_end_sock_shop.post('/orders', headers={'x-requested-with': 'XMLHttpRequest'})
        resp.assert_status_code(201)
        resp.assert_jsonpath('$.address.city', expected_value='Glasgow')
        id_ = jsonpath('$.items[*].itemId', resp)

        # POST http://front-end.sock-shop/cart (endp 16)
        with open('data/16/payload_for_endp_16.json', 'r') as json_payload_file:
            json_payload = json.load(json_payload_file)
        apply_into_json(json_payload, '$.id', id_)
        resp = front_end_sock_shop.post('/cart', json=json_payload, headers={'x-requested-with': 'XMLHttpRequest'})
        resp.assert_status_code(201)

    @json_dataset('data/33/dataset_33.json')
    @clear_session({'spanId': 33})
    def test_033_post_cart(self, data_row):
        size, tags = data_row

        # GET http://front-end.sock-shop/catalogue (endp 17)
        front_end_sock_shop = get_http_client('http://front-end.sock-shop', authenticate)
        qstr = '?' + urlencode({'page': '1', 'size': size, 'sort': 'id', 'tags': tags})
        resp = front_end_sock_shop.get('/catalogue' + qstr, headers={'x-requested-with': 'XMLHttpRequest'})
        resp.assert_status_code(200)
        id_ = jsonpath('$[*].id', resp)

        # POST http://front-end.sock-shop/cart (endp 33)
        with open('data/33/payload_for_endp_33.json', 'r') as json_payload_file:
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
        resp = front_end_sock_shop.get('/cart', headers={'x-requested-with': 'XMLHttpRequest'})
        resp.assert_status_code(200)

    @clear_session({'spanId': 63})
    def test_063_get_cart(self):
        # GET http://front-end.sock-shop/cart (endp 63)
        front_end_sock_shop = get_http_client('http://front-end.sock-shop', authenticate)
        resp = front_end_sock_shop.get('/cart', headers={'x-requested-with': 'XMLHttpRequest'})
        resp.assert_status_code(200)
        resp.assert_cssselect('div#copyright div.container div p.pull-left a', expected_value='Weaveworks')

    @clear_session({'spanId': 146})
    def test_146_get_cart(self):
        # GET http://front-end.sock-shop/cart (endp 146)
        front_end_sock_shop = get_http_client('http://front-end.sock-shop', authenticate)
        resp = front_end_sock_shop.get('/cart', headers={'x-requested-with': 'XMLHttpRequest'})
        resp.assert_status_code(200)
        resp.assert_jsonpath('$[*].id')

    @clear_session({'spanId': 174})
    def test_174_post_cart(self):
        # GET http://front-end.sock-shop/cart (endp 146)
        front_end_sock_shop = get_http_client('http://front-end.sock-shop', authenticate)
        resp = front_end_sock_shop.get('/cart', headers={'x-requested-with': 'XMLHttpRequest'})
        resp.assert_status_code(200)
        resp.assert_jsonpath('$[*].id')
        id_ = jsonpath('$[*].itemId', resp)

        # POST http://front-end.sock-shop/cart (endp 174)
        with open('data/174/payload_for_endp_174.json', 'r') as json_payload_file:
            json_payload = json.load(json_payload_file)
        apply_into_json(json_payload, '$.id', id_)
        resp = front_end_sock_shop.post('/cart', json=json_payload, headers={'x-requested-with': 'XMLHttpRequest'})
        resp.assert_status_code(201)

    @clear_session({'spanId': 175})
    def test_175_delete_cart(self):
        # DELETE http://front-end.sock-shop/cart (endp 175)
        front_end_sock_shop = get_http_client('http://front-end.sock-shop', authenticate)
        resp = front_end_sock_shop.delete('/cart', headers={'x-requested-with': 'XMLHttpRequest'})
        resp.assert_status_code(202)

    @clear_session({'spanId': 286})
    def test_286_delete_cart(self):
        # DELETE http://front-end.sock-shop/cart (endp 286)
        front_end_sock_shop = get_http_client('http://front-end.sock-shop', authenticate)
        resp = front_end_sock_shop.delete('/cart', headers={'x-requested-with': 'XMLHttpRequest'})
        resp.assert_status_code(202)

    @json_dataset('data/17/dataset_17.json')
    @clear_session({'spanId': 17})
    def test_017_get_catalogue(self, data_row):
        size, tags = data_row

        # GET http://front-end.sock-shop/catalogue (endp 17)
        front_end_sock_shop = get_http_client('http://front-end.sock-shop', authenticate)
        qstr = '?' + urlencode({'page': '1', 'size': size, 'sort': 'id', 'tags': tags})
        resp = front_end_sock_shop.get('/catalogue' + qstr, headers={'x-requested-with': 'XMLHttpRequest'})
        resp.assert_status_code(200)

    @clear_session({'spanId': 46})
    def test_046_get_catalogue(self):
        # GET http://front-end.sock-shop/catalogue (endp 46)
        front_end_sock_shop = get_http_client('http://front-end.sock-shop', authenticate)
        resp = front_end_sock_shop.get('/catalogue')
        resp.assert_status_code(201)
        resp.assert_jsonpath('$.address.city', expected_value='Glasgow')

    @json_dataset('data/65/dataset_65.json')
    @clear_session({'spanId': 65})
    def test_065_get_catalogue(self, data_row):
        size, = data_row

        # GET http://front-end.sock-shop/catalogue (endp 65)
        front_end_sock_shop = get_http_client('http://front-end.sock-shop', authenticate)
        qstr = '?' + urlencode({'size': size})
        resp = front_end_sock_shop.get('/catalogue' + qstr, headers={'x-requested-with': 'XMLHttpRequest'})
        resp.assert_status_code(200)

    @json_dataset('data/121/dataset_121.json')
    @clear_session({'spanId': 121})
    def test_121_get_catalogue(self, data_row):
        size, = data_row

        # GET http://front-end.sock-shop/catalogue (endp 121)
        front_end_sock_shop = get_http_client('http://front-end.sock-shop', authenticate)
        qstr = '?' + urlencode({'page': '1', 'size': size, 'tags': 'large'})
        resp = front_end_sock_shop.get('/catalogue' + qstr, headers={'x-requested-with': 'XMLHttpRequest'})
        resp.assert_status_code(200)

    @json_dataset('data/147/dataset_147.json')
    @clear_session({'spanId': 147})
    def test_147_get_catalogue(self, data_row):
        page, size, tags = data_row

        # GET http://front-end.sock-shop/catalogue (endp 147)
        front_end_sock_shop = get_http_client('http://front-end.sock-shop', authenticate)
        qstr = '?' + urlencode({'page': page, 'size': size, 'sort': 'id', 'tags': tags})
        resp = front_end_sock_shop.get('/catalogue' + qstr, headers={'x-requested-with': 'XMLHttpRequest'})
        resp.assert_status_code(200)
        resp.assert_jsonpath('$[*].tag[*]')

    @json_dataset('data/48/dataset_48.json')
    @clear_session({'spanId': 48})
    def test_048_get_catalogue_id(self, data_row):
        page, size, tags = data_row

        # GET http://front-end.sock-shop/catalogue (endp 147)
        front_end_sock_shop = get_http_client('http://front-end.sock-shop', authenticate)
        qstr = '?' + urlencode({'page': page, 'size': size, 'sort': 'id', 'tags': tags})
        resp = front_end_sock_shop.get('/catalogue' + qstr, headers={'x-requested-with': 'XMLHttpRequest'})
        resp.assert_status_code(200)
        resp.assert_jsonpath('$[*].tag[*]')
        id_ = jsonpath('$[*].id', resp)

        # GET http://front-end.sock-shop/catalogue/{id} (endp 48)
        resp = front_end_sock_shop.get(f'/catalogue/{id_}', headers={'x-requested-with': 'XMLHttpRequest'})
        resp.assert_status_code(200)

    @json_dataset('data/166/dataset_166.json')
    @clear_session({'spanId': 166})
    def test_166_get_catalogue_id(self, data_row):
        page, size, tags = data_row

        # GET http://front-end.sock-shop/catalogue (endp 147)
        front_end_sock_shop = get_http_client('http://front-end.sock-shop', authenticate)
        qstr = '?' + urlencode({'page': page, 'size': size, 'sort': 'id', 'tags': tags})
        resp = front_end_sock_shop.get('/catalogue' + qstr, headers={'x-requested-with': 'XMLHttpRequest'})
        resp.assert_status_code(200)
        resp.assert_jsonpath('$[*].tag[*]')
        id_ = jsonpath('$[*].id', resp)

        # GET http://front-end.sock-shop/catalogue/{id} (endp 166)
        resp = front_end_sock_shop.get(f'/catalogue/{id_}', headers={'x-requested-with': 'XMLHttpRequest'})
        resp.assert_status_code(200)

    @clear_session({'spanId': 75})
    def test_075_get_catalogue_size(self):
        # GET http://front-end.sock-shop/tags (endp 83)
        front_end_sock_shop = get_http_client('http://front-end.sock-shop', authenticate)
        resp = front_end_sock_shop.get('/tags', headers={'x-requested-with': 'XMLHttpRequest'})
        resp.assert_status_code(200)
        tags = jsonpath('$.tags[*]', resp)

        # GET http://front-end.sock-shop/catalogue/size (endp 75)
        qstr = '?' + urlencode({'tags': tags})
        resp = front_end_sock_shop.get('/catalogue/size' + qstr, headers={'x-requested-with': 'XMLHttpRequest'})
        resp.assert_status_code(200)

    @clear_session({'spanId': 177})
    def test_177_get_catalogue_size(self):
        # GET http://front-end.sock-shop/catalogue/size (endp 177)
        front_end_sock_shop = get_http_client('http://front-end.sock-shop', authenticate)
        qstr = '?' + urlencode({'tags': ''})
        resp = front_end_sock_shop.get('/catalogue/size' + qstr, headers={'x-requested-with': 'XMLHttpRequest'})
        resp.assert_status_code(200)

    @json_dataset('data/18/dataset_18.json')
    @clear_session({'spanId': 18})
    def test_018_get_category_html(self, data_row):
        tags, = data_row

        # GET http://front-end.sock-shop/category.html (endp 18)
        front_end_sock_shop = get_http_client('http://front-end.sock-shop', authenticate)
        qstr = '?' + urlencode({'tags': tags})
        resp = front_end_sock_shop.get('/category.html' + qstr)
        resp.assert_status_code(200)
        resp.assert_cssselect('div#content div.container div div.row.same-height-row div div.box.same-height h3', expected_value='You may also like these products')

    @clear_session({'spanId': 179})
    def test_179_get_category_html(self):
        # GET http://front-end.sock-shop/category.html (endp 179)
        front_end_sock_shop = get_http_client('http://front-end.sock-shop', authenticate)
        qstr = '?' + urlencode({'page': '2'})
        resp = front_end_sock_shop.get('/category.html' + qstr)
        resp.assert_status_code(200)
        resp.assert_cssselect('div#content div.container div div.panel.panel-default.sidebar-menu div.panel-heading h3.panel-title', expected_value='Filters ')

    @json_dataset('data/77/dataset_77.json')
    @clear_session({'spanId': 77})
    def test_077_get_customer_order_html(self, data_row):
        order, = data_row

        # GET http://front-end.sock-shop/customer-order.html (endp 77)
        front_end_sock_shop = get_http_client('http://front-end.sock-shop', authenticate)
        qstr = '?' + urlencode({'order': order})
        resp = front_end_sock_shop.get('/customer-order.html' + qstr)
        resp.assert_status_code(200)
        resp.assert_cssselect('div#customer-order div.box h2', expected_value='Order #')

    @json_dataset('data/180/dataset_180.json')
    @clear_session({'spanId': 180})
    def test_180_get_customer_order_html(self, data_row):
        order, = data_row

        # GET http://front-end.sock-shop/customer-order.html (endp 180)
        front_end_sock_shop = get_http_client('http://front-end.sock-shop', authenticate)
        qstr = '?' + urlencode({'order': order})
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
        resp = front_end_sock_shop.get(f"/customers/{str(get_data_from_cookie('logged_in'))}", headers={'x-requested-with': 'XMLHttpRequest'})
        resp.assert_status_code(200)

    @clear_session({'spanId': 148})
    def test_148_get_customers_customerId(self):
        # GET http://front-end.sock-shop/customers/{customerId} (endp 148)
        front_end_sock_shop = get_http_client('http://front-end.sock-shop', authenticate)
        resp = front_end_sock_shop.get(f"/customers/{str(get_data_from_cookie('logged_in'))}", headers={'x-requested-with': 'XMLHttpRequest'})
        resp.assert_status_code(200)

    @clear_session({'spanId': 163})
    def test_163_get_customers_wcbVLjJnpzpezACrWupvwuuQUEpXSBhZ(self):
        # GET http://front-end.sock-shop/customers/wcbVLjJnpzpezACrWupvwuuQUEpXSBhZ (endp 163)
        front_end_sock_shop = get_http_client('http://front-end.sock-shop', authenticate)
        resp = front_end_sock_shop.get('/customers/wcbVLjJnpzpezACrWupvwuuQUEpXSBhZ', headers={'x-requested-with': 'XMLHttpRequest'})
        resp.assert_status_code(200)
        resp.assert_jsonpath('$.lastName', expected_value='Name')

    @clear_session({'spanId': 19})
    def test_019_get_detail_html(self):
        # POST http://front-end.sock-shop/orders (endp 21)
        front_end_sock_shop = get_http_client('http://front-end.sock-shop', authenticate)
        resp = front_end_sock_shop.post('/orders', headers={'x-requested-with': 'XMLHttpRequest'})
        resp.assert_status_code(201)
        resp.assert_jsonpath('$.address.city', expected_value='Glasgow')
        id_ = jsonpath('$.items[*].itemId', resp)

        # GET http://front-end.sock-shop/detail.html (endp 19)
        qstr = '?' + urlencode({'id': id_})
        resp = front_end_sock_shop.get('/detail.html' + qstr)
        resp.assert_status_code(200)
        resp.assert_cssselect('div#content div.container div div.row.same-height-row div div.box.same-height h3', expected_value='You may also like these products')

    @json_dataset('data/183/dataset_183.json')
    @clear_session({'spanId': 183})
    def test_183_get_detail_html(self, data_row):
        page, size, tags = data_row

        # GET http://front-end.sock-shop/catalogue (endp 147)
        front_end_sock_shop = get_http_client('http://front-end.sock-shop', authenticate)
        qstr = '?' + urlencode({'page': page, 'size': size, 'sort': 'id', 'tags': tags})
        resp = front_end_sock_shop.get('/catalogue' + qstr, headers={'x-requested-with': 'XMLHttpRequest'})
        resp.assert_status_code(200)
        resp.assert_jsonpath('$[*].tag[*]')
        id_ = jsonpath('$[*].id', resp)

        # GET http://front-end.sock-shop/detail.html (endp 183)
        qstr = '?' + urlencode({'id': id_})
        resp = front_end_sock_shop.get('/detail.html' + qstr)
        resp.assert_status_code(200)
        resp.assert_cssselect('div#content div.container div div.row.same-height-row div div.box.same-height h3', expected_value='You may also like these products')

    @clear_session({'spanId': 54})
    def test_054_get_footer_html(self):
        # GET http://front-end.sock-shop/footer.html (endp 54)
        front_end_sock_shop = get_http_client('http://front-end.sock-shop', authenticate)
        resp = front_end_sock_shop.get('/footer.html', headers={'x-requested-with': 'XMLHttpRequest'})
        resp.assert_status_code(200)
        resp.assert_cssselect('div#copyright div.container div p.pull-left a', expected_value='Weaveworks')

    @clear_session({'spanId': 101})
    def test_101_get_footer_html(self):
        # GET http://front-end.sock-shop/footer.html (endp 101)
        front_end_sock_shop = get_http_client('http://front-end.sock-shop', authenticate)
        resp = front_end_sock_shop.get('/footer.html', headers={'x-requested-with': 'XMLHttpRequest'})
        resp.assert_status_code(200)

    @clear_session({'spanId': 149})
    def test_149_get_footer_html(self):
        # GET http://front-end.sock-shop/footer.html (endp 149)
        front_end_sock_shop = get_http_client('http://front-end.sock-shop', authenticate)
        resp = front_end_sock_shop.get('/footer.html', headers={'x-requested-with': 'XMLHttpRequest'})
        resp.assert_status_code(200)
        resp.assert_cssselect('div#copyright div.container div p.pull-left a', expected_value='Weaveworks')

    @json_dataset('data/61/dataset_61.json')
    @clear_session({'spanId': 61})
    def test_061_get_index_html(self, data_row):
        urlmaskfilter, = data_row

        # GET http://front-end.sock-shop/index.html (endp 61)
        front_end_sock_shop = get_http_client('http://front-end.sock-shop', authenticate)
        qstr = '?' + urlencode({'urlmaskfilter': urlmaskfilter})
        resp = front_end_sock_shop.get('/index.html' + qstr)
        resp.assert_status_code(200)
        resp.assert_cssselect('div#hot div.box div.container div h2', expected_value='Hot this week')

    @json_dataset('data/184/dataset_184.json')
    @clear_session({'spanId': 184})
    def test_184_get_index_html(self, data_row):
        findcli, = data_row

        # GET http://front-end.sock-shop/index.html (endp 184)
        front_end_sock_shop = get_http_client('http://front-end.sock-shop', authenticate)
        qstr = '?' + urlencode({'findcli': findcli, 'test': ''})
        resp = front_end_sock_shop.get('/index.html' + qstr)
        resp.assert_status_code(200)
        resp.assert_cssselect('div#hot div.box div.container div h2', expected_value='Hot this week')

    @clear_session({'spanId': 210})
    def test_210_head_index_html(self):
        # HEAD http://front-end.sock-shop/index.html (endp 210)
        front_end_sock_shop = get_http_client('http://front-end.sock-shop', authenticate)
        resp = front_end_sock_shop.head('/index.html')
        resp.assert_status_code(200)

    @json_dataset('data/95/dataset_95.json')
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
        resp = front_end_sock_shop.get('/login', headers={'x-requested-with': 'XMLHttpRequest'})
        resp.assert_status_code(200)
        resp.assert_cssselect('div#hot div.box div.container div h2', expected_value='Hot this week')

    # authentication-related test
    @clear_session({'spanId': 150})
    def test_150_get_login(self):
        # GET http://front-end.sock-shop/login (endp 150)
        front_end_sock_shop = get_http_client('http://front-end.sock-shop', dummy_auth)
        resp = front_end_sock_shop.get('/login', headers={'x-requested-with': 'XMLHttpRequest'})
        resp.assert_status_code(200)
        resp.assert_cssselect('p', expected_value='Cookie is set')

    @clear_session({'spanId': 215})
    def test_215_get_metrics(self):
        # GET http://front-end.sock-shop/metrics (endp 215)
        front_end_sock_shop = get_http_client('http://front-end.sock-shop', authenticate)
        resp = front_end_sock_shop.get('/metrics')
        resp.assert_status_code(200)

    @clear_session({'spanId': 21})
    def test_021_post_orders(self):
        # POST http://front-end.sock-shop/orders (endp 21)
        front_end_sock_shop = get_http_client('http://front-end.sock-shop', authenticate)
        resp = front_end_sock_shop.post('/orders', headers={'x-requested-with': 'XMLHttpRequest'})
        resp.assert_status_code(201)
        resp.assert_jsonpath('$.address.city', expected_value='Glasgow')

    @clear_session({'spanId': 22})
    def test_022_post_orders(self):
        # POST http://front-end.sock-shop/orders (endp 22)
        front_end_sock_shop = get_http_client('http://front-end.sock-shop', authenticate)
        resp = front_end_sock_shop.post('/orders')
        resp.assert_status_code(200)
        resp.assert_cssselect('div#hot div.box div.container div h2', expected_value='Hot this week')

    @clear_session({'spanId': 80})
    def test_080_get_orders(self):
        # GET http://front-end.sock-shop/orders (endp 80)
        front_end_sock_shop = get_http_client('http://front-end.sock-shop', authenticate)
        resp = front_end_sock_shop.get('/orders', headers={'x-requested-with': 'XMLHttpRequest'})
        resp.assert_status_code(201)
        resp.assert_jsonpath('$.[*].address.city', expected_value='Glasgow')

    @clear_session({'spanId': 186})
    def test_186_get_orders(self):
        # GET http://front-end.sock-shop/orders (endp 186)
        front_end_sock_shop = get_http_client('http://front-end.sock-shop', authenticate)
        resp = front_end_sock_shop.get('/orders', headers={'x-requested-with': 'XMLHttpRequest'})
        resp.assert_status_code(201)
        resp.assert_jsonpath('$[*].address.city', expected_value='elsewhere')

    @clear_session({'spanId': 187})
    def test_187_post_orders(self):
        # POST http://front-end.sock-shop/orders (endp 187)
        front_end_sock_shop = get_http_client('http://front-end.sock-shop', authenticate)
        resp = front_end_sock_shop.post('/orders', headers={'x-requested-with': 'XMLHttpRequest'})
        resp.assert_status_code(201)
        resp.assert_jsonpath('$.card.ccv')

    @clear_session({'spanId': 82})
    def test_082_get_orders_id(self):
        # GET http://front-end.sock-shop/orders (endp 80)
        front_end_sock_shop = get_http_client('http://front-end.sock-shop', authenticate)
        resp = front_end_sock_shop.get('/orders', headers={'x-requested-with': 'XMLHttpRequest'})
        resp.assert_status_code(201)
        resp.assert_jsonpath('$.[*].address.city', expected_value='Glasgow')
        id_ = url_part('/2', jsonpath('$[*]._links.self.href', resp))

        # GET http://front-end.sock-shop/orders/{id} (endp 82)
        resp = front_end_sock_shop.get(f'/orders/{id_}', headers={'x-requested-with': 'XMLHttpRequest'})
        resp.assert_status_code(200)
        resp.assert_jsonpath('$.address.city', expected_value='Glasgow')

    @clear_session({'spanId': 188})
    def test_188_get_orders_id(self):
        # GET http://front-end.sock-shop/orders (endp 80)
        front_end_sock_shop = get_http_client('http://front-end.sock-shop', authenticate)
        resp = front_end_sock_shop.get('/orders', headers={'x-requested-with': 'XMLHttpRequest'})
        resp.assert_status_code(201)
        resp.assert_jsonpath('$.[*].address.city', expected_value='Glasgow')
        id_ = url_part('/2', jsonpath('$[*]._links.self.href', resp))

        # GET http://front-end.sock-shop/orders/{id} (endp 188)
        resp = front_end_sock_shop.get(f'/orders/{id_}', headers={'x-requested-with': 'XMLHttpRequest'})
        resp.assert_status_code(200)
        resp.assert_jsonpath('$.address.city', expected_value='elsewhere')

    @json_dataset('data/102/dataset_102.json')
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
    @json_dataset('data/189/dataset_189.json')
    @clear_session({'spanId': 189})
    def test_189_post_register(self, data_row):
        email_, firstName, lastName, password, username = data_row

        # POST http://front-end.sock-shop/register (endp 189)
        front_end_sock_shop = get_http_client('http://front-end.sock-shop', dummy_auth)
        with open('data/189/payload_for_endp_189.json', 'r') as json_payload_file:
            json_payload = json.load(json_payload_file)
        apply_into_json(json_payload, '$.email', email_)
        apply_into_json(json_payload, '$.firstName', firstName)
        apply_into_json(json_payload, '$.lastName', lastName)
        apply_into_json(json_payload, '$.password', password)
        apply_into_json(json_payload, '$.username', username)
        resp = front_end_sock_shop.post('/register', json=json_payload, headers={'x-requested-with': 'XMLHttpRequest'})
        resp.assert_status_code(200)

    @clear_session({'spanId': 83})
    def test_083_get_tags(self):
        # GET http://front-end.sock-shop/tags (endp 83)
        front_end_sock_shop = get_http_client('http://front-end.sock-shop', authenticate)
        resp = front_end_sock_shop.get('/tags', headers={'x-requested-with': 'XMLHttpRequest'})
        resp.assert_status_code(200)

    @clear_session({'spanId': 190})
    def test_190_get_tags(self):
        # GET http://front-end.sock-shop/tags (endp 190)
        front_end_sock_shop = get_http_client('http://front-end.sock-shop', authenticate)
        resp = front_end_sock_shop.get('/tags', headers={'x-requested-with': 'XMLHttpRequest'})
        resp.assert_status_code(200)

    @clear_session({'spanId': 56})
    def test_056_get_topbar_html(self):
        # GET http://front-end.sock-shop/topbar.html (endp 56)
        front_end_sock_shop = get_http_client('http://front-end.sock-shop', authenticate)
        resp = front_end_sock_shop.get('/topbar.html', headers={'x-requested-with': 'XMLHttpRequest'})
        resp.assert_status_code(200)
        resp.assert_cssselect('div#hot div.box div.container div h2', expected_value='Hot this week')

    @clear_session({'spanId': 152})
    def test_152_get_topbar_html(self):
        # GET http://front-end.sock-shop/topbar.html (endp 152)
        front_end_sock_shop = get_http_client('http://front-end.sock-shop', authenticate)
        resp = front_end_sock_shop.get('/topbar.html', headers={'x-requested-with': 'XMLHttpRequest'})
        resp.assert_status_code(200)
        resp.assert_cssselect('div#top div.container div.offer a.btn.btn-success', expected_value='Offer of the day')

    @clear_session({'spanId': 289})
    def test_289_get_wp_includes_wlwmanifest_xml(self):
        # GET http://front-end.sock-shop/wp-includes/wlwmanifest.xml (endp 289)
        front_end_sock_shop = get_http_client('http://front-end.sock-shop', authenticate)
        resp = front_end_sock_shop.get('/wp-includes/wlwmanifest.xml')
        resp.assert_status_code(200)
        resp.assert_cssselect('div#hot div.box div.container div h2', expected_value='Hot this week')
