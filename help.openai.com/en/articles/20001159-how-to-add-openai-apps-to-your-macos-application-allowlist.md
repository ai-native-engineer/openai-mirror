<!-- source: https://help.openai.com/en/articles/20001159-how-to-add-openai-apps-to-your-macos-application-allowlist -->

# How to add OpenAI apps to your macOS application allowlist

Add OpenAI's macOS applications to an enterprise allowlist using the current developer Team ID and signing certificate details.

Updated: 6 hours ago

Businesses using macOS application allowlisting as part of their security process can add OpenAI’s current Apple Developer signing identity.

Please note; this has changed from the previous version as part of our response to [this](https://openai.com/index/axios-developer-tool-compromise/).

The **Team ID remains unchanged**, so configurations that allow by Team ID may not need changes. However, any policy that validates the signing organization name or certificate fingerprint should be updated.

**Allowlist values to use:**

* Team ID: 2DC432GLL2 (no change)
* Organization Name: "OpenAI OpCo, LLC" (no change)
* Certificate:

* SHA-256: 04f747c40a6e9b8739fe59da61cc41d9519544659a1009c5f5629577ed57edd5
* SHA-1: b9ba257d837a771b72554d380718f98561baa486
