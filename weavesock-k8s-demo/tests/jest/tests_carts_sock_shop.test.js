const authenticate = require("./authentication");
const {JSONBuild, JSONPath, clearSession, dataset, getHttpClient, urlencode} = require("./up9lib");

describe.each(dataset("data/dataset_7.json"))("test_007_delete_carts_customerId", (address, card, customer, items) => {
    it("test_007_delete_carts_customerId", () => {
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

            // DELETE http://carts.sock-shop/carts/{customerId} (endp 7)
            const carts_sock_shop = getHttpClient("http://carts.sock-shop", authenticate);
            return carts_sock_shop.fetch("/carts/" + customerId, {
                method: "DELETE"
            })
            .then((response) => {
                expect(response.status).toEqual(202);
                return response.text();
            })
            .then((text) => {
            })
            .then((data) => {
            });
        });
    });
});

describe.each(dataset("data/dataset_139.json"))("test_139_delete_carts_customerId", (address, card, customer, items) => {
    it("test_139_delete_carts_customerId", () => {
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

            // DELETE http://carts.sock-shop/carts/{customerId} (endp 139)
            const carts_sock_shop = getHttpClient("http://carts.sock-shop", authenticate);
            return carts_sock_shop.fetch("/carts/" + customerId, {
                method: "DELETE"
            })
            .then((response) => {
                expect(response.status).toEqual(202);
                return response.text();
            })
            .then((text) => {
            })
            .then((data) => {
            });
        });
    });
});

describe.each(dataset("data/dataset_8.json"))("test_008_post_carts_customerId_items", (address, card, customer, items) => {
    it("test_008_post_carts_customerId_items", () => {
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
            const itemId = JSONPath({
                path: "$.items[*].itemId",
                json: data
            })[0];
            const unitPrice = JSONPath({
                path: "$.items[*].unitPrice",
                json: data
            })[0];
            const customerId = JSONPath({
                path: "$.customerId",
                json: data
            })[0];

            // POST http://carts.sock-shop/carts/{customerId}/items (endp 8)
            const carts_sock_shop = getHttpClient("http://carts.sock-shop", authenticate);
            return carts_sock_shop.fetch("/carts/" + customerId + "/items", {
                method: "POST",
                headers: {
                    "accept": "application/json",
                    "content-type": "application/json"
                },
                body: JSONBuild("data/payload_for_endp_8.json", {
                    "$.itemId": itemId,
                    "$.unitPrice": unitPrice
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

describe.each(dataset("data/dataset_140.json"))("test_140_post_carts_customerId_items", (address, card, customer, items, page, size, tags) => {
    it("test_140_post_carts_customerId_items", () => {
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

            // GET http://carts.sock-shop/carts/{customerId}/items (endp 142)
            const carts_sock_shop = getHttpClient("http://carts.sock-shop", authenticate);
            return carts_sock_shop.fetch("/carts/" + customerId + "/items", {
                headers: {
                    "accept": "application/json"
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
                const itemId = JSONPath({
                    path: "$[*].itemId",
                    json: data
                })[0];

                // GET http://catalogue.sock-shop/catalogue (endp 137)
                const catalogue_sock_shop = getHttpClient("http://catalogue.sock-shop", authenticate);
                return catalogue_sock_shop.fetch("/catalogue" + urlencode([["page", page], ["size", size], ["sort", "id"], ["tags", tags]]))
                .then((response) => {
                    expect(response.status).toEqual(200);
                    return response.text();
                })
                .then((text) => {
                    return JSON.parse(text);
                })
                .then((data) => {
                    const unitPrice = JSONPath({
                        path: "$[*].price",
                        json: data
                    })[0];

                    // POST http://carts.sock-shop/carts/{customerId}/items (endp 140)
                    return carts_sock_shop.fetch("/carts/" + customerId + "/items", {
                        method: "POST",
                        headers: {
                            "accept": "application/json",
                            "content-type": "application/json"
                        },
                        body: JSONBuild("data/payload_for_endp_140.json", {
                            "$.itemId": itemId,
                            "$.unitPrice": unitPrice
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
    });
});

describe.each(dataset("data/dataset_90.json"))("test_090_delete_carts_customerId_items_itemId", (address, card, customer, items) => {
    it("test_090_delete_carts_customerId_items_itemId", () => {
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

            // GET http://carts.sock-shop/carts/{customerId}/items (endp 26)
            const carts_sock_shop = getHttpClient("http://carts.sock-shop", authenticate);
            return carts_sock_shop.fetch("/carts/" + customerId + "/items", {
                headers: {
                    "accept": "application/json"
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
                const itemId = JSONPath({
                    path: "$[*].itemId",
                    json: data
                })[0];

                // DELETE http://carts.sock-shop/carts/{customerId}/items/{itemId} (endp 90)
                return carts_sock_shop.fetch("/carts/" + customerId + "/items/" + itemId, {
                    method: "DELETE"
                })
                .then((response) => {
                    expect(response.status).toEqual(202);
                    return response.text();
                })
                .then((text) => {
                })
                .then((data) => {
                });
            });
        });
    });
});

describe.each(dataset("data/dataset_9.json"))("test_009_get_carts_customerId_merge", (address, card, customer, items, sessionId) => {
    it("test_009_get_carts_customerId_merge", () => {
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

            // GET http://carts.sock-shop/carts/{customerId}/merge (endp 9)
            const carts_sock_shop = getHttpClient("http://carts.sock-shop", authenticate);
            return carts_sock_shop.fetch("/carts/" + customerId + "/merge" + urlencode([["sessionId", sessionId]]))
            .then((response) => {
                expect(response.status).toEqual(202);
                return response.text();
            })
            .then((text) => {
            })
            .then((data) => {
            });
        });
    });
});

describe.each(dataset("data/dataset_141.json"))("test_141_get_carts_customerId_merge", (address, card, customer, items, sessionId) => {
    it("test_141_get_carts_customerId_merge", () => {
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

            // GET http://carts.sock-shop/carts/{customerId}/merge (endp 141)
            const carts_sock_shop = getHttpClient("http://carts.sock-shop", authenticate);
            return carts_sock_shop.fetch("/carts/" + customerId + "/merge" + urlencode([["sessionId", sessionId]]))
            .then((response) => {
                expect(response.status).toEqual(202);
                return response.text();
            })
            .then((text) => {
            })
            .then((data) => {
            });
        });
    });
});
