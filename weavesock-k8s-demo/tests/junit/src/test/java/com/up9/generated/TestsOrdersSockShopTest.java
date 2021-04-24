package com.up9.generated;

import com.up9.generated.Authentication;
import com.up9.up9lib.HttpRequest;
import com.up9.up9lib.HttpTarget;
import java.io.IOException;
import java.net.MalformedURLException;
import java.util.Hashtable;
import javax.json.JsonObject;
import net.joshka.junit.json.params.JsonFileSource;
import okhttp3.Response;
import org.junit.jupiter.api.MethodOrderer.Alphanumeric;
import org.junit.jupiter.api.Test;
import org.junit.jupiter.api.TestMethodOrder;
import org.junit.jupiter.params.ParameterizedTest;
import static com.up9.up9lib.Common.*;

@TestMethodOrder(Alphanumeric.class)
public class TestsOrdersSockShopTest
{
    @ParameterizedTest
    @JsonFileSource(resources = "/dataset_92.json")
    public void testGetOrdersId092(final JsonObject json) throws MalformedURLException, IOException
    {
        final String address = json.getString("address");
        final String card = json.getString("card");
        final String customer = json.getString("customer");
        final String items = json.getString("items");

        // POST http://orders.sock-shop/orders (endp 10)
        final HttpTarget ordersSockShop = getHttpClient("http://orders.sock-shop", new Authentication());
        final HttpRequest request = new HttpRequest();
        request.setHeaders(new Hashtable<String, Object>() {{
            put("accept", "application/json");
            put("content-type", "application/json");
        }});
        request.setJsonBody("payload_for_endp_10.json", new Hashtable<String, Object>() {{
            put("$.address", address);
            put("$.card", card);
            put("$.customer", customer);
            put("$.items", items);
        }});
        final Response response = ordersSockShop.post(request, "/orders");
        assertStatusCode(response.code(), 201);
        assertJSONPath("$.address.city", "Glasgow", response.body().string());
        final String custId = JSONPath("$.customerId", response.body().string());

        // GET http://orders.sock-shop/orders/search/customerId (endp 94)
        final HttpRequest request2 = new HttpRequest();
        request2.setQueryString(new Hashtable<String, Object>() {{
            put("custId", custId);
            put("sort", "date");
        }});
        final Response response2 = ordersSockShop.get(request2, "/orders/search/customerId");
        assertStatusCode(response2.code(), 200);
        assertJSONPath("$._embedded.customerOrders.[*].address.country", "United Kingdom", response2.body().string());
        final String id = urlPart("/2", JSONPath("$._embedded.customerOrders[*]._links.self.href", response2.body().string()));

        // GET http://orders.sock-shop/orders/{id} (endp 92)
        final HttpRequest request3 = new HttpRequest();
        final Response response3 = ordersSockShop.get(request3, "/orders/" + id);
        assertStatusCode(response3.code(), 200);
        assertJSONPath("$.address.city", "Glasgow", response3.body().string());
    }

    @ParameterizedTest
    @JsonFileSource(resources = "/dataset_199.json")
    public void testGetOrdersId199(final JsonObject json) throws MalformedURLException, IOException
    {
        final String address = json.getString("address");
        final String card = json.getString("card");
        final String customer = json.getString("customer");
        final String items = json.getString("items");

        // POST http://orders.sock-shop/orders (endp 10)
        final HttpTarget ordersSockShop = getHttpClient("http://orders.sock-shop", new Authentication());
        final HttpRequest request = new HttpRequest();
        request.setHeaders(new Hashtable<String, Object>() {{
            put("accept", "application/json");
            put("content-type", "application/json");
        }});
        request.setJsonBody("payload_for_endp_10.json", new Hashtable<String, Object>() {{
            put("$.address", address);
            put("$.card", card);
            put("$.customer", customer);
            put("$.items", items);
        }});
        final Response response = ordersSockShop.post(request, "/orders");
        assertStatusCode(response.code(), 201);
        assertJSONPath("$.address.city", "Glasgow", response.body().string());
        final String custId = JSONPath("$.customerId", response.body().string());

        // GET http://orders.sock-shop/orders/search/customerId (endp 94)
        final HttpRequest request2 = new HttpRequest();
        request2.setQueryString(new Hashtable<String, Object>() {{
            put("custId", custId);
            put("sort", "date");
        }});
        final Response response2 = ordersSockShop.get(request2, "/orders/search/customerId");
        assertStatusCode(response2.code(), 200);
        assertJSONPath("$._embedded.customerOrders.[*].address.country", "United Kingdom", response2.body().string());
        final String id = urlPart("/2", JSONPath("$._embedded.customerOrders[*]._links.self.href", response2.body().string()));

        // GET http://orders.sock-shop/orders/{id} (endp 199)
        final HttpRequest request3 = new HttpRequest();
        final Response response3 = ordersSockShop.get(request3, "/orders/" + id);
        assertStatusCode(response3.code(), 200);
        assertJSONPath("$.address.city", "elsewhere", response3.body().string());
    }

