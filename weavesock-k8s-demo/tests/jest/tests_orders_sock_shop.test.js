const authenticate = require("./authentication");
const {JSONBuild, JSONPath, clearSession, dataset, getHttpClient, urlPart, urlencode} = require("./up9lib");

describe.each(dataset("data/dataset_92.json"))("test_092_get_orders_id", (address, card, customer, items) => {
    it("test_092_get_orders_id", () => {
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
            const custId = JSONPath({
                path: "$.customerId",
                json: data
            })[0];

            // GET http://orders.sock-shop/orders/search/customerId (endp 94)
            return orders_sock_shop.fetch("/orders/search/customerId" + urlencode([["custId", custId], ["sort", "date"]]))
            .then((response) => {
                expect(response.status).toEqual(200);
                return response.text();
            })
            .then((text) => {
                return JSON.parse(text);
            })
            .then((data) => {
                expect(JSONPath({
                    path: "$._embedded.customerOrders.[*].address.country",
                    json: data
                })).toContain("United Kingdom");
                const id = urlPart("/2", JSONPath({
                    path: "$._embedded.customerOrders[*]._links.self.href",
                    json: data
                })[0]);

                // GET http://orders.sock-shop/orders/{id} (endp 92)
                return orders_sock_shop.fetch("/orders/" + id)
                .then((response) => {
                    expect(response.status).toEqual(200);
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
                });
            });
        });
    });
});

describe.each(dataset("data/dataset_199.json"))("test_199_get_orders_id", (address, card, customer, items) => {
    it("test_199_get_orders_id", () => {
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
            const custId = JSONPath({
                path: "$.customerId",
                json: data
            })[0];

            // GET http://orders.sock-shop/orders/search/customerId (endp 94)
            return orders_sock_shop.fetch("/orders/search/customerId" + urlencode([["custId", custId], ["sort", "date"]]))
            .then((response) => {
                expect(response.status).toEqual(200);
                return response.text();
            })
            .then((text) => {
                return JSON.parse(text);
            })
            .then((data) => {
                expect(JSONPath({
                    path: "$._embedded.customerOrders.[*].address.country",
                    json: data
                })).toContain("United Kingdom");
                const id = urlPart("/2", JSONPath({
                    path: "$._embedded.customerOrders[*]._links.self.href",
                    json: data
                })[0]);

                // GET http://orders.sock-shop/orders/{id} (endp 199)
                return orders_sock_shop.fetch("/orders/" + id)
                .then((response) => {
                    expect(response.status).toEqual(200);
                    return response.text();
                })
                .then((text) => {
                    return JSON.parse(text);
                })
                .then((data) => {
                    expect(JSONPath({
                        path: "$.address.city",
                        json: data
                    })).toContain("elsewhere");
                });
            });
        });
    });
});

describe.each(dataset("data/dataset_93.json"))("test_093_get_orders_search_customerId", (address, card, customer, items) => {
    it("test_093_get_orders_search_customerId", () => {
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
            const custId = JSONPath({
                path: "$.customerId",
                json: data
            })[0];

            // GET http://orders.sock-shop/orders/search/customerId (endp 93)
            return orders_sock_shop.fetch("/orders/search/customerId" + urlencode([["custId", custId], ["sort", "date"]]))
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

describe.each(dataset("data/dataset_156.json"))("test_156_get_orders_search_customerId", (address, card, card1, customer, items, items1) => {
    it("test_156_get_orders_search_customerId", () => {
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

            // GET http://user.sock-shop/customers/{customerId} (endp 127)
            const user_sock_shop = getHttpClient("http://user.sock-shop", authenticate);
            return user_sock_shop.fetch("/customers/" + customerId, {
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
                    path: "$._links.self.href",
                    json: data
                })).not.toBeNull();
                const customer1 = JSONPath({
                    path: "$._links.self.href",
                    json: data
                })[0];

                // GET http://user.sock-shop/customers/{customerId}/addresses (endp 128)
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
                        path: "$._embedded.address[*]._links.self.href",
                        json: data
                    })).not.toBeNull();
                    const address1 = JSONPath({
                        path: "$._embedded.address[*]._links.address.href",
                        json: data
                    })[0];

                    // POST http://orders.sock-shop/orders (endp 155)
                    return orders_sock_shop.fetch("/orders", {
                        method: "POST",
                        headers: {
                            "accept": "application/json",
                            "content-type": "application/json"
                        },
                        body: JSONBuild("data/payload_for_endp_155.json", {
                            "$.address": address1,
                            "$.card": card1,
                            "$.customer": customer1,
                            "$.items": items1
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
                            path: "$.card.ccv",
                            json: data
                        })).not.toBeNull();
                        const custId = JSONPath({
                            path: "$.customerId",
                            json: data
                        })[0];

                        // GET http://orders.sock-shop/orders/search/customerId (endp 156)
                        return orders_sock_shop.fetch("/orders/search/customerId" + urlencode([["custId", custId], ["sort", "date"]]))
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
        });
    });
});
