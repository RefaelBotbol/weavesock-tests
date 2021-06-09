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
public class TestsFrontEndSockShopTest
{
    @ParameterizedTest
    @JsonFileSource(resources = "/dataset_11.json")
    public void testGet011(final JsonObject json) throws MalformedURLException, IOException
    {
        final String _meta_http_equiv = json.getString("_meta_http_equiv");
        final String _script_document_cookie = json.getString("_script_document_cookie");
        final String class_classLoader_URLs_0_ = json.getString("class_classLoader_URLs_0_");
        final String content = json.getString("content");
        final String expression = json.getString("expression");

        // GET http://front-end.sock-shop/ (endp 11)
        final HttpTarget frontEndSockShop = getHttpClient("http://front-end.sock-shop", new Authentication());
        final HttpRequest request = new HttpRequest();
        request.setQueryString(new Hashtable<String, Object>() {{
            put("\"</script>", "");
            put("\"><script>alert('struts_sa_surl_xss.nasl-1603621900')</script>", "");
            put("\"><script>alert('struts_sa_surl_xss.nasl-1605657683')</script>", "");
            put("\"><script>alert('struts_sa_surl_xss.nasl-1605658393')</script>", "");
            put("('\\u0023_memberAccess[\\'allowStaticMethodAccess\\']')(meh)", "true");
            put("(aaa)(('\\u0023context[\\'xwork.MethodAccessor.denyMethodExecution\\']\\u003d\\u0023foo')(\\u0023foo\\u003dnew java.lang.Boolean(\"false\")))", "");
            put("(asdf)(('\\u0023thread.sleep(5000)')(\\u0023thread\\u003d@java.lang.Thread@currentThread()))", "1");
            put("<meta http-equiv", _meta_http_equiv);
            put("<script>document.cookie", _script_document_cookie);
            put("XDEBUG_SESSION_START", "phpstorm");
            put("a", "fetch");
            put("class.classLoader.URLs[0]", class_classLoader_URLs_0_);
            put("content", content);
            put("debug", "command");
            put("expression", expression);
            put("ho {COMPLETE_VERSION}", "");
        }});
        request.setHeaders(new Hashtable<String, Object>() {{
            put("content-type", "application/x-www-form-urlencoded");
        }});
        final Response response = frontEndSockShop.get(request, "/");
        assertStatusCode(response.code(), 200);
        assertCSSselect("div#basket div.box form h1", "Shopping cart", response.body().string());
    }

    @Test
    public void testGet028() throws MalformedURLException, IOException
    {
        // GET http://front-end.sock-shop/ (endp 28)
        final HttpTarget frontEndSockShop = getHttpClient("http://front-end.sock-shop", new Authentication());
        final HttpRequest request = new HttpRequest();
        final Response response = frontEndSockShop.get(request, "/");
        assertStatusCode(response.code(), 200);
    }

    @Test
    public void testHead067() throws MalformedURLException, IOException
    {
        // HEAD http://front-end.sock-shop/ (endp 67)
        final HttpTarget frontEndSockShop = getHttpClient("http://front-end.sock-shop", new Authentication());
        final HttpRequest request = new HttpRequest();
        final Response response = frontEndSockShop.head(request, "/");
        assertStatusCode(response.code(), 200);
    }

    @ParameterizedTest
    @JsonFileSource(resources = "/dataset_133.json")
    public void testGet133(final JsonObject json) throws MalformedURLException, IOException
    {
        final String PHPSESSID = json.getString("PHPSESSID");
        final String action = json.getString("action");
        final String album = json.getString("album");
        final String category = json.getString("category");
        final String content = json.getString("content");
        final String dispsize = json.getString("dispsize");
        final String feed = json.getString("feed");
        final String id = json.getString("id");
        final String invitaion_code = json.getString("invitaion_code");
        final String mod = json.getString("mod");
        final String mode = json.getString("mode");
        final String name = json.getString("name");
        final String page = json.getString("page");
        final String param = json.getString("param");
        final String s = json.getString("s");
        final String vars_0_ = json.getString("vars_0_");
        final String weekstartday = json.getString("weekstartday");

        // GET http://front-end.sock-shop/ (endp 133)
        final HttpTarget frontEndSockShop = getHttpClient("http://front-end.sock-shop", new Authentication());
        final HttpRequest request = new HttpRequest();
        request.setQueryString(new Hashtable<String, Object>() {{
            put("", param);
            put("\u0000", "");
            put("\"><script>alert(document.domain)</script>", "");
            put("/'", "");
            put("<script>alert(document.domain)</script>", "");
            put("OpenServer", "");
            put("PHPSESSID", PHPSESSID);
            put("XDEBUG_SESSION_START", "phpstorm");
            put("a", "fetch");
            put("action", action);
            put("album", album);
            put("category", category);
            put("cmd", "show");
            put("content", content);
            put("cpmvc_do_action", "mvparse");
            put("data", "1");
            put("debug", "1");
            put("dispsize", dispsize);
            put("f", "edit");
            put("feed", feed);
            put("filter", "phpinfo");
            put("function", "call_user_func_array");
            put("id", id);
            put("invitaion_code", invitaion_code);
            put("mod", mod);
            put("mode", mode);
            put("name", name);
            put("op", "browse");
            put("page", page);
            put("parent", "0");
            put("q[]", "x");
            put("s", s);
            put("show_dash_widget", "1");
            put("start", "0");
            put("user", "");
            put("vars[0]", vars_0_);
            put("weekstartday", weekstartday);
        }});
        final Response response = frontEndSockShop.get(request, "/");
        assertStatusCode(response.code(), 200);
        assertCSSselect("div#hot div.box div.container div h2", "Hot this week", response.body().string());
    }

    @Test
    public void testHead134() throws MalformedURLException, IOException
    {
        // HEAD http://front-end.sock-shop/ (endp 134)
        final HttpTarget frontEndSockShop = getHttpClient("http://front-end.sock-shop", new Authentication());
        final HttpRequest request = new HttpRequest();
        final Response response = frontEndSockShop.head(request, "/");
        assertStatusCode(response.code(), 200);
    }

    @ParameterizedTest
    @JsonFileSource(resources = "/dataset_154.json")
    public void testGet154(final JsonObject json) throws MalformedURLException, IOException
    {
        final String content = json.getString("content");

        // GET http://front-end.sock-shop/ (endp 154)
        final HttpTarget frontEndSockShop = getHttpClient("http://front-end.sock-shop", new Authentication());
        final HttpRequest request = new HttpRequest();
        request.setQueryString(new Hashtable<String, Object>() {{
            put("a", "fetch");
            put("content", content);
        }});
        request.setHeaders(new Hashtable<String, Object>() {{
            put("content-type", "application/json");
        }});
        final Response response = frontEndSockShop.get(request, "/");
        assertStatusCode(response.code(), 200);
        assertCSSselect("div#hot div.box div.container div h2", "Hot this week", response.body().string());
    }

    @Test
    public void testGet159() throws MalformedURLException, IOException
    {
        // GET http://front-end.sock-shop/ (endp 159)
        final HttpTarget frontEndSockShop = getHttpClient("http://front-end.sock-shop", new Authentication());
        final HttpRequest request = new HttpRequest();
        request.setHeaders(new Hashtable<String, Object>() {{
            put("content-type", "application/x-www-form-urlencoded");
        }});
        final Response response = frontEndSockShop.get(request, "/");
        assertStatusCode(response.code(), 200);
        assertCSSselect("div#hot div.box div.container div h2", "Hot this week", response.body().string());
    }

    @Test
    public void testGet201() throws MalformedURLException, IOException
    {
        // GET http://front-end.sock-shop/ (endp 201)
        final HttpTarget frontEndSockShop = getHttpClient("http://front-end.sock-shop", new Authentication());
        final HttpRequest request = new HttpRequest();
        request.setHeaders(new Hashtable<String, Object>() {{
            put("content-type", "%%{#context['com.opensymphony.xwork2.dispatcher.HttpServletResponse'].addHeader('X-NYU'");
        }});
        final Response response = frontEndSockShop.get(request, "/");
        assertStatusCode(response.code(), 200);
        assertCSSselect("div#hot div.box div.container div h2", "Hot this week", response.body().string());
    }