    @ParameterizedTest
    @JsonFileSource(resources = "/dataset_93.json")
    public void testGetOrdersSearchCustomerid093(final JsonObject json) throws MalformedURLException, IOException
    {
        final String address = json.getString("address");
        final String card = json.getString("card");
        final String customer = json.getString("customer");
        final String items = json.getString("items");

        // POST http://orders.sock-shop/orders (endp 10)
        final HttpTarget ordersSockShop = getHttpClient("http://orders.sock-shop", new Authentication());
        final HttpRequest request = new HttpRequest();
        request.setHeaders(new Hashtable<String, Object>() {{
            put("accept", "application/json");
            put("content-type", "application/json");
        }});
        request.setJsonBody("payload_for_endp_10.json", new Hashtable<String, Object>() {{
            put("$.address", address);
            put("$.card", card);
            put("$.customer", customer);
            put("$.items", items);
        }});
        final Response response = ordersSockShop.post(request, "/orders");
        assertStatusCode(response.code(), 201);
        assertJSONPath("$.address.city", "Glasgow", response.body().string());
        final String custId = JSONPath("$.customerId", response.body().string());

        // GET http://orders.sock-shop/orders/search/customerId (endp 93)
        final HttpRequest request2 = new HttpRequest();
        request2.setQueryString(new Hashtable<String, Object>() {{
            put("custId", custId);
            put("sort", "date");
        }});
        final Response response2 = ordersSockShop.get(request2, "/orders/search/customerId");
        assertStatusCode(response2.code(), 200);
    }

    @ParameterizedTest
    @JsonFileSource(resources = "/dataset_156.json")
    public void testGetOrdersSearchCustomerid156(final JsonObject json) throws MalformedURLException, IOException
    {
        final String address = json.getString("address");
        final String card = json.getString("card");
        final String customer = json.getString("customer");
        final String items = json.getString("items");
        final String items1 = json.getString("items1");

        // POST http://orders.sock-shop/orders (endp 10)
        final HttpTarget ordersSockShop = getHttpClient("http://orders.sock-shop", new Authentication());
        final HttpRequest request = new HttpRequest();
        request.setHeaders(new Hashtable<String, Object>() {{
            put("accept", "application/json");
            put("content-type", "application/json");
        }});
        request.setJsonBody("payload_for_endp_10.json", new Hashtable<String, Object>() {{
            put("$.address", address);
            put("$.card", card);
            put("$.customer", customer);
            put("$.items", items);
        }});
        final Response response = ordersSockShop.post(request, "/orders");
        assertStatusCode(response.code(), 201);
        assertJSONPath("$.address.city", "Glasgow", response.body().string());
        final String customerId = JSONPath("$.customerId", response.body().string());

        // GET http://user.sock-shop/customers/{customerId} (endp 127)
        final HttpTarget userSockShop = getHttpClient("http://user.sock-shop", new Authentication());
        final HttpRequest request2 = new HttpRequest();
        request2.setHeaders(new Hashtable<String, Object>() {{
            put("accept", "application/hal+json");
        }});
        final Response response2 = userSockShop.get(request2, "/customers/" + customerId);
        assertStatusCode(response2.code(), 200);
        final String customer1 = JSONPath("$._links.self.href", response2.body().string());

        // GET http://user.sock-shop/customers/{customerId}/addresses (endp 128)
        final HttpRequest request3 = new HttpRequest();
        final Response response3 = userSockShop.get(request3, "/customers/" + customerId + "/addresses");
        assertStatusCode(response3.code(), 200);
        final String address1 = JSONPath("$._embedded.address[*]._links.address.href", response3.body().string());

        // GET http://user.sock-shop/customers/{customerId}/cards (endp 129)
        final HttpRequest request4 = new HttpRequest();
        final Response response4 = userSockShop.get(request4, "/customers/" + customerId + "/cards");
        assertStatusCode(response4.code(), 200);
        final String card1 = JSONPath("$._embedded.card[*]._links.card.href", response4.body().string());

        // POST http://orders.sock-shop/orders (endp 155)
        final HttpRequest request5 = new HttpRequest();
        request5.setHeaders(new Hashtable<String, Object>() {{
            put("accept", "application/json");
            put("content-type", "application/json");
        }});
        request5.setJsonBody("payload_for_endp_155.json", new Hashtable<String, Object>() {{
            put("$.address", address1);
            put("$.card", card1);
            put("$.customer", customer1);
            put("$.items", items1);
        }});
        final Response response5 = ordersSockShop.post(request5, "/orders");
        assertStatusCode(response5.code(), 201);
        final String custId = JSONPath("$.customerId", response5.body().string());

        // GET http://orders.sock-shop/orders/search/customerId (endp 156)
        final HttpRequest request6 = new HttpRequest();
        request6.setQueryString(new Hashtable<String, Object>() {{
            put("custId", custId);
            put("sort", "date");
        }});
        final Response response6 = ordersSockShop.get(request6, "/orders/search/customerId");
        assertStatusCode(response6.code(), 200);
        assertJSONPath("$._embedded.customerOrders[*].address.city", "elsewhere", response6.body().string());
    }
}

