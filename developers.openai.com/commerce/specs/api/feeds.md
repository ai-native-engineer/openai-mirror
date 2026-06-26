<!-- source: https://developers.openai.com/commerce/specs/api/feeds/ -->

## Search the ChatGPT docs

## Overview

Use these endpoints to create a product feed and retrieve feed metadata.

## REST endpoints

* `GET /product_feeds/{id}` returns metadata for a feed.
* `POST /product_feeds` creates a new product feed and returns its
  metadata.

### **GET /product\_feeds/{id}**

Returns metadata for the specified product feed.

#### Path parameters

| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `string` | Yes | Identifier for the product feed. |

#### Request

This endpoint does not define a request body.

#### Response

`200 OK`

| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `string` | Yes | Identifier for the product feed. |
| `target_country` | `string` | No | Two letter country code per ISO 3166. |
| `updated_at` | `string` | No | Timestamp of the most recent update to the feed. |

`404 Not Found`

Returned when the product feed is not found.

### **POST /product\_feeds**

Creates a new product feed and returns its metadata.

#### Request

| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `target_country` | `string` | No | Two letter country code per ISO 3166. |

#### Response

`200 OK`

| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `id` | `string` | Yes | Identifier for the product feed. |
| `target_country` | `string` | No | Two letter country code per ISO 3166. |
| `updated_at` | `string` | No | Timestamp of the most recent update to the feed. |

`400 Bad Request`

Returned when the product feed payload is invalid.
