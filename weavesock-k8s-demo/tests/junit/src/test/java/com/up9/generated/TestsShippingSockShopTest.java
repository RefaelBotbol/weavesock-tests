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
public class TestsShippingSockShopTest
{
    @ParameterizedTest
    @JsonFileSource(resources = "/dataset_25.json")
    public void testPostShipping025(final JsonObject json) throws MalformedURLException, IOException
    {
        final String id = json.getString("id");

        // GET http://user.sock-shop/cards/{id} (endp 24)
        final HttpTarget userSockShop = getHttpClient("http://user.sock-shop", new Authentication());
        final HttpRequest request = new HttpRequest();
        request.setHeaders(new Hashtable<String, Object>() {{
            put("accept", "application/hal+json");
        }});
        final Response response = userSockShop.get(request, "/cards/" + id);
        assertStatusCode(response.code(), 200);
        assertJSONPath("$.city", "Glasgow", response.body().string());
        final String name = JSONPath("$.id", response.body().string());

        // POST http://shipping.sock-shop/shipping (endp 25)
        final HttpTarget shippingSockShop = getHttpClient("http://shipping.sock-shop", new Authentication());
        final HttpRequest request2 = new HttpRequest();
        request2.setHeaders(new Hashtable<String, Object>() {{
            put("accept", "application/json");
            put("content-type", "application/json");
        }});
        request2.setJsonBody("payload_for_endp_25.json", new Hashtable<String, Object>() {{
            put("$.id", uuidv4());
            put("$.name", name);
        }});
        final Response response2 = shippingSockShop.post(request2, "/shipping");
        assertStatusCode(response2.code(), 201);
    }

    @ParameterizedTest
    @JsonFileSource(resources = "/dataset_144.json")
    public void testPostShipping144(final JsonObject json) throws MalformedURLException, IOException
    {
        final String name = json.getString("name");

        // POST http://shipping.sock-shop/shipping (endp 144)
        final HttpTarget shippingSockShop = getHttpClient("http://shipping.sock-shop", new Authentication());
        final HttpRequest request = new HttpRequest();
        request.setHeaders(new Hashtable<String, Object>() {{
            put("accept", "application/json");
            put("content-type", "application/json");
        }});
        request.setJsonBody("payload_for_endp_144.json", new Hashtable<String, Object>() {{
            put("$.id", uuidv4());
            put("$.name", name);
        }});
        final Response response = shippingSockShop.post(request, "/shipping");
        assertStatusCode(response.code(), 201);
    }
}

