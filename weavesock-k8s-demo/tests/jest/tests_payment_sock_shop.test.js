const authenticate = require("./authentication");
const {JSONBuild, JSONPath, clearSession, dataset, getHttpClient} = require("./up9lib");

describe.each(dataset("data/27/dataset_27.json"))("test_027_post_paymentAuth", (address, amount, card, city, customer, id, items, lastName, longNum, number, username) => {
    it("test_027_post_paymentAuth", () => {
        clearSession();

        // POST http://orders.sock-shop/orders (endp 10)
        const orders_sock_shop = getHttpClient("http://orders.sock-shop", authenticate);
        return orders_sock_shop.fetch("/orders", {
            method: "POST",
            headers: {
                "accept": "application/json",
                "content-type": "application/json"
            },
            body: JSONBuild("data/27/payload_for_endp_10.json", {
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
                const ccv = JSONPath({
                    path: "$.ccv",
                    json: data
                })[0];
                const expires = JSONPath({
                    path: "$.expires",
                    json: data
                })[0];
                const id1 = JSONPath({
                    path: "$.id",
                    json: data
                })[0];

                // GET http://user.sock-shop/customers/{customerId} (endp 3)
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
                        path: "$.city",
                        json: data
                    })).toContain("Glasgow");
                    const firstName = JSONPath({
                        path: "$.firstName",
                        json: data
                    })[0];

                    // GET http://user.sock-shop/addresses/{id} (endp 23)
                    return user_sock_shop.fetch("/addresses/" + id1, {
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
                            path: "$.country",
                            json: data
                        })).toContain("United Kingdom");
                        const country = JSONPath({
                            path: "$.country",
                            json: data
                        })[0];
                        const postcode = JSONPath({
                            path: "$.postcode",
                            json: data
                        })[0];
                        const street = JSONPath({
                            path: "$.street",
                            json: data
                        })[0];

                        // POST http://payment.sock-shop/paymentAuth (endp 27)
                        const payment_sock_shop = getHttpClient("http://payment.sock-shop", authenticate);
                        return payment_sock_shop.fetch("/paymentAuth", {
                            method: "POST",
                            headers: {
                                "accept": "application/json",
                                "content-type": "application/json"
                            },
                            body: JSONBuild("data/27/payload_for_endp_27.json", {
                                "$.address.city": city,
                                "$.address.country": country,
                                "$.address.number": number,
                                "$.address.postcode": postcode,
                                "$.address.street": street,
                                "$.amount": amount,
                                "$.card.ccv": ccv,
                                "$.card.expires": expires,
                                "$.card.longNum": longNum,
                                "$.customer.firstName": firstName,
                                "$.customer.lastName": lastName,
                                "$.customer.username": username
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
            });
        });
    });
});

describe.each(dataset("data/143/dataset_143.json"))("test_143_post_paymentAuth", (address, amount, card, city, customer, id, items, lastName, longNum, number, username) => {
    it("test_143_post_paymentAuth", () => {
        clearSession();

        // POST http://orders.sock-shop/orders (endp 10)
        const orders_sock_shop = getHttpClient("http://orders.sock-shop", authenticate);
        return orders_sock_shop.fetch("/orders", {
            method: "POST",
            headers: {
                "accept": "application/json",
                "content-type": "application/json"
            },
            body: JSONBuild("data/143/payload_for_endp_10.json", {
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
                const id1 = JSONPath({
                    path: "$.id",
                    json: data
                })[0];

                // GET http://user.sock-shop/customers/{customerId} (endp 127)
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
                    const firstName = JSONPath({
                        path: "$.firstName",
                        json: data
                    })[0];

                    // GET http://user.sock-shop/addresses/{id} (endp 131)
                    return user_sock_shop.fetch("/addresses/" + id1, {
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
                        const country = JSONPath({
                            path: "$.country",
                            json: data
                        })[0];
                        const postcode = JSONPath({
                            path: "$.postcode",
                            json: data
                        })[0];
                        const street = JSONPath({
                            path: "$.street",
                            json: data
                        })[0];

                        // GET http://user.sock-shop/cards/{id} (endp 132)
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
                                path: "$._links.card.href",
                                json: data
                            })).not.toBeNull();
                            const ccv = JSONPath({
                                path: "$.ccv",
                                json: data
                            })[0];
                            const expires = JSONPath({
                                path: "$.expires",
                                json: data
                            })[0];

                            // POST http://payment.sock-shop/paymentAuth (endp 143)
                            const payment_sock_shop = getHttpClient("http://payment.sock-shop", authenticate);
                            return payment_sock_shop.fetch("/paymentAuth", {
                                method: "POST",
                                headers: {
                                    "accept": "application/json",
                                    "content-type": "application/json"
                                },
                                body: JSONBuild("data/143/payload_for_endp_143.json", {
                                    "$.address.city": city,
                                    "$.address.country": country,
                                    "$.address.number": number,
                                    "$.address.postcode": postcode,
                                    "$.address.street": street,
                                    "$.amount": amount,
                                    "$.card.ccv": ccv,
                                    "$.card.expires": expires,
                                    "$.card.longNum": longNum,
                                    "$.customer.firstName": firstName,
                                    "$.customer.lastName": lastName,
                                    "$.customer.username": username
                                })
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
                                    path: "$.message",
                                    json: data
                                })).not.toBeNull();
                            });
                        });
                    });
                });
            });
        });
    });
});
