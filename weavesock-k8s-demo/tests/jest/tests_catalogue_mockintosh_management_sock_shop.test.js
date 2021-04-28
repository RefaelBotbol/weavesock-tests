const authenticate = require("./authentication");
const {clearSession, dataset, getHttpClient, urlencode} = require("./up9lib");

describe.each(dataset("data/dataset_287.json"))("test_287_get_catalogue", (size) => {
    it("test_287_get_catalogue", () => {
        clearSession();

        // GET http://catalogue-mockintosh-management.sock-shop/catalogue (endp 287)
        const catalogue_mockintosh_management_sock_shop = getHttpClient("http://catalogue-mockintosh-management.sock-shop", authenticate);
        return catalogue_mockintosh_management_sock_shop.fetch("/catalogue" + urlencode([["size", size]]))
        .then((response) => {
            expect(response.status).toEqual(200);
            return response.text();
        })
        .then((text) => {
        })
        .then((data) => {
        });
    });
});
