<!-- source: https://help.openai.com/en/articles/20001201-ip-allowlisting-for-openai-api -->

# IP allowlisting for OpenAI API

Restrict which IP addresses can access your OpenAI API.

Updated: 10 days ago

# Overview

IP allowlisting is an optional security feature that lets you restrict which IP addresses can access your OpenAI API.  
  
When enabled, only requests coming from configured IP addresses or IP ranges are allowed. Requests from all other IPs are rejected, even if they include a valid API key.  
  
This feature is intended to help reduce the risk of unauthorized API usage by limiting access to trusted network environments.  
  
  
***Note:*** IP allowlisting only applies to API requests. It does not impact access to platform.openai.com or user sign-in.  
  
  
**Why use IP allowlisting**  
  
IP allowlisting can help you:

* Restrict API access to known infrastructure (for example, your servers or cloud environments)
* Reduce exposure in the event of an API key leak
* Add an additional layer of control over where API traffic originates

IP allowlisting is most commonly used in production environments where API traffic originates from fixed or well-defined network ranges.

# How it works

You configure a list of allowed IP addresses or CIDR ranges.

* Requests from allowed IPs are accepted
* Requests from IPs not on the allowlist are rejected

IP allowlisting can be applied at:

* The organization level, or
* The project level

## Availability

IP allowlisting is available to all API customers.  
  
You can configure it in the platform under:  
  
  
**Settings → Security → IP allowlist**

## How to configure IP allowlisting

1. Go to **Settings → Security → IP allowlist**
2. Add one or more IP addresses or CIDR ranges
3. ***Note:*** You can add up to 50 IP addresses or CIDR ranges.
4. (Optional) Use the Check tool to validate whether an IP is included in your allowlist
5. Enable allowlisting for:

   * A specific project, or
   * Your entire organization
6. Test requests from your expected environments

We recommend starting with a single project before enabling organization-wide enforcement.  
  
After changes are made, updates may take up to **15 minutes** to take effect.  
  
  
***Note:*** You must have appropriate organization permissions to configure IP allowlisting settings.

## Troubleshooting

If you experience unexpected request failures:

* Confirm the request originates from an allowed IP address
* Check whether your infrastructure IPs have changed
* Review your configured IP ranges for accuracy
* Allow up to 15 minutes for configuration changes to propagate
* Use the Check tool to validate whether an IP is allowed

## What happens when a request is blocked

If a request originates from an IP address that is not allowlisted, requests will fail with:

* HTTP status: 401 Unauthorized
* Error code: ip\_not\_authorized

`Example response:`

`{`

`"error": {`

`"message": "Your IP is not authorized to access this organization.",`

`"type": "ip_not_authorized"`

`}`

`}`

## FAQ

### Will IP allowlisting prevent all unauthorized use of my API key?

No. IP allowlisting can help reduce risk by restricting where API requests originate, but it does not fully prevent all forms of misuse. It should be used alongside other security best practices such as secure key storage, key rotation and strong account security. For additional security, review our help center guides on [Best practices for API key safety](https://mandrillapp.com/track/click/31165340/help.openai.com?p=eyJzIjoiWHNNSTM5dVFSM0pjejFCdV9pZ1k4aG1MT2UwIiwidiI6MiwicCI6IntcInVcIjozMTE2NTM0MCxcInZcIjoyLFwidXJsXCI6XCJodHRwczpcXFwvXFxcL2hlbHAub3BlbmFpLmNvbVxcXC9lblxcXC9hcnRpY2xlc1xcXC81MTEyNTk1LWJlc3QtcHJhY3RpY2VzLWZvci1hcGkta2V5LXNhZmV0eVwiLFwiaWRcIjpcIjYwOGFjMGIxZWFmOTRkN2VhMjRhNDE2NzAyYTNjYmJhXCIsXCJ1cmxfaWRzXCI6W1wiNzI4ODA0ZmM5MzY4OWEyZTk2MDE2ZDNhYzYyZjhmZGY0MTc5MGJkOVwiXSxcIm1zZ190c1wiOjE3NDUzNjUyMDV9In0) and [Preventing unauthorized usage](https://mandrillapp.com/track/click/31165340/help.openai.com?p=eyJzIjoiYVNac0FydWplUFZJRURWUlVjd1M5VWJOSlFjIiwidiI6MiwicCI6IntcInVcIjozMTE2NTM0MCxcInZcIjoyLFwidXJsXCI6XCJodHRwczpcXFwvXFxcL2hlbHAub3BlbmFpLmNvbVxcXC9lblxcXC9hcnRpY2xlc1xcXC84MzA0Nzg2LXByZXZlbnRpbmctdW5hdXRob3JpemVkLXVzYWdlXCIsXCJpZFwiOlwiNjA4YWMwYjFlYWY5NGQ3ZWEyNGE0MTY3MDJhM2NiYmFcIixcInVybF9pZHNcIjpbXCJmYzY3MzdjMDQ5MTM2Y2U4ZjZkYjQ0NjM2NzA0NDdkZWQxY2YzNzM1XCJdLFwibXNnX3RzXCI6MTc0NTM2NTIwNX0ifQ).

### Does IP allowlisting impact latency?

IP allowlisting may introduce minimal latency in some cases, typically on initial requests. It is not expected to significantly affect overall API performance.

### How do I know if a request is failing due to IP allowlisting?

Requests failing due to IP allowlisting return:

* `HTTP status: 401 Unauthorized`
* `Error code: ip_not_authorized`