    @Test
    public void testGet203() throws MalformedURLException, IOException
    {
        // GET http://front-end.sock-shop/ (endp 203)
        final HttpTarget frontEndSockShop = getHttpClient("http://front-end.sock-shop", new Authentication());
        final HttpRequest request = new HttpRequest();
        request.setHeaders(new Hashtable<String, Object>() {{
            put("content-type", "text/html");
        }});
        final Response response = frontEndSockShop.get(request, "/");
        assertStatusCode(response.code(), 200);
        assertCSSselect("div#hot div.box div.container div h2", "Hot this week", response.body().string());
    }

    @Test
    public void testGet204() throws MalformedURLException, IOException
    {
        // GET http://front-end.sock-shop/ (endp 204)
        final HttpTarget frontEndSockShop = getHttpClient("http://front-end.sock-shop", new Authentication());
        final HttpRequest request = new HttpRequest();
        request.setHeaders(new Hashtable<String, Object>() {{
            put("content-type", "%{#context['com.opensymphony.xwork2.dispatcher.HttpServletResponse'].addHeader('eOdVotoY'");
        }});
        final Response response = frontEndSockShop.get(request, "/");
        assertStatusCode(response.code(), 200);
        assertCSSselect("div#hot div.box div.container div h2", "Hot this week", response.body().string());
    }

    @Test
    public void testGet205() throws MalformedURLException, IOException
    {
        // GET http://front-end.sock-shop/ (endp 205)
        final HttpTarget frontEndSockShop = getHttpClient("http://front-end.sock-shop", new Authentication());
        final HttpRequest request = new HttpRequest();
        request.setHeaders(new Hashtable<String, Object>() {{
            put("content-type", "%{#context['com.opensymphony.xwork2.dispatcher.HttpServletResponse'].addHeader('cpQiapAu'");
        }});
        final Response response = frontEndSockShop.get(request, "/");
        assertStatusCode(response.code(), 200);
        assertCSSselect("div#hot div.box div.container div h2", "Hot this week", response.body().string());
    }

    @Test
    public void testGet206() throws MalformedURLException, IOException
    {
        // GET http://front-end.sock-shop/ (endp 206)
        final HttpTarget frontEndSockShop = getHttpClient("http://front-end.sock-shop", new Authentication());
        final HttpRequest request = new HttpRequest();
        request.setHeaders(new Hashtable<String, Object>() {{
            put("content-type", "%{#context['com.opensymphony.xwork2.dispatcher.HttpServletResponse'].addHeader('frVV3EZN'");
        }});
        final Response response = frontEndSockShop.get(request, "/");
        assertStatusCode(response.code(), 200);
        assertCSSselect("div#hot div.box div.container div h2", "Hot this week", response.body().string());
    }

    @Test
    public void testGet213() throws MalformedURLException, IOException
    {
        // GET http://front-end.sock-shop/ (endp 213)
        final HttpTarget frontEndSockShop = getHttpClient("http://front-end.sock-shop", new Authentication());
        final HttpRequest request = new HttpRequest();
        request.setHeaders(new Hashtable<String, Object>() {{
            put("content-type", "application/xml");
        }});
        final Response response = frontEndSockShop.get(request, "/");
        assertStatusCode(response.code(), 200);
        assertCSSselect("div#hot div.box div.container div h2", "Hot this week", response.body().string());
    }

    @Test
    public void testGet303() throws MalformedURLException, IOException
    {
        // GET http://front-end.sock-shop/ (endp 303)
        final HttpTarget frontEndSockShop = getHttpClient("http://front-end.sock-shop", new Authentication());
        final HttpRequest request = new HttpRequest();
        request.setHeaders(new Hashtable<String, Object>() {{
            put("content-type", "text/xml");
        }});
        final Response response = frontEndSockShop.get(request, "/");
        assertStatusCode(response.code(), 200);
        assertCSSselect("div#hot div.box div.container div h2", "Hot this week", response.body().string());
    }

    @Test
    public void testGet304() throws MalformedURLException, IOException
    {
        // GET http://front-end.sock-shop/ (endp 304)
        final HttpTarget frontEndSockShop = getHttpClient("http://front-end.sock-shop", new Authentication());
        final HttpRequest request = new HttpRequest();
        request.setHeaders(new Hashtable<String, Object>() {{
            put("content-type", "%{#context['com.opensymphony.xwork2.dispatcher.HttpServletResponse'].addHeader('X-Qualys-Struts'");
        }});
        final Response response = frontEndSockShop.get(request, "/");
        assertStatusCode(response.code(), 200);
        assertCSSselect("div#hot div.box div.container div h2", "Hot this week", response.body().string());
    }

    @Test
    public void testGet305() throws MalformedURLException, IOException
    {
        // GET http://front-end.sock-shop/ (endp 305)
        final HttpTarget frontEndSockShop = getHttpClient("http://front-end.sock-shop", new Authentication());
        final HttpRequest request = new HttpRequest();
        request.setHeaders(new Hashtable<String, Object>() {{
            put("content-type", "%{(#nike='multipart/form-data').(#dm=@ognl.OgnlContext@DEFAULT_MEMBER_ACCESS).(#_memberAccess?(#_memberAccess=#dm):((#container=#context['com.opensymphony.xwork2.ActionContext.container']).(#ognlUtil=#container.getInstance(@com.opensymphony.xwork2.ognl.OgnlUtil@class)).(#ognlUtil.getExcludedPackageNames().clear()).(#ognlUtil.getExcludedClasses().clear()).(#context.setMemberAccess(#dm)))).(#cmdlinux='ifconfig').(#cmdwin='ipconfig').(#iswin=(@java.lang.System@getProperty('os.name').toLowerCase().contains('win'))).(#cmds=(#iswin?{'cmd.exe'");
        }});
        final Response response = frontEndSockShop.get(request, "/");
        assertStatusCode(response.code(), 200);
        assertCSSselect("div#hot div.box div.container div h2", "Hot this week", response.body().string());
    }

    @Test
    public void testGet306() throws MalformedURLException, IOException
    {
        // GET http://front-end.sock-shop/ (endp 306)
        final HttpTarget frontEndSockShop = getHttpClient("http://front-end.sock-shop", new Authentication());
        final HttpRequest request = new HttpRequest();
        request.setHeaders(new Hashtable<String, Object>() {{
            put("content-type", "%{#context['com.opensymphony.xwork2.dispatcher.HttpServletResponse'].addHeader('z13mXu0c'");
        }});
        final Response response = frontEndSockShop.get(request, "/");
        assertStatusCode(response.code(), 200);
        assertCSSselect("div#hot div.box div.container div h2", "Hot this week", response.body().string());
    }

    @Test
    public void testGet307() throws MalformedURLException, IOException
    {
        // GET http://front-end.sock-shop/ (endp 307)
        final HttpTarget frontEndSockShop = getHttpClient("http://front-end.sock-shop", new Authentication());
        final HttpRequest request = new HttpRequest();
        request.setHeaders(new Hashtable<String, Object>() {{
            put("content-type", "%{#context['com.opensymphony.xwork2.dispatcher.HttpServletResponse'].addHeader('4IBh1a16'");
        }});
        final Response response = frontEndSockShop.get(request, "/");
        assertStatusCode(response.code(), 200);
        assertCSSselect("div#hot div.box div.container div h2", "Hot this week", response.body().string());
    }

    @Test
    public void testGet308() throws MalformedURLException, IOException
    {
        // GET http://front-end.sock-shop/ (endp 308)
        final HttpTarget frontEndSockShop = getHttpClient("http://front-end.sock-shop", new Authentication());
        final HttpRequest request = new HttpRequest();
        request.setHeaders(new Hashtable<String, Object>() {{
            put("content-type", "%{#context['com.opensymphony.xwork2.dispatcher.HttpServletResponse'].addHeader('fbxxae2T'");
        }});
        final Response response = frontEndSockShop.get(request, "/");
        assertStatusCode(response.code(), 200);
        assertCSSselect("div#hot div.box div.container div h2", "Hot this week", response.body().string());
    }

    @Test
    public void testGet309() throws MalformedURLException, IOException
    {
        // GET http://front-end.sock-shop/ (endp 309)
        final HttpTarget frontEndSockShop = getHttpClient("http://front-end.sock-shop", new Authentication());
        final HttpRequest request = new HttpRequest();
        request.setHeaders(new Hashtable<String, Object>() {{
            put("content-type", "%{#context['com.opensymphony.xwork2.dispatcher.HttpServletResponse'].addHeader('h3VAvCd6'");
        }});
        final Response response = frontEndSockShop.get(request, "/");
        assertStatusCode(response.code(), 200);
        assertCSSselect("div#hot div.box div.container div h2", "Hot this week", response.body().string());
    }

