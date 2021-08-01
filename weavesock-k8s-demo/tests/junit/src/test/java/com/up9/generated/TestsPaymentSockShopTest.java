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
public class TestsPaymentSockShopTest
{
    @ParameterizedTest
    @JsonFileSource(resources = "/dataset_27.json")
    public void testPostPaymentauth027(final JsonObject json) throws MalformedURLException, IOException
    {
        final String address = json.getString("address");
        final String amount = json.getString("amount");
        final String card = json.getString("card");
        final String city = json.getString("city");
        final String customer = json.getString("customer");
        final String id = json.getString("id");
        final String items = json.getString("items");
        final String lastName = json.getString("lastName");
        final String longNum = json.getString("longNum");
        final String number = json.getString("number");
        final String username = json.getString("username");

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

        // GET http://user.sock-shop/cards/{id} (endp 24)
        final HttpTarget userSockShop = getHttpClient("http://user.sock-shop", new Authentication());
        final HttpRequest request2 = new HttpRequest();
        request2.setHeaders(new Hashtable<String, Object>() {{
            put("accept", "application/hal+json");
        }});
        final Response response2 = userSockShop.get(request2, "/cards/" + id);
        assertStatusCode(response2.code(), 200);
        assertJSONPath("$.city", "Glasgow", response2.body().string());
        final String ccv = JSONPath("$.ccv", response2.body().string());
        final String expires = JSONPath("$.expires", response2.body().string());
        final String id1 = JSONPath("$.id", response2.body().string());

        // GET http://user.sock-shop/customers/{customerId} (endp 3)
        final HttpRequest request3 = new HttpRequest();
        request3.setHeaders(new Hashtable<String, Object>() {{
            put("accept", "application/hal+json");
        }});
        final Response response3 = userSockShop.get(request3, "/customers/" + customerId);
        assertStatusCode(response3.code(), 200);
        assertJSONPath("$.city", "Glasgow", response3.body().string());
        final String firstName = JSONPath("$.firstName", response3.body().string());

        // GET http://user.sock-shop/addresses/{id} (endp 23)
        final HttpRequest request4 = new HttpRequest();
        request4.setHeaders(new Hashtable<String, Object>() {{
            put("accept", "application/hal+json");
        }});
        final Response response4 = userSockShop.get(request4, "/addresses/" + id1);
        assertStatusCode(response4.code(), 200);
        assertJSONPath("$.country", "United Kingdom", response4.body().string());
        final String country = JSONPath("$.country", response4.body().string());
        final String postcode = JSONPath("$.postcode", response4.body().string());
        final String street = JSONPath("$.street", response4.body().string());

        // POST http://payment.sock-shop/paymentAuth (endp 27)
        final HttpTarget paymentSockShop = getHttpClient("http://payment.sock-shop", new Authentication());
        final HttpRequest request5 = new HttpRequest();
        request5.setHeaders(new Hashtable<String, Object>() {{
            put("accept", "application/json");
            put("content-type", "application/json");
        }});
        request5.setJsonBody("payload_for_endp_27.json", new Hashtable<String, Object>() {{
            put("$.address.city", city);
            put("$.address.country", country);
            put("$.address.number", number);
            put("$.address.postcode", postcode);
            put("$.address.street", street);
            put("$.amount", amount);
            put("$.card.ccv", ccv);
            put("$.card.expires", expires);
            put("$.card.longNum", longNum);
            put("$.customer.firstName", firstName);
            put("$.customer.lastName", lastName);
            put("$.customer.username", username);
        }});
        final Response response5 = paymentSockShop.post(request5, "/paymentAuth");
        assertStatusCode(response5.code(), 200);
    }

    @ParameterizedTest
    @JsonFileSource(resources = "/dataset_143.json")
    public void testPostPaymentauth143(final JsonObject json) throws MalformedURLException, IOException
    {
        final String address = json.getString("address");
        final String amount = json.getString("amount");
        final String card = json.getString("card");
        final String city = json.getString("city");
        final String customer = json.getString("customer");
        final String id = json.getString("id");
        final String items = json.getString("items");
        final String lastName = json.getString("lastName");
        final String longNum = json.getString("longNum");
        final String number = json.getString("number");
        final String username = json.getString("username");

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

        // GET http://user.sock-shop/cards/{id} (endp 24)
        final HttpTarget userSockShop = getHttpClient("http://user.sock-shop", new Authentication());
        final HttpRequest request2 = new HttpRequest();
        request2.setHeaders(new Hashtable<String, Object>() {{
            put("accept", "application/hal+json");
        }});
        final Response response2 = userSockShop.get(request2, "/cards/" + id);
        assertStatusCode(response2.code(), 200);
        assertJSONPath("$.city", "Glasgow", response2.body().string());
        final String id1 = JSONPath("$.id", response2.body().string());

        // GET http://user.sock-shop/customers/{customerId} (endp 127)
        final HttpRequest request3 = new HttpRequest();
        request3.setHeaders(new Hashtable<String, Object>() {{
            put("accept", "application/hal+json");
        }});
        final Response response3 = userSockShop.get(request3, "/customers/" + customerId);
        assertStatusCode(response3.code(), 200);
        assertJSONPath("$._links.self.href", response3.body().string());
        final String firstName = JSONPath("$.firstName", response3.body().string());

        // GET http://user.sock-shop/addresses/{id} (endp 131)
        final HttpRequest request4 = new HttpRequest();
        request4.setHeaders(new Hashtable<String, Object>() {{
            put("accept", "application/hal+json");
        }});
        final Response response4 = userSockShop.get(request4, "/addresses/" + id1);
        assertStatusCode(response4.code(), 200);
        assertJSONPath("$._links.self.href", response4.body().string());
        final String country = JSONPath("$.country", response4.body().string());
        final String postcode = JSONPath("$.postcode", response4.body().string());
        final String street = JSONPath("$.street", response4.body().string());

        // GET http://user.sock-shop/cards/{id} (endp 132)
        final HttpRequest request5 = new HttpRequest();
        request5.setHeaders(new Hashtable<String, Object>() {{
            put("accept", "application/hal+json");
        }});
        final Response response5 = userSockShop.get(request5, "/cards/" + id);
        assertStatusCode(response5.code(), 200);
        assertJSONPath("$._links.card.href", response5.body().string());
        final String ccv = JSONPath("$.ccv", response5.body().string());
        final String expires = JSONPath("$.expires", response5.body().string());

        // POST http://payment.sock-shop/paymentAuth (endp 143)
        final HttpTarget paymentSockShop = getHttpClient("http://payment.sock-shop", new Authentication());
        final HttpRequest request6 = new HttpRequest();
        request6.setHeaders(new Hashtable<String, Object>() {{
            put("accept", "application/json");
            put("content-type", "application/json");
        }});
        request6.setJsonBody("payload_for_endp_143.json", new Hashtable<String, Object>() {{
            put("$.address.city", city);
            put("$.address.country", country);
            put("$.address.number", number);
            put("$.address.postcode", postcode);
            put("$.address.street", street);
            put("$.amount", amount);
            put("$.card.ccv", ccv);
            put("$.card.expires", expires);
            put("$.card.longNum", longNum);
            put("$.customer.firstName", firstName);
            put("$.customer.lastName", lastName);
            put("$.customer.username", username);
        }});
        final Response response6 = paymentSockShop.post(request6, "/paymentAuth");
        assertStatusCode(response6.code(), 200);
        assertJSONPath("$.message", response6.body().string());
    }
}

