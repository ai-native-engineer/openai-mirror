<!-- source: https://help.openai.com/en/articles/20001606-connecting-chatgpt-sites-to-private-services-with-tunnels -->

# Connecting ChatGPT Sites to private services with tunnels

Learn how tunnels connect Sites to services on your company’s private network and what access you need.

Updated: 13 days ago

A tunnel lets your Site connect to a service on your company’s private network, such as an internal inventory API, without making that service publicly accessible.

Your IT team runs OpenAI’s tunnel client, a small program that passes requests and responses between the Site and the service.

Connect only to services your organization allows the Site to use. Limit access to the data and actions it needs.

A tunnel does not replace the service’s authentication or access controls. It does not give the Site access to your entire network or decide which information visitors can see.

## Availability

Tunnels are rolling out to eligible Enterprise workspaces. They must be enabled for your workspace before you can connect one to a Site.

A workspace admin must enable **Allow members to attach private tunnels** for both the Site owner and the person connecting the tunnel.

## Before you begin

* Work with the Site owner, your workspace administrator, your IT team, and the person responsible for the private service.
* Identify the service, the data and actions the Site needs, and the people who should be able to use them.
* Confirm which Site will use the connection and who will manage the Site, tunnel client, and private service.
* Choose a computer or server that can run OpenAI’s tunnel client and reach the service over HTTP or HTTPS. Confirm that your organization allows the connection.
* Ask the service owner to confirm which data and actions the Site may access and configure the service’s authentication and access controls.

# Install the tunnel client

Your IT team installs and runs OpenAI’s tunnel client on a computer or server that can reach the private service.

For installation and deployment instructions, see the [official tunnel-client documentation](https://github.com/openai/tunnel-client/blob/master/README.md).

On macOS with Homebrew installed, run:

`brew install openai/tools/tunnel-client`

`tunnel-client --version`

Keep runtime credentials on the host running the client. Do not include API keys or passwords in Site content, browser-side code, screenshots, or support messages.

# Prepare the connection

Use a tunnel that’s available to the Site’s workspace. Work with your IT team to connect the Site, and ask the service owner to set up authentication and limit access to the data and actions the Site needs.

Before sharing the Site, test it with non-sensitive sample data. Check that the intended actions work and that the Site cannot access data or perform actions your organization hasn’t allowed.

# Review access before sharing

Review which data and actions each visitor can access through the Site. Keeping the service on a private network does not make a publicly shared Site private.

To make the Site public, **Allow public Sites with private tunnels** must be enabled for both the Site owner and the person publishing it. The workspace must also allow public publishing. If an already-public Site needs a new tunnel, make it private before adding the connection.

Connecting a tunnel does not give a Site access to a visitor’s connected accounts or change that visitor’s connected-app permissions.

For workspace controls, see: [Managing ChatGPT Sites for your workspace](https://help.openai.com/articles/20001338).

# Troubleshoot a connection

## You cannot find or connect a tunnel

Ask your workspace administrator to check:

* Whether tunnels are available in the Site’s workspace.
* Whether **Allow members to attach private tunnels** is enabled for both the Site owner and the person connecting the tunnel.

Do not switch organizations or give the Site broader network access to get around a workspace restriction.

## The tunnel client is not ready

Ask your IT team to check whether the tunnel client is running, has valid credentials, and can reach the private service. Keep API keys and other secrets out of shared logs.

## The Site opens, but a service operation fails

If an action fails while the tunnel is connected, check the private service’s authentication and access controls. The connection may work even when the Site doesn’t have permission to perform that action.

Record the action that failed, its response code or request ID, and when it last worked.

## A Site that uses a tunnel cannot be published publicly

Ask your workspace admin to check that **Allow public Sites with private tunnels** is enabled for both the Site owner and the person publishing it. The workspace must also allow public publishing. **Allow members to attach private tunnels** alone is not enough.

# Remove access

To remove one Site’s access, work with your administrator and IT team to remove its tunnel connection. Verify that requests from that Site no longer reach the service.

To stop the client’s connection, your IT team can stop the tunnel client. This may affect other Sites using the same tunnel. Revoking a runtime key blocks future credential requests, but may not stop a connection that’s already running.

# Contact support

If the issue continues, [contact OpenAI Support](https://help.openai.com/articles/6614161). Include:

* The Site URL and workspace.
* The tunnel identifier, if visible.
* The step that failed and the exact error.
* The request ID and timestamp, including the time zone.
* The client’s status and logs with sensitive information removed, if available.

Do not send API keys, passwords, or private service data.
