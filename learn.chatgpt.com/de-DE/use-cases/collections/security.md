<!-- source: https://learn.chatgpt.com/de-DE/use-cases/collections/security -->

# Sicherheit

Codex unterstützt Entwicklungs- und Sicherheitsteams dabei, autorisierten Code zu analysieren, Belege
zusammenzutragen und aus geprüften Befunden gezielte Korrekturen abzuleiten. Diese Anwendungsfälle umfassen
Repository-Scans, Reviews von Änderungen, Vorfälle mit Abhängigkeiten und die Behebung von
Schwachstellen.

## Ein Repository analysieren

Führe mit dem Codex-Security-Plugin einen umfassenden Scan eines autorisierten
Repositorys durch, prüfe plausible Befunde und erstelle Berichte, die die manuelle
Triage unterstützen. Umfassende Scans dauern länger, weil mehrere
unabhängige Worker die Suche wiederholen.

## Änderungen vor dem Merge überprüfen

Lass Codex einen Pull Request, Branch, Commit oder Working-Tree-Diff auf
Sicherheitsregressionen prüfen und Belege mit direktem Bezug zum geänderten Code liefern.

## Vorfälle mit Abhängigkeiten untersuchen

Wandle eine öffentliche Sicherheitsmeldung zu einem Paket oder zur Lieferkette in ein Audit des Repositorys
ohne Schreibzugriff um, das Manifeste, Lock-Dateien, Skripte, Arbeitsabläufe und Expositionspfade abdeckt.

## Geprüfte Befunde beheben

Gib Codex einen freigegebenen Befund aus einem Sicherheitsbericht, einer Sicherheitsmeldung oder einem Ticket,
lass Codex dann eine minimale Korrektur vornehmen und durch eine Prüfung bestätigen, dass sich die Schwachstelle nicht
mehr reproduzieren lässt.

- [Umfassenden Sicherheitsscan ausführen](/de-DE/use-cases/deep-security-scan)

- [Codeänderungen auf Sicherheitsrisiken prüfen](/de-DE/use-cases/scan-code-changes-for-security)

- [Abhängigkeitsvorfälle prüfen](/de-DE/use-cases/dependency-incident-audits)

- [Einen Schwachstellen-Backlog abarbeiten](/de-DE/use-cases/remediate-vulnerability-backlog)
