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
public class TestsCatalogueMockintoshManagementSockShopTest
{
    @ParameterizedTest
    @JsonFileSource(resources = "/dataset_287.json")
    public void testGetCatalogue287(final JsonObject json) throws MalformedURLException, IOException
    {
        final String size = json.getString("size");

        // GET http://catalogue-mockintosh-management.sock-shop/catalogue (endp 287)
        final HttpTarget catalogueMockintoshManagementSockShop = getHttpClient("http://catalogue-mockintosh-management.sock-shop", new Authentication());
        final HttpRequest request = new HttpRequest();
        request.setQueryString(new Hashtable<String, Object>() {{
            put("size", size);
        }});
        final Response response = catalogueMockintoshManagementSockShop.get(request, "/catalogue");
        assertStatusCode(response.code(), 200);
    }
}

