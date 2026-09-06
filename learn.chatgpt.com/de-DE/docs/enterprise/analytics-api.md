<!-- source: https://learn.chatgpt.com/de-DE/docs/enterprise/analytics-api -->

Die Codex Analytics API liefert für einen ChatGPT-Workspace aggregierte Metriken
zur Nutzung und zu Aktivitäten in Codex.

Die [Referenz zur Codex Analytics API](https://chatgpt.com/public/admin/api-reference#tag/Codex%20Enterprise%20Analytics)
ist die maßgebliche Quelle für aktuelle Zugriffsanforderungen, Routen, Anfrage- und Antwortschemata,
Metriken, Zeitsemantik und Paginierung.

## Wann sich die Analytics API eignet

Die Analytics API eignet sich für folgende Aufgaben:

- Regelmäßige Codex-Berichte automatisieren.
- Aggregierte Codex-Metriken mit internen Daten der Organisation verknüpfen.
- Eine kontrollierte Berichtsebene für autorisierte Zielgruppen aufbauen.
- Vermeiden, eine Integration an ein interaktives Dashboard zu koppeln.

Die Analytics API ist keine Schnittstelle für unaufbereitete Audit-Protokolldaten. Verwende die
[Compliance API](/de-DE/codex/enterprise/compliance-api), wenn der Ablauf
prüfbare Aktivitätsaufzeichnungen erfordert.

## Administrative Abgrenzungen prüfen

Die Ergebnisse der Analytics API sind auf einen ChatGPT-Workspace beschränkt. Anfragen werden jedoch
mit einem API-Schlüssel einer Organisation auf der Plattform authentifiziert. Die Organisation des Schlüssels muss
mit der Organisation übereinstimmen, die dem Workspace zugeordnet ist.

Die API-Referenz enthält die maßgeblichen aktuellen Angaben zur Bereitstellung von Schlüsseln, zu Scope-Anforderungen,
Routen, Schemata, Feldern, zur Zeitsemantik und zum Paginierungsverhalten. Diese Seite
wiederholt diese Vorgaben nicht.

## Weitere Dokumentation

- [Workspace-Analysen](/de-DE/codex/enterprise/workspace-analytics)
- [Leitfaden für den administrativen Rollout](/de-DE/codex/enterprise/admin-setup)
- [Governance](/de-DE/codex/enterprise/governance)
- [Compliance API](/de-DE/codex/enterprise/compliance-api)