    @Test
    public void testGet310() throws MalformedURLException, IOException
    {
        // GET http://front-end.sock-shop/ (endp 310)
        final HttpTarget frontEndSockShop = getHttpClient("http://front-end.sock-shop", new Authentication());
        final HttpRequest request = new HttpRequest();
        request.setHeaders(new Hashtable<String, Object>() {{
            put("content-type", "%{#context['com.opensymphony.xwork2.dispatcher.HttpServletResponse'].addHeader('ZYbIXBxr'");
        }});
        final Response response = frontEndSockShop.get(request, "/");
        assertStatusCode(response.code(), 200);
        assertCSSselect("div#hot div.box div.container div h2", "Hot this week", response.body().string());
    }

    @Test
    public void testGet311() throws MalformedURLException, IOException
    {
        // GET http://front-end.sock-shop/ (endp 311)
        final HttpTarget frontEndSockShop = getHttpClient("http://front-end.sock-shop", new Authentication());
        final HttpRequest request = new HttpRequest();
        request.setHeaders(new Hashtable<String, Object>() {{
            put("content-type", "%{#context['com.opensymphony.xwork2.dispatcher.HttpServletResponse'].addHeader('YUbHNQZB'");
        }});
        final Response response = frontEndSockShop.get(request, "/");
        assertStatusCode(response.code(), 200);
        assertCSSselect("div#hot div.box div.container div h2", "Hot this week", response.body().string());
    }

    @Test
    public void testGet312() throws MalformedURLException, IOException
    {
        // GET http://front-end.sock-shop/ (endp 312)
        final HttpTarget frontEndSockShop = getHttpClient("http://front-end.sock-shop", new Authentication());
        final HttpRequest request = new HttpRequest();
        request.setHeaders(new Hashtable<String, Object>() {{
            put("content-type", "%{#context['com.opensymphony.xwork2.dispatcher.HttpServletResponse'].addHeader('cuXaxm3h'");
        }});
        final Response response = frontEndSockShop.get(request, "/");
        assertStatusCode(response.code(), 200);
        assertCSSselect("div#hot div.box div.container div h2", "Hot this week", response.body().string());
    }

    @Test
    public void testGet313() throws MalformedURLException, IOException
    {
        // GET http://front-end.sock-shop/ (endp 313)
        final HttpTarget frontEndSockShop = getHttpClient("http://front-end.sock-shop", new Authentication());
        final HttpRequest request = new HttpRequest();
        request.setHeaders(new Hashtable<String, Object>() {{
            put("content-type", "%{#context['com.opensymphony.xwork2.dispatcher.HttpServletResponse'].addHeader('NdNYddIL'");
        }});
        final Response response = frontEndSockShop.get(request, "/");
        assertStatusCode(response.code(), 200);
        assertCSSselect("div#hot div.box div.container div h2", "Hot this week", response.body().string());
    }

    @Test
    public void testGet314() throws MalformedURLException, IOException
    {
        // GET http://front-end.sock-shop/ (endp 314)
        final HttpTarget frontEndSockShop = getHttpClient("http://front-end.sock-shop", new Authentication());
        final HttpRequest request = new HttpRequest();
        request.setHeaders(new Hashtable<String, Object>() {{
            put("content-type", "%{#context['com.opensymphony.xwork2.dispatcher.HttpServletResponse'].addHeader('eRpkYaWi'");
        }});
        final Response response = frontEndSockShop.get(request, "/");
        assertStatusCode(response.code(), 200);
        assertCSSselect("div#hot div.box div.container div h2", "Hot this week", response.body().string());
    }

    @ParameterizedTest
    @JsonFileSource(resources = "/dataset_55.json")
    public void testGetParam055(final JsonObject json) throws MalformedURLException, IOException
    {
        final String param = json.getString("param");

        // GET http://front-end.sock-shop/{param} (endp 55)
        final HttpTarget frontEndSockShop = getHttpClient("http://front-end.sock-shop", new Authentication());
        final HttpRequest request = new HttpRequest();
        request.setHeaders(new Hashtable<String, Object>() {{
            put("x-requested-with", "XMLHttpRequest");
        }});
        final Response response = frontEndSockShop.get(request, "/" + param);
        assertStatusCode(response.code(), 200);
        assertCSSselect("div#top div.container div.offer a.btn.btn-success.btn-sm", "Offer of the day", response.body().string());
    }

    @ParameterizedTest
    @JsonFileSource(resources = "/dataset_151.json")
    public void testGetParam151(final JsonObject json) throws MalformedURLException, IOException
    {
        final String param = json.getString("param");

        // GET http://front-end.sock-shop/{param} (endp 151)
        final HttpTarget frontEndSockShop = getHttpClient("http://front-end.sock-shop", new Authentication());
        final HttpRequest request = new HttpRequest();
        request.setHeaders(new Hashtable<String, Object>() {{
            put("x-requested-with", "XMLHttpRequest");
        }});
        final Response response = frontEndSockShop.get(request, "/" + param);
        assertStatusCode(response.code(), 200);
    }

    @ParameterizedTest
    @JsonFileSource(resources = "/dataset_208.json")
    public void testGetParamIndexHtml208(final JsonObject json) throws MalformedURLException, IOException
    {
        final String param = json.getString("param");

        // GET http://front-end.sock-shop/{param}/../index.html (endp 208)
        final HttpTarget frontEndSockShop = getHttpClient("http://front-end.sock-shop", new Authentication());
        final HttpRequest request = new HttpRequest();
        final Response response = frontEndSockShop.get(request, "/" + param + "/../index.html");
        assertStatusCode(response.code(), 200);
        assertCSSselect("div#hot div.box div.container div h2", "Hot this week", response.body().string());
    }

    @ParameterizedTest
    @JsonFileSource(resources = "/dataset_126.json")
    public void testPostLicensesLicenseid126(final JsonObject json) throws MalformedURLException, IOException
    {
        final String licenseId = json.getString("licenseId");

        // POST http://front-end.sock-shop/Licenses/{licenseId} (endp 126)
        final HttpTarget frontEndSockShop = getHttpClient("http://front-end.sock-shop", new Authentication());
        final HttpRequest request = new HttpRequest();
        request.setFormData(new Hashtable<String, Object>() {{
            put("chk", "Test");
        }});
        request.setHeaders(new Hashtable<String, Object>() {{
            put("content-type", "application/x-www-form-urlencoded");
        }});
        final Response response = frontEndSockShop.post(request, "/Licenses/" + licenseId);
        assertStatusCode(response.code(), 100);
    }

    @Test
    public void testGetSitescope123() throws MalformedURLException, IOException
    {
        // GET http://front-end.sock-shop/SiteScope/ (endp 123)
        final HttpTarget frontEndSockShop = getHttpClient("http://front-end.sock-shop", new Authentication());
        final HttpRequest request = new HttpRequest();
        final Response response = frontEndSockShop.get(request, "/SiteScope/");
        assertStatusCode(response.code(), 200);
        assertCSSselect("div#hot div.box div.container div h2", "Hot this week", response.body().string());
    }

    @Test
    public void testGetAddress068() throws MalformedURLException, IOException
    {
        // GET http://front-end.sock-shop/address (endp 68)
        final HttpTarget frontEndSockShop = getHttpClient("http://front-end.sock-shop", new Authentication());
        final HttpRequest request = new HttpRequest();
        request.setHeaders(new Hashtable<String, Object>() {{
            put("x-requested-with", "XMLHttpRequest");
        }});
        final Response response = frontEndSockShop.get(request, "/address");
        assertStatusCode(response.code(), 200);
        assertJSONPath("$.city", "Glasgow", response.body().string());
    }

    @Test
    public void testGetAddress168() throws MalformedURLException, IOException
    {
        // GET http://front-end.sock-shop/address (endp 168)
        final HttpTarget frontEndSockShop = getHttpClient("http://front-end.sock-shop", new Authentication());
        final HttpRequest request = new HttpRequest();
        request.setHeaders(new Hashtable<String, Object>() {{
            put("x-requested-with", "XMLHttpRequest");
        }});
        final Response response = frontEndSockShop.get(request, "/address");
        assertStatusCode(response.code(), 200);
    }

