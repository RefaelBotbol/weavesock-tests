const authenticate = require("./authentication");
const {JSONPath, clearSession, dataset, getHttpClient, urlencode} = require("./up9lib");

describe.each(dataset("data/137/dataset_137.json"))("test_137_get_catalogue", (page, size, tags) => {
    it("test_137_get_catalogue", () => {
        clearSession();

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
            expect(JSONPath({
                path: "$[*].tag[*]",
                json: data
            })).not.toBeNull();
        });
    });
});

describe.each(dataset("data/2/dataset_2.json"))("test_002_get_catalogue_id", (size, tags) => {
    it("test_002_get_catalogue_id", () => {
        clearSession();

        // GET http://catalogue.sock-shop/catalogue (endp 1)
        const catalogue_sock_shop = getHttpClient("http://catalogue.sock-shop", authenticate);
        return catalogue_sock_shop.fetch("/catalogue" + urlencode([["page", "1"], ["size", size], ["sort", "id"], ["tags", tags]]))
        .then((response) => {
            expect(response.status).toEqual(200);
            return response.text();
        })
        .then((text) => {
            return JSON.parse(text);
        })
        .then((data) => {
            const id = JSONPath({
                path: "$[*].id",
                json: data
            })[0];

            // GET http://catalogue.sock-shop/catalogue/{id} (endp 2)
            return catalogue_sock_shop.fetch("/catalogue/" + id)
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

describe.each(dataset("data/135/dataset_135.json"))("test_135_get_catalogue_id", (size, tags) => {
    it("test_135_get_catalogue_id", () => {
        clearSession();

        // GET http://catalogue.sock-shop/catalogue (endp 1)
        const catalogue_sock_shop = getHttpClient("http://catalogue.sock-shop", authenticate);
        return catalogue_sock_shop.fetch("/catalogue" + urlencode([["page", "1"], ["size", size], ["sort", "id"], ["tags", tags]]))
        .then((response) => {
            expect(response.status).toEqual(200);
            return response.text();
        })
        .then((text) => {
            return JSON.parse(text);
        })
        .then((data) => {
            const id = JSONPath({
                path: "$[*].id",
                json: data
            })[0];

            // GET http://catalogue.sock-shop/catalogue/{id} (endp 135)
            return catalogue_sock_shop.fetch("/catalogue/" + id)
            .then((response) => {
                expect(response.status).toEqual(200);
                return response.text();
            })
            .then((text) => {
                return JSON.parse(text);
            })
            .then((data) => {
                expect(JSONPath({
                    path: "$.tag[*]",
                    json: data
                })).not.toBeNull();
            });
        });
    });
});

it("test_085_get_catalogue_size", () => {
    clearSession();

    // GET http://catalogue.sock-shop/tags (endp 87)
    const catalogue_sock_shop = getHttpClient("http://catalogue.sock-shop", authenticate);
    return catalogue_sock_shop.fetch("/tags")
    .then((response) => {
        expect(response.status).toEqual(200);
        return response.text();
    })
    .then((text) => {
        return JSON.parse(text);
    })
    .then((data) => {
        const tags = JSONPath({
            path: "$.tags[*]",
            json: data
        })[0];

        // GET http://catalogue.sock-shop/catalogue/size (endp 85)
        return catalogue_sock_shop.fetch("/catalogue/size" + urlencode([["tags", tags]]))
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

it("test_136_get_catalogue_size", () => {
    clearSession();

    // GET http://catalogue.sock-shop/tags (endp 138)
    const catalogue_sock_shop = getHttpClient("http://catalogue.sock-shop", authenticate);
    return catalogue_sock_shop.fetch("/tags")
    .then((response) => {
        expect(response.status).toEqual(200);
        return response.text();
    })
    .then((text) => {
        return JSON.parse(text);
    })
    .then((data) => {
        const tags = JSONPath({
            path: "$.tags[*]",
            json: data
        })[0];

        // GET http://catalogue.sock-shop/catalogue/size (endp 136)
        return catalogue_sock_shop.fetch("/catalogue/size" + urlencode([["tags", tags]]))
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
