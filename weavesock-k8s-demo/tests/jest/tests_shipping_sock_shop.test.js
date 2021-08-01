const authenticate = require("./authentication");
const {JSONBuild, JSONPath, clearSession, dataset, getHttpClient, uuidv4} = require("./up9lib");

describe.each(dataset("data/dataset_25.json"))("test_025_post_shipping", (id) => {
    it("test_025_post_shipping", () => {
        clearSession();

        // GET http://user.sock-shop/cards/{id} (endp 24)
        const user_sock_shop = getHttpClient("http://user.sock-shop", authenticate);
        return user_sock_shop.fetch("/cards/" + id, {
            headers: {
                "accept": "application/hal+json"
            }
        })
        .then((response) => {
            expect(response.status).toEqual(200);
            return response.text();
        })
        .then((text) => {
            return JSON.parse(text);
        })
        .then((data) => {
            expect(JSONPath({
                path: "$.city",
                json: data
            })).toContain("Glasgow");
            const name = JSONPath({
                path: "$.id",
                json: data
            })[0];

            // POST http://shipping.sock-shop/shipping (endp 25)
            const shipping_sock_shop = getHttpClient("http://shipping.sock-shop", authenticate);
            return shipping_sock_shop.fetch("/shipping", {
                method: "POST",
                headers: {
                    "accept": "application/json",
                    "content-type": "application/json"
                },
                body: JSONBuild("data/payload_for_endp_25.json", {
                    "$.id": String(uuidv4()),
                    "$.name": name
                })
            })
            .then((response) => {
                expect(response.status).toEqual(201);
                return response.text();
            })
            .then((text) => {
            })
            .then((data) => {
            });
        });
    });
});

describe.each(dataset("data/dataset_144.json"))("test_144_post_shipping", (name) => {
    it("test_144_post_shipping", () => {
        clearSession();

        // POST http://shipping.sock-shop/shipping (endp 144)
        const shipping_sock_shop = getHttpClient("http://shipping.sock-shop", authenticate);
        return shipping_sock_shop.fetch("/shipping", {
            method: "POST",
            headers: {
                "accept": "application/json",
                "content-type": "application/json"
            },
            body: JSONBuild("data/payload_for_endp_144.json", {
                "$.id": String(uuidv4()),
                "$.name": name
            })
        })
        .then((response) => {
            expect(response.status).toEqual(201);
            return response.text();
        })
        .then((text) => {
            return JSON.parse(text);
        })
        .then((data) => {
            expect(JSONPath({
                path: "$.id",
                json: data
            })).not.toBeNull();
        });
    });
});