    @ParameterizedTest
    @JsonFileSource(resources = "/dataset_169.json")
    public void testPostAddresses169(final JsonObject json) throws MalformedURLException, IOException
    {
        final String number = json.getString("number");
        final String postcode = json.getString("postcode");

        // POST http://front-end.sock-shop/addresses (endp 169)
        final HttpTarget frontEndSockShop = getHttpClient("http://front-end.sock-shop", new Authentication());
        final HttpRequest request = new HttpRequest();
        request.setHeaders(new Hashtable<String, Object>() {{
            put("content-type", "application/json");
            put("x-requested-with", "XMLHttpRequest");
        }});
        request.setJsonBody("payload_for_endp_169.json", new Hashtable<String, Object>() {{
            put("$.number", number);
            put("$.postcode", postcode);
        }});
        final Response response = frontEndSockShop.post(request, "/addresses");
        assertStatusCode(response.code(), 200);
    }

    @Test
    public void testGetBasketHtml013() throws MalformedURLException, IOException
    {
        // GET http://front-end.sock-shop/basket.html (endp 13)
        final HttpTarget frontEndSockShop = getHttpClient("http://front-end.sock-shop", new Authentication());
        final HttpRequest request = new HttpRequest();
        final Response response = frontEndSockShop.get(request, "/basket.html");
        assertStatusCode(response.code(), 201);
    }

    @Test
    public void testGetBasketHtml014() throws MalformedURLException, IOException
    {
        // GET http://front-end.sock-shop/basket.html (endp 14)
        final HttpTarget frontEndSockShop = getHttpClient("http://front-end.sock-shop", new Authentication());
        final HttpRequest request = new HttpRequest();
        final Response response = frontEndSockShop.get(request, "/basket.html");
        assertStatusCode(response.code(), 200);
        assertCSSselect("div#basket div.box form h1", "Shopping cart", response.body().string());
    }

    @Test
    public void testGetBasketHtml170() throws MalformedURLException, IOException
    {
        // GET http://front-end.sock-shop/basket.html (endp 170)
        final HttpTarget frontEndSockShop = getHttpClient("http://front-end.sock-shop", new Authentication());
        final HttpRequest request = new HttpRequest();
        final Response response = frontEndSockShop.get(request, "/basket.html");
        assertStatusCode(response.code(), 200);
        assertCSSselect("div#basket div.box form h1", "Shopping cart", response.body().string());
    }

    @Test
    public void testGetC103() throws MalformedURLException, IOException
    {
        // GET http://front-end.sock-shop/c (endp 103)
        final HttpTarget frontEndSockShop = getHttpClient("http://front-end.sock-shop", new Authentication());
        final HttpRequest request = new HttpRequest();
        final Response response = frontEndSockShop.get(request, "/c");
        assertStatusCode(response.code(), 200);
        assertCSSselect("div#hot div.box div.container div h2", "Hot this week", response.body().string());
    }

    @Test
    public void testGetCard070() throws MalformedURLException, IOException
    {
        // GET http://front-end.sock-shop/card (endp 70)
        final HttpTarget frontEndSockShop = getHttpClient("http://front-end.sock-shop", new Authentication());
        final HttpRequest request = new HttpRequest();
        request.setHeaders(new Hashtable<String, Object>() {{
            put("x-requested-with", "XMLHttpRequest");
        }});
        final Response response = frontEndSockShop.get(request, "/card");
        assertStatusCode(response.code(), 200);
    }

    @Test
    public void testGetCard171() throws MalformedURLException, IOException
    {
        // GET http://front-end.sock-shop/card (endp 171)
        final HttpTarget frontEndSockShop = getHttpClient("http://front-end.sock-shop", new Authentication());
        final HttpRequest request = new HttpRequest();
        request.setHeaders(new Hashtable<String, Object>() {{
            put("x-requested-with", "XMLHttpRequest");
        }});
        final Response response = frontEndSockShop.get(request, "/card");
        assertStatusCode(response.code(), 200);
    }

    @ParameterizedTest
    @JsonFileSource(resources = "/dataset_172.json")
    public void testPostCards172(final JsonObject json) throws MalformedURLException, IOException
    {
        final String ccv = json.getString("ccv");
        final String expires = json.getString("expires");
        final String longNum = json.getString("longNum");

        // POST http://front-end.sock-shop/cards (endp 172)
        final HttpTarget frontEndSockShop = getHttpClient("http://front-end.sock-shop", new Authentication());
        final HttpRequest request = new HttpRequest();
        request.setHeaders(new Hashtable<String, Object>() {{
            put("content-type", "application/json");
            put("x-requested-with", "XMLHttpRequest");
        }});
        request.setJsonBody("payload_for_endp_172.json", new Hashtable<String, Object>() {{
            put("$.ccv", ccv);
            put("$.expires", expires);
            put("$.longNum", longNum);
        }});
        final Response response = frontEndSockShop.post(request, "/cards");
        assertStatusCode(response.code(), 200);
    }

    @Test
    public void testPostCart016() throws MalformedURLException, IOException
    {
        // POST http://front-end.sock-shop/orders (endp 21)
        final HttpTarget frontEndSockShop = getHttpClient("http://front-end.sock-shop", new Authentication());
        final HttpRequest request = new HttpRequest();
        request.setHeaders(new Hashtable<String, Object>() {{
            put("x-requested-with", "XMLHttpRequest");
        }});
        final Response response = frontEndSockShop.post(request, "/orders");
        assertStatusCode(response.code(), 201);
        assertJSONPath("$.address.city", "Glasgow", response.body().string());
        final String id = JSONPath("$.items[*].itemId", response.body().string());

        // POST http://front-end.sock-shop/cart (endp 16)
        final HttpRequest request2 = new HttpRequest();
        request2.setHeaders(new Hashtable<String, Object>() {{
            put("content-type", "application/json");
            put("x-requested-with", "XMLHttpRequest");
        }});
        request2.setJsonBody("payload_for_endp_16.json", new Hashtable<String, Object>() {{
            put("$.id", id);
        }});
        final Response response2 = frontEndSockShop.post(request2, "/cart");
        assertStatusCode(response2.code(), 201);
    }

    @ParameterizedTest
    @JsonFileSource(resources = "/dataset_33.json")
    public void testPostCart033(final JsonObject json) throws MalformedURLException, IOException
    {
        final String size = json.getString("size");
        final String tags = json.getString("tags");

        // GET http://front-end.sock-shop/catalogue (endp 17)
        final HttpTarget frontEndSockShop = getHttpClient("http://front-end.sock-shop", new Authentication());
        final HttpRequest request = new HttpRequest();
        request.setQueryString(new Hashtable<String, Object>() {{
            put("page", "1");
            put("size", size);
            put("sort", "id");
            put("tags", tags);
        }});
        request.setHeaders(new Hashtable<String, Object>() {{
            put("x-requested-with", "XMLHttpRequest");
        }});
        final Response response = frontEndSockShop.get(request, "/catalogue");
        assertStatusCode(response.code(), 200);
        final String id = JSONPath("$[*].id", response.body().string());

        // POST http://front-end.sock-shop/cart (endp 33)
        final HttpRequest request2 = new HttpRequest();
        request2.setHeaders(new Hashtable<String, Object>() {{
            put("content-type", "application/json");
        }});
        request2.setJsonBody("payload_for_endp_33.json", new Hashtable<String, Object>() {{
            put("$.id", id);
        }});
        final Response response2 = frontEndSockShop.post(request2, "/cart");
        assertStatusCode(response2.code(), 202);
    }

    @Test
    public void testDeleteCart039() throws MalformedURLException, IOException
    {
        // DELETE http://front-end.sock-shop/cart (endp 39)
        final HttpTarget frontEndSockShop = getHttpClient("http://front-end.sock-shop", new Authentication());
        final HttpRequest request = new HttpRequest();
        final Response response = frontEndSockShop.delete(request, "/cart");
        assertStatusCode(response.code(), 200);
        assertCSSselect("div#content div.container div div.row.same-height-row div div.box.same-height h3", "You may also like these products", response.body().string());
    }

    @Test
    public void testGetCart047() throws MalformedURLException, IOException
    {
        // GET http://front-end.sock-shop/cart (endp 47)
        final HttpTarget frontEndSockShop = getHttpClient("http://front-end.sock-shop", new Authentication());
        final HttpRequest request = new HttpRequest();
        request.setHeaders(new Hashtable<String, Object>() {{
            put("x-requested-with", "XMLHttpRequest");
        }});
        final Response response = frontEndSockShop.get(request, "/cart");
        assertStatusCode(response.code(), 200);
    }

