# HTTP Status Codes for APIs

Quick reference for choosing the right response code on a route.

---

## The pattern

| Range | Meaning | You usually... |
|-------|---------|----------------|
| **2xx** | Success | Return data or confirm the action worked |
| **4xx** | Client error | Their request was wrong or unauthorized |
| **5xx** | Server error | Something broke on your side |

---

## Success (2xx)

| Code | Name | When to use |
|------|------|-------------|
| **200** | OK | GET/PUT/PATCH succeeded; return the resource or result |
| **201** | Created | POST succeeded; a new resource exists |
| **204** | No Content | DELETE (or update) succeeded; nothing useful to return |

**Rule of thumb:** GET → 200 · create → 201 · delete with empty body → 204

---

## Client errors (4xx)

| Code | Name | When to use |
|------|------|-------------|
| **400** | Bad Request | Invalid JSON, missing required fields, bad query params |
| **401** | Unauthorized | Not logged in / missing or invalid auth token |
| **403** | Forbidden | Logged in, but not allowed to do this |
| **404** | Not Found | Resource ID doesn't exist (e.g. `GET /events/42`) |
| **405** | Method Not Allowed | Wrong HTTP method on a valid path (e.g. POST on a GET-only route) |
| **409** | Conflict | Request clashes with current state (duplicate email, already booked) |
| **422** | Unprocessable Entity | JSON is valid, but values fail validation (optional; some APIs use 400) |

### 401 vs 403 (easy mix-up)

```text
401  →  "Who are you?"     (no / bad credentials)
403  →  "I know you - but it's still a no."  (authenticated but not permitted)
```

### 404 for missing records

This project uses a consistent shape:

```json
{"error": "Not found"}
```

with status **404** — not 200 with an error body.

---

## Server errors (5xx)

| Code | Name | When to use |
|------|------|-------------|
| **500** | Internal Server Error | Unhandled exception, unexpected failure |
| **502** | Bad Gateway | Upstream service (DB, another API) failed while you were proxying |
| **503** | Service Unavailable | Temporarily down / overloaded / maintenance |

You rarely set 5xx on purpose in route logic — they usually mean a bug or outage.

---

## Common API route map

| Action | Method + path | Success | Typical errors |
|--------|---------------|---------|----------------|
| List | `GET /events` | 200 | 401 |
| Create | `POST /events` | 201 | 400, 401, 403 |
| Read one | `GET /events/<id>` | 200 | 404, 401 |
| Update | `PUT/PATCH /events/<id>` | 200 | 400, 404, 401, 403 |
| Delete | `DELETE /events/<id>` | 204 | 404, 401, 403 |

---

## Flask return shape

```python
return jsonify(...), 200          # success
return jsonify(...), 201          # created
return "", 204                    # no body
return jsonify(error="Not found"), 404
return jsonify(error="Unauthorized"), 401
```

---

## Memory hooks

- **2** = good  
- **4** = their fault  
- **5** = your fault  
- **401** = not authenticated  
- **403** = not authorized  
- **404** = doesn't exist  
- **200 with an error body** = usually wrong; use a real error code instead  
