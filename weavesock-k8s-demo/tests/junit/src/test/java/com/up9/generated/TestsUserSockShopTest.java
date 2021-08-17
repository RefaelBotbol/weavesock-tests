package com.up9.generated;

import com.up9.generated.Authentication;
import com.up9.up9lib.DummyAuth;
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
public class TestsUserSockShopTest
{
    @ParameterizedTest
    @JsonFileSource(resources = "/191/dataset_191.json")
    public void testPostAddresses191(final JsonObject json) throws MalformedURLException, IOException
    {
        final String city = json.getString("city");
        final String country = json.getString("country");
        final String number = json.getString("number");
        final String postcode = json.getString("postcode");
        final String street = json.getString("street");
        final String userID = json.getString("userID");

        // POST http://user.sock-shop/addresses (endp 191)
        final HttpTarget userSockShop = getHttpClient("http://user.sock-shop", new Authentication());
        final HttpRequest request = new HttpRequest();
        request.setHeaders(new Hashtable<String, Object>() {{
            put("accept", "application/json");
            put("content-type", "application/json");
        }});
        request.setJsonBody("191/payload_for_endp_191.json", new Hashtable<String, Object>() {{
            put("$.city", city);
            put("$.country", country);
            put("$.number", number);
            put("$.postcode", postcode);
            put("$.street", street);
            put("$.userID", userID);
        }});
        final Response response = userSockShop.post(request, "/addresses");
        assertStatusCode(response.code(), 200);
    }

    @ParameterizedTest
    @JsonFileSource(resources = "/192/dataset_192.json")
    public void testPostCards192(final JsonObject json) throws MalformedURLException, IOException
    {
        final String ccv = json.getString("ccv");
        final String expires = json.getString("expires");
        final String longNum = json.getString("longNum");
        final String userID = json.getString("userID");

        // POST http://user.sock-shop/cards (endp 192)
        final HttpTarget userSockShop = getHttpClient("http://user.sock-shop", new Authentication());
        final HttpRequest request = new HttpRequest();
        request.setHeaders(new Hashtable<String, Object>() {{
            put("accept", "application/json");
            put("content-type", "application/json");
        }});
        request.setJsonBody("192/payload_for_endp_192.json", new Hashtable<String, Object>() {{
            put("$.ccv", ccv);
            put("$.expires", expires);
            put("$.longNum", longNum);
            put("$.userID", userID);
        }});
        final Response response = userSockShop.post(request, "/cards");
        assertStatusCode(response.code(), 200);
    }

    @ParameterizedTest
    @JsonFileSource(resources = "/4/dataset_4.json")
    public void testGetCustomersCustomeridAddresses004(final JsonObject json) throws MalformedURLException, IOException
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
        request.setJsonBody("10/payload_for_endp_10.json", new Hashtable<String, Object>() {{
            put("$.address", address);
            put("$.card", card);
            put("$.customer", customer);
            put("$.items", items);
        }});
        final Response response = ordersSockShop.post(request, "/orders");
        assertStatusCode(response.code(), 201);
        assertJSONPath("$.address.city", "Glasgow", response.body().string());
        final String customerId = JSONPath("$.customerId", response.body().string());