    @Test
    public void testGetCart063() throws MalformedURLException, IOException
    {
        // GET http://front-end.sock-shop/cart (endp 63)
        final HttpTarget frontEndSockShop = getHttpClient("http://front-end.sock-shop", new Authentication());
        final HttpRequest request = new HttpRequest();
        request.setHeaders(new Hashtable<String, Object>() {{
            put("x-requested-with", "XMLHttpRequest");
        }});
        final Response response = frontEndSockShop.get(request, "/cart");
        assertStatusCode(response.code(), 200);
        assertCSSselect("div#copyright div.container div p.pull-left a", "Weaveworks", response.body().string());
    }

    @Test
    public void testPostCart174() throws MalformedURLException, IOException
    {
        // GET http://front-end.sock-shop/cart (endp 146)
        final HttpTarget frontEndSockShop = getHttpClient("http://front-end.sock-shop", new Authentication());
        final HttpRequest request = new HttpRequest();
        request.setHeaders(new Hashtable<String, Object>() {{
            put("x-requested-with", "XMLHttpRequest");
        }});
        final Response response = frontEndSockShop.get(request, "/cart");
        assertStatusCode(response.code(), 200);
        final String id = JSONPath("$[*].itemId", response.body().string());

        // POST http://front-end.sock-shop/cart (endp 174)
        final HttpRequest request2 = new HttpRequest();
        request2.setHeaders(new Hashtable<String, Object>() {{
            put("content-type", "application/json");
            put("x-requested-with", "XMLHttpRequest");
        }});
        request2.setJsonBody("payload_for_endp_174.json", new Hashtable<String, Object>() {{
            put("$.id", id);
        }});
        final Response response2 = frontEndSockShop.post(request2, "/cart");
        assertStatusCode(response2.code(), 201);
    }

    @Test
    public void testDeleteCart175() throws MalformedURLException, IOException
    {
        // DELETE http://front-end.sock-shop/cart (endp 175)
        final HttpTarget frontEndSockShop = getHttpClient("http://front-end.sock-shop", new Authentication());
        final HttpRequest request = new HttpRequest();
        request.setHeaders(new Hashtable<String, Object>() {{
            put("x-requested-with", "XMLHttpRequest");
        }});
        final Response response = frontEndSockShop.delete(request, "/cart");
        assertStatusCode(response.code(), 202);
    }

    @Test
    public void testDeleteCart286() throws MalformedURLException, IOException
    {
        // DELETE http://front-end.sock-shop/cart (endp 286)
        final HttpTarget frontEndSockShop = getHttpClient("http://front-end.sock-shop", new Authentication());
        final HttpRequest request = new HttpRequest();
        request.setHeaders(new Hashtable<String, Object>() {{
            put("content-type", "application/x-www-form-urlencoded");
            put("x-requested-with", "XMLHttpRequest");
        }});
        final Response response = frontEndSockShop.delete(request, "/cart");
        assertStatusCode(response.code(), 202);
    }

    @Test
    public void testGetCatalogue046() throws MalformedURLException, IOException
    {
        // GET http://front-end.sock-shop/catalogue (endp 46)
        final HttpTarget frontEndSockShop = getHttpClient("http://front-end.sock-shop", new Authentication());
        final HttpRequest request = new HttpRequest();
        final Response response = frontEndSockShop.get(request, "/catalogue");
        assertStatusCode(response.code(), 201);
        assertJSONPath("$.address.city", "Glasgow", response.body().string());
    }

    @ParameterizedTest
    @JsonFileSource(resources = "/dataset_65.json")
    public void testGetCatalogue065(final JsonObject json) throws MalformedURLException, IOException
    {
        final String size = json.getString("size");

        // GET http://front-end.sock-shop/catalogue (endp 65)
        final HttpTarget frontEndSockShop = getHttpClient("http://front-end.sock-shop", new Authentication());
        final HttpRequest request = new HttpRequest();
        request.setQueryString(new Hashtable<String, Object>() {{
            put("size", size);
        }});
        request.setHeaders(new Hashtable<String, Object>() {{
            put("x-requested-with", "XMLHttpRequest");
        }});
        final Response response = frontEndSockShop.get(request, "/catalogue");
        assertStatusCode(response.code(), 200);
    }

    @ParameterizedTest
    @JsonFileSource(resources = "/dataset_121.json")
    public void testGetCatalogue121(final JsonObject json) throws MalformedURLException, IOException
    {
        final String size = json.getString("size");

        // GET http://front-end.sock-shop/catalogue (endp 121)
        final HttpTarget frontEndSockShop = getHttpClient("http://front-end.sock-shop", new Authentication());
        final HttpRequest request = new HttpRequest();
        request.setQueryString(new Hashtable<String, Object>() {{
            put("page", "1");
            put("size", size);
            put("tags", "large");
        }});
        request.setHeaders(new Hashtable<String, Object>() {{
            put("x-requested-with", "XMLHttpRequest");
        }});
        final Response response = frontEndSockShop.get(request, "/catalogue");
        assertStatusCode(response.code(), 200);
    }

    @ParameterizedTest
    @JsonFileSource(resources = "/dataset_48.json")
    public void testGetCatalogueId048(final JsonObject json) throws MalformedURLException, IOException
    {
        final String page = json.getString("page");
        final String size = json.getString("size");
        final String tags = json.getString("tags");

        // GET http://front-end.sock-shop/catalogue (endp 147)
        final HttpTarget frontEndSockShop = getHttpClient("http://front-end.sock-shop", new Authentication());
        final HttpRequest request = new HttpRequest();
        request.setQueryString(new Hashtable<String, Object>() {{
            put("page", page);
            put("size", size);
            put("sort", "id");
            put("tags", tags);
        }});
        request.setHeaders(new Hashtable<String, Object>() {{
            put("x-requested-with", "XMLHttpRequest");
        }});
        final Response response = frontEndSockShop.get(request, "/catalogue");
        assertStatusCode(response.code(), 200);
        final String id = JSONPath("$[*].id", response.body().string());

        // GET http://front-end.sock-shop/catalogue/{id} (endp 48)
        final HttpRequest request2 = new HttpRequest();
        request2.setHeaders(new Hashtable<String, Object>() {{
            put("x-requested-with", "XMLHttpRequest");
        }});
        final Response response2 = frontEndSockShop.get(request2, "/catalogue/" + id);
        assertStatusCode(response2.code(), 200);
    }

    @ParameterizedTest
    @JsonFileSource(resources = "/dataset_166.json")
    public void testGetCatalogueId166(final JsonObject json) throws MalformedURLException, IOException
    {
        final String page = json.getString("page");
        final String size = json.getString("size");
        final String tags = json.getString("tags");

        // GET http://front-end.sock-shop/catalogue (endp 147)
        final HttpTarget frontEndSockShop = getHttpClient("http://front-end.sock-shop", new Authentication());
        final HttpRequest request = new HttpRequest();
        request.setQueryString(new Hashtable<String, Object>() {{
            put("page", page);
            put("size", size);
            put("sort", "id");
            put("tags", tags);
        }});
        request.setHeaders(new Hashtable<String, Object>() {{
            put("x-requested-with", "XMLHttpRequest");
        }});
        final Response response = frontEndSockShop.get(request, "/catalogue");
        assertStatusCode(response.code(), 200);
        final String id = JSONPath("$[*].id", response.body().string());

        // GET http://front-end.sock-shop/catalogue/{id} (endp 166)
        final HttpRequest request2 = new HttpRequest();
        request2.setHeaders(new Hashtable<String, Object>() {{
            put("x-requested-with", "XMLHttpRequest");
        }});
        final Response response2 = frontEndSockShop.get(request2, "/catalogue/" + id);
        assertStatusCode(response2.code(), 200);
    }

    @Test
    public void testGetCatalogueSize075() throws MalformedURLException, IOException
    {
        // GET http://front-end.sock-shop/tags (endp 83)
        final HttpTarget frontEndSockShop = getHttpClient("http://front-end.sock-shop", new Authentication());
        final HttpRequest request = new HttpRequest();
        request.setHeaders(new Hashtable<String, Object>() {{
            put("x-requested-with", "XMLHttpRequest");
        }});
        final Response response = frontEndSockShop.get(request, "/tags");
        assertStatusCode(response.code(), 200);
        final String tags = JSONPath("$.tags[*]", response.body().string());

        // GET http://front-end.sock-shop/catalogue/size (endp 75)
        final HttpRequest request2 = new HttpRequest();
        request2.setQueryString(new Hashtable<String, Object>() {{
            put("tags", tags);
        }});
        request2.setHeaders(new Hashtable<String, Object>() {{
            put("x-requested-with", "XMLHttpRequest");
        }});
        final Response response2 = frontEndSockShop.get(request2, "/catalogue/size");
        assertStatusCode(response2.code(), 200);
    }

