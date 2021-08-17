from up9lib import *
from authentication import authenticate

# logging.basicConfig(level=logging.DEBUG)


@data_driven_tests
class Tests_catalogue_sock_shop(unittest.TestCase):

    @json_dataset('data/1/dataset_1.json')
    @clear_session({'spanId': 1})
    def test_001_get_catalogue(self, data_row):
        size, tags = data_row

        # GET http://catalogue.sock-shop/catalogue (endp 1)
        catalogue_sock_shop = get_http_client('http://catalogue.sock-shop', authenticate)
        qstr = '?' + urlencode({'page': '1', 'size': size, 'sort': 'id', 'tags': tags})
        resp = catalogue_sock_shop.get('/catalogue' + qstr)
        resp.assert_status_code(200)

    @json_dataset('data/137/dataset_137.json')
    @clear_session({'spanId': 137})
    def test_137_get_catalogue(self, data_row):
        page, size, tags = data_row

        # GET http://catalogue.sock-shop/catalogue (endp 137)
        catalogue_sock_shop = get_http_client('http://catalogue.sock-shop', authenticate)
        qstr = '?' + urlencode({'page': page, 'size': size, 'sort': 'id', 'tags': tags})
        resp = catalogue_sock_shop.get('/catalogue' + qstr)
        resp.assert_status_code(200)
        resp.assert_jsonpath('$[*].tag[*]')

    @json_dataset('data/2/dataset_2.json')
    @clear_session({'spanId': 2})
    def test_002_get_catalogue_id(self, data_row):
        size, tags = data_row

        # GET http://catalogue.sock-shop/catalogue (endp 1)
        catalogue_sock_shop = get_http_client('http://catalogue.sock-shop', authenticate)
        qstr = '?' + urlencode({'page': '1', 'size': size, 'sort': 'id', 'tags': tags})
        resp = catalogue_sock_shop.get('/catalogue' + qstr)
        resp.assert_status_code(200)
        id_ = jsonpath('$[*].id', resp)

        # GET http://catalogue.sock-shop/catalogue/{id} (endp 2)
        resp = catalogue_sock_shop.get(f'/catalogue/{id_}')
        resp.assert_status_code(200)

    @json_dataset('data/135/dataset_135.json')
    @clear_session({'spanId': 135})
    def test_135_get_catalogue_id(self, data_row):
        size, tags = data_row

        # GET http://catalogue.sock-shop/catalogue (endp 1)
        catalogue_sock_shop = get_http_client('http://catalogue.sock-shop', authenticate)
        qstr = '?' + urlencode({'page': '1', 'size': size, 'sort': 'id', 'tags': tags})
        resp = catalogue_sock_shop.get('/catalogue' + qstr)
        resp.assert_status_code(200)
        id_ = jsonpath('$[*].id', resp)

        # GET http://catalogue.sock-shop/catalogue/{id} (endp 135)
        resp = catalogue_sock_shop.get(f'/catalogue/{id_}')
        resp.assert_status_code(200)
        resp.assert_jsonpath('$.tag[*]')

    @clear_session({'spanId': 85})
    def test_085_get_catalogue_size(self):
        # GET http://catalogue.sock-shop/tags (endp 87)
        catalogue_sock_shop = get_http_client('http://catalogue.sock-shop', authenticate)
        resp = catalogue_sock_shop.get('/tags')
        resp.assert_status_code(200)
        tags = jsonpath('$.tags[*]', resp)

        # GET http://catalogue.sock-shop/catalogue/size (endp 85)
        qstr = '?' + urlencode({'tags': tags})
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
        qstr = '?' + urlencode({'tags': tags})
        resp = catalogue_sock_shop.get('/catalogue/size' + qstr)
        resp.assert_status_code(200)

    @clear_session({'spanId': 87})
    def test_087_get_tags(self):
        # GET http://catalogue.sock-shop/tags (endp 87)
        catalogue_sock_shop = get_http_client('http://catalogue.sock-shop', authenticate)
        resp = catalogue_sock_shop.get('/tags')
        resp.assert_status_code(200)

    @clear_session({'spanId': 138})
    def test_138_get_tags(self):
        # GET http://catalogue.sock-shop/tags (endp 138)
        catalogue_sock_shop = get_http_client('http://catalogue.sock-shop', authenticate)
        resp = catalogue_sock_shop.get('/tags')
        resp.assert_status_code(200)