        // GET http://user.sock-shop/customers/{customerId}/addresses (endp 4)
        final HttpTarget userSockShop = getHttpClient("http://user.sock-shop", new Authentication());
        final HttpRequest request2 = new HttpRequest();
        final Response response2 = userSockShop.get(request2, "/customers/" + customerId + "/addresses");
        assertStatusCode(response2.code(), 200);
        assertJSONPath("$._embedded.address.[*].country", "United Kingdom", response2.body().string());
    }

    @ParameterizedTest
    @JsonFileSource(resources = "/5/dataset_5.json")
    public void testGetCustomersCustomeridCards005(final JsonObject json) throws MalformedURLException, IOException
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
        request.setJsonBody("10/payload_for_endp_10.json", new Hashtable<String, Object>() {{
            put("$.address", address);
            put("$.card", card);
            put("$.customer", customer);
            put("$.items", items);
        }});
        final Response response = ordersSockShop.post(request, "/orders");
        assertStatusCode(response.code(), 201);
        assertJSONPath("$.address.city", "Glasgow", response.body().string());
        final String customerId = JSONPath("$.customerId", response.body().string());

        // GET http://user.sock-shop/customers/{customerId}/cards (endp 5)
        final HttpTarget userSockShop = getHttpClient("http://user.sock-shop", new Authentication());
        final HttpRequest request2 = new HttpRequest();
        final Response response2 = userSockShop.get(request2, "/customers/" + customerId + "/cards");
        assertStatusCode(response2.code(), 200);
    }

    @ParameterizedTest
    @JsonFileSource(resources = "/129/dataset_129.json")
    public void testGetCustomersCustomeridCards129(final JsonObject json) throws MalformedURLException, IOException
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
        request.setJsonBody("10/payload_for_endp_10.json", new Hashtable<String, Object>() {{
            put("$.address", address);
            put("$.card", card);
            put("$.customer", customer);
            put("$.items", items);
        }});
        final Response response = ordersSockShop.post(request, "/orders");
        assertStatusCode(response.code(), 201);
        assertJSONPath("$.address.city", "Glasgow", response.body().string());
        final String customerId = JSONPath("$.customerId", response.body().string());

        // GET http://user.sock-shop/customers/{customerId}/cards (endp 129)
        final HttpTarget userSockShop = getHttpClient("http://user.sock-shop", new Authentication());
        final HttpRequest request2 = new HttpRequest();
        final Response response2 = userSockShop.get(request2, "/customers/" + customerId + "/cards");
        assertStatusCode(response2.code(), 200);
        assertJSONPath("$._embedded.card[*]._links.card.href", response2.body().string());
    }

    /**
     * authentication-related test
     */
    @Test
    public void testGetLogin006() throws MalformedURLException, IOException
    {
        // GET http://user.sock-shop/login (endp 6)
        final HttpTarget userSockShop = getHttpClient("http://user.sock-shop", new DummyAuth());
        final HttpRequest request = new HttpRequest();
        final Response response = userSockShop.get(request, "/login");
        assertStatusCode(response.code(), 200);
    }

    /**
     * authentication-related test
     */
    @Test
    public void testGetLogin130() throws MalformedURLException, IOException
    {
        // GET http://user.sock-shop/login (endp 130)
        final HttpTarget userSockShop = getHttpClient("http://user.sock-shop", new DummyAuth());
        final HttpRequest request = new HttpRequest();
        final Response response = userSockShop.get(request, "/login");
        assertStatusCode(response.code(), 200);
        assertJSONPath("$.user._links.self.href", response.body().string());
    }

    /**
     * authentication-related test
     */
    @ParameterizedTest
    @JsonFileSource(resources = "/197/dataset_197.json")
    public void testPostRegister197(final JsonObject json) throws MalformedURLException, IOException
    {
        final String email = json.getString("email");
        final String firstName = json.getString("firstName");
        final String lastName = json.getString("lastName");
        final String password = json.getString("password");
        final String username = json.getString("username");

        // POST http://user.sock-shop/register (endp 197)
        final HttpTarget userSockShop = getHttpClient("http://user.sock-shop", new DummyAuth());
        final HttpRequest request = new HttpRequest();
        request.setHeaders(new Hashtable<String, Object>() {{
            put("accept", "application/json");
            put("content-type", "application/json");
        }});
        request.setJsonBody("197/payload_for_endp_197.json", new Hashtable<String, Object>() {{
            put("$.email", email);
            put("$.firstName", firstName);
            put("$.lastName", lastName);
            put("$.password", password);
            put("$.username", username);
        }});
        final Response response = userSockShop.post(request, "/register");
        assertStatusCode(response.code(), 200);
    }
}