    @Test
    public void testGetCatalogueSize177() throws MalformedURLException, IOException
    {
        // GET http://front-end.sock-shop/catalogue/size (endp 177)
        final HttpTarget frontEndSockShop = getHttpClient("http://front-end.sock-shop", new Authentication());
        final HttpRequest request = new HttpRequest();
        request.setQueryString(new Hashtable<String, Object>() {{
            put("tags", "");
        }});
        request.setHeaders(new Hashtable<String, Object>() {{
            put("x-requested-with", "XMLHttpRequest");
        }});
        final Response response = frontEndSockShop.get(request, "/catalogue/size");
        assertStatusCode(response.code(), 200);
    }

    @ParameterizedTest
    @JsonFileSource(resources = "/dataset_18.json")
    public void testGetCategoryHtml018(final JsonObject json) throws MalformedURLException, IOException
    {
        final String tags = json.getString("tags");

        // GET http://front-end.sock-shop/category.html (endp 18)
        final HttpTarget frontEndSockShop = getHttpClient("http://front-end.sock-shop", new Authentication());
        final HttpRequest request = new HttpRequest();
        request.setQueryString(new Hashtable<String, Object>() {{
            put("tags", tags);
        }});
        final Response response = frontEndSockShop.get(request, "/category.html");
        assertStatusCode(response.code(), 200);
        assertCSSselect("div#content div.container div div.row.same-height-row div div.box.same-height h3", "You may also like these products", response.body().string());
    }

    @Test
    public void testGetCategoryHtml179() throws MalformedURLException, IOException
    {
        // GET http://front-end.sock-shop/category.html (endp 179)
        final HttpTarget frontEndSockShop = getHttpClient("http://front-end.sock-shop", new Authentication());
        final HttpRequest request = new HttpRequest();
        request.setQueryString(new Hashtable<String, Object>() {{
            put("page", "2");
        }});
        final Response response = frontEndSockShop.get(request, "/category.html");
        assertStatusCode(response.code(), 200);
        assertCSSselect("div#content div.container div div.panel.panel-default.sidebar-menu div.panel-heading h3.panel-title", "Filters ", response.body().string());
    }

    @ParameterizedTest
    @JsonFileSource(resources = "/dataset_77.json")
    public void testGetCustomerOrderHtml077(final JsonObject json) throws MalformedURLException, IOException
    {
        final String order = json.getString("order");

        // GET http://front-end.sock-shop/customer-order.html (endp 77)
        final HttpTarget frontEndSockShop = getHttpClient("http://front-end.sock-shop", new Authentication());
        final HttpRequest request = new HttpRequest();
        request.setQueryString(new Hashtable<String, Object>() {{
            put("order", order);
        }});
        final Response response = frontEndSockShop.get(request, "/customer-order.html");
        assertStatusCode(response.code(), 200);
        assertCSSselect("div#customer-order div.box h2", "Order #", response.body().string());
    }

    @ParameterizedTest
    @JsonFileSource(resources = "/dataset_180.json")
    public void testGetCustomerOrderHtml180(final JsonObject json) throws MalformedURLException, IOException
    {
        final String order = json.getString("order");

        // GET http://front-end.sock-shop/customer-order.html (endp 180)
        final HttpTarget frontEndSockShop = getHttpClient("http://front-end.sock-shop", new Authentication());
        final HttpRequest request = new HttpRequest();
        request.setQueryString(new Hashtable<String, Object>() {{
            put("order", order);
        }});
        final Response response = frontEndSockShop.get(request, "/customer-order.html");
        assertStatusCode(response.code(), 200);
        assertCSSselect("div#customer-order div.box h2", "Order #", response.body().string());
    }

    @Test
    public void testGetCustomerOrdersHtml078() throws MalformedURLException, IOException
    {
        // GET http://front-end.sock-shop/customer-orders.html (endp 78)
        final HttpTarget frontEndSockShop = getHttpClient("http://front-end.sock-shop", new Authentication());
        final HttpRequest request = new HttpRequest();
        final Response response = frontEndSockShop.get(request, "/customer-orders.html");
        assertStatusCode(response.code(), 200);
        assertCSSselect("div#customer-orders div.box h1", "My orders", response.body().string());
    }

    @Test
    public void testGetCustomerOrdersHtml181() throws MalformedURLException, IOException
    {
        // GET http://front-end.sock-shop/customer-orders.html (endp 181)
        final HttpTarget frontEndSockShop = getHttpClient("http://front-end.sock-shop", new Authentication());
        final HttpRequest request = new HttpRequest();
        final Response response = frontEndSockShop.get(request, "/customer-orders.html");
        assertStatusCode(response.code(), 200);
        assertCSSselect("div#customer-orders div.box h1", "My orders", response.body().string());
    }

    @Test
    public void testGetCustomersCustomerid050() throws MalformedURLException, IOException
    {
        // GET http://front-end.sock-shop/customers/{customerId} (endp 50)
        final HttpTarget frontEndSockShop = getHttpClient("http://front-end.sock-shop", new Authentication());
        final HttpRequest request = new HttpRequest();
        request.setHeaders(new Hashtable<String, Object>() {{
            put("x-requested-with", "XMLHttpRequest");
        }});
        final Response response = frontEndSockShop.get(request, "/customers/" + getCookie(response, "logged_in"));
        assertStatusCode(response.code(), 200);
    }

    @Test
    public void testGetCustomersCustomerid148() throws MalformedURLException, IOException
    {
        // GET http://front-end.sock-shop/customers/{customerId} (endp 148)
        final HttpTarget frontEndSockShop = getHttpClient("http://front-end.sock-shop", new Authentication());
        final HttpRequest request = new HttpRequest();
        request.setHeaders(new Hashtable<String, Object>() {{
            put("x-requested-with", "XMLHttpRequest");
        }});
        final Response response = frontEndSockShop.get(request, "/customers/" + getCookie(response, "logged_in"));
        assertStatusCode(response.code(), 200);
    }

    @Test
    public void testGetCustomersWcbvljjnpzpezacrwupvwuuquepxsbhz163() throws MalformedURLException, IOException
    {
        // GET http://front-end.sock-shop/customers/wcbVLjJnpzpezACrWupvwuuQUEpXSBhZ (endp 163)
        final HttpTarget frontEndSockShop = getHttpClient("http://front-end.sock-shop", new Authentication());
        final HttpRequest request = new HttpRequest();
        request.setHeaders(new Hashtable<String, Object>() {{
            put("x-requested-with", "XMLHttpRequest");
        }});
        final Response response = frontEndSockShop.get(request, "/customers/wcbVLjJnpzpezACrWupvwuuQUEpXSBhZ");
        assertStatusCode(response.code(), 200);
        assertJSONPath("$.lastName", "Name", response.body().string());
    }

    @Test
    public void testGetDetailHtml019() throws MalformedURLException, IOException
    {
        // POST http://front-end.sock-shop/orders (endp 21)
        final HttpTarget frontEndSockShop = getHttpClient("http://front-end.sock-shop", new Authentication());
        final HttpRequest request = new HttpRequest();
        request.setHeaders(new Hashtable<String, Object>() {{
            put("x-requested-with", "XMLHttpRequest");
        }});
        final Response response = frontEndSockShop.post(request, "/orders");
        assertStatusCode(response.code(), 201);
        assertJSONPath("$.address.city", "Glasgow", response.body().string());
        final String id = JSONPath("$.items[*].itemId", response.body().string());

        // GET http://front-end.sock-shop/detail.html (endp 19)
        final HttpRequest request2 = new HttpRequest();
        request2.setQueryString(new Hashtable<String, Object>() {{
            put("id", id);
        }});
        final Response response2 = frontEndSockShop.get(request2, "/detail.html");
        assertStatusCode(response2.code(), 200);
        assertCSSselect("div#content div.container div div.row.same-height-row div div.box.same-height h3", "You may also like these products", response2.body().string());
    }

