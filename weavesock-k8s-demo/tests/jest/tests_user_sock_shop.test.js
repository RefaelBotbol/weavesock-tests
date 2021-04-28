const authenticate = require("./authentication");
const {JSONBuild, JSONPath, clearSession, dataset, getHttpClient} = require("./up9lib");

describe.each(dataset("data/dataset_191.json"))("test_191_post_addresses", (city, country, number, postcode, street, userID) => {
    it("test_191_post_addresses", () => {
        clearSession();

        // POST http://user.sock-shop/addresses (endp 191)
        const user_sock_shop = getHttpClient("http://user.sock-shop", authenticate);
        return user_sock_shop.fetch("/addresses", {
            method: "POST",
            headers: {
                "accept": "application/json",
                "content-type": "application/json"
            },
            body: JSONBuild("data/payload_for_endp_191.json", {
                "$.city": city,
                "$.country": country,
                "$.number": number,
                "$.postcode": postcode,
                "$.street": street,
                "$.userID": userID
            })
        })
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

describe.each(dataset("data/dataset_192.json"))("test_192_post_cards", (ccv, expires, longNum, userID) => {
    it("test_192_post_cards", () => {
        clearSession();

        // POST http://user.sock-shop/cards (endp 192)
        const user_sock_shop = getHttpClient("http://user.sock-shop", authenticate);
        return user_sock_shop.fetch("/cards", {
            method: "POST",
            headers: {
                "accept": "application/json",
                "content-type": "application/json"
            },
            body: JSONBuild("data/payload_for_endp_192.json", {
                "$.ccv": ccv,
                "$.expires": expires,
                "$.longNum": longNum,
                "$.userID": userID
            })
        })
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

describe.each(dataset("data/dataset_4.json"))("test_004_get_customers_customerId_addresses", (address, card, customer, items) => {
    it("test_004_get_customers_customerId_addresses", () => {
        clearSession();

        // POST http://orders.sock-shop/orders (endp 10)
        const orders_sock_shop = getHttpClient("http://orders.sock-shop", authenticate);
        return orders_sock_shop.fetch("/orders", {
            method: "POST",
            headers: {
                "accept": "application/json",
                "content-type": "application/json"
            },
            body: JSONBuild("data/payload_for_endp_10.json", {
                "$.address": address,
                "$.card": card,
                "$.customer": customer,
                "$.items": items
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
                path: "$.address.city",
                json: data
            })).toContain("Glasgow");
            const customerId = JSONPath({
                path: "$.customerId",
                json: data
            })[0];

            // GET http://user.sock-shop/customers/{customerId}/addresses (endp 4)
            const user_sock_shop = getHttpClient("http://user.sock-shop", authenticate);
            return user_sock_shop.fetch("/customers/" + customerId + "/addresses")
            .then((response) => {
                expect(response.status).toEqual(200);
                return response.text();
            })
            .then((text) => {
                return JSON.parse(text);
            })
            .then((data) => {
                expect(JSONPath({
                    path: "$._embedded.address.[*].country",
                    json: data
                })).toContain("United Kingdom");
            });
        });
    });
});

describe.each(dataset("data/dataset_5.json"))("test_005_get_customers_customerId_cards", (address, card, customer, items) => {
    it("test_005_get_customers_customerId_cards", () => {
        clearSession();

        // POST http://orders.sock-shop/orders (endp 10)
        const orders_sock_shop = getHttpClient("http://orders.sock-shop", authenticate);
        return orders_sock_shop.fetch("/orders", {
            method: "POST",
            headers: {
                "accept": "application/json",
                "content-type": "application/json"
            },
            body: JSONBuild("data/payload_for_endp_10.json", {
                "$.address": address,
                "$.card": card,
                "$.customer": customer,
                "$.items": items
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
                path: "$.address.city",
                json: data
            })).toContain("Glasgow");
            const customerId = JSONPath({
                path: "$.customerId",
                json: data
            })[0];

            // GET http://user.sock-shop/customers/{customerId}/cards (endp 5)
            const user_sock_shop = getHttpClient("http://user.sock-shop", authenticate);
            return user_sock_shop.fetch("/customers/" + customerId + "/cards")
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
});

// authentication-related test
it("test_006_get_login", () => {
    clearSession();

    // GET http://user.sock-shop/login (endp 6)
    const user_sock_shop = getHttpClient("http://user.sock-shop");
    return user_sock_shop.fetch("/login")
    .then((response) => {
        expect(response.status).toEqual(200);
        return response.text();
    })
    .then((text) => {
    })
    .then((data) => {
    });
});

// authentication-related test
it("test_130_get_login", () => {
    clearSession();

    // GET http://user.sock-shop/login (endp 130)
    const user_sock_shop = getHttpClient("http://user.sock-shop");
    return user_sock_shop.fetch("/login")
    .then((response) => {
        expect(response.status).toEqual(200);
        return response.text();
    })
    .then((text) => {
    })
    .then((data) => {
    });
});

// authentication-related test
describe.each(dataset("data/dataset_197.json"))("test_197_post_register", (email, firstName, lastName, password, username) => {
    it("test_197_post_register", () => {
        clearSession();

        // POST http://user.sock-shop/register (endp 197)
        const user_sock_shop = getHttpClient("http://user.sock-shop");
        return user_sock_shop.fetch("/register", {
            method: "POST",
            headers: {
                "accept": "application/json",
                "content-type": "application/json"
            },
            body: JSONBuild("data/payload_for_endp_197.json", {
                "$.email": email,
                "$.firstName": firstName,
                "$.lastName": lastName,
                "$.password": password,
                "$.username": username
            })
        })
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