    @ParameterizedTest
    @JsonFileSource(resources = "/dataset_183.json")
    public void testGetDetailHtml183(final JsonObject json) throws MalformedURLException, IOException
    {
        final String page = json.getString("page");
        final String size = json.getString("size");
        final String tags = json.getString("tags");

        // GET http://front-end.sock-shop/catalogue (endp 147)
        final HttpTarget frontEndSockShop = getHttpClient("http://front-end.sock-shop", new Authentication());
        final HttpRequest request = new HttpRequest();
        request.setQueryString(new Hashtable<String, Object>() {{
            put("page", page);
            put("size", size);
            put("sort", "id");
            put("tags", tags);
        }});
        request.setHeaders(new Hashtable<String, Object>() {{
            put("x-requested-with", "XMLHttpRequest");
        }});
        final Response response = frontEndSockShop.get(request, "/catalogue");
        assertStatusCode(response.code(), 200);
        final String id = JSONPath("$[*].id", response.body().string());

        // GET http://front-end.sock-shop/detail.html (endp 183)
        final HttpRequest request2 = new HttpRequest();
        request2.setQueryString(new Hashtable<String, Object>() {{
            put("id", id);
        }});
        final Response response2 = frontEndSockShop.get(request2, "/detail.html");
        assertStatusCode(response2.code(), 200);
        assertCSSselect("div#content div.container div div.row.same-height-row div div.box.same-height h3", "You may also like these products", response2.body().string());
    }

    @Test
    public void testGetFooterHtml054() throws MalformedURLException, IOException
    {
        // GET http://front-end.sock-shop/footer.html (endp 54)
        final HttpTarget frontEndSockShop = getHttpClient("http://front-end.sock-shop", new Authentication());
        final HttpRequest request = new HttpRequest();
        request.setHeaders(new Hashtable<String, Object>() {{
            put("x-requested-with", "XMLHttpRequest");
        }});
        final Response response = frontEndSockShop.get(request, "/footer.html");
        assertStatusCode(response.code(), 200);
        assertCSSselect("div#copyright div.container div p.pull-left a", "Weaveworks", response.body().string());
    }

    @Test
    public void testGetFooterHtml101() throws MalformedURLException, IOException
    {
        // GET http://front-end.sock-shop/footer.html (endp 101)
        final HttpTarget frontEndSockShop = getHttpClient("http://front-end.sock-shop", new Authentication());
        final HttpRequest request = new HttpRequest();
        request.setHeaders(new Hashtable<String, Object>() {{
            put("x-requested-with", "XMLHttpRequest");
        }});
        final Response response = frontEndSockShop.get(request, "/footer.html");
        assertStatusCode(response.code(), 200);
    }

    @Test
    public void testGetFooterHtml149() throws MalformedURLException, IOException
    {
        // GET http://front-end.sock-shop/footer.html (endp 149)
        final HttpTarget frontEndSockShop = getHttpClient("http://front-end.sock-shop", new Authentication());
        final HttpRequest request = new HttpRequest();
        request.setHeaders(new Hashtable<String, Object>() {{
            put("x-requested-with", "XMLHttpRequest");
        }});
        final Response response = frontEndSockShop.get(request, "/footer.html");
        assertStatusCode(response.code(), 200);
        assertCSSselect("div#copyright div.container div p.pull-left a", "Weaveworks", response.body().string());
    }

    @ParameterizedTest
    @JsonFileSource(resources = "/dataset_61.json")
    public void testGetIndexHtml061(final JsonObject json) throws MalformedURLException, IOException
    {
        final String urlmaskfilter = json.getString("urlmaskfilter");

        // GET http://front-end.sock-shop/index.html (endp 61)
        final HttpTarget frontEndSockShop = getHttpClient("http://front-end.sock-shop", new Authentication());
        final HttpRequest request = new HttpRequest();
        request.setQueryString(new Hashtable<String, Object>() {{
            put("urlmaskfilter", urlmaskfilter);
        }});
        final Response response = frontEndSockShop.get(request, "/index.html");
        assertStatusCode(response.code(), 200);
        assertCSSselect("div#hot div.box div.container div h2", "Hot this week", response.body().string());
    }

    @ParameterizedTest
    @JsonFileSource(resources = "/dataset_184.json")
    public void testGetIndexHtml184(final JsonObject json) throws MalformedURLException, IOException
    {
        final String findcli = json.getString("findcli");

        // GET http://front-end.sock-shop/index.html (endp 184)
        final HttpTarget frontEndSockShop = getHttpClient("http://front-end.sock-shop", new Authentication());
        final HttpRequest request = new HttpRequest();
        request.setQueryString(new Hashtable<String, Object>() {{
            put("findcli", findcli);
            put("test", "");
        }});
        final Response response = frontEndSockShop.get(request, "/index.html");
        assertStatusCode(response.code(), 200);
        assertCSSselect("div#hot div.box div.container div h2", "Hot this week", response.body().string());
    }

    @Test
    public void testHeadIndexHtml210() throws MalformedURLException, IOException
    {
        // HEAD http://front-end.sock-shop/index.html (endp 210)
        final HttpTarget frontEndSockShop = getHttpClient("http://front-end.sock-shop", new Authentication());
        final HttpRequest request = new HttpRequest();
        final Response response = frontEndSockShop.head(request, "/index.html");
        assertStatusCode(response.code(), 200);
    }

    @ParameterizedTest
    @JsonFileSource(resources = "/dataset_95.json")
    public void testPostLibPhpunitPhpunitSrcUtilPhpEvalStdinPhp095(final JsonObject json) throws MalformedURLException, IOException
    {
        final String __ = json.getString("__");

        // POST http://front-end.sock-shop/lib/phpunit/phpunit/src/Util/PHP/eval-stdin.php (endp 95)
        final HttpTarget frontEndSockShop = getHttpClient("http://front-end.sock-shop", new Authentication());
        final HttpRequest request = new HttpRequest();
        request.setFormData(new Hashtable<String, Object>() {{
            put("<?", __);
            put("?>", "");
        }});
        request.setHeaders(new Hashtable<String, Object>() {{
            put("content-type", "application/x-www-form-urlencoded");
        }});
        final Response response = frontEndSockShop.post(request, "/lib/phpunit/phpunit/src/Util/PHP/eval-stdin.php");
        assertStatusCode(response.code(), 200);
        assertCSSselect("div#hot div.box div.container div h2", "Hot this week", response.body().string());
    }

    /**
     * authentication-related test
     */
    @Test
    public void testGetLogin020() throws MalformedURLException, IOException
    {
        // GET http://front-end.sock-shop/login (endp 20)
        final HttpTarget frontEndSockShop = getHttpClient("http://front-end.sock-shop", new DummyAuth());
        final HttpRequest request = new HttpRequest();
        request.setHeaders(new Hashtable<String, Object>() {{
            put("x-requested-with", "XMLHttpRequest");
        }});
        final Response response = frontEndSockShop.get(request, "/login");
        assertStatusCode(response.code(), 200);
        assertCSSselect("div#hot div.box div.container div h2", "Hot this week", response.body().string());
    }

    /**
     * authentication-related test
     */
    @Test
    public void testGetLogin150() throws MalformedURLException, IOException
    {
        // GET http://front-end.sock-shop/login (endp 150)
        final HttpTarget frontEndSockShop = getHttpClient("http://front-end.sock-shop", new DummyAuth());
        final HttpRequest request = new HttpRequest();
        request.setHeaders(new Hashtable<String, Object>() {{
            put("x-requested-with", "XMLHttpRequest");
        }});
        final Response response = frontEndSockShop.get(request, "/login");
        assertStatusCode(response.code(), 200);
        assertCSSselect("p", "Cookie is set", response.body().string());
    }

    @Test
    public void testGetMetrics215() throws MalformedURLException, IOException
    {
        // GET http://front-end.sock-shop/metrics (endp 215)
        final HttpTarget frontEndSockShop = getHttpClient("http://front-end.sock-shop", new Authentication());
        final HttpRequest request = new HttpRequest();
        final Response response = frontEndSockShop.get(request, "/metrics");
        assertStatusCode(response.code(), 200);
    }

    @Test
    public void testPostOrders022() throws MalformedURLException, IOException
    {
        // POST http://front-end.sock-shop/orders (endp 22)
        final HttpTarget frontEndSockShop = getHttpClient("http://front-end.sock-shop", new Authentication());
        final HttpRequest request = new HttpRequest();
        final Response response = frontEndSockShop.post(request, "/orders");
        assertStatusCode(response.code(), 200);
        assertCSSselect("div#hot div.box div.container div h2", "Hot this week", response.body().string());
    }

    @Test
    public void testGetOrders186() throws MalformedURLException, IOException
    {
        // GET http://front-end.sock-shop/orders (endp 186)
        final HttpTarget frontEndSockShop = getHttpClient("http://front-end.sock-shop", new Authentication());
        final HttpRequest request = new HttpRequest();
        request.setHeaders(new Hashtable<String, Object>() {{
            put("x-requested-with", "XMLHttpRequest");
        }});
        final Response response = frontEndSockShop.get(request, "/orders");
        assertStatusCode(response.code(), 201);
        assertJSONPath("$[*].address.city", "elsewhere", response.body().string());
    }

    @Test
    public void testPostOrders187() throws MalformedURLException, IOException
    {
        // POST http://front-end.sock-shop/orders (endp 187)
        final HttpTarget frontEndSockShop = getHttpClient("http://front-end.sock-shop", new Authentication());
        final HttpRequest request = new HttpRequest();
        request.setHeaders(new Hashtable<String, Object>() {{
            put("x-requested-with", "XMLHttpRequest");
        }});
        final Response response = frontEndSockShop.post(request, "/orders");
        assertStatusCode(response.code(), 201);
        assertJSONPath("$.address.city", "elsewhere", response.body().string());
    }

    @Test
    public void testGetOrdersId082() throws MalformedURLException, IOException
    {
        // GET http://front-end.sock-shop/orders (endp 80)
        final HttpTarget frontEndSockShop = getHttpClient("http://front-end.sock-shop", new Authentication());
        final HttpRequest request = new HttpRequest();
        request.setHeaders(new Hashtable<String, Object>() {{
            put("x-requested-with", "XMLHttpRequest");
        }});
        final Response response = frontEndSockShop.get(request, "/orders");
        assertStatusCode(response.code(), 201);
        assertJSONPath("$.[*].address.city", "Glasgow", response.body().string());
        final String id = urlPart("/2", JSONPath("$[*]._links.self.href", response.body().string()));

        // GET http://front-end.sock-shop/orders/{id} (endp 82)
        final HttpRequest request2 = new HttpRequest();
        request2.setHeaders(new Hashtable<String, Object>() {{
            put("x-requested-with", "XMLHttpRequest");
        }});
        final Response response2 = frontEndSockShop.get(request2, "/orders/" + id);
        assertStatusCode(response2.code(), 200);
        assertJSONPath("$.address.city", "Glasgow", response2.body().string());
    }

    @Test
    public void testGetOrdersId188() throws MalformedURLException, IOException
    {
        // GET http://front-end.sock-shop/orders (endp 80)
        final HttpTarget frontEndSockShop = getHttpClient("http://front-end.sock-shop", new Authentication());
        final HttpRequest request = new HttpRequest();
        request.setHeaders(new Hashtable<String, Object>() {{
            put("x-requested-with", "XMLHttpRequest");
        }});
        final Response response = frontEndSockShop.get(request, "/orders");
        assertStatusCode(response.code(), 201);
        assertJSONPath("$.[*].address.city", "Glasgow", response.body().string());
        final String id = urlPart("/2", JSONPath("$[*]._links.self.href", response.body().string()));

        // GET http://front-end.sock-shop/orders/{id} (endp 188)
        final HttpRequest request2 = new HttpRequest();
        request2.setHeaders(new Hashtable<String, Object>() {{
            put("x-requested-with", "XMLHttpRequest");
        }});
        final Response response2 = frontEndSockShop.get(request2, "/orders/" + id);
        assertStatusCode(response2.code(), 200);
        assertJSONPath("$.address.city", "elsewhere", response2.body().string());
    }

    @ParameterizedTest
    @JsonFileSource(resources = "/dataset_102.json")
    public void testPostPlusQiangPhp102(final JsonObject json) throws MalformedURLException, IOException
    {
        final String blbl = json.getString("blbl");

        // POST http://front-end.sock-shop/plus/qiang.php (endp 102)
        final HttpTarget frontEndSockShop = getHttpClient("http://front-end.sock-shop", new Authentication());
        final HttpRequest request = new HttpRequest();
        request.setFormData(new Hashtable<String, Object>() {{
            put("blbl", blbl);
        }});
        request.setHeaders(new Hashtable<String, Object>() {{
            put("content-type", "application/x-www-form-urlencoded");
        }});
        final Response response = frontEndSockShop.post(request, "/plus/qiang.php");
        assertStatusCode(response.code(), 200);
        assertCSSselect("div#hot div.box div.container div h2", "Hot this week", response.body().string());
    }

    /**
     * authentication-related test
     */
    @Test
    public void testGetPorLoginPswCsp066() throws MalformedURLException, IOException
    {
        // GET http://front-end.sock-shop/por/login_psw.csp (endp 66)
        final HttpTarget frontEndSockShop = getHttpClient("http://front-end.sock-shop", new DummyAuth());
        final HttpRequest request = new HttpRequest();
        final Response response = frontEndSockShop.get(request, "/por/login_psw.csp");
        assertStatusCode(response.code(), 200);
        assertCSSselect("div#hot div.box div.container div h2", "Hot this week", response.body().string());
    }

    /**
     * authentication-related test
     */
    @ParameterizedTest
    @JsonFileSource(resources = "/dataset_189.json")
    public void testPostRegister189(final JsonObject json) throws MalformedURLException, IOException
    {
        final String email = json.getString("email");
        final String firstName = json.getString("firstName");
        final String lastName = json.getString("lastName");
        final String password = json.getString("password");
        final String username = json.getString("username");

        // POST http://front-end.sock-shop/register (endp 189)
        final HttpTarget frontEndSockShop = getHttpClient("http://front-end.sock-shop", new DummyAuth());
        final HttpRequest request = new HttpRequest();
        request.setHeaders(new Hashtable<String, Object>() {{
            put("content-type", "application/json");
            put("x-requested-with", "XMLHttpRequest");
        }});
        request.setJsonBody("payload_for_endp_189.json", new Hashtable<String, Object>() {{
            put("$.email", email);
            put("$.firstName", firstName);
            put("$.lastName", lastName);
            put("$.password", password);
            put("$.username", username);
        }});
        final Response response = frontEndSockShop.post(request, "/register");
        assertStatusCode(response.code(), 200);
    }

    @Test
    public void testGetTags190() throws MalformedURLException, IOException
    {
        // GET http://front-end.sock-shop/tags (endp 190)
        final HttpTarget frontEndSockShop = getHttpClient("http://front-end.sock-shop", new Authentication());
        final HttpRequest request = new HttpRequest();
        request.setHeaders(new Hashtable<String, Object>() {{
            put("x-requested-with", "XMLHttpRequest");
        }});
        final Response response = frontEndSockShop.get(request, "/tags");
        assertStatusCode(response.code(), 200);
    }

    @Test
    public void testGetTopbarHtml056() throws MalformedURLException, IOException
    {
        // GET http://front-end.sock-shop/topbar.html (endp 56)
        final HttpTarget frontEndSockShop = getHttpClient("http://front-end.sock-shop", new Authentication());
        final HttpRequest request = new HttpRequest();
        request.setHeaders(new Hashtable<String, Object>() {{
            put("x-requested-with", "XMLHttpRequest");
        }});
        final Response response = frontEndSockShop.get(request, "/topbar.html");
        assertStatusCode(response.code(), 200);
        assertCSSselect("div#hot div.box div.container div h2", "Hot this week", response.body().string());
    }

    @Test
    public void testGetTopbarHtml152() throws MalformedURLException, IOException
    {
        // GET http://front-end.sock-shop/topbar.html (endp 152)
        final HttpTarget frontEndSockShop = getHttpClient("http://front-end.sock-shop", new Authentication());
        final HttpRequest request = new HttpRequest();
        request.setHeaders(new Hashtable<String, Object>() {{
            put("x-requested-with", "XMLHttpRequest");
        }});
        final Response response = frontEndSockShop.get(request, "/topbar.html");
        assertStatusCode(response.code(), 200);
        assertCSSselect("div#top div.container div.offer a.btn.btn-success.btn-sm", "Offer of the day", response.body().string());
    }

    @Test
    public void testGetWpIncludesWlwmanifestXml289() throws MalformedURLException, IOException
    {
        // GET http://front-end.sock-shop/wp-includes/wlwmanifest.xml (endp 289)
        final HttpTarget frontEndSockShop = getHttpClient("http://front-end.sock-shop", new Authentication());
        final HttpRequest request = new HttpRequest();
        final Response response = frontEndSockShop.get(request, "/wp-includes/wlwmanifest.xml");
        assertStatusCode(response.code(), 200);
        assertCSSselect("div#hot div.box div.container div h2", "Hot this week", response.body().string());
    }
}

